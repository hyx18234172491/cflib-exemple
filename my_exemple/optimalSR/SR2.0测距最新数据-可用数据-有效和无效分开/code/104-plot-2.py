import pandas as pd
import matplotlib.pyplot as plt

# File paths for both old and new data
old_file_paths = [
    "../data/104-TrRrBuffer3-lastTimeStamp3-5loss-5loss-50ms-100s.csv",
    "../data/104-TrRrBuffer3-lastTimeStamp3-10loss-10loss-50ms-100s.csv",
    "../data/104-TrRrBuffer3-lastTimeStamp3-15loss-15loss-50ms-100s.csv",
    "../data/104-TrRrBuffer3-lastTimeStamp3-20loss-20loss-50ms-100s.csv",
    "../data/104-TrRrBuffer3-lastTimeStamp3-25loss-25loss-50ms-100s.csv",
    "../data/104-TrRrBuffer3-lastTimeStamp3-30loss-30loss-50ms-100s.csv"
]
new_file_paths = [
    "../data/104-TrRrBuffer1-lastTimeStamp1-只携带一次时间戳-5loss-5loss-50ms-100s.csv",
    "../data/104-TrRrBuffer1-lastTimeStamp1-只携带一次时间戳-10loss-10loss-50ms-100s.csv",
    "../data/104-TrRrBuffer1-lastTimeStamp1-只携带一次时间戳-15loss-15loss-50ms-100s.csv",
    "../data/104-TrRrBuffer1-lastTimeStamp1-只携带一次时间戳-20loss-20loss-50ms-100s.csv",
    "../data/104-TrRrBuffer1-lastTimeStamp1-只携带一次时间戳-25loss-25loss-50ms-100s.csv",
    "../data/104-TrRrBuffer1-lastTimeStamp1-只携带一次时间戳-30loss-30loss-50ms-100s.csv"
]

# Function to process files and calculate medians
def process_files(file_paths, new=False):
    processed_data = []
    medians = []

    for path in file_paths:
        data = pd.read_csv(path)
        if not new:
            first_row = data.iloc[0]
            data -= first_row
        data['timestamp'] = data['timestamp']
        filtered_data = data[data['recvSeq2'] != 0]
        filtered_data['ratio1'] = filtered_data['compute1num2'] / filtered_data['recvSeq2']
        if not new:
            filtered_data['ratio2'] = (filtered_data['compute1num2'] + filtered_data['compute2num2']) / filtered_data['recvSeq2']
            medians.append([filtered_data['ratio1'].median(), filtered_data['ratio2'].median()])
        else:
            medians.append(filtered_data['ratio1'].median())
        processed_data.append(filtered_data)

    return processed_data, medians

# Process old and new data
old_data, old_medians = process_files(old_file_paths)
new_data, new_medians = process_files(new_file_paths, new=True)

# Extract packet loss rates from file names
packet_loss_rates = [int(path.split('-')[3].replace('loss', '')) for path in old_file_paths]

# Plotting
fig, ax = plt.subplots(figsize=(9, 6))
width = 0.26
space_between_groups = 0.15

# Adjust the positions for the bars
positions3 = [i * (3 * width + space_between_groups) for i in range(len(packet_loss_rates))]  # New data at the beginning
positions1 = [p + width for p in positions3]  # Old data, first metric
positions2 = [p + width for p in positions1]  # Old data, second metric


# Plot the new bars (new data) at the beginning
bars3 = ax.bar(positions3, new_medians, width=width, label='Swarm ranging 1.0')

# Plot the original bars (previous data)
bars1 = ax.bar(positions1, [m[0] for m in old_medians], width=width, label='Swarm ranging 1.0 with 3 lastTxTimestamp')
bars2 = ax.bar(positions2, [m[1] for m in old_medians], width=width, label='Swarm ranging 2.0')

# Add value annotations to all bars
for bars in [bars3, bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:.2f}', xy=(bar.get_x() + bar.get_width() / 2, height), xytext=(0, 3), textcoords="offset points", ha='center', va='bottom')

# Adjust x-ticks to be in the middle of the grouped bars and set labels
ax.set_xticks([p + width for p in positions3])
ax.set_xticklabels([f"{rate}%" for rate in packet_loss_rates])

# ax.set_title('Median Computed Ratios by Packet Loss Rate (Updated Positions)')
ax.set_xlabel('Packet Loss Rate',fontsize=16)
ax.set_ylabel('Ranging Rate',fontsize=16)
ax.legend()

plt.show()
