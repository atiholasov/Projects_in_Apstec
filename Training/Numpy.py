import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# СОЗДАНИЕ МАССИВОВ
arr = np.random.random(40).reshape(10, 4)
arr[:,0] = [311,34,1,90,28,0,1,12,28,65]
arr[:,1] = [282,28,0,70,14,0,0,10,5,3]
arr[:,2] = [0.907,0.824,0.0,0.967,0.929,1,1,1,1.0,0.833]

ex_format = pd.DataFrame(arr, index=['11.12', '12.12', '13.12', '14.12', '15.12', '16.12', '17.12', '18.12', '19.12',
                                     '20.12'], columns=['numbers', 'sum', 'name', 'price'])

print(ex_format)
# ПОСТРОЕНИЕ

width_for_plot = 1
level_of_good_result: float = 0.85
plt.figure('Log file statistics')

plt.subplot(1, 2, 1)
plt.title("Number of targets and targets with alarm")
plt.xlabel("Time")
plt.xticks(np.arange(len(ex_format)), ex_format.index, rotation=45)
plt.ylabel("Numbers")
plt.bar(np.arange(len(ex_format)), ex_format.iloc[:, 0], label="Full number of targets", align='edge',
        width=width_for_plot/2)
plt.bar(np.arange(len(ex_format)) + width_for_plot/2, ex_format.iloc[:, 1], label="Targets with alarm", align='edge',
        width=width_for_plot/2)
plt.legend()

plt.subplot(1, 2, 2)
plt.title("Percentage of alarms")
plt.xlabel("Time")
plt.xticks(rotation=45)
plt.ylabel("Ratio")
plt.step(ex_format.index, ex_format.iloc[:, 2], label="Ratio")
plt.plot(ex_format.index, np.ones(len(ex_format))*level_of_good_result, "r--", label=f"Good result, {level_of_good_result} percent")
plt.legend()

new_arr = ex_format.iloc[:, 1:]
print(new_arr)