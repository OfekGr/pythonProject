grade=int(input("insert grade: "))
count=0
sum=0
if 0<=grade<=100:
    while grade>=60:
        count+=1
        sum+=grade
        grade = int(input("insert grade: "))
    print(sum/count)
else:
    print("fail")