num1=int(input("insert number here: "))
while num1>=0 and num1<=120:
    if num1<=18:
        print("child")
    if num1>=19 and num1<=60:
        print("adult")
    if num1>=61:
        print("senior")
    num1 = int(input("insert number here: "))
print("error, number not between 0-120")