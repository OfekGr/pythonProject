num1=int(input("insert 3 digits here: "))
rdig=(num1%10)     #right digit
mdig=(num1//10%10)      #middle digit
ldig=(num1//100%10) #left digit
print(f"{rdig}{mdig}{ldig}")
