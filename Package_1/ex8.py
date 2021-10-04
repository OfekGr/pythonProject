num1=input("insert number of computers worked on today: ")
if num1=="" or num1=="0":
    num1=15
    print("tomorrow you need to work on ", num1*2, "computers")
else:
    num1=int(num1)
    print("tomorrow you need to work on ", num1*2, "computers")