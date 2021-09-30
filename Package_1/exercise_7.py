name=input("Insert name here: ")
currentyear=int(input("Insert current year here:"))
age=int(input("Insert age here: "))
futureyear=int(input("Insert future year here: "))
addedyears=futureyear-currentyear
old=age+addedyears
print(f"{name} will be {old} in year {futureyear}")