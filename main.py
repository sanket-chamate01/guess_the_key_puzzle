import random
from colorama import Fore as co
from colorama import Style 

r = 0
temp = r
c = 0
temp = temp//10
b = 0
temp = temp//10
a = 0

def startGame():
    global r  
    r = random.randint(100,999)
    rannum(r)
    hints()
    print("******************************\nChoose your option\n1.Enter answer\n2.Next question\n3.Exit\n******************************\n")
    condi2 = True
    while condi2:
        choice2 = int(input("Enter your choice : "))

        if choice2==2:
            startGame()
        elif choice2==3:
            condi2 = False
            exit()
        elif choice2==1:
            checkAns()
        else:
            print(co.BLUE + "Invalid option, choose again")
            print(Style.RESET_ALL)

def rannum(r):
    temp = r
    global c
    c = temp%10
    temp = temp//10
    global b
    b = temp%10
    temp = temp//10
    global a
    a = temp%10

def hints():
    print("******************************\nHints: ")
    print("1.One digit is correct at correct position : ")
    hint1()
    print("2.One digit is correct but wrongly placed : ")
    hint2()
    print("3.One digit is correct but wrongly placed : ")
    hint2()
    print("4.Two digit are correct but wrongly placed : ")
    hint3()
    print("5.One digit is correct at correct position : ")
    hint1()

def hint1():
    ran = random.randint(1,3)
    ran1 = random.randint(2,8)
    ran2 = random.randint(2,8)

    if ran==1:
        if ran2 == b or c:
            ran2-=1
        if ran1 == b or c:
            ran1+=1
        print(a*100 + ran1*10 + ran2)
    if ran==2:
        if ran2 == a or c:
            ran2-=1
        if ran1 == a or c:
            ran1+=1
        print(ran2*100 + b*10 + ran1)
    if ran==3:
        if ran2 == a or b:
            ran2-=1
        if ran1 == a or b:
            ran1+=1
        print(ran1*100 + ran2*10 + c)

def hint2():
    ran = random.randint(1,3)
    ran1 = random.randint(2,8)
    ran2 = random.randint(2,8)

    if ran==1:
        if ran2 == a or c:
            ran2-=1
        if ran1 == a or c:
            ran1+=1
        sum = ran1*100 + ran2*10 + b
        if sum<100:print(sum*10)
        else:print(sum)
    if ran==2:
        if ran2 == a or b:
            ran2-=1
        if ran1 == a or b:
            ran1+=1
        sum = ran2*100 + c*10 + ran1
        if sum<100:print(sum*10)
        else:print(sum)
    if ran==3:
        if ran2 == b or c:
            ran2-=1
        if ran1 == b or c:
            ran1+=1
        sum = ran1*100 + a*10 + ran2
        if sum<100:print(sum*10)
        else:print(sum)

def hint3():
    ran = random.randint(1,3)
    ran1 = random.randint(2,8)

    if ran==1:
        if ran1 == b:
            ran1+=1
        print(a*100 + ran1*10 + c)
    if ran==2:
        if ran1 == c:
            ran1-=1
        print(ran1*100 + b*10 + a)
    if ran==3:
        if ran1 == a:
            ran1+=1
        print(ran1*100 + c*10 + b)

def checkAns():
    ans = int(input("Enter your answer : "))
    temp1 = ans
    c1 = temp1%10
    temp1 = temp1//10
    b1 = temp1%10
    temp1 = temp1//10
    a1 = temp1%10

    isa,isb,isc = 0,0,0

    if c1==c:
        isc+=1
    if b1==b:
        isb+=1
    if a1==a:
        isa+=1

    if isb == isa == isc == 1:
        print(co.GREEN + "Correct Answer")
        print(Style.RESET_ALL)
        correctAns()
    else:
        print(co.RED + "Wrong Answer")
        print(Style.RESET_ALL)
        wrongAns(ans)

def correctAns():
    print("******************************\nChoose your option\n1.Next question\n2.Exit\n******************************\n")

    condi3 = True
    while condi3:
        choice3 = int(input("Enter your choice : "))

        if choice3==1:
            startGame()
        elif choice3==2:
            condi3 = False
            exit()
        else:
            print(co.BLUE + "Invalid option, choose again")
            print(Style.RESET_ALL)

def wrongAns(ans):
    print("******************************\nChoose your option\n1.Retry\n2.Next question\n3.Check Correctness\n4.Exit\n******************************\n")

    condi4 = True
    while condi4:
        choice4 = int(input("Enter your choice : "))

        if choice4==2:
            startGame()
        elif choice4==4:
            condi4 = False
            exit()
        elif choice4==1:
            checkAns()
        elif choice4==3:
            checkCorr(ans)
        else:
            print(co.BLUE + "Invalid option, choose again")
            print(Style.RESET_ALL)

def checkCorr(ans):
    temp2 = ans
    c2 = temp2%10
    temp2 = temp2//10
    b2 = temp2%10
    temp2 = temp2//10
    a2 = temp2%10

    isa1,isb1,isc1 = 0,0,0

    if c2==c:
        isc1+=1
    if b2==b:
        isb1+=1
    if a2==a:
        isa1+=1
    
    if isc1!=1 and isb1!=1 and isa1!=1:
        print("All three digits is incorrect")
    elif isb1!=1 and isa1!=1:
        print("First and Second digit are incorrect")
    elif isa1!=1 and isc1!=1:
        print("First and Third digit are incorrect")
    elif isc1!=1 and isb1!=1:
        print("Second and Third digit are incorrect")
    elif isc1!=1:
        print("Third digit is incorrect")
    elif isb1!=1:
        print("Second digit is incorrect")
    elif isa1!=1:
        print("First digit is incorrect")

    print("******************************\nChoose your option\n1.Retry\n2.Next question\n3.Exit\n******************************\n")

    condi4 = True
    while condi4:
        choice4 = int(input("Enter your choice : "))

        if choice4==2:
            startGame()
        elif choice4==3:
            condi4 = False
            exit()
        elif choice4==1:
            checkAns()
        else:
            print(co.BLUE + "Invalid option, choose again")
            print(Style.RESET_ALL)

if __name__=="__main__":
    print("******************************\nChoose your option\n1.Start\n2.Exit\n******************************\n")

    condi1 = True
    while condi1:
        choice1 = int(input("Enter your choice : "))

        if choice1==1:
            startGame()
        elif choice1==2:
            condi1 = False
            exit()
        else:
            print(co.BLUE + "Invalid option, choose again")
            print(Style.RESET_ALL)