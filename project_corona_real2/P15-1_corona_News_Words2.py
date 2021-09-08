# -*- coding:utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt 
import matplotlib.font_manager as fm 
from wordcloud.wordcloud import WordCloud

fontFile = "C:\\windows\\Fonts\\malgun.ttf"
fontName = fm.FontProperties(fname = fontFile, size = 50).get_name()
plt.rc("font",family=fontName) 


df = pd.read_csv("C:/wodnd_file/NewsBigDF.csv", names=['word','count'])
print(df)

df2 = df.head(20)
plt.bar(df2['word'], df2['count'])
plt.xticks(rotation=35)
plt.show()

txt = ""
for i in df['word']:
    txt += i + " "


wc = WordCloud(font_path="C:\\windows\\Fonts\\malgun.ttf", background_color='white').generate(txt)
                                                        # # 알아서 단어수 세가지고 많이 나오는건 크게 적게 나오는건 작게
plt.imshow(wc) # 이미지 그릴때는 imshow()
plt.show()








# 이렇게 해봤더니 쓸모없는 뉴스가 너무 많았다
# 그래서 지도학습을 통해 필요없는 뉴스 내용은 빼기로 결정













