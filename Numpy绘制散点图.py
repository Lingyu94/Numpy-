# 开发者：Lingyu
# 开发时间：2021/1/22 20:04
import numpy as np
from matplotlib import pyplot as plt

file_path = 'F:/shuju.csv'
t1 = np.loadtxt(file_path, dtype='int', delimiter=',', skiprows=1)  # 读取文件shuju.csv，赋值为t1
print(t1)
print('*'*50)
t1 = t1[t1[:, 0] <= 25]  # 选取年龄小于等于25的数据
t1_age = t1[:, 0]    # 选取第一列年龄，赋值为t1_age
t1_eGFR = t1[:, -1]   # 选取最后一列eGFR，赋值为t1_eGFR
plt.figure(figsize=(10, 8), dpi=300)  # 设置图形大小，像素
plt.scatter(t1_age, t1_eGFR)    # 绘制散点图，逗号前为X轴，逗号后为Y轴

plt.show()
