import pandas as pd
import matplotlib.pyplot as plt


def process_data(df):
    df_filtered = df[df['logNumber'] == 'log0']
    numeric_cols = df_filtered.select_dtypes(include='number').columns
    df_subtracted = df_filtered[numeric_cols] - df_filtered[numeric_cols].iloc[0]
    for col in df_filtered.columns.difference(numeric_cols):
        df_subtracted[col] = df_filtered[col]
    df_cleaned = df_subtracted[df_subtracted['Statistic.recvSeq2'] != 0]
    df_cleaned['recvNum2_ratio'] = df_cleaned['Statistic.recvNum2'] / df_cleaned['Statistic.recvSeq2']
    df_cleaned['computeNum2_ratio'] = (df_cleaned['Statistic.compute1num2']) / \
                                      df_cleaned['Statistic.recvSeq2']
    df_cleaned['computeNum2_and1_ratio'] = (df_cleaned['Statistic.compute1num2'] + df_cleaned[
        'Statistic.compute2num2']) / \
                                           df_cleaned['Statistic.recvSeq2']
    # 计算中位数并保留两位小数
    recvNum2_ratio_median = round(df_cleaned['recvNum2_ratio'].median(), 2)
    computeNum2_ratio_median = round(df_cleaned['computeNum2_ratio'].median(), 2)
    computeNum2_and1_ratio_median = round(df_cleaned['computeNum2_and1_ratio'].median(), 2)

    return recvNum2_ratio_median, computeNum2_ratio_median, computeNum2_and1_ratio_median


def load_data(file_paths):
    data_frames = [pd.read_csv(path) for path in file_paths]
    return data_frames


def plot_medians(results, labels):
    recvNum2_medians = [result[0] for result in results]
    computeNum4_medians = [result[1] for result in results]
    computeNum2_and1_ratio = [result[2] for result in results]
    x = range(len(labels))
    width = 0.26
    fig, ax = plt.subplots(figsize=(9, 6))
    rects1 = ax.bar(x, recvNum2_medians, width, label='Reception packet')
    rects2 = ax.bar([p + width for p in x], computeNum4_medians, width,
                    label='swarm ranging 1.0 Ranging')
    rects3 = ax.bar([p + 2 * width for p in x], computeNum2_and1_ratio, width, label='swarm ranging 2.0 Ranging')

    ax.set_ylabel('Reception (Ranging) Rate',fontsize=16)
    ax.set_xlabel('Period (ms)',fontsize=16)
    # ax.set_title('Median Ratios by Frame Setup')
    ax.set_xticks([p + width / 2 for p in x])
    ax.set_xticklabels(labels)
    # 设置图例位置在一行上方居中
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.10), ncol=3,fontsize=11)

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)
    ax.bar_label(rects3, padding=3)
    fig.tight_layout()
    plt.show()


# Example usage
file_paths = [
    '../data/2号20+0号70-2.0.csv',
    '../data/2号30+0号70-2.0.csv',
    '../data/2号40+0号70-2.0.csv',
    '../data/2号50+0号70-2.0.csv',
    '../data/2号60+0号70-2.0.csv',
    '../data/2号70+0号70-2.0.csv',
    # '../data/2号40+0号70-1.0.csv',

]
labels = [
    '20',
    '30',
    '40',
    '50',
    '60',
    '70',
]

data_frames = load_data(file_paths)
results = [process_data(df) for df in data_frames]
plot_medians(results, labels)
