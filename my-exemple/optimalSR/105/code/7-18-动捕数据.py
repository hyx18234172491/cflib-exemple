import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data
data_path = "../data/7-18-100ms-1m-第一组.csv"
data = pd.read_csv(data_path)

# Calculate Euclidean distance between UAV1 and UAV2
data['UAV_Distance'] = np.sqrt((data['UAV1x'] - data['UAV3x'])**2 +
                               (data['UAV1y'] - data['UAV3y'])**2 +
                               (data['UAV1z'] - data['UAV3z'])**2)

# Filter out rows where Statistic.dist1 is -1
filtered_data = data[data['Statistic.dist1'] != -1]

# Convert UAV distance from meters to centimeters
filtered_data['UAV_Distance_cm'] = filtered_data['UAV_Distance'] * 100

# Plotting the distances
plt.figure(figsize=(12, 6))
plt.plot(filtered_data['timestamp'], filtered_data['Statistic.dist1'], label='Statistic.dist1', marker='o')
plt.plot(filtered_data['timestamp'], filtered_data['UAV_Distance_cm'], label='UAV Distance (cm)', marker='x')

plt.title('Comparison of Statistic.dist1 and UAV Distance (cm) Over Time')
plt.xlabel('Timestamp')
plt.ylabel('Distance (cm)')
plt.legend()
plt.grid(True)
plt.show()
