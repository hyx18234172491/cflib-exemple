import pandas as pd
import matplotlib.pyplot as plt

# Load the data
file_path = 'optimal3_lighthouse_2024-07-18_22-53-14-还可以.csv'

data = pd.read_csv(file_path)

# Plot all distances on a single plot with thicker lines and distinct colors, changing red to orange
fig, ax = plt.subplots(figsize=(12, 5.5))

# Plot for Ranging.distTo0 vs Ranging.truthDistTo0
plt.plot(data['T'], data['Ranging.distTo0'], label='Ranging to 0', linestyle='--', linewidth=2, color='blue')
plt.plot(data['T'], data['Ranging.truthDistTo0'], label='Ground-truth to 0', linewidth=2, color='cyan')

# Plot for Ranging.distTo2 vs Ranging.truthDistTo2
plt.plot(data['T'], data['Ranging.distTo2'], label='Ranging to 2', linestyle='--', linewidth=2, color='orange')
plt.plot(data['T'], data['Ranging.truthDistTo2'], label='Ground-truth to 2', linewidth=2, color='yellow')

# Plot for Ranging.distTo5 vs Ranging.truthDistTo5
plt.plot(data['T'], data['Ranging.distTo5'], label='Ranging to 4', linestyle='--', linewidth=2, color='green')
plt.plot(data['T'], data['Ranging.truthDistTo5'], label='Ground-truth to 4', linewidth=2, color='lime')

# Plot for Ranging.distTo7 vs Ranging.truthDistTo7
plt.plot(data['T'], data['Ranging.distTo7'], label='Ranging to 6', linestyle='--', linewidth=2, color='purple')
plt.plot(data['T'], data['Ranging.truthDistTo7'], label='Ground-truth to 6', linewidth=2, color='magenta')

# Set title and labels
plt.xlabel('Time (s)',fontsize=24)
plt.ylabel('Distance (cm)',fontsize=24)
plt.legend(fontsize='14',ncol=2,loc='best')
plt.grid(True)
# plt.xlim(0,48)
# ax.set_xlim(0, 50)
plt.subplots_adjust(left=0.08, right=0.99, top=0.999, bottom=0.118)
# Show the plot
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.show()
