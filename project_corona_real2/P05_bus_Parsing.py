# -*- coding:utf-8 -*-
# 2015-01-01~2020-12-31
# 연도별로 
from http.client import HTTPConnection
from json import loads

# http://openapi.seoul.go.kr:8088/4f6a6547456b6368333355736a714f/json/CardBusStatisticsServiceNew/1/5/20151102


con = HTTPConnection("openapi.seoul.go.kr:8088") # 연결은 한번만 시켜놓으면 됨
# for year in range(2015, 2021): # 년도까지 해서 성공한 역사가 없음
year = 2020 # 하나씩 넣자    
f = open("D://wodnd_file//buseoul%d.csv"% year,"a",encoding="utf-8")
for month in range(1, 13):
    for day in range(1, 32):
        for start in range(1,38002,1000): # 1~1000, 1001~2000 .... 38001~39000
            url = "/4f6a6547456b6368333355736a714f/json/CardBusStatisticsServiceNew/%d/%d/%d%02d%02d"% (start, start+999, year, month, day)
            con.request("GET", url)
            resBody = con.getresponse().read()
                
            busData = loads(resBody)
            if "CardBusStatisticsServiceNew" in busData: # "CardBusStatisticsServiceNew"가 없어도 에러가 안나게, busData안에 "CardBusStatisticsServiceNew"가 있을때만 하게     
                cbssn = busData["CardBusStatisticsServiceNew"]
                row = cbssn["row"]
                for r in row:
                    # f.write("%s,"% r["USE_DT"]) # 위에 날짜 다있는데 구지 파싱 노
                    f.write("%d,%d,%d,"% (year, month, day))
                    f.write("%s,"%r["BUS_ROUTE_NM"].replace(",",".")) # 혹시 들어있을 콤마를 없애기 위해서
                    f.write("%s,"%r["BUS_STA_NM"].replace(",",".")) # CSV라 ,로 나누는데 나누지 말아야 할 것에 있을경우를 대비
                    f.write("%.0f,"%r["RIDE_PASGR_NUM"]) # 저 데이터는 소수점 한자리까지 나오는데 떼버리기 .0f -> 18.0 - 18
                    f.write("%.0f\n"%r["ALIGHT_PASGR_NUM"])
        print(year, month, day)

print("끝")
con.close()
f.close()


# for v in range(1,13):
    # for k in range(1,32):
        # # print(i,v,k)
        #
        # when = "%02d%02d"% (v,k)
        # # when = datetime.strptime(when,"%Y/%m/%d")
        # # when = datetime.strftime(when,"%Y%m%d")
        #
        # for i in searchBus["CardBusStatisticsServiceNew"]["row"]:
            # print(i["RIDE_PASGR_NUM"])
            #
            #
# # print(resBody.decode())
#
#
# # print(searchBus["CardBusStatisticsServiceNew"]["row"][0])
#
#
    #
    #
    #
# # "USE_DT" - 년월일
# # "BUS_ROUTE_NM" - "100번(하계동~용산구청)"
# # "BUS_STA_NM" - 명륜3가.성대입구
# # "RIDE_PASGR_NUM" - 탄사람수
# # "ALIGHT_PASGR_NUM" - 내린사람수


