# -*- coding:utf-8 -*-
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

f = open("C:/wodnd_file/BigNews1_1.csv","r",encoding="utf-8")
f2 = open("C:/wodnd_file/BigNewsLabel.csv","r",encoding="utf-8")
l,l2 = [],[]

for i in f.readlines():
    i = i.replace("\n","").split("||")[0]
    l.append(i)
for i in f2.readlines():
    i = i.replace("\n","")
    l2.append(i)
f2.close()
f.close()
    
cv = CountVectorizer() # 단어별 등장횟수
cvResult = cv.fit_transform(l).toarray() # 학습시키고, 변환시키고
mnb = MultinomialNB().fit(cvResult,l2) # 객체를 만들어서 학습
good = []
for k in range(1,6):
    f3 = open("C:/wodnd_file/BigNews%s.csv"% k,"r",encoding="utf-8")
    f4 = open("C:/wodnd_file/realNews%s.csv"% k,"a",encoding="utf-8")
    for i in f3.readlines():
        i = i.replace("\n","").split("||")
        review = i[0]
        reviewR = cv.transform([review]).toarray() # 뉴스 내용 변환
        result = mnb.predict(reviewR)[0] # 위에서 객체를 학습시킨 것을 이용해 판단하기
        f4.write("%s||"% result)
        f4.write("%s||"% review)
        f4.write("%s\n"% i[1])
    f3.close()
    f4.close()
# 뉴스 내용에 맞게 라벨링 한 것들을 가지고 나머지 뉴스들을 지도학습을 통해 AI가 스스로 판단해 
# 라벨을 부착할수 있도록 학습시킨 것











