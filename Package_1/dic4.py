max_len=int(input("insert number: "))
dic1={}
for i in max_len:
    dic1.update(dic1.keys(i))
    dic1.update(dic1.values(i*i))
print(dic1)