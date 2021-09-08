# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from pandas.core.frame import DataFrame

fontFile = "C:\\windows\\Fonts\\malgun.ttf"
fontName = fm.FontProperties(fname = fontFile, size = 50).get_name()
plt.rc("font",family=fontName) 



l = ["","2","3","4","5","6","7","8","9"]
wc = {}
f = None
for i in l:
    f = open("C:/wodnd_file/test%s.csv"% i,"r",encoding="utf-8")
    for s,v in enumerate(f.readlines()): # 18,19중복, 인덱스 번호말고 1부터
        v = v.replace("\n","").replace("'","").replace(".0","").split(",")
        if v[0] in wc:
            pass
        else:
            wc[v[0]] = np.array(int(v[1])/10000)
        
    f.close()
    
day,count = [],[]
for i,v in wc.items():
    day.append(i)
    count.append(v)
    
print(day)
print(count)


df4 = DataFrame()
df4['일자'] = day
df4['대여수'] = count
df4 = df4.sort_values(by='일자',ascending=True)
print(df4)
print(df4.head(10))
df4 = df4.set_index(df4['일자'])
print(df4)

print(df4.loc['201701':'201712'])
df17 = df4.loc['201701':'201712']
print(df4.loc['201801':'201812'])
df18 = df4.loc['201801':'201812']
print(df4.loc['201901':'201912'])
df19 = df4.loc['201901':'201912']
# print(df4.loc['202001':'202012'])
df20 = df4.loc['202001':'202012']
x = (df4.loc['202005']['대여수'] + df4.loc['202007']['대여수'])/2
i = {"일자":"202006","대여수":"%.3f"% x}
df20 = df20.append(i, ignore_index=True)
df20 = df20.sort_values(by='일자',ascending=True)
print(df20)
print(df4.loc['202101':'202112'])
df21 = df4.loc['202101':'202112']

# i = {"이름" : "이", "나이" : 40}
# gg = gg.append(i, ignore_index=True)
# print(gg)

# plt.plot(df17['일자'],df17['대여수'])
# plt.plot(df18['일자'],df18['대여수'])
# plt.plot(df19['일자'],df19['대여수'])
# plt.plot(df20['일자'],df20['대여수'])
# plt.plot(df21['일자'],df21['대여수'])
# plt.xticks(rotation=45)
# plt.show()
plt.title("따릉이 년도별 비교")
plt.plot(range(1,len(df17['대여수'])+1),df17['대여수'], linewidth=4)
plt.plot(range(1,len(df18['대여수'])+1),df18['대여수'], linewidth=4)
plt.plot(range(1,len(df19['대여수'])+1),df19['대여수'], linewidth=4)
plt.plot(range(1,len(df20['대여수'])+1),df20['대여수'], linewidth=4)
plt.plot(range(1,len(df21['대여수'])+1),df21['대여수'], linewidth=4)
# plt.xticks(rotation=45)
plt.legend(['17','18','19','20','21'])
plt.grid(axis = 'x', color='#2E7D32', linestyle='-')
plt.show()








