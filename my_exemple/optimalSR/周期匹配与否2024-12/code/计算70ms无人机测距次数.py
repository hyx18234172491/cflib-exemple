import pandas as pd


def load_data(file_paths):
    data_frames = [pd.read_csv(path) for path in file_paths]
    return data_frames
def process_data(df):
    df_filtered = df[df['logNumber'] == 'log1']
    numeric_cols = df_filtered.select_dtypes(include='number').columns
    # 下面是所有数值行减去第0行
    df_subtracted = df_filtered[numeric_cols] - df_filtered[numeric_cols].iloc[0]
    # 因为采集是10ms每次，但是数据可能是20，30或者其他才更新一次
    df_subtracted = df_subtracted[df_subtracted['Statistic.recvNum0'] != df_subtracted['Statistic.recvNum0'].shift(1)]

    df_subtracted["compute2diff"] = df_subtracted["Statistic.compute2num0"] - df_subtracted["Statistic.compute2num0"].shift(1)
    # 从第二行开始判断，统计当前行的前1行是0的个数
    # 判断前一行是否为0，结果为布尔值
    df_subtracted['compute2diff_previous_is_zero'] = ((df_subtracted['compute2diff'].shift(1) == 0) & (df_subtracted['compute2diff']==1))
    df_subtracted['zero_count'] = df_subtracted['compute2diff_previous_is_zero'].cumsum()

    df_subtracted.to_csv("valid.csv")
    # 下面是把所有列都填充上
    for col in df_filtered.columns.difference(numeric_cols):
        df_subtracted[col] = df_filtered[col]
    df_cleaned = df_subtracted[df_subtracted['Statistic.recvSeq0'] != 0]
    last_row = df_cleaned.iloc[-1]

    valid_compute2 = last_row['zero_count']
    print('发包数量：',last_row['Statistic.recvSeq0'])
    print('收包数量：',last_row['Statistic.recvNum0'])
    print('1.0测距数量：',last_row['Statistic.compute1num0'])
    print('2.0测距总数量（有效和无效）：',last_row['Statistic.compute1num0']+last_row['Statistic.compute2num0'])
    print('2.0有效测距数量:',last_row['Statistic.compute1num0'] + valid_compute2)
    print('----')

file_paths = [
    '../data/2号100ms-0号10ms-采集100s.csv',
    '../data/2号100ms-0号20ms-采集100s.csv',
    '../data/2号100ms-0号30ms-采集100s.csv',
    '../data/2号100ms-0号40ms-采集100s.csv',
    '../data/2号100ms-0号50ms-采集100s.csv',
    '../data/2号100ms-0号60ms-采集100s.csv',
    '../data/2号100ms-0号70ms-采集100s.csv',
    '../data/2号100ms-0号80ms-采集100s.csv',
    '../data/2号100ms-0号90ms-采集100s.csv',
    '../data/2号100ms-0号100ms-采集100s.csv',

]
data_frames = load_data(file_paths)
results = [process_data(df) for df in data_frames]