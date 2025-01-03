import matplotlib.pyplot as plt

# 数据定义
x_label = [5, 10, 15, 20, 25, 30]
y_recvRate = [0.95, 0.90, 0.84, 0.79, 0.75, 0.68]
y_rangingRate = [0.88, 0.75, 0.62, 0.52, 0.45, 0.36]
y_recvRate = [x * 100 for x in y_recvRate]
y_rangingRate = [x * 100 for x in y_rangingRate]
# 创建图表和轴对象
fig, ax = plt.subplots(figsize=(8, 6))

# 计算柱状图的宽度
bar_width = 2

# 绘制柱状图
bars1 = ax.bar([x + bar_width/2 for x in x_label], y_rangingRate, width=bar_width, label='Ranging')
bars2 = ax.bar([x - bar_width/2 for x in x_label], y_recvRate, width=bar_width, label='Reception')

ax.set_xlabel('Loss level(%)', fontsize=24)
ax.set_ylabel('Reception(Ranging) rate(%)', fontsize=24)
ax.tick_params(axis='both', labelsize=14)

# 为柱状图的每个柱子添加数值标注
for bars in [bars1, bars2]:
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval, f'{yval:.0f}', ha='center', va='bottom', fontsize=22)
ax.set_ylim(0, 105)
# 图例添加所有图形的标签
ax.legend(fontsize=20, ncol=1)
plt.yticks(fontsize=18)
plt.xticks(fontsize=18)
plt.subplots_adjust(left=0.123, right=0.99, top=0.99, bottom=0.12)

# 显示图表
plt.show()
