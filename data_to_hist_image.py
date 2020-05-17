#!/usr/bin/env python
# coding: utf-8
# author : Ashish Patel

import pandas as pd
from row2plot import row2plot


df = pd.read_excel("Dataset.xlsx")
rp = row2plot.row2plot(data=df)
rp.row2hist()
rp.row2kde()





