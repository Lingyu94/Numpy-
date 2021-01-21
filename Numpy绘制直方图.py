# 开发者：Lingyu
# 开发时间：2021/1/21 22:03
import numpy as np
from matplotlib import pyplot as plt
file_path = 'F:/shuju.csv'
t1 = np.loadtxt(file_path, dtype=np.int, delimiter=',', skiprows=1)
print(t1)
print('*' * 50)
t1_age = t1[:, 0]  # 取数组t1里面的最后一列，即eGFR
print(t1_age)
print(t1_age.max(), t1_age.min())  # 看一下age最大值及最小值，用于参考设定Y
print(len(t1))  # 看一下t1的行数
bin_nums = len(t1)  # 设定组数=行数=人数

# 绘制直方图
plt.figure(figsize=(30, 8), dpi=300)

plt.hist(t1_age, bin_nums)

plt.show()