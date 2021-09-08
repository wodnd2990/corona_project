# -*- coding:utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from pandas.core.frame import DataFrame

fontFile = "C:\\windows\\Fonts\\malgun.ttf"
fontName = fm.FontProperties(fname = fontFile, size = 50).get_name()
plt.rc("font",family=fontName) 


df2015 = pd.read_csv("C:/wodnd_file/subwayDF2015.csv")
df2016 = pd.read_csv("C:/wodnd_file/subwayDF2016.csv")
df2017 = pd.read_csv("C:/wodnd_file/subwayDF2017.csv")
df2018 = pd.read_csv("C:/wodnd_file/subwayDF2018.csv")
df2019 = pd.read_csv("C:/wodnd_file/subwayDF2019.csv")
df2020 = pd.read_csv("C:/wodnd_file/subwayDF2020.csv")

df = DataFrame()
df['월'] = df2015['월']
df['탄'] = (df2015['탄'] + df2016['탄'] + df2017['탄'] + df2018['탄'] + df2019['탄'] + df2020['탄'])/5   
print(df)
print(df2020['탄']/10000)

# plt.title("지하철")
# plt.plot(df2015['월'],df2015['탄']/10000,color="red")
# plt.plot(df2016['월'],df2016['탄']/10000,color="orange")
# plt.plot(df2017['월'],df2017['탄']/10000)
# plt.plot(df2018['월'],df2018['탄']/10000,color="green")
# plt.plot(df2019['월'],df2019['탄']/10000,color="blue")
# plt.plot(df2020['월'],df2020['탄']/10000,color="black")
# plt.legend(['2015','2016','2017','2018','2019','2020'])
# plt.show()


plt.title("지하철")
plt.plot(df['월'],df['탄']/10000,color="red")
plt.plot(df2020['월'],df2020['탄']/10000,color="black")
plt.legend(["15~19평균",'2020'])
plt.show()





# df2015, df2016, df2017, df2018, df2019, df2020 = None, None, None, None, None, None
# for i in range(2015,2021):
    # a = pd.read_csv("C:/wodnd_file/busDF%s.csv"% i)
    # "df" + str(i) = a
    # print(i)
    # print(a)
    # print("________")
# print(df2015)




















