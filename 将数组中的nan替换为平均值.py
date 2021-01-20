# 开发者：Lingyu
# 开发时间：2021/1/20 20:37

import numpy as np


def fill_ndarray(t1):
    for i in range(t1.shape[1]):  # 一列一列的循环
        temp_col = t1[:, i]  # 当前的一列
        nan_num = np.count_nonzero(temp_col != temp_col)  # nan的个数之和，np.count_nonzero():不为0的个数之和
        if nan_num != 0:  # 不为0，说明此列有nan
            temp_not_nan_col = temp_col[temp_col == temp_col]  # temp_col中不为nan的array
            temp_col[np.isnan(temp_col)] = temp_not_nan_col.mean()  # 选中当前为nan的位置，赋值为不为nan的均值
    return t1


if __name__ == '__main__':
    t1 = np.arange(12).reshape((3, 4)).astype('float')
    t1[1, 2:] = np.nan
    print('t1:', t1)
    t2 = fill_ndarray(t1)
    print('*' * 50)
    print('t2:', t2)
