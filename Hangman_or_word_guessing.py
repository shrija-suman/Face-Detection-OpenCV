import random
list=["Mumbai","Delhi","Banglore","Pune","Jaipur","Kolkata","Chennai","Amritsar"]
city=random.choice(list)
turns=12
count=0
wcount=0
gcount=0
for char in city:
    wcount+=1
guess=[]
while count<wcount+2:
    count+=1
    print("Guess it....it is a city name")
    word=input("Enter the guessing word:")
    for char in city:
        if word==char:
            gcount+=1
        if word==char:
            guess.append(char)
            print(word,end=" ")
        elif char in guess:
            print(char,end=" ")
        else:
            print("-",end=" ")
    if gcount==wcount:
        flag=True
        print("\n")
        print("CONGRATULATIONS!!..YOU GUESSED RIGHT")
        print("You guessed completely...your word is",city)    
        break

if not flag:
    print("\n")
    print("OOPS!! YOU LOST ALL THE CHANCES")
    print("Better luck next time")