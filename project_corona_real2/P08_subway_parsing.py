# -*- coding:utf-8 -*-
# 2015-01-01~2020-12-31
# 연도별로 
# 몇년월일, 100번(하계동~용산구청),명륜3가.성대입구,108,171
from http.client import HTTPConnection
from xml.etree.ElementTree import fromstring

# http://openapi.seoul.go.kr:8088/4f6a6547456b6368333355736a714f/xml/CardSubwayStatsNew/1/5/20200302

con = HTTPConnection("openapi.seoul.go.kr:8088") 
year = 2021 
f = open("D://wodnd_file//subwaySeoul%d.csv"% year,"a",encoding="utf-8")
for month in range(1, 13):
    for day in range(1, 32):
        url = "/4f6a6547456b6368333355736a714f/xml/CardSubwayStatsNew/1/1000/%d%02d%02d"% (year, month, day)
        con.request("GET", url)
        resBody = con.getresponse().read()
        # print(resBody.decode())    

        subData = fromstring(resBody)
        # if "CardSubwayStatsNew" in subData:
        for i in subData.iter("row"):
            f.write("%d,%d,%d,"% (year, month, day))
            f.write("%s,"% i.find("LINE_NUM").text) # 호선
            f.write("%s,"% i.find("RIDE_PASGR_NUM").text) # 탄
            f.write("%s\n"% i.find("ALIGHT_PASGR_NUM").text) # 내린
        
    print(year, month, day)

print("끝")
con.close()
f.close()



