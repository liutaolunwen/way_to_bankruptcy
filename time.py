# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 09:42:06 2020

@author: P
"""
import time



print(time.localtime())


start_date = '2019-11-21 00:00:00'

one_hour = 60 * 60

start_date_time = time.mktime(time.strptime(start_date,"%Y-%m-%d %H:%M:%S"))
after_one_hour = start_date_time + one_hour


now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(after_one_hour))