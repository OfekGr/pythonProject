num1=int(input("insert number: "))
count=0
while num1!=0:
    if num1%3==0:
        count+=1
        num1 = int(input("insert number: "))
    elif num1%7==0:
        count += 1
        num1 = int(input("insert number: "))
    else:
        num1 = int(input("insert number:"))
else:
    print("amount of numbers that can be divided by 3 or 7 is:", count)