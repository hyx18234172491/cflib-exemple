# 模拟3*3旋转
MY_UWB_ADDRESS = 1

INNER_3_3_NUM = 3*3
INNER_3_3_START = 1

OUTER5_5_NUM = 5*5 - INNER_3_3_NUM
OUTER5_5_START = INNER_3_3_NUM
for targetShift in range(0, 20):
    index = (MY_UWB_ADDRESS - INNER_3_3_START + targetShift//2) % (INNER_3_3_NUM-1) + INNER_3_3_START
    print(index)
print('------------')

MY_UWB_ADDRESS = 9
for targetShift in range(0, 30):
    index = (MY_UWB_ADDRESS - OUTER5_5_START + targetShift) % (OUTER5_5_NUM-1) + OUTER5_5_START
    print(index)
