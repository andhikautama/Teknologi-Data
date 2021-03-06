# -*- coding: utf-8 -*-
"""Untitled

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1i_Bs79iO5jzp8fCZILzBP1dalYMn-8TT
"""

import pandas as pd
import numpy as np

dummydata = {
    "D1": [np.nan, 0.763, 0.617, 0.738, np.nan,
            0.716, 0.730, np.nan, 0.710, 0.546],
    "D2": [0.875,0.772, 0.643, 0.542, 0.071,
            0.685, np.nan, 0.209, 0.547, np.nan]}

df = pd.DataFrame(dummydata)
print(df)

df_mean_imputed = df.fillna(df.mean())
print(df_mean_imputed)

df_median_imputed  = df.fillna(df.median())
print(df_median_imputed)

df_zero_imputed = df.fillna(0)
print(df_zero_imputed)