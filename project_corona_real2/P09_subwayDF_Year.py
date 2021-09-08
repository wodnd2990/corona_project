# -*- coding:utf-8 -*-
import pandas as pd
from pandas.core.frame import DataFrame
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

fontFile = "C:\\windows\\Fonts\\malgun.ttf"
fontName = fm.FontProperties(fname = fontFile, size = 50).get_name()
plt.rc("font",family=fontName) 

for ii in range(2015,2021):
    df = pd.read_csv("D:/wodnd_file/subwaySeoul%s.csv"% ii,names=["년","월","일","노선","탄","내린"])
    
    df2 = df[["월","탄",]]
    
    wc = {}
    for i in range(1,13):
        if i in wc:
            pass
        else:
            wc[i] = df2[df2['월']==i]['탄'].sum()
    
    month,count = [],[]
    
    for i,v in wc.items():
        month.append(i)
        count.append(v)
    
    subwayDF = DataFrame()
    subwayDF['월'] = month
    subwayDF['탄'] = count
    # print(busDF)
    
    subwayDF.to_csv("D:/wodnd_file/subwayDF%s.csv"% ii, index=False)
    print(ii)
print("끝")













