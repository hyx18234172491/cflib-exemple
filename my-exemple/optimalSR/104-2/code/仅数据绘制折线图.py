import matplotlib.pyplot as plt

# 数据定义
x_label = [5, 10, 15, 20, 25, 30]
y_recv_count = [1590.0, 1504, 1340, 1331, 1238, 1148]
y_recv_ranging = [1511, 1387, 1215, 1127, 986, 872]

# 创建图表和轴对象
fig, ax = plt.subplots(figsize=(8.7, 6.4))

# 绘制折线图
line1, = ax.plot(x_label, y_recv_count, 'r-',linewidth=2, label='Receive Count', marker='o')
line2, = ax.plot(x_label, y_recv_ranging, 'g-', linewidth=2,label='Receive Ranging', marker='s')

ax.set_xlabel('Loss level(%)', fontsize=20)
ax.set_ylabel('Receive(Ranging) count', fontsize=20)
ax.tick_params(axis='both', labelsize=18)

# 图例添加所有图形的标签
ax.legend(fontsize=18)
plt.grid(True)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
# 显示图表
plt.show()
