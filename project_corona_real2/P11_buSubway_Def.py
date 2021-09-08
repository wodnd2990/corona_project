# -*- coding:utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from pandas.core.frame import DataFrame

fontFile = "C:\\windows\\Fonts\\malgun.ttf"
fontName = fm.FontProperties(fname = fontFile, size = 50).get_name()
plt.rc("font",family=fontName)

def busAverage():
    bus2015 = pd.read_csv("C:/wodnd_file/busDF2015.csv")
    bus2016 = pd.read_csv("C:/wodnd_file/busDF2016.csv")
    bus2017 = pd.read_csv("C:/wodnd_file/busDF2017.csv")
    bus2018 = pd.read_csv("C:/wodnd_file/busDF2018.csv")
    bus2019 = pd.read_csv("C:/wodnd_file/busDF2019.csv")
    bus2020 = pd.read_csv("C:/wodnd_file/busDF2020.csv")
    
    plt.style.use('grayscale')
    plt.title("버스 년도별 비교")
    plt.plot(bus2015['월'],bus2015['탄']/10000,color="red")
    plt.plot(bus2016['월'],bus2016['탄']/10000,color="orange")
    plt.plot(bus2017['월'],bus2017['탄']/10000)
    plt.plot(bus2018['월'],bus2018['탄']/10000,color="green")
    plt.plot(bus2019['월'],bus2019['탄']/10000,color="blue")
    plt.plot(bus2020['월'],bus2020['탄']/10000,color="black")
    plt.legend(['2015','2016','2017','2018','2019','2020'],loc='upper right')
    plt.show()

def busYear():
    bus2015 = pd.read_csv("C:/wodnd_file/busDF2015.csv")
    bus2016 = pd.read_csv("C:/wodnd_file/busDF2016.csv")
    bus2017 = pd.read_csv("C:/wodnd_file/busDF2017.csv")
    bus2018 = pd.read_csv("C:/wodnd_file/busDF2018.csv")
    bus2019 = pd.read_csv("C:/wodnd_file/busDF2019.csv")
    bus2020 = pd.read_csv("C:/wodnd_file/busDF2020.csv")
    
    df = DataFrame()
    df['월'] = bus2015['월']
    df['탄'] = (bus2015['탄'] + bus2016['탄'] + bus2017['탄'] + bus2018['탄'] + bus2019['탄'] + bus2020['탄'])/5
    
    # plt.title("버스 평균 비교")
    # plt.plot(df['월'],df['탄']/10000,color="red")
    # plt.plot(bus2020['월'],bus2020['탄']/10000,color="black")
    # plt.legend(["15~19평균",'2020'])
    # plt.show()
    
    plt.title("버스 평균 비교")
    plt.bar(df['월']-0.4,df['탄']/10000, width=0.4, align='edge')
    plt.bar(bus2020['월']+0.2,bus2020['탄']/10000, width=0.4,color="red") # 이게 20년이자나
    plt.legend(['15~19평균','2020'],loc='upper right')
    plt.show()
    
def subwayAverage():
    subway2015 = pd.read_csv("C:/wodnd_file/subwayDF2015.csv")
    subway2016 = pd.read_csv("C:/wodnd_file/subwayDF2016.csv")
    subway2017 = pd.read_csv("C:/wodnd_file/subwayDF2017.csv")
    subway2018 = pd.read_csv("C:/wodnd_file/subwayDF2018.csv")
    subway2019 = pd.read_csv("C:/wodnd_file/subwayDF2019.csv")
    subway2020 = pd.read_csv("C:/wodnd_file/subwayDF2020.csv")
    
    plt.title("지하철 년도별 비교")
    plt.plot(subway2015['월'],subway2015['탄']/10000,color="red")
    plt.plot(subway2016['월'],subway2016['탄']/10000,color="orange")
    plt.plot(subway2017['월'],subway2017['탄']/10000)
    plt.plot(subway2018['월'],subway2018['탄']/10000,color="green")
    plt.plot(subway2019['월'],subway2019['탄']/10000,color="blue")
    plt.plot(subway2020['월'],subway2020['탄']/10000,color="black")
    plt.legend(['2015','2016','2017','2018','2019','2020'],loc='upper right')
    plt.show()

def subwayYear():
    subway2015 = pd.read_csv("C:/wodnd_file/subwayDF2015.csv")
    subway2016 = pd.read_csv("C:/wodnd_file/subwayDF2016.csv")
    subway2017 = pd.read_csv("C:/wodnd_file/subwayDF2017.csv")
    subway2018 = pd.read_csv("C:/wodnd_file/subwayDF2018.csv")
    subway2019 = pd.read_csv("C:/wodnd_file/subwayDF2019.csv")
    subway2020 = pd.read_csv("C:/wodnd_file/subwayDF2020.csv")
    df = DataFrame()
    df['월'] = subway2015['월']
    df['탄'] = (subway2015['탄'] + subway2016['탄'] + subway2017['탄'] + subway2018['탄'] + subway2019['탄'] + subway2020['탄'])/5
    
    # plt.title("지하철 평균 비교")
    # plt.plot(df['월'],df['탄']/10000,color="red")
    # plt.plot(subway2020['월'],subway2020['탄']/10000,color="black")
    # plt.legend(["15~19평균",'2020'])
    # plt.show()
    
    plt.title("지하철 평균 비교")
    plt.bar(df['월']-0.4,df['탄']/10000, width=0.4, align='edge')
    plt.bar(subway2020['월']+0.2,subway2020['탄']/10000, width=0.4,color="red") # 이게 20년이자나
    plt.legend(['15~19평균','2020'],loc='upper right')
    plt.show()

def busubway():
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
    plt.plot(busdf['월'],busdf['탄']/10000, color="blue")
    plt.plot(bus2020['월'],bus2020['탄']/10000, linewidth=5, color="blue")
    plt.plot(subwaydf['월'],subwaydf['탄']/10000, color="red")
    plt.plot(subway2020['월'],subway2020['탄']/10000, linewidth=5, color="red")
    plt.legend(["버스15~19평균",'2020버스', "지하철15~19평균",'2020지하철'],loc='upper right')
    plt.grid(axis = 'x', color='#2E7D32', linestyle='-')
    plt.show()

def number():
    print("1 : 버스 년도별 비교")
    print("2 : 버스 평균 비교")
    print("3 : 지하철 년도별 비교")
    print("4 : 지하철 평균 비교")
    print("5 : 버스&지하철")
    try:
        a = int(input("몇 번 : "))
    except:
        print("1~5 사이의 숫자만 입력하세요")
        return number()
    
    if a == 1:
        busAverage()
        return number()
    elif a == 2:
        busYear()
        return number()
    elif a == 3:
        subwayAverage()
        return number()
    elif a == 4:
        subwayYear()
        return number()
    elif a == 5:
        busubway()
        return number()
    else:
        print("1~5 사이의 숫자만 입력하세요")
        return number()


number()








