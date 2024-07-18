import pandas as pd
import matplotlib.pyplot as plt

# 加载数据
data_path = '../data/7-18-50ms-1ms-第四组-4.csv'  # 替换为你的文件路径
data = pd.read_csv(data_path)

# 筛选 logNumber 为 0 的数据
filtered_data = data[data['logNumber'] == 1]
filtered_data['distance_3_to_1'] = filtered_data['distance_3_to_1']*100
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
