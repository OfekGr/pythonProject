a=int(input("Insert number: "))
b=2
while b<=9:
    if a%b==0:
        print(b,"number not primary")
    else:
        b=b+1
if a%b!=0:
    print(b,"primary number")