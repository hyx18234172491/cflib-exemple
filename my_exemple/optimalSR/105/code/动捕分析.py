import pandas as pd
import matplotlib.pyplot as plt

# 加载数据
data_path = '../data/7-18-一架50-一架70ms-1.csv'  # 替换为你的文件路径
data = pd.read_csv(data_path)

# 筛选 logNumber 为 0 的数据
filtered_data = data[data['logNumber'] == 1]
# filtered_data = filtered_data[
#     ((filtered_data['timestamp'] > 24800) & (filtered_data['timestamp'] < 25600))
#
#     ]
filtered_data['distance_3_to_1'] = filtered_data['distance_3_to_1']*100
# 移除没有更新的数值
filtered_data = filtered_data[
    (filtered_data['Statistic.compute2num1'] != filtered_data['Statistic.compute2num1'].shift()) |
    (filtered_data['Statistic.compute1num1'] != filtered_data['Statistic.compute1num1'].shift())
    ]

# 绘制折线图
plt.figure(figsize=(12, 6))
plt.plot(filtered_data['timestamp'], filtered_data['Statistic.dist1'], label='Statistic.dist1', marker='o', linestyle='-')
plt.plot(filtered_data['timestamp'], filtered_data['distance_3_to_1'], label='distance_3_to_1', marker='x', linestyle='--')
plt.xlabel('Timestamp')
plt.ylabel('Value')
plt.title('Line Plot of Statistic.dist1 and distance_3_to_1')
plt.legend()
plt.grid(True)
plt.show()
