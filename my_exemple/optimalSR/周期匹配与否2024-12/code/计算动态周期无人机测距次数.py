import pandas as pd


def load_data(file_paths):
    data_frames = [pd.read_csv(path) for path in file_paths]
    return data_frames
def process_data(df):
    df_filtered = df[df['logNumber'] == 'log0']
    numeric_cols = df_filtered.select_dtypes(include='number').columns
    df_subtracted = df_filtered[numeric_cols] - df_filtered[numeric_cols].iloc[0]
    for col in df_filtered.columns.difference(numeric_cols):
        df_subtracted[col] = df_filtered[col]
    df_cleaned = df_subtracted[df_subtracted['Statistic.recvSeq2'] != 0]
    last_row = df_cleaned.iloc[-1]

    print('发包数量：',last_row['Statistic.recvSeq2'])
    print('收包数量：',last_row['Statistic.recvNum2'])
    print('1.0测距数量：',last_row['Statistic.compute1num2'])
    print('2.0测距数量：',last_row['Statistic.compute1num2']+last_row['Statistic.compute2num2'])
    print('----')

file_paths = [
    '../data/2号100ms-0号10ms-采集100s.csv',

]
data_frames = load_data(file_paths)
results = [process_data(df) for df in data_frames]