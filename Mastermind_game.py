import random
def Game(Banda):
    player=Banda
    print("Now...Player is ",player)
    number = random.randrange(1000, 10000)
    number=str(number)
    count=0
    turns=6
    gcount=0
    guess=[]
    flag=False
    while count<turns:
        count+=1
        print("Start guessing...again")
        num=input("Enter a four digit guessing number:")
        for i in range(0,4):
            if num==number[i]:
                gcount+=1
            if num[i]==number[i]:
                guess.append(number[i])
                print(num[i],end=" ")
            elif number[i] in guess:
                print(number[i],end=" ")
            else:
                print("X",end=" ")
        if gcount==4:
            flag=True
            print("\n")
            print("CONGRATULATIONS!!..YOU IS MATERMIND",player)
            print("You guessed completely...your number is",number)
            return True 
    if not flag:
        print("\n")
        print("OOPS!! YOU LOST ALL THE CHANCES")
        print("other player will play now")
        return False
    
person1=input("Enter the name of first player:")
person2=input("Enter the name of second player:")
result=Game(person1)
while result==False:
    temp=person1
    person1=person2
    person2=temp
    result=Game(person1)