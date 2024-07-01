import pandas as pd
import matplotlib.pyplot as plt

# Load the first dataset
file_path = '../data/104-TrRrBuffer3-每个收到的数据包只携带一次/104-TrRrBuffer3-lastTimeStamp3-30loss-30loss-50ms-100s.csv'
data = pd.read_csv(file_path)

# Subtract each row by the first row's values
data_subtracted = data - data.iloc[0]

# Remove rows where recvNum equals zero
filtered_data = data_subtracted[data_subtracted['recvNum'] != 0]

# Calculate ratios and adjust timestamps
filtered_data['ratio1'] = filtered_data['compute1num'] / filtered_data['recvNum']
filtered_data['ratio2'] = (filtered_data['compute1num'] + filtered_data['compute2num']) / filtered_data['recvNum']
filtered_data['timestamp_seconds'] = filtered_data['timestamp'] / 1000

# Load the second dataset
new_file_path = '../data/104-TrRrBuffer1-lastTimeStamp1-30loss-30loss-50ms-100s.csv'
new_data = pd.read_csv(new_file_path)

# Subtract each row by the first row's values
new_data_subtracted = new_data - new_data.iloc[0]

# Remove rows where recvNum equals zero
new_filtered_data = new_data_subtracted[new_data_subtracted['recvNum'] != 0]

# Calculate new column for plotting and adjust timestamps
new_filtered_data['ratio1_new'] = new_filtered_data['compute1num'] / new_filtered_data['recvNum']
new_filtered_data['timestamp_seconds'] = new_filtered_data['timestamp'] / 100

# Calculate medians
median_ratio1 = filtered_data['ratio1'].median()
median_ratio2 = filtered_data['ratio2'].median()
median_ratio1_new = new_filtered_data['ratio1_new'].median()

# Plotting all data
plt.figure(figsize=(10, 6))
plt.plot(filtered_data['timestamp_seconds'], filtered_data['ratio1'], label='optimal: compute1num/recvNum', color='tab:red')
plt.axhline(y=median_ratio1, color='tab:red', linestyle='--', label=f'Median (optimal: compute1num/recvNum): {median_ratio1:.2f}')
plt.plot(filtered_data['timestamp_seconds'], filtered_data['ratio2'], label='optimal: (compute1num + compute2num)/recvNum', color='tab:blue')
plt.axhline(y=median_ratio2, color='tab:blue', linestyle='--', label=f'Median (optimal: (compute1num + compute2num)/recvNum): {median_ratio2:.2f}')
plt.plot(new_filtered_data['timestamp_seconds'], new_filtered_data['ratio1_new'], label='original: compute1num/recvNum', color='tab:green')
plt.axhline(y=median_ratio1_new, color='tab:green', linestyle='--', label=f'Median (original: compute1num/recvNum): {median_ratio1_new:.2f}')
plt.xlabel('Time (seconds)')
plt.ylabel('Ratios')
plt.title('Comparison of Ratios Over Time with Medians')
plt.legend()
plt.grid(True)
plt.show()
