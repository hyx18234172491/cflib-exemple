# python中没有类型的概念
# list

test1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
test2 = [1, 2, 3, 4, 5, [6, "bc"], 7, "abc", 9]

# print(test1[3]) # 用下标取

# print(len(test2))

# test2[5] = 1000
# print(test2)

# for item in test2:
#     print(item)
#
# for i in range(0, len(test1)):
#     print(test1[i])

# range函数：第一个参数：起始位置，第二个参数终止位置,第三个参数是步长（如果不写，默认是1）
# range(1,3): 1,2
# range(0,7):0,1,2,3,4,5,6
# range(0,7,2) : 0, 2, 4, 6

# dict 字典,dict不能通过index进行访问
# 其实就是我们的哈希
test_dict1 = {"202401": 18, "202402": "fgh"}
# key, value
for key,value in test_dict1.items():
    print(key, value)

test_dict1["202401"] = 19
print(test_dict1)
