#List from 1-10-------------------------------------------- 2
newlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(newlist)

#Slice last 3 numbers-------------------------------------- 3
newlist=newlist[7:10:1]
print(newlist)

#Reverse list order----------------------------------------- 4
print((newlist)[::-1])

#Print list of even indexes---------------------------------- 5
print(newlist[::2])

#Print list of first 5 numbers ------------------------------- 6
newlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
newlist = newlist[0:5:1]
print(newlist)

#New list of odd numbers from old list ------------------------ 7
newlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nlist= []
for i in range(len(newlist)):
    if i%2!=0:
        nlist.append(i)
print(nlist)

#