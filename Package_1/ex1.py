day=int(input("Insert day: "))
month=int(input("Insert month: "))
year=int(input("Insert year: "))
updated_year=year//10%100
print(f"{day}/{month}/{updated_year}")