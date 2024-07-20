import pandas as pd
import matplotlib.pyplot as plt

# 加载数据
data_path = '../../data/7-18-一架40-一架70ms-2.csv'  # 替换为你的文件路径
data = pd.read_csv(data_path)

# 筛选 logNumber 为 0 的数据
filtered_data = data[data['logNumber'] == 1]
# 移除没有更新的数值
filtered_data = filtered_data[
    (filtered_data['Statistic.compute2num1'] != filtered_data['Statistic.compute2num1'].shift()) |
    (filtered_data['Statistic.compute1num1'] != filtered_data['Statistic.compute1num1'].shift())
    ]
filtered_data = filtered_data[
    ((filtered_data['timestamp'] > 28800) & (filtered_data['timestamp'] < 30000)) |
    ((filtered_data['timestamp'] > 35000) & (filtered_data['timestamp'] < 36100)) |
    ((filtered_data['timestamp'] > 40800) & (filtered_data['timestamp'] < 42000)) |
    ((filtered_data['timestamp'] > 47000) & (filtered_data['timestamp'] < 48000)) |
    ((filtered_data['timestamp'] > 52800) & (filtered_data['timestamp'] < 54000)) |
    ((filtered_data['timestamp'] > 59000) & (filtered_data['timestamp'] < 59800)) |
    ((filtered_data['timestamp'] > 65000) & (filtered_data['timestamp'] < 66000))

    ]
filtered_data['distance_3_to_1'] = filtered_data['distance_3_to_1'] * 100
filtered_data=filtered_data.head(150)
print(len(filtered_data))
# 绘制折线图
plt.figure(figsize=(12, 6))
plt.plot(filtered_data['timestamp'], filtered_data['Statistic.dist1'], label='Statistic.dist1', marker='o',
         linestyle='-')
plt.plot(filtered_data['timestamp'], filtered_data['distance_3_to_1'], label='distance_3_to_1', marker='x',
         linestyle='--')
plt.xlabel('Timestamp')
plt.ylabel('Value')
plt.title('40-70,moving towards')
plt.legend()
plt.grid(True)
plt.show()
