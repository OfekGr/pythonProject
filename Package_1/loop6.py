grade=int(input("insert grade: "))
count=0
sum=0
fcount=0
fsum=0
while 0<=grade<=100:
    if grade>60 or grade==60:
        sum+=grade
        count+=1
        grade = int(input("insert grade: "))
    if grade<60:
        fcount+=1
        fsum+=grade
        grade = int(input("insert grade: "))
print(f"pass count:,{count}pass average,{sum/count}")
print(f"fail count:,{fcount}fail average,{fsum/fcount}")