# -*- coding:utf-8 -*-

f = open("D:/wodnd_file/BigNews5.csv","r",encoding="utf-8")
ff = open("D:/wodnd_file/BigNews1_1.csv","a",encoding="utf-8")

for v,i in enumerate(f.readlines()):
    i = i.replace("\n","")
    print(i[0],":",i[1])
    ff.write("%s\n"% i)
    if v == 299:
        break
    
f.close()
f2.close()
ff.close()


























