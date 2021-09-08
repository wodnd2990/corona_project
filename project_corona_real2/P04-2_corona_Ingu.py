# -*- coding:utf-8 -*-
from pandas.core.frame import DataFrame
import matplotlib.pyplot as plt 
import matplotlib.font_manager as fm 
import numpy as np

fontFile = "C:\\windows\\Fonts\\malgun.ttf"
fontName = fm.FontProperties(fname = fontFile, size = 50).get_name()
plt.rc("font",family=fontName)

f = open("C:/wodnd_file/siIngu.csv","r",encoding="utf-8")

wc = {}
for v,i in enumerate(f.readlines()):
    if v > 2:
        i = i.replace("\n","").replace('"',"").split(",")
        if i[0] in wc:
            pass
        else:
            wc[i[0]] = int(i[1])

f.close()

si, count = [],[]
for i,v in wc.items():
    si.append(i)
    count.append(v)
    
df = DataFrame()
df['지역'] = si
df['인구수'] = count
###########################
sum = DataFrame()
sum['지역'] = df['지역']
sum['인구수'] = df['인구수']
##########################
dfdf = df.sort_values(by="인구수",ascending=False)

plt.title("지역별 인구수")
plt.bar(dfdf['지역'], dfdf['인구수'])
plt.xticks(rotation=40)
plt.show()


f = open("C:/wodnd_file/area_ingu.csv","r",encoding="utf-8")

wc2 = {}
for v,i in enumerate(f.readlines()):
    if v > 2:
        i = i.replace("\n","").replace('"',"").split(",") 
        if i[0] in wc2:
            pass
        else:
            wc2[i[0]] = int(i[1])*1000*3.3
    
f.close()

sim, countm = [],[]
for i,v in wc2.items():
    sim.append(i)
    countm.append(v)

dfm = DataFrame()
dfm['지역'] = sim
dfm['면적'] = countm
################################
sum['면적'] = dfm['면적']
################################
dfm = dfm.sort_values(by="면적",ascending=False)
print(dfm)
dfm = dfm.set_index(dfm['지역'])

dd = dfm.loc['제주특별자치도':'세종특별자치시']

mm = 0
for i in dd['면적']:
    if i != float(dfm[dfm['지역']=='서울특별시']['면적']):
        mm += i

print(mm)

ss = float(dfm[dfm['지역']=='서울특별시']['면적'])

print("____________")
print(dfm.loc['경상북도':"충청북도"])
dfm = dfm.loc['경상북도':"충청북도"]
i = [{'지역' : "그 외", '면적' : mm},{'지역' : "서울", '면적' : ss}]
dfm = dfm.append(i, ignore_index=True)
######################################
sum = sum.sort_values(by='면적',ascending=False)
sum = sum.set_index(sum["지역"])
dd2 = sum.loc['경상북도':'충청북도']
dd3 = sum.loc["제주특별자치도":"세종특별자치시"]

mm1 = 0
for i in dd3['인구수']:
    if i != float(dd3[dd3['지역']=='서울특별시']['인구수']):
        mm1 += i


ss1 = float(df[df['지역']=='서울특별시']['인구수'])

i = [{'지역' : "그 외","인구수" : mm1, '면적' : mm},{'지역' : "서울특별시","인구수" : ss1, '면적' : ss}]
dd2 = dd2.append(i, ignore_index=True)
dd2['면적대비 밀집도'] = dd2['인구수']/dd2['면적']
print("_____sum_____")

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
fig,axes = plt.subplots()

plt.title("지역별 면적&인구수")
axes.bar(x-0.4, dd2['면적'], width=0.4, align='edge')
axes.bar(x, dd2['인구수'], width=0.4, align='edge')
plt.xticks(x)
axes.set_xticklabels(dd2['지역'])
plt.xticks(rotation=20)
plt.legend(['면적',"인구수"])
plt.show()

ddd = dd2.sort_values(by="면적대비 밀집도",ascending=True)

plt.title("면적대비 밀집도")
plt.barh(ddd['지역'],ddd['면적대비 밀집도'])
plt.show()
######################################

d = {'width':0.7, 'edgecolor':'black','linewidth':1}
plt.pie(dfm['면적'], labels = dfm['지역'], startangle=90, autopct="%.f%%",wedgeprops=d)
plt.title("지역별 면적")
plt.show()

#plt.title("지역별 면적")
#plt.bar(dfm['지역'],dfm['면적'])
#plt.xticks(rotation=20)
#plt.show()



df3 = DataFrame()
df3['지역'] = df['지역']
df3['인구'] = df['인구수']
df3['면적'] = dfm['면적']
# df3 = df3.sort_values(by="면적대비 밀집도",ascending=False)
print(df3)

# plt.title("지역별 면적대비 밀집도")
# plt.bar(df3['지역'],df3['면적대비 밀집도'])
# plt.show()


# from sklearn.preprocessing._data import MinMaxScaler
#
# data = df3[['면적']]
#
# mms = MinMaxScaler() 
# data = mms.fit_transform(data)
# print(data)
# print(data[1])
#
#
# l = []
# for i in data:
    # for v in i:
        # l.append(v)
# print(l)
#
# plt.bar(df['지역'],l)
# plt.xticks(rotation=20)
# plt.show()
#
# data2 = df3[['면적대비 밀집도','인구']].to_numpy()
# mms2 = MinMaxScaler() 
# data2 = mms2.fit_transform(data2)
# # print(data2)
#
# print("_______")
# for i in data2:
    # for k,v in enumerate(i):
        # if k % 2 == 0:
            # print(v)
        # else:
            # print(v,"_")
            
        
            


# plt.plot(df['지역'],df['인구수'])
# plt.plot(df['지역'],dfm['면적'])
# plt.plot(df['지역'],df3['면적대비 밀집도'])
# plt.legend(["인구수",'면적대비 밀집도'])
# plt.xticks(rotation=20)
# plt.show()















    