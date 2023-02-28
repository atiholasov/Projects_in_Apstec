# Author: Alexey Tiholasov (alexey.tiholasov@apstecsystems.com)
# Must be installed openpyxl.   pip install openpyxl

def main():
    global exel_out, DF_out
    import argparse
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib.ticker as ticker
    import seaborn as sns
    from datetime import datetime, timedelta

    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help="Name for input file")
    parser.add_argument('-out', '--output_file', default="stat.сsv", help="Name for output file. Default = stat.csv")
    parser.add_argument('-period', default=3600, help="Period for splitting statistics over time. Default = 3600 sec",
                        type=int)
    parser.add_argument('-ghost_cutoff_time', default=1,
                        help="Minimum target lifetime to avoid becoming a ghost. Default = 1 sec", type=float)
    args = parser.parse_args()

    inp_file_name = args.input_file
    out_file_name = args.output_file
    time_step_sec = args.period

    log_file = open(inp_file_name, "r")
    str_data = log_file.read()
    lines_of_file = str_data.split('\n')
    lines_of_file.pop()

    data_for_NewTargets = [[], {}, []]  # [0_date_time NewTarget, 1_{index Target with alarm :
                                        #  0 - no ghost, 1 - alarm, 2 - ghost ],  2_indexes NewTarget]

    alarm_dict = {}                     # dict {index: [type_1, type_2, ...]
    all_alarms_types = []               # list of all available anomalies in log file
    column_times = []                   # list of start times for intervals
    shift = 0                           # Target index shift when counting again from 1
    N_words_target = 0

    for i in range(len(lines_of_file)):

        if lines_of_file[i].find("New target") != -1:
            N_words_target += 1
            arr_string = lines_of_file[i].split()
            data_for_NewTargets[0].append(str(arr_string[0] + " " + arr_string[1]))

            if len(data_for_NewTargets[2]) > 0 and int(arr_string[8]) <= data_for_NewTargets[2][N_words_target-2]\
                    and int(arr_string[8]) == 1:
                shift = data_for_NewTargets[2][N_words_target-2]

            data_for_NewTargets[2].append(int(arr_string[8]) + shift)
            data_for_NewTargets[1].update({int(arr_string[8]) + shift: 0})

        if lines_of_file[i].find("alarm=") != -1:
            arr_string = lines_of_file[i].split()
            alarm_index = int(arr_string[18])+shift
            type_alarm = arr_string[5]

            if type_alarm not in all_alarms_types:
                all_alarms_types.append(type_alarm)

            if alarm_index in data_for_NewTargets[2]:
                alarm_dict.setdefault(alarm_index, [])
                data_for_NewTargets[1].update({alarm_index: 1})
                if type_alarm not in alarm_dict[alarm_index]:
                    alarm_dict[alarm_index].append(type_alarm)

        if lines_of_file[i].find("Deleted target") != -1:
            arr_string = lines_of_file[i].split()
            if float(arr_string[16]) < args.ghost_cutoff_time:
                del_index = int(arr_string[8])+shift
                data_for_NewTargets[1].update({del_index: 2})

    if len(data_for_NewTargets[0]) == 0:
        print("NO TARGETS LOG FILE")
    else:
        first_line_for_output = ["Start time", "N_targets", "Targets_with_alarm", "Alarm ratio"]
        dict_for_index_in_line = {}
        for type_anomal in all_alarms_types:
            first_line_for_output.append(type_anomal)
            dict_for_index_in_line[type_anomal] = 0                 # Reference dictionary for anomaly types
        total_anomal_dict = dict_for_index_in_line.copy()           # Dictionary for last line anomaly types
        intermediate_anomal_dict = dict_for_index_in_line.copy()    # Dictionary for intermediate string anomaly types

        num_intervals = (datetime.fromisoformat(data_for_NewTargets[0][-1])
                         - datetime.fromisoformat(data_for_NewTargets[0][0])) // timedelta(seconds=time_step_sec) + 1

        array_out_0 = np.zeros(len(first_line_for_output))

        # Work with periods of time

        for i in range(num_intervals):
            delta = timedelta(seconds=time_step_sec)
            first_time = datetime.fromisoformat(data_for_NewTargets[0][0]) + delta * i
            last_time = datetime.fromisoformat(data_for_NewTargets[0][0]) + delta * i + delta

            one_line_of_index = []
            N_targets_with_anomal: int = 0
            N_targets_ghost: int = 0
            N_targets_no_ghost: int = 0

            for k in range(len(data_for_NewTargets[0])):
                if first_time <= datetime.fromisoformat(data_for_NewTargets[0][k]) <= last_time:
                    one_line_of_index.append(data_for_NewTargets[2][k])

            for indexes in one_line_of_index:
                if data_for_NewTargets[1][indexes] == 1:
                    N_targets_with_anomal += 1
                    N_targets_no_ghost += 1
                if data_for_NewTargets[1][indexes] == 2:
                    N_targets_ghost += 1
                if data_for_NewTargets[1][indexes] == 0:
                    N_targets_no_ghost += 1

                if indexes in alarm_dict and data_for_NewTargets[1][indexes] != 2:
                    for elem in alarm_dict[indexes]:
                        intermediate_anomal_dict[elem] += 1
                        total_anomal_dict[elem] += 1

            out_intermediate_list = [str(first_time)[:-7], N_targets_no_ghost]
            column_times.append(str(first_time)[:-7])
            out_intermediate_list.append(N_targets_with_anomal)

            if N_targets_no_ghost != 0:
                ratio = float('{:.3f}'.format(N_targets_with_anomal / N_targets_no_ghost))  # 3 numbers after dot
            elif N_targets_with_anomal == 0:
                ratio = 0.0
            else:
                ratio = -1.0  # check suddenly at 0 targets there are not 0 targets with an alarm
            out_intermediate_list.append(ratio)

            for key in intermediate_anomal_dict:
                out_intermediate_list.append(intermediate_anomal_dict[key])

            array_out_0 = np.vstack([array_out_0, out_intermediate_list])
            array_out_1 = np.delete(array_out_0, 0, axis=0)
            array_out = np.delete(array_out_1, 0, axis=1)
            exel_out = pd.DataFrame(array_out, index=column_times, columns=first_line_for_output[1:])
            DF_out = exel_out.astype(np.float)  # DataFrame for work with plots

            intermediate_anomal_dict = dict_for_index_in_line.copy()

        # Writing output file

        if out_file_name.split(".")[1] == "xlsx":
            writer = pd.ExcelWriter(out_file_name)
            exel_out.to_excel(writer)
            writer.save()
        elif out_file_name.split(".")[1] == "csv":
            exel_out.to_csv(out_file_name)
        else:
            print("Output file format should be xlsx or csv")

        # Plotting
        # Plotting first N_targets(period)

        width_for_plot = 1
        plt.rcParams["figure.autolayout"] = True
        plt.rcParams["figure.figsize"] = [15, 6]
        plt.figure('Log file statistics')

        x_axis = []     # Making only time on the axis x
        for elem in DF_out.index:
            x_axis.append(elem.split()[1])
        x_axis = np.array(x_axis)
        DF_out.index = x_axis

        ax = plt.subplot(1, 2, 1)
        plt.title("Number of targets and targets with alarm")
        plt.xlabel("Time")
        plt.ylabel("Numbers")
        ax.xaxis.set_tick_params(which='minor', bottom=False)
        plt.xticks(np.arange(len(x_axis)), x_axis, rotation=45)
        plt.minorticks_on()
        plt.grid(which='major', color="gray")
        plt.grid(which='minor', linestyle='dotted', axis="y", color="gray")
        plt.bar(np.arange(len(x_axis)), DF_out.iloc[:, 0], label="Full number of targets", align='edge',
                width=width_for_plot / 2, edgecolor="gray")
        plt.bar(np.arange(len(x_axis)) + width_for_plot / 2, DF_out.iloc[:, 1], label="Targets with alarm",
                align='edge', width=width_for_plot / 2, edgecolor="gray")
        plt.legend()

        # Plotting second Alarm_ratio(period)

        ax = plt.subplot(1, 2, 2)
        plt.title("Percentage of alarms")
        plt.xlabel("Time")
        plt.ylabel("Alarm ratio")
        ax.yaxis.set_major_locator(ticker.MultipleLocator(0.1))
        ax.xaxis.set_tick_params(which="minor", bottom=False, color="gray")
        plt.xticks(np.arange(len(x_axis)), x_axis, rotation=45)
        plt.grid(which='major')
        plt.ylim([0., 1.])
        plt.minorticks_on()
        plt.bar(np.arange(len(x_axis)), DF_out.iloc[:, 2], label="Ratio", align='edge', width=width_for_plot,
                color="#ffa600", edgecolor="gray")
        plt.legend()

        # Plotting third Alarm_types(period)

        plt.rcParams["figure.autolayout"] = True
        plt.rcParams["figure.figsize"] = [15, 6]
        DF_out_by_types = DF_out.iloc[:, 3:]
        DF_out_by_types = DF_out_by_types.astype(np.int)
        arr_for_Transpose = np.array(DF_out_by_types)
        arr_for_plot_alarm_types = np.transpose(arr_for_Transpose)
        DF_out_by_types_right_order = pd.DataFrame(arr_for_plot_alarm_types, index=DF_out_by_types.columns,
                                                   columns=DF_out_by_types.index)
        plt.figure('Log file statistics by types')
        sns.heatmap(DF_out_by_types_right_order, annot=True, linewidth=.5, fmt='g')
        plt.xticks(rotation=45)
        plt.yticks(rotation=45)
        plt.show()


if __name__ == "__main__":
    main()
    