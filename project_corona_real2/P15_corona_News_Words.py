# -*- coding:utf-8 -*-
# 한국언론진흥재단_뉴스빅데이터_메타데이터_코로나
# data.go.kr
# 네이버 검색어를 단어화한 것들은 딱히 쓸모가 없어보여 다시 찾은 데이터
# 이번에도 타이틀과 내용만 빼서 csv로 저장 후
# 단어로 나누고 다듬고 수세서 pd로 csv에 저장
import pandas as pd
import numpy as np
from sys import maxunicode
from unicodedata import category
from nltk.tokenize import word_tokenize
import seaborn as sns
import matplotlib.pyplot as plt 
import matplotlib.font_manager as fm 
from konlpy.tag._okt import Okt

fontFile = "C:\\windows\\Fonts\\malgun.ttf"
fontName = fm.FontProperties(fname = fontFile, size = 50).get_name()
plt.rc("font",family=fontName) 

 # f = open("D:/wodnd_file/coronaSearch.csv","r",encoding="utf=8")
f = open("D:/wodnd_file/NewsBig3.csv","r",encoding="utf-8")
special = []
for i in range(maxunicode):
    if category(chr(i)).startswith('P'):
        special.append(chr(i))
        
wt = None
wc = {}
l = []
o = Okt()
for i in f.readlines():
    i = i.replace("\n","")
    for s in special:
        i = i.replace(s,"")
    wt = word_tokenize(i) # 정규화
    wt = o.nouns(i) # 명사
    for v in wt:
        # v = o.pos(v)
        # for w,p in v:
            # if p != "Josa":
        # print(len(v),v)
        if v != '코로나' and v != '사건' and v != '뉴스' and v != '���완' and v != '신종' and v != '추가' and v != '확진' and v != '환자' and v != '코확진' and v != '환자' and v != '속보' and v != '코로' and len(v) != 1 and v != '진자' and v != '코로나바이러스' and v != '검사' and v != '명확' and v != '감염' and v != '사람' and v != '슈퍼' and v != '[속보]' and v != '코로' and v != '코로' and v != '코로':                           
            # if v =='진자':
                # v = '확진자'
            print(v) 
            if v in wc:
                wc[v] += 1
            else:
                wc[v] = 1
f.close()

word, count = [],[]

for i,v in wc.items():
    if v >= 10:
        word.append(i)
        count.append(v)
        
df = pd.DataFrame()
df['word'] = word
df['count'] = count
df = df.sort_values(by='count', ascending=False)

df.to_csv("D:/wodnd_file/NewsBigDF.csv",header=False, index=False)




