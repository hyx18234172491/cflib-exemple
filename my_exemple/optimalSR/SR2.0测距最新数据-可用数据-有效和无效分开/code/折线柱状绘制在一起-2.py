import matplotlib.pyplot as plt

# 数据定义
x_label = [5, 10, 15, 20, 25, 30]
y_rangingRate = [0.85, 0.75, 0.47, 0.52, 0.40, 0.32]
y_recv_count = [1590.0, 1504, 1240, 1331, 1238, 1148]
y_recv_ranging = [1511, 1387, 1015, 1127, 986, 872]
y_recvRate = [0.95, 0.90, 0.85, 0.80, 0.75, 0.70]  # 新增数据

# 创建图表和轴对象
fig, ax1 = plt.subplots(figsize=(10, 6.8))

# 计算柱状图的宽度，这里取总宽度的一半
bar_width = 2

# 绘制柱状图在主y轴
bars1 = ax1.bar([x + bar_width/2 for x in x_label], y_rangingRate, width=bar_width, label='Ranging Rate')
bars2 = ax1.bar([x - bar_width/2 for x in x_label], y_recvRate, width=bar_width, label='Receive Rate')

ax1.set_xlabel('Loss level(%)', fontsize=20)
ax1.set_ylabel('Rate', fontsize=20)
ax1.tick_params(axis='y', labelsize=14)
ax1.tick_params(axis='x', labelsize=14)

# 创建第二个y轴用于折线图，调整折线图的 x 坐标以匹配柱状图的中间位置
ax2 = ax1.twinx()
line1, = ax2.plot([x - bar_width/2 for x in x_label], y_recv_count, 'r-', label='Received Count', marker='o')
line2, = ax2.plot([x + bar_width/2 for x in x_label], y_recv_ranging, 'g-', label='Received Ranging', marker='s')
ax2.set_ylabel('Receive(Ranging) count', fontsize=20)
ax2.tick_params(axis='y', labelsize=14)
ax2.set_ylim(0, 1700)

# 为柱状图的每个柱子添加数值标注
for bars in [bars1, bars2]:
    for bar in bars:
        yval = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2, yval, f'{yval:.2f}', ha='center', va='bottom', fontsize=14)

# 图例添加所有图形的标签
lines = [bars1, bars2, line1, line2]
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper right', fontsize=16)

# 显示图表
plt.show()
