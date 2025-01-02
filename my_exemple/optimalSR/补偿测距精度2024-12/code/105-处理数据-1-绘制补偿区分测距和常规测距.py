import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data
data_path = "../data-backup-代码有S4_NO的问题/一架40ms-一架160ms-应该是完美的.csv"
data = pd.read_csv(data_path)
plt.figure(figsize=(12, 6))
# Filter out rows where Statistic.dist1 is -1
filtered_data = data[data['Statistic.dist1'] != -1]
filtered_data = filtered_data[filtered_data['logNumber'] == 1]
filtered_data['distance_3_to_1'] = filtered_data['distance_3_to_1'] * 100
filtered_data['Statistic.dist1'] = filtered_data['Statistic.dist1'] + 15
# 因为采集是10ms每次，但是数据可能是20，30或者其他才更新一次
filtered_data = filtered_data[filtered_data['Statistic.recvNum1'] != filtered_data['Statistic.recvNum1'].shift(1)]
filtered_data = filtered_data.iloc[200:400]

# 得到compute2计算的点
compute2_data = filtered_data[
    filtered_data['Statistic.compute2num1'] != filtered_data['Statistic.compute2num1'].shift(1)]
plt.scatter(compute2_data['timestamp'],compute2_data['Statistic.dist1'],label = "compute2")
# 得到compute1计算的点
compute1_data = filtered_data[
    filtered_data['Statistic.compute1num1'] != filtered_data['Statistic.compute1num1'].shift(1)]
plt.scatter(compute1_data['timestamp'],compute1_data['Statistic.dist1'],label = "compute1")




# Plotting the distances
# plt.plot(filtered_data['timestamp'], filtered_data['Statistic.dist1'], label='Statistic.dist1', marker='x')
plt.plot(filtered_data['timestamp'], filtered_data['Statistic.dist1'], label='Statistic.dist1', marker='')
plt.plot(filtered_data['timestamp'], filtered_data['distance_3_to_1'], label='UAV Distance (cm)', marker='')
# plt.plot(filtered_data['timestamp'], filtered_data['distance_3_to_1'], label='UAV Distance (cm)', marker='o')

plt.title('Comparison of Statistic.dist1 and UAV Distance (cm) Over Time')
plt.xlabel('Timestamp')
plt.ylabel('Distance (cm)')
plt.legend()
plt.grid(True)
plt.show()
