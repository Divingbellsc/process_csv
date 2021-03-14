#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 23:25:31 2021

@author: divingbell
"""

import os
import pandas as pd
import numpy as np
import glob


path = os.getcwd()
all_files = glob.glob(path + "/*.csv")

list_of_files = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    list_of_files.append(df)

df_all= pd.concat(list_of_files, axis=0, ignore_index=True)

df_all=df_all.loc[df_all.name.notnull(),:]
df_all.reset_index(drop=True,inplace=True)
df_all[['first_name', 'last_name']] = df_all['name'].str.split(' ', 1, expand=True)
df_all = df_all.drop('name', 1)
df_all['price']=pd.to_numeric(df_all['price'], errors='coerce')
df_all=df_all[df_all['price'].notnull()]
df_all.reset_index(drop=True,inplace=True)
df_all['price_more_than_100'] = np.where(df_all['price']>100, True, False)
df_all.to_csv('processed_doc.csv')