import matplotlib.pyplot as plt

# 数据定义
x_label = [70, 60, 50, 40, 30, 20]
y_recvPacketNum = [1428, 1659, 2001, 2499, 3333, 4999]  # 收包数量
y_rangingNum_var_SR1 = [1422, 1409, 1423, 1419, 1421, 1423]  # SR1 测距数量
y_rangingRate_SR1 = [y_rangingNum_var_SR1[i] / y_recvPacketNum[i] for i in range(0, len(x_label))]

y_rangingNum_var_SR2 = [1422, 1653, 1996, 2490, 2844, 2844]  # SR2 测距数量
y_rangingRate_SR2 = [y_rangingNum_var_SR2[i] / y_recvPacketNum[i] for i in range(0, len(x_label))]


# 绘图
plt.figure(figsize=(8, 6))
plt.plot(x_label, y_recvPacketNum, label='Reception count',
         linestyle='-.', marker='^', linewidth=2, markersize=10)
plt.plot(x_label, y_rangingNum_var_SR1, label='Ranging count(SRv1)',
         linestyle=':', marker='d', linewidth=2, markersize=10)
plt.plot(x_label, y_rangingNum_var_SR2, label='Ranging count(SRv2)',
         linestyle=':', marker='d', linewidth=2, markersize=10)

# 自定义图表
plt.xlabel('Period(ms)', fontsize=24)
plt.ylabel('Reception(Ranging) count', fontsize=24)
# plt.title('Packet and Ranging Numbers at Different Distances (Enhanced Markers)')
plt.legend(fontsize=22)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.subplots_adjust(left=0.145, right=0.99, top=0.999, bottom=0.112)
plt.gca().invert_xaxis()
plt.grid(True)

# 显示图表
plt.show()
