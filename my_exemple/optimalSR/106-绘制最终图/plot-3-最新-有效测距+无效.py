import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
# 数据
SR1_receive_rate = [0.97, 0.94, 0.91, 0.86, 0.82]
SR2_receive_rate = [0.96, 0.92, 0.88, 0.84, 0.80]
SR1_ranging_rate = [0.77, 0.7, 0.64, 0.55, 0.48]
SR2_ranging_rate = [0.89, 0.84, 0.79, 0.75, 0.69]
# 将每个列表中的元素乘以 100
SR1_receive_rate = [x * 100 for x in SR1_receive_rate]
SR2_receive_rate = [x * 100 for x in SR2_receive_rate]
SR1_ranging_rate = [x * 100 for x in SR1_ranging_rate]
SR2_ranging_rate = [x * 100 for x in SR2_ranging_rate]

SR1_receive_count = [1622, 1583, 1520, 1433, 1367]
SR1_ranging_count = [1297, 1195, 1057, 929, 809]

SR2_receive_count = [1617, 1563, 1495, 1421, 1348]
SR2_ranging_count = [1490, 1412, 1314, 1261, 1143]

x_labels = [5, 10, 15, 20, 25]

# 设置柱状图的宽度和x轴位置
bar_width = 0.16
spacing = 0.0
x = np.arange(len(x_labels))

# 创建柱状图
fig, ax1 = plt.subplots(figsize=(9, 5))

# 绘制每个系列的数据
bars1 = ax1.bar(x - 1.5 * (bar_width + spacing), SR1_receive_rate, width=bar_width, label='SRv1 Reception',
                )
bars3 = ax1.bar(x - 0.5 * (bar_width + spacing), SR1_ranging_rate, width=bar_width, label='SRv1 Ranging',
                )
bars2 = ax1.bar(x + 0.5 * (bar_width + spacing), SR2_receive_rate, width=bar_width, label='SRv2 Ranging all',
                )

bars4 = ax1.bar(x + 1.5 * (bar_width + spacing), SR2_ranging_rate, width=bar_width, color="#FEDC5E",
                label='SRv2 Ranging valid', )

# 设置x轴标签和刻度
ax1.set_xlabel('Number of UAVs', fontsize=18)
ax1.set_ylabel('Reception(Ranging) Rate(%)', fontsize=18)
ax1.set_xticks(x)
ax1.set_xticklabels(x_labels)
ax1.set_ylim(0, 114)  # 调整y轴范围，使柱状图变矮
# 设置x轴刻度标签字体大小
ax1.tick_params(axis='x', labelsize=14)
ax1.tick_params(axis='y', labelsize=14)
ax2 = ax1.twinx()

# 绘制折线图
line1, = ax2.plot(x, SR1_receive_count, color='tab:blue', marker='o', markersize=6, label='SRv1 Reception')
line3, = ax2.plot(x, SR1_ranging_count, color='tab:orange', marker='^', markersize=6, label='SRv1 Ranging')
line2, = ax2.plot(x, SR2_receive_count, color='tab:green', marker='s', markersize=6, label='SRv2 Ranging all')
line4, = ax2.plot(x, SR2_ranging_count, color='#FEDC5E', marker='D', markersize=6, label='SRv2 Ranging valid')
# 添加折线图的图例
lines = [line1, line3, line2, line4]
labels_lines = [line.get_label() for line in lines]
ax2.legend(lines, labels_lines, loc='upper center', bbox_to_anchor=(0.5, 1.18), ncol=4, fontsize='12.5')

# 在每个柱子顶部添加数值标签
for bars in [bars1, bars3, bars2, bars4]:
    for bar in bars:
        yval = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width() / 2.0, yval, f'{yval:.0f}', va='bottom', ha='center', fontsize=16)

# 创建第二个y轴并绘制 receive 和 ranging count 数据

# 设置第二个y轴的标签和范围
ax2.set_ylabel('Reception(Ranging) Count', fontsize=18)
ax2.set_ylim(0, 1650)
# 设置y轴刻度标签字体大小
ax2.tick_params(axis='y', labelsize=14)

# 添加柱状图的图例
bars = [bars1, bars3,bars2, bars4]
labels_bars = [bar.get_label() for bar in [bars1, bars3,bars2, bars4]]
ax1.legend(bars, labels_bars, loc='upper center', bbox_to_anchor=(0.5, 1.1), ncol=4, fontsize='12.5')
axins = inset_axes(ax1, width="80%", height="38%",bbox_to_anchor=(-0.1, -0.603, 1, 1), bbox_transform=ax1.transAxes)
# axins = inset_axes(ax1, width="80%", height="38%", bbox_to_anchor=(0.5, 0.5, 0.2, 0.4))
img = mpimg.imread('B.png')
axins.imshow(img)
axins.axis('off')  # 关闭轴标签显示
# 显示图形
plt.subplots_adjust(left=0.09, right=0.9, top=0.88, bottom=0.11)
plt.show()
