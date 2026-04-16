import random
flag=True
while flag:
 
 name=input('\nEnter player name:\n')
 user_choice=input('\nEnter your choice:\n')

 comp_choice=random.randint(1,3)
 if comp_choice==1:
     comp_choice='Rock'
 if comp_choice==2:
     comp_choice='Paper'
 if comp_choice==3:
      comp_choice='Scissor'

 print("\nNow it's computer's turn....")
 print("Computer choose",comp_choice)

 if comp_choice == 'Rock' and user_choice == 'Paper' or comp_choice == 'Paper' and user_choice == 'Scissor'  or comp_choice == 'Scissor' and user_choice == 'Rock':
     print("\nSo...",name,'CONGRATULATIONS...YOU WON!!...')
 elif user_choice == 'Rock' and comp_choice == 'Paper' or user_choice == 'Paper' and comp_choice == 'Scissor'  or user_choice == 'Scissor' and comp_choice == 'Rock': 
     print("\nSo...COMPUTER WON!!...better luck next time")
 elif user_choice==comp_choice:
     print("\nMatch is drawn...you both choose same choice...")

 M=int(input("\nDo you want to play again...\nPress 1 for yess \n Press 2 for no\n"))
 if M == 1:
     flag=True
 else:
     flag=False