import matplotlib.pyplot as plt

# 数据定义
x_label = [5, 10, 15, 20, 25, 30]
y_recv_count_SR2 = [1590.0, 1504, 1404, 1331, 1238, 1148]
y_ranging_count_SR2_optimal1 = [1511, 1387, 1218, 1127, 986, 872]
y_ranging_count_SR2_optimal2 = [1584, 1498, 1385, 1320, 1214, 1120]

y_recv_count_SR1 = [1590.0, 1503, 1404, 1323, 1242, 1128]
y_ranging_count_SR1 = [1461, 1244, 1038, 870, 754, 606]

# 创建图表和轴对象
fig, ax = plt.subplots(figsize=(8, 6))

# 绘制折线图
line1, = ax.plot(x_label, y_recv_count_SR2, linewidth=2, label='Reception', marker='o')
line2, = ax.plot(x_label, y_ranging_count_SR1, linewidth=2,label='SRv1 Ranging', marker='s')
# line3, = ax.plot(x_label, y_ranging_count_SR2_optimal1, linewidth=2,label='SR2.0 without downward Ranging', marker='s')
line4, = ax.plot(x_label, y_ranging_count_SR2_optimal2, linewidth=2,label='SRv2 Ranging', marker='s')

ax.set_xlabel('Loss level(%)', fontsize=24)
ax.set_ylabel('Reception(Ranging) count', fontsize=24)
ax.tick_params(axis='both', labelsize=18)
plt.subplots_adjust(left=0.14, right=0.99, top=0.999, bottom=0.13)
# 图例添加所有图形的标签
ax.legend(fontsize=24)
plt.grid(True)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
# 显示图表
plt.show()
