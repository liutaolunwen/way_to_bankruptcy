# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 23:17:43 2019

@author: 骨灰盒
"""
import pandas as pd
import tushare as ts
import numpy as np
import time

code_list = pd.read_csv('code_list.csv',index_col=0,header=None)

#----------------------load into memory----------------------------------------

main_data = {}

for code in code_list[1]:
    print(str(code))
    try:
        main_data[code] =  pd.read_csv(code + '.csv',index_col=0)    
    except FileNotFoundError:
        print('该代码股票CSV文件不存在。')
        continue

