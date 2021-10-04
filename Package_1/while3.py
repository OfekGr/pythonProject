num1=int(input("Insert first number: "))
num2=int(input("Insert second number: "))
while num1%2==0 and num2%2==0:
    print(num1+num2)
    num1 = int(input("Insert first number: "))
    num2 = int(input("Insert second number: "))
print(num1*num2)