import pandas as pd
import matplotlib.pyplot as plt


def load_data(file_paths):
    data_frames = {label: pd.read_csv(path) for label, path in zip(labels, file_paths)}
    return data_frames


def plot_final_adjusted_combined_graphs(data_frames, labels):
    fig, ax1 = plt.subplots(figsize=(9, 6))

    # Lists to store computed values for plotting
    bar_values_log0 = []
    bar_values_log1 = []
    log0_y_values = []
    log1_y_values = []

    # Process data for log0 and log1
    for label, df in data_frames.items():
        # Process for log0
        df_log0 = df[df['logNumber'] == 'log0']
        numeric_cols = df_log0.select_dtypes(include='number').columns
        df_log0[numeric_cols] = df_log0[numeric_cols].subtract(df_log0[numeric_cols].iloc[0], axis='columns')
        df_log0 = df_log0[df_log0['Statistic.recvSeq2'] != 0]
        if not df_log0.empty:
            ratio_log0 = df_log0['Statistic.compute1num2'].iloc[-1] / df_log0['Statistic.recvSeq2'].iloc[-1]
            bar_values_log0.append(ratio_log0)
            log0_y_values.append(df_log0['Statistic.compute1num2'].iloc[-1])
        else:
            bar_values_log0.append(0)
            log0_y_values.append(0)

        # Process for log1
        df_log1 = df[df['logNumber'] == 'log1']
        numeric_cols = df_log1.select_dtypes(include='number').columns
        df_log1[numeric_cols] = df_log1[numeric_cols].subtract(df_log1[numeric_cols].iloc[0], axis='columns')
        df_log1 = df_log1[df_log1['Statistic.recvSeq0'] != 0]
        if not df_log1.empty:
            ratio_log1 = df_log1['Statistic.compute1num0'].iloc[-1] / df_log1['Statistic.recvSeq0'].iloc[-1]
            bar_values_log1.append(ratio_log1)
            log1_y_values.append(df_log1['Statistic.compute1num0'].iloc[-1])
        else:
            bar_values_log1.append(0)
            log1_y_values.append(0)

    ax1.bar([x - 0.125 for x in range(len(labels))], bar_values_log0, width=0.25, label='log0 Bar (compute1num2/recvSeq2)',
            )
    ax1.bar([x + 0.125 for x in range(len(labels))], bar_values_log1, width=0.25, label='log1 Bar (compute1num0/recvSeq0)',
            )
    ax1.set_ylabel('Ratio')
    ax1.legend(loc='upper right')
    # Plotting line for log0 and log1
    ax2 = ax1.twinx()
    ax2.plot(labels, log0_y_values, marker='o', linestyle='-', label='log0 Line (compute1num2)')
    ax2.plot(labels, log1_y_values, marker='o', linestyle='--', label='log1 Line (compute1num0)')
    ax2.set_xlabel('Configuration Labels')
    ax2.set_ylabel('Computed Statistic Value')
    ax2.legend(loc='upper left')

    # Create a second y-axis for the bar plots

    plt.title('Final Adjusted Combined Line and Bar Charts for Different Logs and Configurations')
    plt.grid(True)
    plt.show()


# File paths and labels
file_paths = [
    '../data/2号70+0号70-2.0.csv',
    '../data/2号60+0号70-2.0.csv',
    '../data/2号50+0号70-2.0.csv',
    '../data/2号40+0号70-2.0.csv',
    '../data/2号30+0号70-2.0.csv',
    '../data/2号20+0号70-2.0.csv',
]
labels = ['70', '60', '50', '40', '30', '20']

# Load data and plot graphs
data_frames = load_data(file_paths)
# Call the function to plot the final adjusted combined graphs
plot_final_adjusted_combined_graphs(data_frames, labels)
