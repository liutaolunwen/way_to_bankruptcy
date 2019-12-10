# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 23:17:43 2019

@author: 骨灰盒
"""

import tushare as ts
import numpy as np
import time

ts.set_token('TOKEN')
pro = ts.pro_api()

TODAY = time.strftime("%Y%m%d", time.localtime())
START_DATE = '20190801'
trade_days = pro.query('trade_cal', start_date=START_DATE, end_date=TODAY)
trade_days = trade_days[trade_days['is_open'] == 1]

right = 0
wrong = 0
signal_counter = 0


#------------------------------------------------------------------------------
codes = pro.query('stock_basic', exchange='', list_status='L', market= '',fields='ts_code,symbol,name,area,industry,list_date')
my_codes = codes.ts_code
my_codes = my_codes[0:300]

#--------------------观察点-----------------------------------------------------


#默认6个交易日之前
OB_DATE = trade_days.iat[trade_days.shape[0]-6,1]
#观察日的次日
TEST_DATA = trade_days.iat[trade_days.shape[0]-5,1]

for code in my_codes:
    print('正在对' + code + '进行扫描')
#----------------------策略区--------------------------------------------------
    try:
        tmp_df = ts.pro_bar(ts_code= code, start_date=START_DATE,end_date=OB_DATE,ma=[15, 35, 60,125])
#降速器：调取一次睡眠10秒
        time.sleep(10)
        signal_1 = tmp_df.iat[0,5] > tmp_df.iat[0,11]
        signal_2 = tmp_df.iat[0,5] > tmp_df.iat[0,13]
        signal_3 = tmp_df.iat[0,5] > tmp_df.iat[0,15]
        signal_4 = tmp_df.iat[0,5] > tmp_df.iat[0,17]
        
        signal_a = signal_1 & signal_2 & signal_3 & signal_4
        
#---------------------暂时先不考虑四根均线的距离 节约算力-------------------------
        #signal_b = max(tmp_df.iat[0,11],tmp_df.iat[0,13],tmp_df.iat[0,15],tmp_df.iat[0,17]) - min(tmp_df.iat[0,11],tmp_df.iat[0,13],tmp_df.iat[0,15],tmp_df.iat[0,17])
        
        #signal_c = np.std((tmp_df.iat[0,11],tmp_df.iat[0,13],tmp_df.iat[0,15],tmp_df.iat[0,17]),ddof=1) / np.mean((tmp_df.iat[0,11],tmp_df.iat[0,13],tmp_df.iat[0,15],tmp_df.iat[0,17]))
        singal_v = tmp_df.iat[0,9] > tmp_df.iat[1,9]
        signal = signal_a & singal_v
    
    
        if(signal):
            signal_counter += 1
            print('发现信号，该观察日信号个数为：' + signal_counter)
#----------------------验证区--------------------------------------------------
        result = ts.pro_bar(ts_code= code, start_date=TEST_DATA,end_date=TEST_DATA)
        #此处写交易费率 默认0 
        get_money = result.iat[0,7] > 0
        
        if(signal & get_money):
            right = right + 1
        elif(signal & (not get_money)):
            wrong = wrong + 1
    except IndexError:
        print('数据不完整')
        continue
        
print('在观察期' + OB_DATE + '遍历股票' + str(my_codes.shape[0]) + '支，共发现信号' + str(signal_counter) +  '次。')
print('其中正确次数为：' + str(right))











