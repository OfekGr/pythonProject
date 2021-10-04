pword=input("Insert password: ")
count=0
while count<5:
    if pword!="abcd":
        count+=1
        print("wrong password, please try again")
        pword = input("Insert password: ")
    else:
        print("successful login! welcome back")
        break
else:
    print("Your account has been blocked, too many wrong attempts")