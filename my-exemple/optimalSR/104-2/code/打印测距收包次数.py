import pandas as pd
import matplotlib.pyplot as plt
import warnings

# 忽略所有警告
warnings.filterwarnings("ignore")
# File paths for both old and new data
old_file_paths = [
    "../data/104-TrRrBuffer3-lastTimeStamp3-5loss-5loss-50ms-100s.csv",
    "../data/104-TrRrBuffer3-lastTimeStamp3-10loss-10loss-50ms-100s.csv",
    "../data/104-TrRrBuffer3-lastTimeStamp3-15loss-15loss-50ms-100s.csv",
    "../data/104-TrRrBuffer3-lastTimeStamp3-20loss-20loss-50ms-100s.csv",
    "../data/104-TrRrBuffer3-lastTimeStamp3-25loss-25loss-50ms-100s.csv",
    "../data/104-TrRrBuffer3-lastTimeStamp3-30loss-30loss-50ms-100s.csv"
]
new_file_paths = [
    "../data/104-TrRrBuffer1-lastTimeStamp1-只携带一次时间戳-5loss-5loss-50ms-100s.csv",
    "../data/104-TrRrBuffer1-lastTimeStamp1-只携带一次时间戳-10loss-10loss-50ms-100s.csv",
    "../data/104-TrRrBuffer1-lastTimeStamp1-只携带一次时间戳-15loss-15loss-50ms-100s.csv",
    "../data/104-TrRrBuffer1-lastTimeStamp1-只携带一次时间戳-20loss-20loss-50ms-100s.csv",
    "../data/104-TrRrBuffer1-lastTimeStamp1-只携带一次时间戳-25loss-25loss-50ms-100s.csv",
    "../data/104-TrRrBuffer1-lastTimeStamp1-只携带一次时间戳-30loss-30loss-50ms-100s.csv"
]

# Function to process files and calculate medians
def process_files(file_paths, new=False):
    processed_data = []
    medians = []

    for path in file_paths:
        data = pd.read_csv(path)
        if not new:
            first_row = data.iloc[0]
            data -= first_row
        data['timestamp'] = data['timestamp']
        filtered_data = data[data['recvSeq2'] != 0]
        filtered_data['ratio1'] = filtered_data['compute1num2'] / filtered_data['recvSeq2']
        print('收包率：',data.iloc[-1]['recvNum2']/data.iloc[-1]['recvSeq2'])
        print('收包次数：',data.iloc[-1]['recvNum2'])
        print('ranging次数:',data.iloc[-1]['compute1num2'])
        print('ranging率:',data.iloc[-1]['compute1num2']/data.iloc[-1]['recvSeq2'])
        if not new:
            filtered_data['ratio2'] = (filtered_data['compute1num2'] + filtered_data['compute2num2']) / filtered_data['recvSeq2']
            medians.append([filtered_data['ratio1'].median(), filtered_data['ratio2'].median()])
        else:
            medians.append(filtered_data['ratio1'].median())
        processed_data.append(filtered_data)

    return processed_data, medians

# Process old and new data
old_data, old_medians = process_files(old_file_paths)
# new_data, new_medians = process_files(new_file_paths, new=True)


