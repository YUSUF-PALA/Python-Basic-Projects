import sys
import time
XOX=[
        ["_","_","_"],
        ["_","_","_"],
        ["_","_","_"]
    ]
PlayerTurns=[]#To check has if player played

def startGame():
    
    print(" ".join(XOX[0]))
    print(" ".join(XOX[1]))
    print(" ".join(XOX[2]))
def gamerO():
    looper=False
    
    while looper==False:
        RowO=int(input("The row you want to put 'o' :  "))
        ColumnO=int(input("The column you want to put 'o' :  "))
        if RowO>2 or ColumnO>2:
            print("Invalid row or column ! \nTry again ")
            time.sleep(0.5)
            continue
        if XOX[RowO][ColumnO]=="_":
            XOX[RowO][ColumnO]="O"
            PlayerTurns.append("O")
            print(" ".join(XOX[0]))
            print(" ".join(XOX[1]))
            print(" ".join(XOX[2]))
            looper=True

        else:
            time.sleep(0.5)
            print("This place has already been occupied !!")
            looper=False
    
def gamerX():
    looper=False
    
    while looper==False:
        RowX=int(input("The row you want to put 'x' :  "))
        ColumnX=int(input("The column you want to put 'x' :  "))
        if XOX[RowX][ColumnX]=="_":
            XOX[RowX][ColumnX]="X"
            PlayerTurns.append("X")
            print(" ".join(XOX[0]))
            print(" ".join(XOX[1]))
            print(" ".join(XOX[2]))  
            looper=True 
          
        else:
            time.sleep(0.5)
            print("This place has already been occupied !!")
            time.sleep(0.5)
            print("TRY AGAIN")
            looper=False     
def winner():
    if XOX[0][0]==XOX[1][1]==XOX[2][2]=="X":
        print("Player 2 WON !")
        sys.exit()
    elif XOX[0][0]==XOX[1][1]==XOX[2][2]=="O":
        print("Player 1 WON !")
        sys.exit()
    elif XOX[0][2]==XOX[1][1]==XOX[2][0]=="O":
        print("Player 1 WON !")
        sys.exit()
    elif XOX[0][2]==XOX[1][1]==XOX[2][0]=="X":
        print("Player 2 WON !")
        sys.exit()
    elif XOX[0][0]==XOX[0][1]==XOX[0][2]=="X":
        print("Player 2 WON !")
        sys.exit()
    elif XOX[0][0]==XOX[1][0]==XOX[2][0]=="X":
        print("Player 2 WON !")
        sys.exit()
    elif XOX[1][0]==XOX[1][1]==XOX[1][2]=="X":
        print("Player 2 WON !")
        sys.exit()
    elif XOX[2][0]==XOX[2][1]==XOX[2][2]=="X":
        print("Player 2 WON !")
        sys.exit()
    elif XOX[0][1]==XOX[1][1]==XOX[2][1]=="X":
        print("Player 2 WON !")
        sys.exit()
    elif XOX[0][2]==XOX[1][2]==XOX[2][2]=="X":
        print("Player 2 WON !")
        sys.exit()
    elif XOX[0][0]==XOX[0][1]==XOX[0][2]=="O":
        print("Player 1 WON !") 
        sys.exit()                 
    elif XOX[0][0]==XOX[1][0]==XOX[2][0]=="O":
        print("Player 1 WON !")
        sys.exit()
    elif XOX[1][0]==XOX[1][1]==XOX[1][2]=="O":
        print("Player 1 WON !")
        sys.exit()
    elif XOX[2][0]==XOX[2][1]==XOX[2][2]=="O":
        print("Player 1 WON !")
        sys.exit()
    elif XOX[0][1]==XOX[1][1]==XOX[2][1]=="O":
        print("Player 1 WON !")
        sys.exit()
    elif XOX[0][2]==XOX[1][2]==XOX[2][2]=="O":
        print("Player 1 WON !")
        sys.exit()
    elif len(PlayerTurns)==9:
        print("NO WINNER !")
        sys.exit()

is_started=input("Start Game : (start/exit)").lower()
if is_started=="start":
    print("PLAYER 1 -> O")
    print("PLAYER 2 -> X")
    startGame()
    while True:
        gamerO()
        winner()
        gamerX()
        winner()
else :
    print("Exitting...")
    sys.exit()
    
        


