import matplotlib.pyplot as plt

# 数据定义
x_label = [70, 60, 50, 40, 30, 20]
y_recvPacketNum_70_SR1 = [1429, 1415, 1429, 1429, 1428, 1429]
y_rangingNum_70_SR1 = [1423, 1409, 1422, 1420, 1421, 1423]
y_recvPacketNum_var_SR1 = [1428, 1659, 2001, 2499, 3333, 4999]
y_rangingNum_var_SR1 = [1422, 1409, 1423, 1419, 1421, 1423]

# 绘图
plt.figure(figsize=(8, 6))
plt.plot(x_label, y_recvPacketNum_70_SR1, label='Received Packet (variable period)',
         linestyle='-', marker='o', linewidth=2, markersize=10)
plt.plot(x_label, y_rangingNum_70_SR1, label='Ranging (variable period)',
         linestyle='--', marker='s', linewidth=2, markersize=10)
plt.plot(x_label, y_recvPacketNum_var_SR1, label='Received Packet (70ms period)',
        linestyle='-.', marker='^', linewidth=2, markersize=10)
plt.plot(x_label, y_rangingNum_var_SR1, label='Ranging (70ms period)',
         linestyle=':', marker='d', linewidth=2, markersize=10)

# 自定义图表
plt.xlabel('Period(ms)',fontsize=16)
plt.ylabel('Receive(Ranging) count',fontsize=16)
# plt.title('Packet and Ranging Numbers at Different Distances (Enhanced Markers)')
plt.legend()
plt.gca().invert_xaxis()
plt.grid(True)

# 显示图表
plt.show()
