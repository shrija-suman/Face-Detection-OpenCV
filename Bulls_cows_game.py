secret_code=input("\n1st Player please....enter the secret code:")
list2=list(secret_code)
print(list2)
bulls=0
count=0
n=input("\nSecond player please gues...")
list1=list(n)
print("\nYou have 12 turns")
for i in range(12):
    while list1!=list2:
        n=input("\nSecond player please gues...")
        list1=list(n)
        for j in range(4):
            if(list1[j]==list2[j]):
                bulls+=1
        for i in list2:
            if i in list1:
                count+=1
        print("Bulls",bulls)
        print('Cows',count-bulls)
        bulls=0
        count=0
if(list1==list2):
    print("\nPlayer2 WON!!....player2 guessed right...")
else:
   print("\nPlayer1 WON!!...Player2 you didn't guessed right...")
            

