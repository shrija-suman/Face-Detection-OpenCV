import random
def startgame():
    mat=[]
    for i in range(4):
        mat.append([0] * 4)
    print("Commands are as follows : ")
    print("'u'  : Move Up")
    print("'d'  : Move Down")
    print("'l'  : Move Left")
    print("'r'  : Move Right")
    add_new_2(mat)
    return mat

def add_new_2(mat):
    r=random.randint(0,3)
    c=random.randint(0,3)
    mat[r][c]=2
    r=random.randint(0,3)
    c=random.randint(0,3)
    mat[r][c]=2

def get_current_state(mat):
    for i in range(4):
        for j in range(4):
            if(mat[i][j]== 2048):
                return 'WON'
    for i in range(4):
        for j in range(4):
            if(mat[i][j]== 0):
                return 'GAME NOT OVER'
            
    for i in range(3):
        for j in range(3):
            if(mat[i][j]== mat[i + 1][j] or mat[i][j]== mat[i][j + 1]):
                return 'GAME NOT OVER'
 
    for j in range(3):
        if(mat[3][j]== mat[3][j + 1]):
            return 'GAME NOT OVER'
 
    for i in range(3):
        if(mat[i][3]== mat[i + 1][3]):
            return 'GAME NOT OVER'
    return "LOST"

def add_2(mat):
    r=random.randint(0,3)
    c=random.randint(0,3)
    while mat[r][c]!=0:
        r=random.randint(0,3)
        c=random.randint(0,3)
    mat[r][c]=2
    return mat

def move_right(mat,r,c):
    while(mat[r][c+1]==0 or c<3 ):
            c+=1
            mat[r][c]=mat[r][c-1]
            mat[r][c-1]=0
    if(mat[r][c+1]!=0):
        if(mat[r][c]==mat[r][c+1]):
            mat[r][c+1]=mat[r][c]+mat[r][c+1]
            mat[r][c]=0
        else:
            print("You can't move more right")
    return mat,r,c

def move_left(mat,r,c):
    while(mat[r][c-1]==0 or c>0):
            mat[r][c+1]=mat[r][c]
            mat[r][c]=0
            c-=1
    if(mat[r][c-1]!=0):
        if(mat[r][c-1]==mat[r][c]):
            mat[r][c-1]=mat[r][c-1]+mat[r][c]
            mat[r][c]=0
        else:
            print("You can't move more left")
    return mat,r,c

def move_upward(mat,r,c):
    while(mat[r-1][c]==0 or r>0):
            mat[r+1][c]=mat[r][c]
            mat[r][c]=0
            r-=1
    if(mat[r-1][c]!=0):
        if(mat[r-1][c]==mat[r][c]):
            mat[r-1][c]=mat[r-1][c]+mat[r][c]
            mat[r][c]=0
        else:
            print("You can't move more upward")
    return mat,r,c

def move_downward(mat,r,c):
    while(mat[r+1][c]==0 or (r<2)):
            r+=1
            mat[r][c]=mat[r-1][c]
            mat[r-1][c]=0
    if(mat[r+1][c]!=0):
        if(mat[r][c]==mat[r+1][c]):
            mat[r+1][c]=mat[r+1][c]+mat[r][c]
            mat[r][c]=0
        else:
            print("You can't move more right")
    return mat,r,c

def game():
    mat=startgame()
    p=get_current_state(mat)   
    for i in range(4):
        for j in range(4):
            print(mat[i][j],end='  ')
        print("\n")
    Rw=int(input("\nEnter the row number you want to operate the operation:"))
    Cl=int(input("\nEnter the column number you want to operate the operation:"))
    while p!='WON':
        for i in range(4):
            for j in range(4):
                print(mat[i][j],end='  ')
            print("\n")
        Op=input("\nEnter the operation you wanna perform:")
        mat=add_2(mat)
        if(Op=="r"):
            mat,Rw,Cl=move_right(mat,Rw,Cl)
        if(Op=='l'):
            mat,Rw,Cl=move_left(mat,Rw,Cl)
        if(Op=='u'):
            mat,Rw,Cl=move_upward(mat,Rw,Cl)
        if(Op=='d'):
            mat,Rw,Cl=move_downward(mat,Rw,Cl)
        print('\n')
        print(p)
    
game()


 
