grade=int(input("insert grade: "))
count=0
sum=0
high=0
while 0<=grade<=100:
        if grade >= high:
            high = grade
            count+=1
            sum+=grade
        grade = int(input("insert grade: "))
print("average is:",sum/count)
print("highest grade is:",high)
print("difference between highest and average is: ",high-(sum/count))
