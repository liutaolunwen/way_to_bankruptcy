# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 14:17:55 2020

@author: P
"""

import time
import tushare as ts

ts.set_token('6688c5efb62bdd6cf6637cac0717304abde5265e36af12f478537e5a')
pro = ts.pro_api()

ini_date = '2019-01-01 00:00:00'
last_data = '2020-01-01 00:00:00'
last_tick = time.mktime(time.strptime(last_data,"%Y-%m-%d %H:%M:%S"))
ONE_HOUR = 60 * 60
ONE_STEP = ONE_HOUR * 24

start_ticks = time.mktime(time.strptime(ini_date,"%Y-%m-%d %H:%M:%S"))
end_ticks = start_ticks + ONE_STEP
my_start_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start_ticks))
my_end_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(end_ticks))

csv_name = "s2019-01-01-2020-01-01" + ".csv"

while(end_ticks < last_tick):
    start_ticks = end_ticks
    end_ticks = start_ticks + ONE_STEP
    my_start_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start_ticks))
    my_end_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(end_ticks))
    print("从" + my_start_date)
    print("至" + my_end_date)
    #新闻全文数据量太大，用简版
    #df = pro.major_news(src='', start_date=my_start_date, end_date=my_end_date, fields='pub_time,title,content,src')
    df = pro.news(src='sina',start_date=my_start_date, end_date=my_end_date,fields='datetime,title,content,channels')
    print("读取新闻行数：" + str(df.shape[0]))
    time.sleep(1)
    df.to_csv(csv_name, mode='a')

print("done")