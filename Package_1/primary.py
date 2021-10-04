num1=int(input("insert number "))
count=2
for i in range(2,10):
    if num1%count!=0:
        count+=1
        if count==9:
            print("the number you entered is primary: ",num1)
if num1%count==0:
    print("not primary")