# 开发者：Lingyu
# 开发时间：2020/12/26 9:56
# Location：C:\Users\admin\anaconda3\envs\Numpy
# Conda executable：C:\Users\admin\anaconda3\Scripts\conda.exe

# 创建数组，得到ndarray的数据类型
from random import random

import numpy as np

a = np.array([1, 2, 3, 4, 5, 6, 7, ])
b = np.array(range(1, 8))
c = np.arange(1, 8)
#  a, b, c内容相同
d = np.arange(2, 24, 2)  # 2为步长
print(a, b, c, d)
print(type(a), type(b), type(c), type(d))
print('*' * 100)

# numpy中的数据类型
t1 = np.array(range(1, 4), dtype=float)
print(t1)
print(t1.dtype)
t2 = np.array(range(1, 6), dtype='float32')  # 指定数据类型
print(t2)
print(t2.dtype)
t3 = np.array(range(3, 6), dtype='i1')  # 1个字节对应8位
print(t3)
print(t3.dtype)
print('*' * 100)

# numpy中的布尔类型
t4 = np.array([1, 0, 1, 1, 0, ], dtype=bool)
print(t4)
print(t4.dtype)
print('*' * 100)

# 调整数据类型
t5 = t4.astype('i8')
print(t5)
print(t5.dtype)
print('*' * 100)

# numpy中的小数
import random

t6 = np.array([random.random() for i in range(13)])
print(t6)
print(t6.dtype)
t7 = np.round(t6, 3)
print(t7)
print(t7.dtype)
print(round(random.random(), 4))
print(round(random.random(), 4))
print(round(random.random(), 4))
print(round(random.random(), 4))



