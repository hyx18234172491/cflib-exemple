import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 加载数据
data_path = '../../data/7-18-一架30-一架70ms-1.csv'  # 替换为你的文件路径
data = pd.read_csv(data_path)

# 筛选 logNumber 为 0 的数据
filtered_data = data[data['logNumber'] == 1]
filtered_data = filtered_data[(filtered_data['timestamp'] > 30000) & (filtered_data['timestamp'] < 60000)]
filtered_data['distance_3_to_1'] = filtered_data['distance_3_to_1'] * 100
# 移除没有更新的数值
filtered_data = filtered_data[
    (filtered_data['Statistic.compute2num1'] != filtered_data['Statistic.compute2num1'].shift()) |
    (filtered_data['Statistic.compute1num1'] != filtered_data['Statistic.compute1num1'].shift())
]
filtered_data = filtered_data[
    ((filtered_data['timestamp'] > 33000) & (filtered_data['timestamp'] < 34000)) |
    ((filtered_data['timestamp'] > 45100) & (filtered_data['timestamp'] < 46000)) |
    ((filtered_data['timestamp'] > 51000) & (filtered_data['timestamp'] < 52000)) |
    ((filtered_data['timestamp'] > 57000) & (filtered_data['timestamp'] < 58000)) |
    ((filtered_data['timestamp'] > 63500) & (filtered_data['timestamp'] < 64000))
]
filtered_data = filtered_data.head(150)
ABSCHA = 2.21 # 计算出的绝对差
# 计算误差
filtered_data['error'] = filtered_data['distance_3_to_1'] - filtered_data['Statistic.dist1']
# 筛选误差小于20的数据
# filtered_data = filtered_data[filtered_data['error'].abs() < 20]
filtered_data['error'] = filtered_data['error'] - ABSCHA
average_error = filtered_data['error'].mean()
std_error = filtered_data['error'].std()
print(f"Average Error: {average_error}")
print(f"Standard Deviation of Error: {std_error}")

# 绘制误差分布
plt.figure(figsize=(10, 6))
sns.histplot(filtered_data['error'], kde=True, color="blue", binwidth=1)  # binwidth根据误差值的范围调整
plt.title('Error Distribution 30-70 moving away')
plt.xlabel('Error')
plt.ylabel('Frequency')

# # 标注均值和方差
# plt.axvline(x=average_error, color='red', linestyle='--')
# plt.axvline(x=-average_error, color='red', linestyle='--')
# plt.axvline(x=std_error, color='green', linestyle='-.')
# plt.axvline(x=-std_error, color='green', linestyle='-.')

# 添加文本标注
plt.text(-1, 5, f'$\mu={average_error:.2f}$\n$\sigma={std_error:.3f}$', bbox=dict(facecolor='white', alpha=0.5),fontsize=25)

plt.show()
