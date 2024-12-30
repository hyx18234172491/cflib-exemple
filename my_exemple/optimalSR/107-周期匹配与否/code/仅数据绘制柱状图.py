from matplotlib import pyplot as plt

# 定义数据
x_positions = [70, 60, 50, 40, 30, 20]  # 用于定位柱状图的 x 位置
y_rangingRate_70msPeriod = [0.28, 0.43, 0.57, 0.71, 0.85, 1]
y_rangingRate_varPeriod = [1, 1, 0.99, 1, 0.99, 1]
y_rangingRate_70msPeriod = [x * 100 for x in y_rangingRate_70msPeriod]
y_rangingRate_varPeriod = [x * 100 for x in y_rangingRate_varPeriod]
# 定义柱状图宽度
bar_width = 4

# 创建柱状图
fig, ax = plt.subplots(figsize=(8, 6))
bars1 = plt.bar([x - bar_width/2 for x in x_positions], y_rangingRate_70msPeriod, width=bar_width, label='70 ms Period')
bars2 = plt.bar([x + bar_width/2 for x in x_positions], y_rangingRate_varPeriod, width=bar_width, label='Variable Period')

# 为每个柱子添加数值标注
for bars in [bars1, bars2]:
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, f'{yval:.0f}', ha='center', va='bottom', fontsize=18)
ax.set_ylim(0, 108)
# 自定义 x 轴为字符串
labels = ['20', '30', '40', '50', '60', '70']  # 转换为字符串，按照期望顺序
plt.xlabel('Period(ms)', fontsize=24)
plt.ylabel('Ranging Rate(%)', fontsize=24)
plt.xticks(x_positions, labels, fontsize=18)  # 使用字符串标签
plt.yticks(fontsize=18)
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.16), ncol=2, fontsize=22)  # Legend placed at the top center
plt.subplots_adjust(left=0.12, right=0.99, top=0.89, bottom=0.12)
# 显示图表
plt.show()
