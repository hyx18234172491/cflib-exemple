import matplotlib.pyplot as plt

# 数据定义
x_label = [5, 10, 15, 20, 25, 30]
y_recv_count_SR2 = [1583.0, 1507, 1408, 1326, 1230, 1149]
# y_ranging_count_SR2_optimal1 = [1511, 1387, 1218, 1127, 986, 872]
y_ranging_count_SR2_optimal2 = [1574, 1494, 1381, 1288, 1174, 1101]

y_recv_count_SR1 = [1590.0, 1503, 1404, 1323, 1242, 1128]
y_ranging_count_SR1 = [1461, 1244, 1038, 870, 754, 606]

# 创建图表和轴对象
fig, ax = plt.subplots(figsize=(8, 6))

# 绘制折线图
line1, = ax.plot(x_label, y_recv_count_SR2, linewidth=2, label='Receive', marker='o')
line2, = ax.plot(x_label, y_ranging_count_SR1, linewidth=2,label='SRv1 Ranging', marker='s')
# line3, = ax.plot(x_label, y_ranging_count_SR2_optimal1, linewidth=2,label='SR2.0 without downward Ranging', marker='s')
line4, = ax.plot(x_label, y_ranging_count_SR2_optimal2, linewidth=2,label='SRv2 Ranging', marker='s')

ax.set_xlabel('Loss level(%)', fontsize=26)
ax.set_ylabel('Receive(Ranging) count', fontsize=26)
ax.tick_params(axis='both', labelsize=18)
plt.subplots_adjust(left=0.145, right=0.99, top=0.999, bottom=0.13)
# 图例添加所有图形的标签
ax.legend(fontsize=24)
plt.grid(True)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
# 显示图表
plt.show()
