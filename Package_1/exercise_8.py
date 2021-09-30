a=int(input("insert first number here: "))
b=int(input("insert second number here: "))
count=a+1
while a<count<b:
    if count%2==0:
        print(count)
        count=count+2
    else:
        if count%2!=0:
            count=count+1