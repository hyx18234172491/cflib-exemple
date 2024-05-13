# 定义初始坐标列表
initDist = 0.4
coordinates = [
    (0.0, 0.0, 0.0),                   # 0
    (0.0, -initDist, 0.0),             # 1
    (-initDist, -initDist, 0.0),       # 2
    (-initDist, 0.0, 0.0),             # 3
    (-initDist, initDist, 0.0),        # 4
    (0.0, initDist, 0.0),              # 5
    (initDist, initDist, 0.0),         # 6
    (initDist, 0.0, 0.0),              # 7
    (initDist, -initDist, 0.0),        # 8
]

# 指定起始位置
start_point = 3

# 从起始位置开始构建循环列表
looped_coordinates = coordinates[start_point:] + coordinates[:start_point]

# 输出循环列表
print(looped_coordinates)