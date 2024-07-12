import numpy as np

# 设置随机种子，以保持结果的可重现性
np.random.seed(0)

all_num=10000
# 生成1000个A和B随机数，范围从30到90
A_random_numbers = 30 + np.random.randint(0, 61, all_num)
B_random_numbers = 30 + np.random.randint(0, 61, all_num)

# 对A和B随机数进行累加
A_cumulative = np.cumsum(A_random_numbers)
B_cumulative = np.cumsum(B_random_numbers)

# 将A和B的累加序列和标记结合到一个序列中，并排序
AB_combined = list(zip(A_cumulative, ['A'] * all_num)) + list(zip(B_cumulative, ['B'] * all_num))
AB_sorted = sorted(AB_combined, key=lambda x: x[0])

# 计算前一个B和后一个B之间有两个或多个A的次数，以及这些情况中的A总数
count_two_or_more_As_between_Bs = 0
total_As_between_Bs = 0
prev_B_index = -1  # 用来跟踪上一个B的位置

# 遍历排序后的AB序列
for i, (value, label) in enumerate(AB_sorted):
    if label == 'B':
        if prev_B_index != -1:
            # 检查两个B之间是否至少有两个A
            num_As = i - prev_B_index - 1
            if num_As >= 2:
                count_two_or_more_As_between_Bs += 1
                total_As_between_Bs += num_As
        prev_B_index = i

# 输出结果
print(f'总共{all_num}个数')
print(f"前一个B和后一个B之间至少有两个A的次数: {count_two_or_more_As_between_Bs}")
print(f"这些情况中的A总数: {total_As_between_Bs}")
print(f'成功测距率:{(all_num-total_As_between_Bs+count_two_or_more_As_between_Bs)/all_num}')

