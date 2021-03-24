# -*- coding: utf-8 -*-
"""Untitled

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1i_Bs79iO5jzp8fCZILzBP1dalYMn-8TT
"""

import pandas as pd

## ----- data overview example-2 ----- ##

df = pd.read_excel("/content/drive/MyDrive/OnlineRetail.xlsx")
df.info()
print(df.isnull().any())
print(df.isnull().sum())
print(df[df['Description'].isnull()].head())