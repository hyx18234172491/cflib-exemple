import pandas as pd
import matplotlib.pyplot as plt


def process_data(df):
    df_filtered = df[df['logNumber'] == 'log1']
    numeric_cols = df_filtered.select_dtypes(include='number').columns
    df_subtracted = df_filtered[numeric_cols] - df_filtered[numeric_cols].iloc[0]
    for col in df_filtered.columns.difference(numeric_cols):
        df_subtracted[col] = df_filtered[col]
    df_cleaned = df_subtracted[df_subtracted['Statistic.recvSeq2'] != 0]
    df_cleaned['recvNum2_ratio'] = df_cleaned['Statistic.recvNum2'] / df_cleaned['Statistic.recvSeq2']
    df_cleaned['computeNum2_ratio'] = (df_cleaned['Statistic.computenum2']) / \
                                      df_cleaned['Statistic.recvSeq2']
    return df_cleaned['recvNum2_ratio'].median(), df_cleaned['computeNum2_ratio'].median()


def load_data(file_paths):
    data_frames = [pd.read_csv(path) for path in file_paths]
    return data_frames


def plot_medians(results, labels):
    recvNum4_medians = [result[0] for result in results]
    computeNum4_medians = [result[1] for result in results]
    x = range(len(labels))
    width = 0.35
    fig, ax = plt.subplots()
    rects1 = ax.bar(x, recvNum4_medians, width, label='recvNum2/recvSeq2')
    rects2 = ax.bar([p + width for p in x], computeNum4_medians, width, label='(computenum2)/recvSeq2')
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
file_paths = ['../data/13号30ms-2号50ms.csv',
              # '../data/10架1.0-30+rand(60).csv',

              ]
labels = ['5-frame',
          # '21-frame',
          ]

data_frames = load_data(file_paths)
results = [process_data(df) for df in data_frames]
plot_medians(results, labels)
