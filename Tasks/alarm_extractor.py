import sys

#inp_file_name = sys.argv[1]
inp_file_name = "221219_hss1a3_logs/hss_server.8.log"
log_file = open(inp_file_name, "r")
str_data = log_file.read()

names_out_file = {}
lines_of_file = str_data.split('\n')
lines_of_file.pop()
for line in lines_of_file:
    number_in_line = line.find("alarm=")
    if number_in_line != -1:

        # filename creation
        array_of_elem_line = list(line.split())
        date = array_of_elem_line[0].replace("-", "")[2:]
        out_file_name = "hss_" + date + "_" + array_of_elem_line[5] + ".dat"

        # creating a dictionary of filename
        if out_file_name not in names_out_file:
            names_out_file[out_file_name] = 1
        else:
            names_out_file[out_file_name] += 1


        # file write
        alarm_data_file = open(out_file_name, 'a')
        alarm_data_file.write(line[(number_in_line+7):-1])
        alarm_data_file.write("\n")


for elem in names_out_file:
    print(elem, names_out_file[elem])
