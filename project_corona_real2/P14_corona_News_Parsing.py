# -*- coding:utf-8 -*-
# 한국언론진흥재단_뉴스빅데이터_메타데이터_코로나
# data.go.kr
# 네이버 검색어를 단어화한 것들은 딱히 쓸모가 없어보여 다시 찾은 데이터
# 이번에도 타이틀과 내용만 빼서 csv로 저장
from http.client import HTTPSConnection
from json import loads
con = HTTPSConnection("api.odcloud.kr")
url = ['/api/15069309/v1/uddi:a148f666-5234-4c6b-98ea-ee05ae36336d?returnType=json&serviceKey=HrnNf4pnWx5QT47fzIrM9AMLZIdDSAvPlXB0yvDRvTNEMkWdyL64dt5Ca7H5DORRHx1QYy1Saf4XJrr3BGGYNQ%3D%3D',
       '/api/15069309/v1/uddi:973ad0df-617a-4565-8e82-8ea7869e75d4?returnType=json&serviceKey=HrnNf4pnWx5QT47fzIrM9AMLZIdDSAvPlXB0yvDRvTNEMkWdyL64dt5Ca7H5DORRHx1QYy1Saf4XJrr3BGGYNQ%3D%3D',
       '/api/15069309/v1/uddi:7fbf03b1-49f2-4d29-99f8-a717aec01d09?returnType=json&serviceKey=HrnNf4pnWx5QT47fzIrM9AMLZIdDSAvPlXB0yvDRvTNEMkWdyL64dt5Ca7H5DORRHx1QYy1Saf4XJrr3BGGYNQ%3D%3D',
       '/api/15069309/v1/uddi:4df22b16-2ff8-4154-86d5-97bcd030f1bd?returnType=json&serviceKey=HrnNf4pnWx5QT47fzIrM9AMLZIdDSAvPlXB0yvDRvTNEMkWdyL64dt5Ca7H5DORRHx1QYy1Saf4XJrr3BGGYNQ%3D%3D',
       '/api/15069309/v1/uddi:0c9d1607-44b9-47d0-8614-a9089ebb1848?returnType=json&serviceKey=HrnNf4pnWx5QT47fzIrM9AMLZIdDSAvPlXB0yvDRvTNEMkWdyL64dt5Ca7H5DORRHx1QYy1Saf4XJrr3BGGYNQ%3D%3D']
for l in range(5):
    s = {}
    for o in range(1,1000):
        for v in range(2211,1,-1100):
            con.request("GET",url[l] + '&page=%s&perPage=%s'% (o,v))
            rb = con.getresponse().read()
            news = loads(rb)
            try:
                for i in news['data']:
                    i1 = i['본문'] + "||" + i['일자']
                    if i1 in s:
                        pass
                    else:
                        s[i1] = 1
            except:
                pass
    
    f = open("D:/wodnd_file/BigNews%s.csv"%(l+1),"a",encoding="utf-8")
    for i,v in s.items():
        f.write("%s\n"%i)
    f.close()
    print(l+1)
con.close()
