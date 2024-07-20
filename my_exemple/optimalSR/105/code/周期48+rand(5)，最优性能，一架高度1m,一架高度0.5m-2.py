import pandas as pd
import matplotlib.pyplot as plt

# Load the data
file_path = '../data/周期48+rand(5)，最优性能，一架高度1m,一架高度0.5m.csv'
data = pd.read_csv(file_path)

# Remove rows where Statistic.dist1 is -1
data_filtered = data[data['Statistic.dist1'] != -1]

# Calculate the distance between UAV1 and UAV2
data_filtered['distance_UAV1_UAV2'] = (((data_filtered['UAV1x'] - data_filtered['UAV2x'])**2 +
                                       (data_filtered['UAV1y'] - data_filtered['UAV2y'])**2 +
                                       (data_filtered['UAV1z'] - data_filtered['UAV2z'])**2)**0.5)*100

# Create scatter plot
plt.figure(figsize=(12, 6))

# Plot distance between UAV1 and UAV2
# plt.scatter(data_filtered['timestamp'], data_filtered['distance_UAV1_UAV2'], color='red', s=10,label='Distance UAV1-UAV2')

# Plot Statistic.dist1 based on Statistic.distSrc1
plt.scatter(data_filtered[data_filtered['Statistic.distSrc1'] == 1]['timestamp'],
            data_filtered[data_filtered['Statistic.distSrc1'] == 1]['Statistic.dist1'],
            color='blue', s=10,label='Statistic.dist1 (distSrc1=1)')

plt.scatter(data_filtered[data_filtered['Statistic.distSrc1'] == 2]['timestamp'],
            data_filtered[data_filtered['Statistic.distSrc1'] == 2]['Statistic.dist1'],
            color='green', s=10,label='Statistic.dist1 (distSrc1=2)')

# Add labels and legend
plt.xlabel('Timestamp')
plt.ylabel('Distance / Statistic.dist1')
plt.legend()
plt.title('Scatter Plot of UAV Distances and Statistic.dist1')
plt.show()
