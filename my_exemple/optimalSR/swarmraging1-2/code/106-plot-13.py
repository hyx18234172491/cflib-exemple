import pandas as pd
import matplotlib.pyplot as plt


def process_data(df):
    df_filtered = df[df['logNumber'] == 'log0']
    numeric_cols = df_filtered.select_dtypes(include='number').columns
    df_subtracted = df_filtered[numeric_cols] - df_filtered[numeric_cols].iloc[0]
    for col in df_filtered.columns.difference(numeric_cols):
        df_subtracted[col] = df_filtered[col]
    df_cleaned = df_subtracted[df_subtracted['Statistic.recvSeq13'] != 0]
    df_cleaned['recvNum13_ratio'] = df_cleaned['Statistic.recvNum13'] / df_cleaned['Statistic.recvSeq13']
    df_cleaned['computeNum13_ratio'] = (df_cleaned['Statistic.computenum13']) / \
                                      df_cleaned['Statistic.recvSeq13']
    return df_cleaned['recvNum13_ratio'].median(), df_cleaned['computeNum13_ratio'].median()


def load_data(file_paths):
    data_frames = [pd.read_csv(path) for path in file_paths]
    return data_frames


def plot_medians(results, labels):
    recvNum4_medians = [result[0] for result in results]
    computeNum4_medians = [result[1] for result in results]
    x = range(len(labels))
    width = 0.35
    fig, ax = plt.subplots()
    rects1 = ax.bar(x, recvNum4_medians, width, label='recvNum13/recvSeq13')
    rects2 = ax.bar([p + width for p in x], computeNum4_medians, width, label='(computenum13)/recvSeq13')
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
