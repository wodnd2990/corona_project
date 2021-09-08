# -*- coding:utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from wordcloud.wordcloud import WordCloud

fontFile = "C:\\windows\\Fonts\\malgun.ttf"
fontName = fm.FontProperties(fname = fontFile, size = 50).get_name()
plt.rc("font",family=fontName)

df = pd.read_csv("C:/wodnd_file/goodNews20.08.csv")

df = df[(df['단어'] != "기자") & (df['단어'] != "지역") & (df['단어'] != "환자") & (df['단어'] != "추가") & (df['단어'] != "국내") & (df['단어'] != "위해") & (df['단어'] != "당국") & (df['단어'] != "중앙") & (df['단어'] != "대책") & (df['단어'] != "오전") & (df['단어'] != "오후")]
#df = df.head(20)
#plt.bar(df['단어'], df['단어수'])
#plt.xticks(rotation=45)
#plt.show()

#plt.pie(df['단어수'], labels = df['단어'], autopct = "%.1f%%")
#plt.show()

txt = ""

for i in df['단어']:
    txt += i + " "
    print(i)
print(txt)
wc = WordCloud(font_path="C:\\windows\\Fonts\\malgun.ttf", background_color='white').generate(txt)
plt.imshow(wc) 
plt.show() 