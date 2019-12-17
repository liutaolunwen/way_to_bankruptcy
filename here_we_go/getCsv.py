# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 23:17:43 2019

@author: 骨灰盒
"""

import tushare as ts
import numpy as np
import time

ts.set_token('7d6ac63764d82662169992641f582aab920fc6a0564f3147a773e8bf')
pro = ts.pro_api()


TODAY = time.strftime("%Y%m%d", time.localtime())
START_DATE = '20190801'
#------------------------------------------------------------------------------
codes = pro.query('stock_basic', exchange='', list_status='L', market= '',fields='ts_code,symbol,name,area,industry,list_date')
my_codes = codes.ts_code
my_codes = my_codes[0:3]

for code in my_codes:
#----------------------策略区--------------------------------------------------
    try:
        tmp_df = pro.query('daily',ts_code= code, start_date=START_DATE,end_date=TODAY,
        fields='trade_date,open,high,low,close,change,vol,amount')
# ts_code 	str 	股票代码
# trade_date 	str 	交易日期
# open 	float 	开盘价
# high 	float 	最高价
# low 	float 	最低价
# close 	float 	收盘价
# pre_close 	float 	昨收价
# change 	float 	涨跌额
# pct_chg 	float 	涨跌幅 （未复权，如果是复权请用 通用行情接口 ）
# vol 	float 	成交量 （手）
# amount 	float 	成交额 （千元）
        tmp_df.to_csv(str(code) + '.csv')
    
    except IndexError:
        print('数据不完整')
        continue

#--------------------观察点-----------------------------------------------------

