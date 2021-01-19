# 开发者：Lingyu
# 开发时间：2021/1/18 17:13

import numpy as np
# 数组与数值之间的运算
t1 = np.arange(12).reshape(3, 4)
print('t1:', t1)
print(t1 + 2)
print(t1 * 2)
print(t1 / 2)
print(t1 / 0)  # nan: not a number; inf:infinite,无限的，无穷的
print('*'*100)

# 数组与数组之间的运算
t2 = np.arange(21, 33).reshape((3, 4))
print('t2:', t2)
print(t1+t2)
t3 = np.arange(0, 4)
print('t3:', t3)
print(t2+t3)
t4 = np.arange(3).reshape((3, 1))
print('t4:', t4)
print(t2+t4)


