CurrentPay=int(input("insert current payment: "))
Payraise=int(input("insert payraise amount by precent: "))
Payraiseprecent=int(CurrentPay*(Payraise/100))
Futurepayment=CurrentPay+Payraiseprecent
print("Your future payment will be:", Futurepayment)