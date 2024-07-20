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

# Combine data for easier plotting
all_ratios = pd.concat([data1_filtered['ratio1'], data2_filtered['ratio2'], data2_filtered['ratio3']], axis=1)
all_ratios.columns = ['Ratio1', 'Ratio2', 'Ratio3']

# Plotting the probability distributions
plt.figure(figsize=(12, 8))
for column in all_ratios.columns:
    sns.kdeplot(all_ratios[column], fill=True, common_norm=False, alpha=0.6, label=f'KDE of {column}')

plt.title('Probability Distribution of Compute Ratios')
plt.xlabel('Ratio Value')
plt.ylabel('Density')
plt.legend()
plt.show()
