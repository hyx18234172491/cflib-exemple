import matplotlib.pyplot as plt

# 数据定义
x_labels = [5, 10, 15, 20, 25, 30]
y_rangingRate = [0.85, 0.75, 0.64, 0.52, 0.40, 0.32]
y_rangingRate_optimal1 = [0.91, 0.83, 0.73, 0.67, 0.58, 0.51]
y_rangingRate_optimal2 = [0.95, 0.89, 0.83, 0.77, 0.72, 0.65]
import matplotlib.pyplot as plt
import numpy as np


# 设置柱状图的宽度和x轴位置
bar_width = 0.20
spacing = 0.075
left_offset = -0  # 调整第一个柱子和图表左边界之间的空白
x = np.arange(len(x_labels)) + left_offset

# 创建柱状图
fig, ax1 = plt.subplots(figsize=(8.7, 6.4))

# 绘制每个系列的数据
bars1 = ax1.bar(x - 1.5 * (bar_width + spacing), y_rangingRate, width=bar_width, label='SR1 Ranging', edgecolor='black')
bars2 = ax1.bar(x - 0.5 * (bar_width + spacing), y_rangingRate_optimal1, width=bar_width, label='SR2 without downward Ranging', edgecolor='black')
bars3 = ax1.bar(x + 0.5 * (bar_width + spacing), y_rangingRate_optimal2, width=bar_width, label='SR2 Ranging', edgecolor='black')
# 设置x轴标签和刻度
ax1.set_xlabel('Loss level(%)', fontsize=20)
ax1.set_ylabel('Ranging Rate', fontsize=20)
ax1.set_xticks(x)
ax1.set_xticklabels(x_labels)
# ax1.set_ylim(0, 1.1)  # 调整y轴范围，使柱状图变矮
# ax1.set_xlim(-0.50, len(x_labels) - 0.57)  # 调整x轴范围，使边界更紧凑
# 设置x轴刻度标签字体大小
ax1.tick_params(axis='x', labelsize=20)
ax1.tick_params(axis='y', labelsize=20)

# 在每个柱子顶部添加数值标签
for bars in [bars1, bars2, bars3]:
    for bar in bars:
        yval = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width() / 2.0, yval, f'{yval:.2f}', va='bottom', ha='center', fontsize=14)

# # 创建第二个y轴并绘制 receive 和 ranging count 数据
# ax2 = ax1.twinx()
#
# # 绘制折线图
# line1, = ax2.plot(x - left_offset, SR1_receive_count, color='tab:blue', marker='o', label='SR1 Receive')
# line2, = ax2.plot(x - left_offset, SR2_receive_count, color='tab:orange', marker='s', label='SR2 Receive')
# line3, = ax2.plot(x - left_offset, SR1_ranging_count, color='tab:green', marker='^', label='SR1 Ranging')
# line4, = ax2.plot(x - left_offset, SR2_ranging_count, color='#FEDC5E', marker='D', label='SR2 Ranging')

# # 设置第二个y轴的标签和范围
# ax2.set_ylabel('Receive(Ranging) Count', fontsize=18)
# ax2.set_ylim(0, 1650)
# # 设置y轴刻度标签字体大小
# ax2.tick_params(axis='y', labelsize=16)

# 添加柱状图的图例
bars = [bars1, bars2, bars3]
labels_bars = [bar.get_label() for bar in [bars1, bars2, bars3]]
ax1.legend(bars, labels_bars, loc='upper right', fontsize='13.7')
# bbox_to_anchor=(0.5, 1.08)

# 添加折线图的图例
# lines = [line1, line2, line3, line4]
# labels_lines = [line.get_label() for line in lines]
# ax2.legend(lines, labels_lines, loc='upper center', bbox_to_anchor=(0.5, 1.16), ncol=4, fontsize='12')

# 显示图形
plt.tight_layout()
plt.show()
