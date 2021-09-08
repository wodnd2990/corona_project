# -*- coding:utf-8 -*-

f = open("C:/wodnd_file/BigNews1_1.csv","r",encoding="utf-8")
f2 = open("C:/wodnd_file/BigNewsLabel.csv","a",encoding="utf=8")

l = ['적격','부적격']

for v, i in enumerate(f.readlines()):
    i = i.replace("\n","").split("||")
    if v == 0:
        print("1",l[0],"2",l[1])
    print(v,":",i[0])
    what = int(input("뭐 : "))-1
    print(l[what])
    print("")
    f2.write("%s\n"% l[what])
    
f.close()
f2.close()
# 파싱해서 가져온 뉴스데이터를 Naive-Bayes하기 위해 하나 하나 라벨링을 하고 있다

























