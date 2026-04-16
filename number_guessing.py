import random
import math
a=int(input("Enter the starting range:"))
b=int(input("Enter the ending range:"))
number=random.randint(a,b)
total_chances = math.ceil(math.log(a - b + 1, 2))
count=0
while True:
    count+=1
    user_number=int(input("Guess the number:"))
    if user_number==number:
        print("You guessed right...you took",count,"try")
        flag=True
        break
    elif user_number>number:
        print("You guessed too high!")
        print("Guess again!")
        continue
    elif user_number<number:
        print("You guessed too low!")
        print("Guess again!")
        continue

if not flag:
    print("Sorry you lost all the chances")
    print("The number is",number)
print("Game ended....")
    
