import matplotlib.pyplot as plt

# 数据定义
x_label = [5, 10, 15, 20, 25, 30]
y_recv_count_SR2 = [1590.0, 1504, 1404, 1331, 1238, 1148]
y_ranging_count_SR2_optimal1 = [1511, 1387, 1218, 1127, 986, 872]
y_ranging_count_SR2_optimal2 = [1584, 1498, 1385, 1320, 1214, 1120]

y_recv_count_SR1 = [1590.0, 1503, 1404, 1323, 1242, 1128]
y_ranging_count_SR1 = [1461, 1244, 1038, 870, 754, 606]

# 创建图表和轴对象
fig, ax = plt.subplots(figsize=(8.7, 6.4))

# 绘制折线图
line1, = ax.plot(x_label, y_recv_count_SR2, linewidth=2, label='Receive', marker='o')
line2, = ax.plot(x_label, y_ranging_count_SR1, linewidth=2,label='SR1.0 Ranging', marker='s')
line3, = ax.plot(x_label, y_ranging_count_SR2_optimal1, linewidth=2,label='SR2.0 without downward Ranging', marker='s')
line4, = ax.plot(x_label, y_ranging_count_SR2_optimal2, linewidth=2,label='SR2.0 Ranging', marker='s')

ax.set_xlabel('Loss level(%)', fontsize=20)
ax.set_ylabel('Receive(Ranging) count', fontsize=20)
ax.tick_params(axis='both', labelsize=18)

# 图例添加所有图形的标签
ax.legend(fontsize=18)
plt.grid(True)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
# 显示图表
plt.show()
