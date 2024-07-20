import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Load the data
file_path = '../data/1m-s-60ms-第二组.csv'  # Replace with your actual file path
data = pd.read_csv(file_path)

# Filter the data where logNumber is 0
filtered_data = data[data['logNumber'] == 0]

# Additional timestamp filtering
filtered_data = filtered_data[(filtered_data['timestamp'] > 26500) & (filtered_data['timestamp'] < 50000)]
# 移除没有更新的数值
filtered_data = filtered_data[filtered_data['Statistic.recvSeq3'] != filtered_data['Statistic.recvSeq3'].shift()]

# Multiply Statistic.distReal3 by 100
filtered_data['Statistic.distReal3'] *= 100

# Calculate the average error
filtered_data['error'] = filtered_data['Statistic.distReal3'] - filtered_data['Statistic.dist3']-9
average_error = filtered_data['error'].abs().mean()


# 绘制误差分布
plt.figure(figsize=(10, 6))
sns.histplot(filtered_data['error'], kde=True, color="blue", binwidth=1)  # binwidth根据误差值的范围调整
plt.title('Error Distribution')
plt.xlabel('Error')
plt.ylabel('Frequency')
plt.show()

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(filtered_data['timestamp'], filtered_data['Statistic.distReal3'], label='Statistic.distReal3 * 100', marker='o')
plt.plot(filtered_data['timestamp'], filtered_data['Statistic.dist3'], label='Statistic.dist3', marker='x')

plt.xlabel('Timestamp')
plt.ylabel('Values')
plt.title('Line Graph of Statistic.distReal3 * 100 and Statistic.dist3')
plt.legend()
plt.grid(True)
plt.show()

# Print the average error
print(f"The average error is {average_error}")
