# 开发者：Lingyu
# 开发时间：2021/1/19 10:13

import numpy as np

# Numpy读取本地数据
us_file_path = "F:/shuju.csv"
t1 = np.loadtxt(us_file_path, dtype=np.float, delimiter=',', skiprows=1)
print(t1)
print('*' * 100)

# 取数组中的某一行,第一行是0行
print(t1[0])  # 取第1行记录 == print(t1[0, :]) , :表示列全取
print('*' * 100)
print(t1[8:])  # 取第9行及以后连续的记录
print('*' * 100)
print(t1[[4, 8, 10], :])  # 取第5、9、11行不连续的记录
print('*' * 100)

#  取数组中的某一列,第一列是0列
print(t1[:, 2])  # 取第3列
print('*' * 100)
print(t1[:, 2:])  # 取第3列及以后连续的记录
print('*' * 100)
print(t1[:, [1, 3]])  # 取第2,4列不连续的记录
print('*' * 100)

#  取数组中的某一行及某一列的数值
t2 = t1[2, 3]  # 取数组中的第三行、第四列的数值
print('t2:', t2)
print(type(t2))
print('*' * 100)

#  取数组中的多行及多列，取的是行和列交差点的位置
t3 = t1[1:6, 1:3]  # 取第2行到第6行，第2列到第3列
print(t3)
print(type(t3))
print('*' * 100)

# 取数组中多个不相邻的点
t4 = t1[[2, 3], [1, 2]]  # 取数组中第3行第2列、第4行第3列的结果
print(t4)
print(type(t4))
