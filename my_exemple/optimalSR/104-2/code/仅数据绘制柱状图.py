import matplotlib.pyplot as plt

# 数据定义
x_label = [5, 10, 15, 20, 25, 30]
y_recvRate = [0.95, 0.90, 0.85, 0.80, 0.75, 0.70]
y_rangingRate = [0.85, 0.75, 0.64, 0.52, 0.40, 0.32]

# 创建图表和轴对象
fig, ax = plt.subplots(figsize=(8, 6))

# 计算柱状图的宽度
bar_width = 2

# 绘制柱状图
bars1 = ax.bar([x + bar_width/2 for x in x_label], y_rangingRate, width=bar_width, label='Ranging Rate')
bars2 = ax.bar([x - bar_width/2 for x in x_label], y_recvRate, width=bar_width, label='Receive Rate')

ax.set_xlabel('Loss level(%)', fontsize=20)
ax.set_ylabel('Receive(Ranging) rate', fontsize=20)
ax.tick_params(axis='both', labelsize=14)

# 为柱状图的每个柱子添加数值标注
for bars in [bars1, bars2]:
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval, f'{yval:.2f}', ha='center', va='bottom', fontsize=14)

# 图例添加所有图形的标签
ax.legend(fontsize=16, ncol=1)
plt.yticks(fontsize=18)
plt.xticks(fontsize=18)

# 显示图表
plt.show()
