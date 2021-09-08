# -*- coding:utf-8 -*-
from cx_Oracle import connect
from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.font_manager as fm 
from pandas.core.frame import DataFrame

fontFile = "C:\\windows\\Fonts\\malgun.ttf"
fontName = fm.FontProperties(fname = fontFile, size = 50).get_name()
plt.rc("font",family=fontName)

con = connect("sdedu/1@121.160.41.151:1521/xe")
sql = "select * from project_corona_2" 
cur = con.cursor()
cur.execute(sql)
day, name, count = [], [], []
for _, day1, name1, count1 in cur:
    day1 = datetime.strftime(day1, "%Y-%m")
    # print(day1, name1, count1)
    day.append(day1)
    name.append(name1)
    count.append(count1)
    
con.close()
df = DataFrame()
df['찐날짜'] = day
df['시.도'] = name
df['추가 확진'] = count

print(df)
print(df['찐날짜'].unique())
print(df['시.도'].unique())
print(df.groupby("시.도").sum())
df2 = df.groupby("시.도").sum()
# plt.plot(df2)
# plt.show()

df2 = df2.sort_values(by = "추가 확진", ascending=False)
print(df2)
# df2.to_csv("C:/wodnd_file/soso.csv",header=False) # 보내고 나서 다음페이지에 해야겠지만 그냥 이번페이지에

df3 = pd.read_csv("C:/wodnd_file/soso.csv",names=['시.도',"추가 확진"])
print(df3)
df3 = df3.sort_values(by="추가 확진", ascending=True)
# plt.bar(df3['시.도'],df3['추가 확진'])
# plt.show()

d = {'width':0.7, 'edgecolor':'black','linewidth':1}
plt.pie(df3['추가 확진'], labels = df3['시.도'], startangle=90, autopct="%.f%%",wedgeprops=d)
plt.title("전국 코로나 누적 확진자%")

plt.show()






