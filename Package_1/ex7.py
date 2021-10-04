num1=int(input("enter 1st number: "))
num2=int(input("enter 2nd number: "))
num3=int(input("enter 3rd number: "))
if (num3>num1) and (num3>num2):
    print(num3, "is the biggest number of the three")
else:
    if (num2>num1) and (num2>num3):
        print(num2, "is the biggest number of the three")
    else:
        if (num1>num2) and (num1>num3):
            print(num1, "is the biggest number of the three")
        else:
            print("one or more of the numbers is equal to another number")
