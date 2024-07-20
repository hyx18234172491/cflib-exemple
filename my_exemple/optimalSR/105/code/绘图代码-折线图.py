import pandas as pd
import matplotlib.pyplot as plt

# Load the data
file_path = '../data/7-18-100ms-1m-第一组.csv'  # Replace with your actual file path
data = pd.read_csv(file_path)

# Filter the data where logNumber is 0
filtered_data = data[data['logNumber'] == 0]
# 移除没有更新的数值
filtered_data = filtered_data[filtered_data['Statistic.recvSeq3'] != filtered_data['Statistic.recvSeq3'].shift()]

# Additional timestamp filtering
filtered_data = filtered_data[(filtered_data['timestamp'] > 35000)]

# Multiply Statistic.distReal3 by 100
filtered_data['Statistic.distReal3'] *= 100

# Calculate the average error
filtered_data['error'] = filtered_data['Statistic.distReal3'] - filtered_data['Statistic.dist3']
average_error = filtered_data['error'].abs().mean()

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
