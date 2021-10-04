from random import randint
num1=randint(0, 120)
print(num1)
if 0<=num1<=18:
    print("child")
else:
    if 19<=num1<=60:
        print("adult")
    else:
        if 61<=num1<=120:
            print("senior")

if num1<0 or num1>120:
    print("invalid age")
