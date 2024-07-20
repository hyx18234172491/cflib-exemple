import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def getPlotData():
    # 加载数据
    data_path = '../../data/7-18-一架50-一架70ms-1.csv'  # 替换为你的文件路径
    data = pd.read_csv(data_path)

    # 筛选 logNumber 为 0 的数据
    filtered_data = data[data['logNumber'] == 1]
    filtered_data = filtered_data[(filtered_data['timestamp'] > 30000) & (filtered_data['timestamp'] < 60000)]
    filtered_data['distance_3_to_1'] = filtered_data['distance_3_to_1'] * 100
    # 移除没有更新的数值
    filtered_data = filtered_data[
        (filtered_data['Statistic.compute2num1'] != filtered_data['Statistic.compute2num1'].shift()) |
        (filtered_data['Statistic.compute1num1'] != filtered_data['Statistic.compute1num1'].shift())
        ]
    filtered_data = filtered_data[
        ((filtered_data['timestamp'] > 24000) & (filtered_data['timestamp'] < 25500)) |
        ((filtered_data['timestamp'] > 30000) & (filtered_data['timestamp'] < 31500)) |
        ((filtered_data['timestamp'] > 41900) & (filtered_data['timestamp'] < 43800)) |
        ((filtered_data['timestamp'] > 54000) & (filtered_data['timestamp'] < 55800)) |
        ((filtered_data['timestamp'] > 60100) & (filtered_data['timestamp'] < 61800)) |
        ((filtered_data['timestamp'] > 65000) & (filtered_data['timestamp'] < 67000))
        ]
    filtered_data = filtered_data.head(150)
    ABSCHA = 3.271540200383761  # 计算出的绝对差
    # 计算误差
    filtered_data['error'] = filtered_data['distance_3_to_1'] - filtered_data['Statistic.dist1'] - ABSCHA
    return filtered_data

if __name__ == '__main__':
    filtered_data=getPlotData()
    average_error = filtered_data['error'].mean()
    std_error = filtered_data['error'].std()
    print(f"Average Error: {average_error}")
    print(f"Standard Deviation of Error: {std_error}")

    # 绘制误差分布
    plt.figure(figsize=(10, 6))
    sns.histplot(filtered_data['error'], kde=True, color="blue", binwidth=1)  # binwidth根据误差值的范围调整
    plt.title('Error Distribution')
    plt.xlabel('Error')
    plt.ylabel('Frequency')

    # # 标注均值和方差
    # plt.axvline(x=average_error, color='red', linestyle='--')
    # plt.axvline(x=-average_error, color='red', linestyle='--')
    # plt.axvline(x=std_error, color='green', linestyle='-.')
    # plt.axvline(x=-std_error, color='green', linestyle='-.')

    # 添加文本标注
    plt.text(-5, 5, f'$\mu={average_error:.2f}$\n$\sigma={std_error:.3f}$', bbox=dict(facecolor='white', alpha=0.5),
             fontsize=25)

    plt.show()
