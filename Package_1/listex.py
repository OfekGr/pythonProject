import random
randomlist = []
for i in range(10):
    num1 = random.randint(1,100)
    randomlist.append(num1)
print(randomlist)

from random import randint
randomlist2 = [ randint(1,100) for i in range(10)]
print (randomlist2)