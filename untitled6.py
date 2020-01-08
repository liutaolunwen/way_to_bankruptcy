# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 14:37:26 2020

@author: P
"""

import pandas as pd

csv_name = "s2019-01-01-2019-02-01" + ".csv"
df = pd.read_csv(csv_name)
df.head(3)