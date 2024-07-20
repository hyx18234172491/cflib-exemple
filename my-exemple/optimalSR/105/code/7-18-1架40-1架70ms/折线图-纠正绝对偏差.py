import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 加载数据
data_path = '../../data/7-18-一架40-一架70ms-2.csv'  # 替换为你的文件路径
data = pd.read_csv(data_path)

# 筛选 logNumber 为 0 的数据
filtered_data = data[data['logNumber'] == 1]
filtered_data.reset_index(drop=True, inplace=True)
# 移除没有更新的数值
filtered_data = filtered_data[
    (filtered_data['Statistic.compute2num1'] != filtered_data['Statistic.compute2num1'].shift()) |
    (filtered_data['Statistic.compute1num1'] != filtered_data['Statistic.compute1num1'].shift())
    ]
filtered_data = filtered_data[
    ((filtered_data['timestamp'] > 0))
]
filtered_data['distance_3_to_1'] = filtered_data['distance_3_to_1'] * 100

# 绘制折线图
plt.figure(figsize=(12, 6))
plt.plot(filtered_data['timestamp'], filtered_data['Statistic.dist1'], label='Statistic.dist1', marker='o',
         linestyle='-')
plt.plot(filtered_data['timestamp'], filtered_data['distance_3_to_1'], label='distance_3_to_1', marker='x',
         linestyle='--')
plt.xlabel('Timestamp')
plt.ylabel('Value')
plt.title('Line Plot of Statistic.dist1 and distance_3_to_1')
plt.legend()
plt.grid(True)
plt.show()

# 计算误差
filtered_data['error'] = filtered_data['distance_3_to_1'] - filtered_data['Statistic.dist1']
filtered_data = filtered_data[filtered_data['error'].abs() < 20]
average_error = filtered_data['error'].mean()
std_error = filtered_data['error'].std()
print(f"Average Error: {average_error}")
print(f"Standard Deviation of Error: {std_error}")

# 绘制误差分布
plt.figure(figsize=(10, 6))
sns.histplot(filtered_data['error'], kde=True, color="blue", binwidth=1)  # binwidth根据误差值的范围调整
plt.title('Error Distribution')
plt.xlabel('Error')
plt.ylabel('Frequency')

# # 标注均值和方差
# plt.axvline(x=average_error, color='red', linestyle='--')
# plt.axvline(x=-average_error, color='red', linestyle='--')
# plt.axvline(x=std_error, color='green', linestyle='-.')
# plt.axvline(x=-std_error, color='green', linestyle='-.')

# 添加文本标注
plt.text(-5, 5, f'$\mu={average_error:.2f}$\n$\sigma={std_error:.3f}$', bbox=dict(facecolor='white', alpha=0.5),
         fontsize=25)

plt.show()
