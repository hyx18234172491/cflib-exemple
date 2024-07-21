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
bar_width = 0.2
x = np.arange(len(x_labels))

# 创建柱状图
fig, ax = plt.subplots(figsize=(12, 6))

# 绘制每个系列的数据
bars1 = ax.bar(x - bar_width, SR1_receive_rate, width=bar_width, label='SR1 Receive', alpha=0.8, hatch='xx')
bars2 = ax.bar(x, SR2_receive_rate, width=bar_width, label='SR2 Receive', alpha=0.8, hatch='\\')
bars3 = ax.bar(x + bar_width, SR1_ranging_rate, width=bar_width, label='SR1 Ranging', alpha=0.8, hatch='xx')
bars4 = ax.bar(x + 2 * bar_width, SR2_ranging_rate, width=bar_width, label='SR2 Ranging', alpha=0.8, hatch='\\')

# 设置x轴标签和刻度
ax.set_xlabel('Number of UAVs')
ax.set_ylabel('Receive(Ranging) Rate')
# ax.set_title('Rates by Distance')
ax.set_xticks(x + bar_width / 2)
ax.set_xticklabels(x_labels)

# 添加图例
ax.legend()

# 在每个柱子顶部添加数值标签
for bars in [bars1, bars2, bars3, bars4]:
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2.0, yval, f'{yval:.2f}', va='bottom', ha='center', fontsize=12)
# 添加图例，设置为1行4列
# ax.legend(ncol=4, loc='upper right', bbox_to_anchor=(0.5, 1.1))
ax.legend(ncol=4, loc='upper right', fontsize='12')
# 显示图形
plt.tight_layout()
plt.show()
