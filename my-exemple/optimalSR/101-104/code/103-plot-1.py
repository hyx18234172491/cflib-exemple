import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Apply the Seaborn style
sns.set(style="whitegrid")

# Load the uploaded CSV files
data1 = pd.read_csv('../data/103-TrRrBuffer3-lastTimeStamp3-30loss-nolossDelay5-20ms-100s.csv')
data2 = pd.read_csv('../data/103-TrRrBuffer3-lastTimeStamp3-normal-delay5-20ms-100s.csv')

# Subtract the first row from each dataset
data1_adjusted = data1 - data1.iloc[0]
data2_adjusted = data2 - data2.iloc[0]

# Remove rows where 'recvNum' is zero
data1_filtered = data1_adjusted[data1_adjusted['recvNum'] != 0]
data2_filtered = data2_adjusted[data2_adjusted['recvNum'] != 0]

# Calculate the required ratios
data1_filtered['ratio1'] = data1_filtered['compute1num'] / data1_filtered['recvNum']
data2_filtered['ratio2'] = data2_filtered['compute1num'] / data2_filtered['recvNum']
data2_filtered['ratio3'] = (data2_filtered['compute1num'] + data2_filtered['compute2num']) / data2_filtered['recvNum']

# Select relevant columns for plotting
plot_data1 = data1_filtered[['timestamp', 'ratio1']]
plot_data2 = data2_filtered[['timestamp', 'ratio2', 'ratio3']]

plot_data1['timestamp'] = plot_data1['timestamp'] / 1000
plot_data2['timestamp'] = plot_data2['timestamp'] / 1000

# Merging data for plotting
plot_data = pd.merge(plot_data1, plot_data2, on='timestamp', how='outer')
# Calculate medians
median_ratio1 = plot_data['ratio1'].median()
median_ratio2 = plot_data['ratio2'].median()
median_ratio3 = plot_data['ratio3'].median()

# Plotting the data with median lines and annotations
plt.figure(figsize=(12, 8))
plt.plot(plot_data['timestamp'], plot_data['ratio1'], label='Data 1 (compute1num / recvNum)', linestyle='-', color='blue')
plt.axhline(y=median_ratio1, color='blue', linestyle='--', label=f'Median for Data 1: {median_ratio1:.2f}')
plt.text(plot_data['timestamp'].max(), median_ratio1, f'{median_ratio1:.2f}', color='blue', ha='right', va='bottom')

plt.plot(plot_data['timestamp'], plot_data['ratio2'], label='Data 2 (compute1num / recvNum)', linestyle='-', color='red')
plt.axhline(y=median_ratio2, color='red', linestyle='--', label=f'Median for Data 2: {median_ratio2:.2f}')
plt.text(plot_data['timestamp'].max(), median_ratio2, f'{median_ratio2:.2f}', color='red', ha='right', va='bottom')

plt.plot(plot_data['timestamp'], plot_data['ratio3'], label='Data 2 ((compute1num + compute2num) / recvNum)', linestyle='-', color='green')
plt.axhline(y=median_ratio3, color='green', linestyle='--', label=f'Median for Data 2 (combined): {median_ratio3:.2f}')
plt.text(plot_data['timestamp'].max(), median_ratio3, f'{median_ratio3:.2f}', color='green', ha='right', va='bottom')

plt.xlabel('Timestamp / 1000')
plt.ylabel('Ratios')
plt.title('Simplified Visualization of Compute Ratios Over Time')
plt.legend()
plt.show()
