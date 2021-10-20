from random import randint
randomlist2 = [ randint(1,100) for i in range(10)]
print (randomlist2)

t1=()
t1=tuple(randomlist2)
print(t1)

num1=int(input("insert number here: "))
t1=t1+(num1,)
print(t1)

newlist=list(t1)
num2=(len(newlist)-1)
edited_list=newlist[0:4]+newlist[6:10]
t2=tuple(edited_list)
print(t2)

no_first=list(t2)
t3=tuple(no_first[1:8])
print (t3)