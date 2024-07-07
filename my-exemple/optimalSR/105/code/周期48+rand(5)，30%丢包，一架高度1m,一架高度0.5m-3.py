import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data
data_path = "../data/周期48+rand(5)，30%丢包，一架高度1m,一架高度0.5m.csv"
data = pd.read_csv(data_path)

# Calculate Euclidean distance between UAV1 and UAV2
data['UAV_Distance'] = np.sqrt((data['UAV1x'] - data['UAV2x'])**2 +
                               (data['UAV1y'] - data['UAV2y'])**2 +
                               (data['UAV1z'] - data['UAV2z'])**2)

# Filter out rows where Statistic.dist1 is -1
filtered_data = data[data['Statistic.dist1'] != -1]

# Filter data for timestamp between 40000 and 50000
time_filtered_data = filtered_data[(filtered_data['timestamp'] > 40000) & (filtered_data['timestamp'] < 50000)]

# Convert UAV distance from meters to centimeters
time_filtered_data['UAV_Distance_cm'] = time_filtered_data['UAV_Distance'] * 100

# Adjust timestamps to start from 0
time_filtered_data['Adjusted_Timestamp'] = (time_filtered_data['timestamp'] - time_filtered_data['timestamp'].iloc[0])/1000

# Plotting the distances
plt.figure(figsize=(10, 6))

# Plot UAV Distance as a red line
plt.plot(time_filtered_data['Adjusted_Timestamp'], time_filtered_data['UAV_Distance_cm'], label='Ground Truth', linestyle='-', color='red')

# Plot Statistic.dist1 as a line and also mark points based on distSrc1 values
plt.plot(time_filtered_data['Adjusted_Timestamp'], time_filtered_data['Statistic.dist1'], label='Calculate', linestyle='-', color='green')

# Plot Statistic.dist1 based on distSrc1 values with points
distSrc1_1 = time_filtered_data[time_filtered_data['Statistic.distSrc1'] == 1]
distSrc1_2 = time_filtered_data[time_filtered_data['Statistic.distSrc1'] == 2]

plt.scatter(distSrc1_1['Adjusted_Timestamp'], distSrc1_1['Statistic.dist1'], color='orange', label='Upward Calculate', marker='o', s=20)
plt.scatter(distSrc1_2['Adjusted_Timestamp'], distSrc1_2['Statistic.dist1'], color='blue', label='Downward Calculate', marker='o', s=20)

# plt.title('Comparison of Ground Truth and Calculate distance (cm) Over Time')
plt.xlabel('Time (s)')
plt.ylabel('Distance (cm)')
plt.legend()
plt.grid(True)
plt.show()
