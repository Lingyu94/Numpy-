# 开发者：Lingyu
# 开发时间：2021/1/19 16:04

import numpy as np

t1 = np.arange(12).reshape(2, 6)
t2 = np.arange(12, 24).reshape(2, 6)
print('t1:', t1)
print('*' * 50)
print('t2:', t2)
print('*' * 50)

# 数组的拼接
t3 = np.vstack((t1, t2))  # 竖直拼接（vertically），两数组每一列代表意义一样
t4 = np.vstack((t2, t1))
t5 = np.hstack((t1, t2))  # 水平拼接（horizontally），两数组每一行代表意义一样
t6 = np.hstack((t2, t1))
print('t3:', t3)
print('*' * 50)
print('t4:', t4)
print('*' * 50)
print('t5:', t5)
print('*' * 50)
print('t6:', t6)
print('*' * 50)

# 数组的行列交换，拼接时两数组对应的行或列意义不同
t7 = np.arange(12).reshape(3, 4)
t8 = np.arange(12, 24).reshape(3, 4)
print(t7)
print('*' * 50)
print(t8)
print('*' * 50)
t7[[0, 2], :] = t7[[2, 0], :]  # t7的第1行和第3行交换
t8[:, [1, 3]] = t8[:, [3, 1]]  # t8的第2列和第4列交换
print('t7:', t7)
print('*' * 50)
print('t8:', t8)
print('*' * 50)

# 数据拼接练习
a_file_path = 'F:/shuju.csv'
t9 = np.loadtxt(a_file_path, dtype=np.float, delimiter=',', skiprows=1)
print('t9:', t9)
b_file_path = 'F:/shuju2.csv'
t10 = np.loadtxt(b_file_path, dtype=np.float, delimiter=',', skiprows=1)
print('t10:', t10)
t10[:, [1, 2]] = t10[:, [2, 1]]
print('t10:', t10)
print('*' * 50)
# t9(0)与t10(1)加上一列分组信息
zeros = np.zeros((t9.shape[0], 1)).astype(float)  # 构建一列0，行数与t9的行数一样
ones = np.ones((t10.shape[0], 1)).astype(float)  # 构建一列1，行数与t10的行数一样
print('zeros:', zeros)
print('*' * 50)
print('ones:', ones)
print('*' * 50)
t11 = np.hstack((zeros, t9))
t12 = np.hstack((ones, t10))
t13 = np.vstack((t11, t12))
print('t13:', t13)
print('*' * 50)

# 创建一个三行四列的全为0的矩阵
t14 = np.zeros((3, 4))
print(t14)
print('*' * 50)

# 创建一个三行四列的全为1的矩阵
t15 = np.ones((3, 4))
print(t15)
print('*' * 50)

# 创建一个对角线为1其余为0的正方形矩阵
t16 = np.eye(6)
print(t16)
print('*' * 50)

# 获取最大值及最小值的位置
t17 = np.eye(4)
print(t17)
print((np.argmax(t17, axis=0)))  # 数组t17里0轴(行）中最大值的位置
print((np.argmin(t17, axis=1)))  # 数组t17里1轴(列）中最大值的位置
t17[t17 == 1] = -1  # 数组t17里1替换成-1
print('t17:', t17)
t18 = np.array([1, 3, 6, 8, 2, 4, 9, 3, 5, 4, 2, 10, 7, 9, 4, 9, ]).reshape(4,4)
print(t18)
print((np.argmax(t18, axis=0)))
print((np.argmin(t18, axis=1)))