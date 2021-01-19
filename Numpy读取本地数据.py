# 开发者：Lingyu
# 开发时间：2021/1/19 9:01

import numpy as np
# Numpy读取本地数据
us_file_path = "F:/shuju.csv"
t1 = np.loadtxt(us_file_path, dtype=np.float, delimiter=',', skiprows=1, )
print(t1)
print('*' * 100)
t2 = np.loadtxt(us_file_path, dtype=np.float, delimiter=',', skiprows=1, unpack=True)
print(t2)

# 转置
t3 = np.arange(24).reshape((4, 6))
print('t3:', t3)
print(t3.transpose())
print(t3.T)
print(t3.swapaxes(1, 0))



