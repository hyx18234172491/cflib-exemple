import matplotlib.pyplot as plt
import numpy as np

# 数据
SR1_receive_rate = [0.97, 0.94, 0.91, 0.89, 0.86]
SR2_receive_rate = [0.98, 0.94, 0.91, 0.87, 0.83]
SR1_ranging_rate = [0.77, 0.7, 0.64, 0.57, 0.35]
SR2_ranging_rate = [0.97, 0.93, 0.89, 0.86, 0.81]

SR1_receive_count = [1622, 1583, 1520, 1488, 1437]
SR1_ranging_count = [1297, 1195, 1057, 639, 447]

SR2_receive_count = [1624, 1572, 1516, 1450, 1386]
SR2_ranging_count = [1610, 1533, 1471, 1417, 1338]

x_labels = [5, 10, 15, 20, 25]

# 设置柱状图的宽度和x轴位置
bar_width = 0.13
spacing = 0.08
x = np.arange(len(x_labels))

# 创建柱状图
fig, ax1 = plt.subplots(figsize=(10.3, 6))

# 绘制每个系列的数据
bars1 = ax1.bar(x - 1.5 * (bar_width + spacing), SR1_receive_rate, width=bar_width, label='SR1 Receive', edgecolor='black')
bars2 = ax1.bar(x - 0.5 * (bar_width + spacing), SR2_receive_rate, width=bar_width, label='SR2 Receive', edgecolor='black')
bars3 = ax1.bar(x + 0.5 * (bar_width + spacing), SR1_ranging_rate, width=bar_width, label='SR1 Ranging', edgecolor='black')
bars4 = ax1.bar(x + 1.5 * (bar_width + spacing), SR2_ranging_rate, width=bar_width, color = "#FEDC5E",label='SR2 Ranging', edgecolor='black')

# 设置x轴标签和刻度
ax1.set_xlabel('Number of UAVs', fontsize=18)
ax1.set_ylabel('Receive(Ranging) Rate', fontsize=18)
ax1.set_xticks(x)
ax1.set_xticklabels(x_labels)
ax1.set_ylim(0, 1.1)  # 调整y轴范围，使柱状图变矮
# 设置x轴刻度标签字体大小
ax1.tick_params(axis='x', labelsize=12)
ax1.tick_params(axis='y', labelsize=12)

# 在每个柱子顶部添加数值标签
for bars in [bars1, bars2, bars3, bars4]:
    for bar in bars:
        yval = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width() / 2.0, yval, f'{yval:.2f}', va='bottom', ha='center', fontsize=12)

# 创建第二个y轴并绘制 receive 和 ranging count 数据
ax2 = ax1.twinx()

# 绘制折线图
line1, = ax2.plot(x, SR1_receive_count, color='tab:blue', marker='o', label='SR1 Receive')
line2, = ax2.plot(x, SR2_receive_count, color='tab:orange', marker='s', label='SR2 Receive')
line3, = ax2.plot(x, SR1_ranging_count, color='tab:green', marker='^', label='SR1 Ranging')
line4, = ax2.plot(x, SR2_ranging_count, color='#FEDC5E', marker='D', label='SR2 Ranging')

# 设置第二个y轴的标签和范围
ax2.set_ylabel('Receive(Ranging) Count', fontsize=18)
ax2.set_ylim(0, 1650)
# 设置y轴刻度标签字体大小
ax2.tick_params(axis='y', labelsize=12)

# 添加柱状图的图例
bars = [bars1, bars2, bars3, bars4]
labels_bars = [bar.get_label() for bar in [bars1, bars2, bars3, bars4]]
ax1.legend(bars, labels_bars, loc='upper center', bbox_to_anchor=(0.5, 1.08), ncol=4, fontsize='12')

# 添加折线图的图例
lines = [line1, line2, line3, line4]
labels_lines = [line.get_label() for line in lines]
ax2.legend(lines, labels_lines, loc='upper center', bbox_to_anchor=(0.5, 1.16), ncol=4, fontsize='12')

# 显示图形
plt.tight_layout()
plt.show()
