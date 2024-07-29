import pandas as pd
import matplotlib.pyplot as plt
import warnings

# 忽略所有警告
warnings.filterwarnings("ignore")
# File paths for both old and new data
old_file_paths = [
    "../data/2架60ms-5%丢包.csv",
    "../data/2架60ms-10%丢包.csv",
    "../data/2架60ms-15%丢包.csv",
    "../data/2架60ms-20%丢包.csv",
    "../data/2架60ms-25%丢包.csv",
    "../data/2架60ms-30%丢包.csv",
    "../data/一架20ms-一架70ms.csv",
    "../data/一架30ms-一架70ms.csv",
    "../data/一架40ms-一架70ms.csv",
   ]
new_file_paths = [
    "../data/SR1-20架30+rand(61).csv",
    "../data/SR1-25架30+rand(61).csv",
]

# Function to process files and calculate medians
def process_files(file_paths, new=False):
    processed_data = []
    medians = []

    for path in file_paths:
        data = pd.read_csv(path)
        # if not new:
        first_row = data.iloc[0]
        data -= first_row
        data['timestamp'] = data['timestamp']
        filtered_data = data[data['recvSeq1'] != 0]
        filtered_data['ratio1'] = filtered_data['compute1num1'] / filtered_data['recvSeq1']
        print('----')
        print(path)


        if not new:
            print('收包率：', data.iloc[-1]['recvNum1'] / data.iloc[-1]['recvSeq1'])
            print('收包次数：', data.iloc[-1]['recvNum1'])
            # print('compute1次数：', data.iloc[-1]['compute1num1'])
            # print('compute2次数：', data.iloc[-1]['compute2num1'])
            # print('compute3次数：', data.iloc[-1]['compute3num1'])
            print('ranging总次数(1,3):', data.iloc[-1]['compute1num1'] + data.iloc[-1]['compute3num1'])
            print('ranging总次数(1,2):', data.iloc[-1]['compute1num1'] + data.iloc[-1]['compute2num1'])
            # print('compute1比率:', data.iloc[-1]['compute1num1'] / data.iloc[-1]['recvSeq1'])
            print('ranging总比率(1,2):',
                  (data.iloc[-1]['compute1num1'] + data.iloc[-1]['compute2num1']) / data.iloc[-1]['recvSeq1'])
            print('ranging总比率(1,3):',
                  (data.iloc[-1]['compute1num1'] + data.iloc[-1]['compute3num1']) / data.iloc[-1]['recvSeq1'])
            filtered_data['ratio2'] = (filtered_data['compute1num1'] + filtered_data['compute2num1']) / filtered_data['recvSeq1']
            medians.append([filtered_data['ratio1'].median(), filtered_data['ratio2'].median()])
        else:
            print('收包率：', data.iloc[-1]['recvNum1'] / data.iloc[-1]['recvSeq1'])
            print('收包次数：', data.iloc[-1]['recvNum1'])
            # print('compute1次数：', data.iloc[-1]['compute1num1'])
            # print('compute2次数：', data.iloc[-1]['compute2num1'])
            # print('compute3次数：', data.iloc[-1]['compute3num1'])
            print('ranging总次数(1,2):', data.iloc[-1]['compute1num1'] + data.iloc[-1]['compute2num1'])
            print('ranging总次数(1,3):', data.iloc[-1]['compute1num1'] + data.iloc[-1]['compute3num1'])
            print('compute1比率:', data.iloc[-1]['compute1num1'] / data.iloc[-1]['recvSeq1'])
            # print('ranging总比率(1,2):',
            #       (data.iloc[-1]['compute1num1'] + data.iloc[-1]['compute2num1']) / data.iloc[-1]['recvSeq1'])
            print('ranging总比率(1,3):',
                  (data.iloc[-1]['compute1num1'] + data.iloc[-1]['compute3num1']) / data.iloc[-1]['recvSeq1'])

            medians.append(filtered_data['ratio1'].median())
        processed_data.append(filtered_data)

    return processed_data, medians

# Process old and new data
old_data, old_medians = process_files(old_file_paths)
# new_data, new_medians = process_files(new_file_paths, new=True)


