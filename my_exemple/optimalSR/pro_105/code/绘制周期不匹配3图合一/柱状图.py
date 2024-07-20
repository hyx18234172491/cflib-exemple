
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# 加载数据
data_path = '../../data/7-18-一架50-一架70ms-1.csv'  # 替换为你的文件路径
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
    ((filtered_data['timestamp'] > 24000) & (filtered_data['timestamp'] < 25500)) |
    ((filtered_data['timestamp'] > 30000) & (filtered_data['timestamp'] < 31500)) |
    ((filtered_data['timestamp'] > 41900) & (filtered_data['timestamp'] < 43800)) |
    ((filtered_data['timestamp'] > 54000) & (filtered_data['timestamp'] < 55800)) |
    ((filtered_data['timestamp'] > 60100) & (filtered_data['timestamp'] < 61800))
]
filtered_data = filtered_data.head(100)

# 计算误差
filtered_data['error'] = filtered_data['distance_3_to_1'] - filtered_data['Statistic.dist1']

# 筛选误差小于20的数据
filtered_data = filtered_data[filtered_data['error'].abs() < 20]

# 创建三个不同的错误数据集
error_data_1 = filtered_data['error']
error_data_2 = filtered_data['error'] * 1.1  # 示例数据，可以根据实际情况替换
error_data_3 = filtered_data['error'] * 0.9  # 示例数据，可以根据实际情况替换

# 创建子图
fig, axes = plt.subplots(1, 3, figsize=(10, 18))

# 绘制第一个误差分布
sns.histplot(error_data_1, kde=True, color="blue", binwidth=1, ax=axes[0])
axes[0].set_title('Error Data 1 Distribution')
axes[0].set_xlabel('Error')
axes[0].set_ylabel('Frequency')

# 绘制第二个误差分布
sns.histplot(error_data_2, kde=True, color="green", binwidth=1, ax=axes[1])
axes[1].set_title('Error Data 2 Distribution')
axes[1].set_xlabel('Error')
axes[1].set_ylabel('Frequency')

# 绘制第三个误差分布
sns.histplot(error_data_3, kde=True, color="red", binwidth=1, ax=axes[2])
axes[2].set_title('Error Data 3 Distribution')
axes[2].set_xlabel('Error')
axes[2].set_ylabel('Frequency')

# 显示图例
axes[0].legend(['Error Data 1'])
axes[1].legend(['Error Data 2'])
axes[2].legend(['Error Data 3'])

plt.tight_layout()
plt.show()
