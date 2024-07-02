import pandas as pd
import matplotlib.pyplot as plt

# 加载第一个数据集
file_path = '../data/102-1-50ms-30loss-noloss-100s-1.csv'
data = pd.read_csv(file_path)
adjusted_data = data - data.iloc[0]
filtered_data = adjusted_data[adjusted_data['recvNum'] != 0]
filtered_data['ratio'] = filtered_data['compute1num'] / filtered_data['recvNum']
filtered_data['timestamp'] = filtered_data['timestamp'] / 1000

# 加载第二个数据集
new_file_path = '../data/102-3-50ms-30loss-noloss-100s-1.csv'
new_data = pd.read_csv(new_file_path)
new_adjusted_data = new_data - new_data.iloc[0]
new_filtered_data = new_adjusted_data[new_adjusted_data['recvNum'] != 0]
new_filtered_data['ratio'] = new_filtered_data['compute1num'] / new_filtered_data['recvNum']
new_filtered_data['timestamp'] = new_filtered_data['timestamp'] / 1000

# 绘制两个数据集的比较图
plt.figure(figsize=(10, 5))
plt.plot(filtered_data['timestamp'], filtered_data['ratio'], label='With 1 lastTxTimeStamp', color='blue')
plt.plot(new_filtered_data['timestamp'], new_filtered_data['ratio'], label='With 3 lastTxTimeStamp', color='red')
plt.xlabel('Timestamp (s)')
plt.ylabel('Ratio of compute1num to recvNum')
plt.title('Comparison of compute1num to recvNum over Time')
plt.legend()
plt.grid(True)
plt.show()
