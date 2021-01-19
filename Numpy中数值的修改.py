# 开发者：Lingyu
# 开发时间：2021/1/19 13:59

import numpy as np

t1 = np.arange(24).reshape(4, 6)
print(t1)
t2 = t1[1:4, 2:5]
print(t2)
print('*' * 100)
t1[0:4, 2:5] = 3  # 将数组中1-4行、3-5列中的数值替换成3
print(t1)
print(t2)  # t1变了，所以t2也跟着变了
print('*' * 100)

# 将t1中数值小于8的替换成4
print(t1 < 8)  # Numpy中的布尔索引
t1[t1 < 8] = 4
print(t1)
print('*' * 100)

# 将t1中数值小于8的替换成0,大于等于8的替换成1
# (1) Numpy中的布尔索引
t1[t1 < 8] = 0
t1[t1 >= 8] = 1
print(t1)
# (2)使用np.where:三元运算符
np.where(t1 < 8, 0, 1)
print(t1)
print('*' * 100)

# 将t1中数值小于8的替换成8,大于12的替换成12
t1 = np.arange(24).reshape((4, 6))
print(t1)
t1 = t1.clip(8, 12)
print(t1)
print('*' * 100)

# 查看及修改t1类型
t1 = np.arange(24).reshape(4, 6)
print(t1.shape)
print(t1.dtype)
t1 = t1.astype(float)  # t1变为浮点数
t1 = np.round(t1, 2)  # t1保留两位小数
print(t1)
print(t1.dtype)
print(t1.shape)
