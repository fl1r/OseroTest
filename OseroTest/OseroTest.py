import os

#コンソール上に基盤の表示
def SeeBoard():
    os.system('cls')
    print("012345678")
    for a in range(0,8):
        print(a+1,end='')
        for b in range(0,8):
            print(board[b][a],end='')
        print()

#石の設置
def move():
    global PlayerAttribute
    print("You are ",end='')
    print(PlayerAttribute)
    print("Where do you want to move?")
    x,y= map(int, input().split())
    board[x-1][y-1]=PlayerAttribute
    if(PlayerAttribute==1):
        PlayerAttribute=2
    else:
        PlayerAttribute=1


#盤面初期設定
board = [[0 for col in range(8)] for row in range(8)]
PlayerAttribute=1
for a in range(0,8):
    for b in range(0,8):
        board[a][b]=0
board[3][3]=1
board[4][4]=1
board[4][3]=2
board[3][4]=2

while(True):
    SeeBoard()
    move()
    SeeBoard()
    move()
'''
print("Player:",end='')
print(PlayerAttribute)
'''