import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

# File paths
file_names = [
    "../data/104-TrRrBuffer1-lastTimeStamp1-5loss-5loss-50ms-100s.csv",
    "../data/104-TrRrBuffer1-lastTimeStamp1-10loss-10loss-50ms-100s.csv",
    "../data/104-TrRrBuffer1-lastTimeStamp1-15loss-15loss-50ms-100s.csv",
    "../data/104-TrRrBuffer1-lastTimeStamp1-20loss-20loss-50ms-100s.csv",
    "../data/104-TrRrBuffer1-lastTimeStamp1-25loss-25loss-50ms-100s.csv",
    "../data/104-TrRrBuffer1-lastTimeStamp1-30loss-30loss-50ms-100s.csv",
    "../data/104-TrRrBuffer3-lastTimeStamp3-5loss-5loss-50ms-100s.csv",
    "../data/104-TrRrBuffer3-lastTimeStamp3-10loss-10loss-50ms-100s.csv",
    "../data/104-TrRrBuffer3-lastTimeStamp3-15loss-15loss-50ms-100s-1.csv",
    "../data/104-TrRrBuffer3-lastTimeStamp3-20loss-20loss-50ms-100s.csv",
    "../data/104-TrRrBuffer3-lastTimeStamp3-25loss-25loss-50ms-100s.csv",
    "../data/104-TrRrBuffer3-lastTimeStamp3-30loss-30loss-50ms-100s.csv"
]

# Initialize the dictionary to hold the median values
buffer_medians_updated_seq = {key: {} for key in ["Buffer1", "Buffer3", "Buffer3 Combined"]}

# Process each file and update ratios to use 'recvSeq'
for file_name in file_names:
    df = pd.read_csv(file_name)
    df -= df.iloc[0]  # Subtract first row from all rows
    df = df[df['recvSeq'] != 0]  # Remove rows where recvSeq is 0
    df['ratio'] = df['compute1num'] / df['recvSeq']
    if 'compute2num' in df.columns:
        df['combined_ratio'] = (df['compute1num'] + df['compute2num']) / df['recvSeq']
        combined_median = df['combined_ratio'].median()
    else:
        combined_median = df['ratio'].median()  # Fallback if compute2num is not present

    median_value = df['ratio'].median()
    parts = os.path.basename(file_name).split('-')
    loss_value = parts[4].replace('loss', '')
    buffer_type = parts[1][-1]

    # Store median values
    buffer_medians_updated_seq[f"Buffer{buffer_type}"][loss_value + 'loss'] = median_value
    if buffer_type == '3':  # Only buffer type 3 has compute2num based on file naming
        buffer_medians_updated_seq["Buffer3 Combined"][loss_value + 'loss'] = combined_median

# Bar chart parameters
loss_levels = ['5loss', '10loss', '15loss', '20loss', '25loss', '30loss']

bar_width = 0.25
# Reduce the spacing between groups in the bar chart
# Retry generating the chart with reduced group spacing
index = np.arange(len(loss_levels)) * 1.2  # Moderately reduced spacing

plt.figure(figsize=(10, 6))

# Define improved colors for each group
colors = ['#e6194B', '#3cb44b', '#4363d8']
legend = ["Swarm ranging1.0", "Swarm ranging1.0 with 3 txTimeStamp", "Swarm ranging1.0"]
# Plotting with aesthetic enhancements and adjusted group spacing
for i, (buffer_type, medians) in enumerate(buffer_medians_updated_seq.items()):
    median_values = [medians.get(loss, 0) for loss in loss_levels]
    bars = plt.bar(index + i * bar_width, median_values, bar_width, label=legend[i], color=colors[i % len(colors)])
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom', fontweight='bold')

xtick = ['5%loss', '10%loss', '15%loss', '20%loss', '25%loss', '30%loss']
plt.xlabel('Loss Levels', fontsize=12)
plt.ylabel('Average Ranging Ratio', fontsize=12)
# plt.title('Enhanced Median Ratio by Loss Level and Buffer Type', fontsize=14)
plt.xticks(index + bar_width, xtick, fontsize=11)
plt.legend(fontsize=11)
# plt.grid(axis='y', linestyle='--', zorder=0, color='grey')
plt.tight_layout()
plt.show()