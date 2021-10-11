num1=input("insert 1st number")
num2=input("insert 2nd number")
num3=input("insert 3rd number")
list1=[num1, num2, num3]
while list1[0]!='done' and list1[1]!='done' and list1[2]!='done':
    print(list1)
    list1[0] = input("insert 1st number")
    if list1[0]=='done':
        break
    list1[1] = input("insert 2nd number")
    if list1[1]=='done':
        break
    list1[2] = input("insert 3rd number")
    if list1[2]=='done':
        break
print("program ended")