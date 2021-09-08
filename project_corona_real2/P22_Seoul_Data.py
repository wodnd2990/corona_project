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
    # print(day1)
    
con.close()
df = DataFrame()
df['찐날짜'] = day
df['시.도'] = name
df['추가 확진'] = count
# print(df.groupby("찐날짜").sum())


print(df)
print("_______")
df = df[df['시.도']=="서울"] # 이거 빼면 밑의 그래프가 전체로 됨
print(df)
print("______")
print(df['찐날짜'].unique()) # 아근데 순서가 반대로 돼야 시각화할수있는데 어떻게 바꿀수 있을까....
a = df['찐날짜'].unique()
l,l2 = [],[]
for i in a:
    i = datetime.strptime(i,"%Y-%m")
    l.append(i)
l.sort()
for i in l:
    i = datetime.strftime(i,"%Y-%m")
    l2.append(i)
print(l2)
print("______")

df2 = df.groupby("찐날짜").sum()
# print(df2)
print("+_____")
# df2['찐날짜'] = df['찐날짜'].unique()


df2 = df2.sort_index(ascending=True) # 이걸 한 이유는 .unique()를 하면 순서가 반대로 나오기 때문에 맞춰주기 위해
print(df2)
df2['찐날짜'] = l2
print(df2)
print("여기보세요_________________-")
i = [{"추가 확진" : 1, "찐날짜" : "2020-02"},{"추가 확진" : 1, "찐날짜" : "2020-01"}]
df2 = df2.append(i, ignore_index=True) # 이 과정에서 인덱스가 set_index("찐날짜에서") 원래 숫자 인덱스로 돌아오네, ignore_index=True의 효과인듯
print("_____________________________")
# print(df2)
df2 = df2[df2['찐날짜'].str.contains("2020")]
# print(df2)
df2 = df2.sort_values(by="찐날짜",ascending=True)
# print(df2)

####################################################

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
            wc[v[0]] = np.array(int(v[1])/1000)
        
    f.close()
    
day,count = [],[]
for i,v in wc.items():
    day.append(i)
    count.append(v)
    

df4 = DataFrame()
df4['일자'] = day
df4['대여수'] = count
df4 = df4.sort_values(by='일자',ascending=True)
# print(df4)
# print(df4.head(10))
df4 = df4.set_index(df4['일자'])
# print(df4)

df20 = df4.loc['202001':'202012']
print("________")
# print(df20)
x = (df4.loc['202005']['대여수'] + df4.loc['202007']['대여수'])/2
i = {"일자":"202006","대여수":"%.3f"% x} # 6월 데이터가 없어서 5월과 7월 대여수 평균으로 추가함
df20 = df20.append(i, ignore_index=True)
print(df20)
df20 = df20.sort_values(by='일자',ascending=True)
# print(df20)

dfFix = DataFrame()
dfFix['일자'] = df20['일자']
# print(dfFix)
plt.title("서울시 월별 추가 확진자")
plt.bar(df2["찐날짜"],df2['추가 확진'],color="red")
plt.xticks(rotation=20)
plt.show()

plt.title("서울시 월별 확진자&따릉이 관계도")
plt.bar(df2["찐날짜"],df2['추가 확진'],color="red")
plt.plot(range(len(df20)),df20['대여수'], linewidth=5)
plt.legend(['20년도 따릉이',"2020년 서울 추가 확진"])
plt.grid(axis = 'x', color='#2E7D32', linestyle='-')
plt.xticks(rotation=20)
plt.show()

##########################서울 추가 확진자랑 따릉이 비교

##########################밑에는 버스&지하철과 따릉이 비교


bus2015 = pd.read_csv("C:/wodnd_file/busDF2015.csv")
bus2016 = pd.read_csv("C:/wodnd_file/busDF2016.csv")
bus2017 = pd.read_csv("C:/wodnd_file/busDF2017.csv")
bus2018 = pd.read_csv("C:/wodnd_file/busDF2018.csv")
bus2019 = pd.read_csv("C:/wodnd_file/busDF2019.csv")
bus2020 = pd.read_csv("C:/wodnd_file/busDF2020.csv")

busdf = DataFrame()
busdf['월'] = bus2015['월']
busdf['탄'] = (bus2015['탄'] + bus2016['탄'] + bus2017['탄'] + bus2018['탄'] + bus2019['탄'] + bus2020['탄'])/5

subway2015 = pd.read_csv("C:/wodnd_file/subwayDF2015.csv")
subway2016 = pd.read_csv("C:/wodnd_file/subwayDF2016.csv")
subway2017 = pd.read_csv("C:/wodnd_file/subwayDF2017.csv")
subway2018 = pd.read_csv("C:/wodnd_file/subwayDF2018.csv")
subway2019 = pd.read_csv("C:/wodnd_file/subwayDF2019.csv")
subway2020 = pd.read_csv("C:/wodnd_file/subwayDF2020.csv")

subwaydf = DataFrame()
subwaydf['월'] = subway2015['월']
subwaydf['탄'] = (subway2015['탄'] + subway2016['탄'] + subway2017['탄'] + subway2018['탄'] + subway2019['탄'] + subway2020['탄'])/5

plt.title("버스&지하철")
plt.bar(df2["찐날짜"],df2['추가 확진']*2,color="green")
plt.plot(busdf['월']-1,busdf['탄']/10000, color="blue")
plt.plot(bus2020['월']-1,bus2020['탄']/10000, linewidth=5, color="blue")
plt.plot(subwaydf['월']-1,subwaydf['탄']/10000, color="red")
plt.plot(subway2020['월']-1,subway2020['탄']/10000, linewidth=5, color="red")
plt.legend(["버스15~19평균",'2020버스', "지하철15~19평균",'2020지하철',"2020년 추가 확진 수"])
plt.grid(axis = 'x', color='#2E7D32', linestyle='-')
plt.xticks(rotation=20)
plt.show()




