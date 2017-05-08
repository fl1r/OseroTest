import os



board = [[0 for col in range(9)] for row in range(9)]
PlayerAttribute=1
for a in range(0,9):
    for b in range(0,9):
        board[a][b]=0

#盤面初期設定
def Initialize():
    board[3][3]=1
    board[4][4]=1
    board[4][3]=2
    board[3][4]=2

#コンソール上に基盤の表示
def SeeBoard():
    os.system('cls')
    for a in range(0,9):
        for b in range(0,9):
            print(board[b][a],end='')
        print('\n')

#石の設置
def move():
    print("You are "+PlayerAttribute)
    print("Where do you want to move?")
    x=input()
    y=input()
    board[b-1][a-1]=PlayerAttribute
    if(PlayerAttribute=='1'):
        PlayerAttribute=2
    else:
        PlayerAttribute=1



Initialize()
SeeBoard()
move()
SeeBoard()

while(True):
    print("Player:",end='')
    p=input()
    if(p=='1'):
        print("you are 1")
    if(p=='2'):
        print("you are 2")
    else:
        print("error")