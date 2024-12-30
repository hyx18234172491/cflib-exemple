import matplotlib.pyplot as plt

# 数据定义
x_label = [5, 10, 15, 20, 25, 30]
y_recv_count = [1590.0, 1504, 1404, 1331, 1238, 1128]
y_recv_ranging = [1461, 1244, 1038, 870, 754, 606]

# 创建图表和轴对象
fig, ax = plt.subplots(figsize=(8, 6))

# 绘制折线图
line1, = ax.plot(x_label, y_recv_count, 'r-',linewidth=2, label='Reception Count', marker='o')
line2, = ax.plot(x_label, y_recv_ranging, 'g-', linewidth=2,label='Ranging Count', marker='s')

ax.set_xlabel('Loss level(%)', fontsize=24)
ax.set_ylabel('Reception(Ranging) count', fontsize=24)
ax.tick_params(axis='both', labelsize=18)

# 图例添加所有图形的标签
ax.legend(fontsize=24)
plt.grid(True)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
# 显示图表
plt.subplots_adjust(left=0.145, right=0.99, top=0.999, bottom=0.112)
plt.show()
