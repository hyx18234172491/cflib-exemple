import pandas as pd
import matplotlib.pyplot as plt


def process_data(df):
    df_filtered = df[df['logNumber'] == 'log0']
    numeric_cols = df_filtered.select_dtypes(include='number').columns
    df_subtracted = df_filtered[numeric_cols] - df_filtered[numeric_cols].iloc[0]
    for col in df_filtered.columns.difference(numeric_cols):
        df_subtracted[col] = df_filtered[col]
    df_cleaned = df_subtracted[df_subtracted['Statistic.recvSeq4'] != 0]
    df_cleaned['recvNum4_ratio'] = df_cleaned['Statistic.recvNum4'] / df_cleaned['Statistic.recvSeq4']
    df_cleaned['computeNum4_ratio'] = (df_cleaned['Statistic.compute1num4']+df_cleaned['Statistic.compute2num4']) / \
                                      df_cleaned['Statistic.recvSeq4']
    return df_cleaned['recvNum4_ratio'].median(), df_cleaned['computeNum4_ratio'].median()


def load_data(file_paths):
    data_frames = [pd.read_csv(path) for path in file_paths]
    return data_frames


def plot_medians(results, labels):
    recvNum4_medians = [result[0] for result in results]
    computeNum4_medians = [result[1] for result in results]
    x = range(len(labels))
    width = 0.35
    fig, ax = plt.subplots()
    rects1 = ax.bar(x, recvNum4_medians, width, label='recvNum4/recvSeq4')
    rects2 = ax.bar([p + width for p in x], computeNum4_medians, width, label='(compute1num4+compute2num4)/recvSeq4')
    ax.set_ylabel('Medians')
    ax.set_title('Median Ratios by Frame Setup')
    ax.set_xticks([p + width / 2 for p in x])
    ax.set_xticklabels(labels)
    ax.legend()
    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)
    fig.tight_layout()
    plt.show()


# Example usage
file_paths = [
    '../data/5架2.0-30+rand(60).csv',
    '../data/10架2.0-30+rand(60).csv',
    '../data/15架2.0-30+rand(60).csv',
    # '../data/20架2.0-30+rand(60).csv',
    # '../data/25架2.0-30+rand(60).csv',
    # '../data/10架1.0-60.csv',
    # '../data/15架1.0-60.csv',
    # '../data/20架1.0-60.csv',
    # '../data/5架1.0-30+rand(60).csv',
    # '../data/10架1.0-30+rand(60).csv',

    # '../data/25架1.0-60.csv',
    # '../data/10架1.0-30+rand(60).csv',

]
labels = [
    '5-frame',
    '10-frame',
    '15-frame',
    # '20-frame',
    # '25-frame',
    # '5-frame',
    # '10-frame',
    # '21-frame',
]

data_frames = load_data(file_paths)
results = [process_data(df) for df in data_frames]
plot_medians(results, labels)
