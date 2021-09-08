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
    df = pd.read_csv("D:/wodnd_file/buseoul%s.csv"% ii,names=["년","월","일","노선","정류장","탄","내린"])
    
    df2 = df[["월","탄"]]
    
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
    
    busDF = DataFrame()
    busDF['월'] = month
    busDF['탄'] = count
    # print(busDF)
    
    busDF.to_csv("D:/wodnd_file/BusDF%s.csv"% ii, index=False)
    print(ii)
print("끝")
plt.bar(busDF['월'], busDF['탄'])
plt.show()
df.to_csv("D:/wodnd_file/Rcorona.csv",header=False, index=False)













