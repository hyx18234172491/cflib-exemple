import pandas as pd
import numpy as np

# Load your data
data = pd.read_csv('../data/48+rand(5).csv')

# Ensure the filtered_data only contains rows with valid 'Statistic.dist1'
filtered_data = data[data['Statistic.dist1'] != -1]

# Convert UAV distance from meters to centimeters
filtered_data['UAV_Distance_cm'] = filtered_data['UAV_Distance'] * 100


