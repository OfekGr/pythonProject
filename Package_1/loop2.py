sum=0
count=0
for i in range(6):
    num=int(input("insert number"))
    if num%2==0:
        sum+=num
        count+=1
print("sum",sum, "average", sum/count)