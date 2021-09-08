# -*- coding:utf-8 -*-
from cx_Oracle import connect
import pandas as pd
from datetime import datetime


# df = pd.read_csv("C:/wodnd_file/goodNews20.01.csv")
# print(df)
# df['단어'] = df['단어'].head(20)
# df['단어수'] = df['단어수'].head(20)

f = open("C:/wodnd_file/coronaSido.csv","r",encoding="utf-8")

con = connect("sdedu/1@121.160.41.151:1521/xe")
for i in f.readlines():
    i = i.replace("\n","").split(",")
    ii = i[0].replace("년 ","-").replace("월 ","-").replace("일 00시","")
    if ii.endswith("시"):
        for v in range(1,19):
            ii = ii.replace("일 %02d시"%v,"")
    ii = datetime.strptime(ii,"%Y-%m-%d")
    ii = datetime.strftime(ii,"%Y-%m-%d")
    print(ii)
    sql = "insert into project_corona_3 values(project_corona_2_seq.nextval, to_date('%s','YYYY-MM-DD'),'%s',%s)"% (ii,i[1],i[2])    
    cur = con.cursor()
    cur.execute(sql)
    con.commit()



# if cur.rowcount == 1:
    # print('성공')
    
con.close()

f.close()
