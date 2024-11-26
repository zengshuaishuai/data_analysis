#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2024/10/25 13:13
@Author  : petrus
@Project : data_analysis
@File    : study_pandas.py
"""
import pandas as pd

source_data={
    'name':['petrus','jack','tom','lucy'],
    'age':[18,19,20,21],
    'sex':['male','female','male','female']
}


df= pd.DataFrame(source_data)
print(df)
