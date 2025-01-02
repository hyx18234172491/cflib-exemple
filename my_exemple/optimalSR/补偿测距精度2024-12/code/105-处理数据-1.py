import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data
data_path = "../data-liu/2架均5ms周期.csv"
data = pd.read_csv(data_path)

# Filter out rows where Statistic.dist1 is -1
filtered_data = data[data['Statistic.dist1'] != -1]
filtered_data = filtered_data[filtered_data['distance_3_to_1'] != 0]  # 过滤动捕不正常数据
filtered_data = filtered_data[filtered_data['logNumber'] == 1]
# 因为采集是10ms每次，但是数据可能是20，30或者其他才更新一次
filtered_data = filtered_data[filtered_data['Statistic.recvNum1'] != filtered_data['Statistic.recvNum1'].shift(1)]

filtered_data['distance_3_to_1'] = filtered_data['distance_3_to_1'] * 100
# filtered_data['Statistic.dist1'] = filtered_data['Statistic.dist1'] + 15
filtered_data = filtered_data.iloc[500:600]
# Plotting the distances
plt.figure(figsize=(12, 6))

plt.plot(filtered_data['timestamp'], filtered_data['Statistic.dist1'], label='Statistic.dist1', marker='x')
plt.plot(filtered_data['timestamp'], filtered_data['distance_3_to_1'], label='UAV Distance (cm)', marker='o')

plt.title('Comparison of Statistic.dist1 and UAV Distance (cm) Over Time')
plt.xlabel('Timestamp')
plt.ylabel('Distance (cm)')
plt.legend()
plt.grid(True)
plt.show()
