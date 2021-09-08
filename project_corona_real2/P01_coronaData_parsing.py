# -*- coding:utf-8 -*-
# 공공데이터활용지원센터_보건복지부 코로나19 시·도발생 현황
# data.go.kr
# 일별 시.도별 추가 확진자
from http.client import HTTPConnection
from xml.etree.ElementTree import fromstring

# http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson?serviceKey=HrnNf4pnWx5QT47fzIrM9AMLZIdDSAvPlXB0yvDRvTNEMkWdyL64dt5Ca7H5DORRHx1QYy1Saf4XJrr3BGGYNQ%3D%3D&pageNo=1&numOfRows=1000&startCreateDt=20200210&endCreateDt=20210710
con = HTTPConnection("openapi.data.go.kr")
con.request("GET","/openapi/service/rest/Covid19/getCovid19SidoInfStateJson?serviceKey=HrnNf4pnWx5QT47fzIrM9AMLZIdDSAvPlXB0yvDRvTNEMkWdyL64dt5Ca7H5DORRHx1QYy1Saf4XJrr3BGGYNQ%3D%3D&pageNo=1&numOfRows=1000&startCreateDt=20200210&endCreateDt=20210710")
rb = con.getresponse().read()
con.close()

sidoData = fromstring(rb)

f = open("D:/wodnd_file/coronaSido.csv","a",encoding="utf-8")

sido = sidoData.iter("item")
l = []
for s in sido:
    # l.append(s.find("stdDay").text)
    if s.find("gubun").text != '합계':
        print(s.find("stdDay").text)
        print(s.find("gubun").text)
        print(s.find("incDec").text)
        # f.write("%s,"% s.find("stdDay").text)
        # f.write("%s,"% s.find("gubun").text)
        # f.write("%s\n"% s.find("incDec").text)
        
    
print("끝")
print(len(l))
f.close()
