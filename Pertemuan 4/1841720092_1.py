# -*- coding: utf-8 -*-
"""Untitled

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1i_Bs79iO5jzp8fCZILzBP1dalYMn-8TT
"""

import pandas as pd

## ----- import data example-1 ----- ##
# import data from ms.excel file
# and save it into a pandas dataframe object named df

df = pd.read_excel("/content/drive/MyDrive/OnlineRetail.xlsx")
df.info()