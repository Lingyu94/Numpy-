# 开发者：Lingyu
# 开发时间：2021/1/18 15:24

import numpy as np

t1 = np.arange(12)  # t1为一维数组
print(t1)
print(t1.shape)
t2 = np.array([[1, 2, 3], [4, 5, 6]])
print(t2)
print(t2.shape)  # t2为二维数组，2为行数，3为列数
t3 = np.array([[[1, 2, 3, 4], [5, 6, 7, 8]], [[9, 10, 11, 12], [13, 14, 15, 16]]])
print(t3)
print(t3.shape)  # t3为三维数组，第二个2为行数，4为列数
print('*' * 100)

# 修改数组形状
t1 = np.arange(12)  # t1为一维数组
print(t1)
print(t1.shape)
t4 = t1.reshape((3, 4))
print(t4)
print(t4.shape)
print('*' * 100)
t5 = np.arange(60).reshape((3, 4, 5))
print(t5)
t6 = t5.reshape(3, 20)  # 有返回值，只是t5的形状变了，t5数组本身没有变；若无返回值，则为原地修改，t5数组本身发生变化，如：t5 = t5.reshape(3, 20)
print(t6)
t7 = t5.reshape((60,))  # t7为一维数组
t8 = t5.reshape([1, 60])  # t8为二维数组
print(t7)
print(t8)
t9 = t8.reshape((t8.shape[0]*t8.shape[1],))  # t9为一维数字，t8.shape[0]为t8的行数，t8.shape[1]为t8的列数
t10 = t8.flatten()  # 将数组以一维的形状展开
print(t8)
print(t9)
print(t10)
