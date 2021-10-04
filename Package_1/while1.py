num1=int(input("insert number here"))
while num1>=100 and num1<=999:
    ldig=(num1//100)
    mdig=num1//10%10
    rdig=num1%10
    print(ldig+mdig+rdig)
    num1 = int(input("insert number here"))
print("error, number not between 100-999")