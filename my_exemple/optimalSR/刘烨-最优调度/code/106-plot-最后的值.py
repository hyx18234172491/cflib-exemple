import pandas as pd

# Load the data from the uploaded CSV file
file_path = '../data/10架周期60ms.csv'
data = pd.read_csv(file_path)

# Subtract all data values (for relevant columns) from the first row's corresponding values
data_subtracted = data.iloc[:, 3:7] - data.iloc[0, 3:7]

# Calculate the packet loss rate for the last row
packet_loss_rate = data_subtracted.iloc[-1, 1] / data_subtracted.iloc[-1, 0]

# Calculate the range rate for the last row
range_rate = (data_subtracted.iloc[-1, 2] + data_subtracted.iloc[-1, 3]) / data_subtracted.iloc[-1, 0]

# Display the results
print("Packet Loss Rate:", packet_loss_rate)
print("Range Rate:", range_rate)
