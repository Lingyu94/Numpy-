# 开发者：Lingyu
# 开发时间：2021/1/19 22:09

import numpy as np
import random as random

# np.random.rand(d0, d1, ...dn) 创建d0-dn维度的均匀分布的随机数数组，浮点数，范围0-1
t1 = np.random.rand(3, 4, 4)
t1 = np.round(t1, 2)  # 保留2位小数
print(t1)
print('*' * 50)

# np.random.randn(d0, d1, ...dn) 创建d0-dn维度的标准正态分布的随机数，浮点数，平均值0，标准差1
t2 = np.random.randn(2, 3, 4)
t2 = np.round(t2, 2)  # 保留2位小数
print(t2)
print('*' * 50)

# np.random.randint(low, high, (shape)) 给定上下范围（low-high）选取随机整数，形状为shape
t3 = np.random.randint(1, 12, (2, 3, 4))
print(t3)
print('*' * 50)

# np.random.uniform(low, high, (size)) 产生具有均匀分布的数组，low为起始值，high结束值，size形状
t4 = np.random.uniform(1, 12, (2, 3, 4))
t4 = np.round(t4, 2)  # 保留2位小数
print(t4)
print('*' * 50)

# np.random.normal(loc, scale, (size)) 从正态分布中随机抽取样本，分布中心是loc（概率分布的均值），标准差是scale，形状是size
t5 = np.random.normal(0.6, 3, (2, 3, 4))
t5 = np.round(t5, 2)  # 保留2位小数
print(t5)
print('*' * 50)

# np.random.seed(s) 随机数种子，s为给定的种子值，通过设定相同的随机数种子，可每次生成相同的随机数
np.random.seed(9)
t6 = np.random.normal(0.6, 3, (2, 3, 4))
t6 = np.round(t6, 2)  # 保留2位小数
print(t6)
print('*' * 50)
# t5每run一次都会发生改变，t6每run一次都不会发生改变
