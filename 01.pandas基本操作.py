#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2024/11/26 21:14
@Author  : petrus
@Project : data_analysis
@File    : 01.pandas基本操作.py
"""
from pandas import DataFrame, Series
import pandas as pd
import numpy as np

s1=Series([1,2,3,4,5])
#print(s1)
dict={
    'A':100,
    'B':99,
    'C':120
}
s2=Series(data=dict)
#print(s2)
## Series 的索引
# 隐式索引:默认形式的索引(0,1,2...)
# 显示索引:自定义的索引,可以通过index参数设置显示索引
s3=Series(data=np.random.randint(0,100,size=(3,))) #隐式索引

s4=Series(data=np.random.randint(0,100,size=(3,)),index=['A','B','C']) #显示索引
#print(s4)


## Series的索引和切片
s5=Series(data=np.linspace(0,30,num=5),index=['a','b','c','d','e'])
# print("s5:",s5)
# print("\n")
# print("s5.iloc[1]:",s5.iloc[1])
# print("\n")
# print("s5['c']:",s5['c'])
# print("\n")
# print("s5[0:3]:",s5[0:3])
# print("\n")
# print("s5['a':'d']:",s5['a':'d'])
# print("\n")

## Series的常用属性
# shape 对于 Series，其形状是一个元组，表示 Series 的长度。
# print(s5.shape)
# size
# print(s5.size)
# index
# print(s5.index)
# values
# print(s5.values)

## Series的常用方法
# head(),tail()
# print(s5.head(3))
# print(s5.tail(2))

# unique()
s6=Series(data=[1,1,2,2,3,3,4,4,5,5,6,6,7,7,7])
# print(s6.unique()) # 对元素进行去重
# print(s6.nunique()) # 统计去重后元素的个数

# isnull(),notnull()
s7=Series(data=[1, 2, np.nan, 4, np.nan, 6])
# print(s7.isnull())
# print(s7.notnull())

# add() sub() mul() div()
s8 = Series([1, 2, 3, 4, 5])
s9 = Series([5, 4, 3, 2, 1])

# print(s8.add(s9))  # 加法
# print(s8.sub(s9))  # 减法
# print(s8.mul(s9))  # 乘法
# print(s8.div(s9))  # 除法

# Series 与标量运算
# print(s8.add(10))  # 加法
# print(s8.mul(2))  # 乘法

### Series的算术运算
# 法则: 索引一致的元素进行算术运算否则补空
s10=Series(data=[1,2,3,4,5],index=['a','b','c','d','e'])
s11=Series(data=[1,2,3,4,5],index=['a','b','f','d','e'])
s = s10+s11
print(s)
