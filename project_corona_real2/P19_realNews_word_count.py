# -*- coding:utf-8 -*-
# 지도학을 통해 적합 판정을 받은 뉴스들만 빼서 정규화, 명사화 해서 단어 수 세기
from konlpy.tag._okt import Okt
import matplotlib.pyplot as plt
from wordcloud.wordcloud import WordCloud
from pandas.core.frame import DataFrame
import matplotlib.font_manager as fm

fontFile = "C:\\windows\\Fonts\\malgun.ttf"
fontName = fm.FontProperties(fname = fontFile, size = 50).get_name()
plt.rc("font",family=fontName)

f = open("C:/wodnd_file/realNews1.csv","r",encoding="utf-8")
o = Okt()
wc12 = {}
wc01 = {}
a = None
txt = ""
for i in f.readlines():
    i = i.replace("\n","").split("||")
    if i[0] == "적격":            # 제대로 된 데이터를 위해 Machine Learning한 데이터들 중에 적격 판정을 받은 데이터 들만 가져오기 
        a = o.normalize(i[1])    # 단어들 정규화
        a = o.nouns(a)           # 단어 나눠서 명사인것들만 리스트로
        for k in a:
            if len(k) != 1 and k != "코로나" and k != "확진" and k != "판정" and k != "코로나바이러스" and k != "감염증" and k != "코로나 신규" and k != "코로나 확진" and k != "신종" and k != "신규" and k != "진자" and k != "감염" and k != "지난" and k != "발생" and k != "확산" and k != "방역" and k != "검사" and k != "관련" and k != "본부" and k != "정부" and k != "가운데": # 한글자인건 빼기
                if i[2].startswith("2020"): # 불러온 csv파일에 20년 데이터와 19년 데이터를 구분하기 위해 넣은 소스
                    if k in wc01:           # 그런데 확인해보니 19년의 데이터가 별로 없기 때문에 구분하지 않았어도 됐다
                        wc01[k] += 1        
                    else:
                        wc01[k] = 1
                else:
                    if k in wc12:
                        wc12[k] += 1
                    else:
                        wc12[k] = 1
f.close()

word, count = [],[]
for i,v in wc12.items():
    word.append(i)
    count.append(v)


df12 = DataFrame()
df12['단어'] = word
df12['단어수'] = count
df12 = df12.sort_values(by = '단어수', ascending=False)
print(df12)
df12.to_csv("C:/wodnd_file/goodNews19.12.csv",index=False)

word2, count2 = [],[]
for i,v in wc01.items():
    word2.append(i)
    count2.append(v)


df01 = DataFrame()
df01['단어'] = word2
df01['단어수'] = count2
df01 = df01.sort_values(by = '단어수', ascending=False)
print(df01)
df01.to_csv("C:/wodnd_file/goodNews20.01.csv",index=False)
# df.to_csv("D:/wodnd_file/test7.csv",header=False)

# wc = WordCloud(font_path="C:\\windows\\Fonts\\malgun.ttf", background_color='white').generate(txt)
                                                        # # # 알아서 단어수 세가지고 많이 나오는건 크게 적게 나오는건 작게
# plt.imshow(wc) # 이미지 그릴때는 imshow()
# plt.show()
# df = df.head(20)
# plt.bar(df['단어'], df['단어수'])
# plt.show()






