import matplotlib.pyplot as plt

# 数据定义
x_label = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
y_recv_fix = [10004, 5002, 3309, 2481, 1983, 1657, 1419, 1239, 1102, 994][::-1]
y_ranging_all_fix_SRV2 = [9998, 4996, 3303, 2475, 1977, 1651, 1413, 1233, 1096, 988][::-1]
y_ranging_valid_fix_SRV2 = [1987, 1994, 1961, 1967, 1969, 1647, 1408, 1231, 1095, 988][::-1]
y_ranging_fix_SRV1 = [994, 994, 978, 981, 987, 987, 987, 987, 991, 986][::-1]

x_label = x_label[:-2:]
y_recv_fix = y_recv_fix[:-2:]
y_ranging_all_fix_SRV2 = y_ranging_all_fix_SRV2[:-2:]
y_ranging_valid_fix_SRV2 = y_ranging_valid_fix_SRV2[:-2:]
y_ranging_fix_SRV1 = y_ranging_fix_SRV1[:-2:]

y_rangingRate_SR1 = [y_ranging_fix_SRV1[i] / y_recv_fix[i] for i in range(0, len(x_label))]
y_rangingRate_SR2 = [y_ranging_valid_fix_SRV2[i] / y_recv_fix[i] for i in range(0, len(x_label))]
fig, ax1 = plt.subplots(figsize=(8, 6))

# ax1.plot(x_label, y_recv_fix, label='Reception count',
#          marker='^', linewidth=2, markersize=10)
# ax1.plot(x_label, y_ranging_fix_SRV1, label='Ranging count(SRv1)',
#          marker='d', linewidth=2, markersize=10)
# ax1.plot(x_label, y_ranging_valid_fix_SRV2, label='Ranging count(SRv2)',
#          marker='d', linewidth=2, markersize=10)

# ax1.plot(x_label, y_recv_fix, label='Reception count',
#          linestyle='-.', marker='^', linewidth=2, markersize=10)
# ax1.plot(x_label, y_ranging_fix_SRV1, label='Ranging count(SRv1)',
#          linestyle=':', marker='d', linewidth=2, markersize=10)
# ax1.plot(x_label, y_ranging_valid_fix_SRV2, label='Ranging count(SRv2)',
#          linestyle=':', marker='d', linewidth=2, markersize=10)

# 设置x轴标签和刻度
ax1.set_xlabel('Period(ms)', fontsize=24)
ax1.set_ylabel('Ranging rate', fontsize=24)

ax1.plot(x_label, y_rangingRate_SR1, label='Ranging rate(SRv1)',
         linestyle='-', marker='d', linewidth=2, markersize=10)
ax1.plot(x_label, y_rangingRate_SR2, label='Ranging rate(SRv2)',
         linestyle='-', marker='d', linewidth=2, markersize=10)

ax1.axvline(x=50, color='r', linestyle='--', label='M=2')

# 自定义图表
plt.xlabel('Period(ms)', fontsize=24)
plt.ylabel('Ranging rate', fontsize=24)
# plt.title('Packet and Ranging Numbers at Different Distances (Enhanced Markers)')
plt.legend(fontsize=22)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.subplots_adjust(left=0.145, right=0.99, top=0.99, bottom=0.12)
plt.gca().invert_xaxis()
plt.grid(True)

# 显示图表
plt.show()
