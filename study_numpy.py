#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2024/10/17 15:08
@Author  : petrus
@Project : data_analysis
@File    : study_numpy.py
"""
import numpy as np
import time


# 一维数组
# arr1 = np.array([1, 2, 3, 4, 5])
# print(arr1)
#
# # 二维数组
# arr2 = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr2)
#
# # 三维数组
# arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# print(arr3)
# 开始时间
my_arr = np.arange(1000000)
my_list =list(range(1000000))

# 开始时间
start_time = time.time()
# 使用numpy的数组进行操作
result = my_arr * 2
# 结束时间
end_time = time.time()
print("Numpy数组操作时间：", end_time - start_time)
# 开始时间
start_time = time.time()
# 使用列表进行操作
result = [i * 2 for i in my_list]
# 结束时间
end_time = time.time()
print("列表操作时间：", end_time - start_time)
