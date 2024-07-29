import matplotlib.pyplot as plt

# 数据定义
x_label = [5, 10, 15, 20, 25, 30]
y_recvRate = [0.95, 0.90, 0.84, 0.79, 0.75, 0.68]
y_rangingRate = [0.88, 0.75, 0.62, 0.52, 0.45, 0.36]

y_rangingRate_optimal1 = [0.91, 0.83, 0.73, 0.67, 0.58, 0.51]
y_rangingRate_optimal2 = [0.95, 0.90, 0.83, 0.77, 0.71, 0.66]
# 创建图表和轴对象
fig, ax = plt.subplots(figsize=(8, 6))

# 计算柱状图的宽度
bar_width = 2.1

# 绘制柱状图
bars1 = ax.bar([x - bar_width/2 for x in x_label], y_rangingRate, width=bar_width, label='SRv1')
bars2 = ax.bar([x + bar_width/2 for x in x_label], y_rangingRate_optimal2, width=bar_width, label='SRv2')

ax.set_xlabel('Loss level(%)', fontsize=25)
ax.set_ylabel('Ranging rate', fontsize=25)
ax.tick_params(axis='both', labelsize=14)
ax.set_ylim(0, 1.04)
# 为柱状图的每个柱子添加数值标注
for bars in [bars1, bars2]:
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2-0.2, yval, f'{yval:.2f}', ha='center', va='bottom', fontsize=20)

# 图例添加所有图形的标签
ax.legend(fontsize=24, ncol=1)
plt.yticks(fontsize=20)
plt.xticks(fontsize=20)
plt.subplots_adjust(left=0.12, right=0.99, top=0.99, bottom=0.13)
# 显示图表
plt.show()
