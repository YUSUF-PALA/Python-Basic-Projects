#I tried but I couldn't find a way to write it by using Class,This way was easier.
#I tried but I couldn't find a way to write it by using Class,This way was easier.
#I tried but I couldn't find a way to write it by using Class,This way was easier.
import random
import sys


GuessCount=[]

PlayerGuess=None
Start=input("Start the Game :  \n(Start/Exit) : ").capitalize()
if Start=="Start":
    Unknown=random.randint(1,100)
    while PlayerGuess!=Unknown:
        PlayerGuess=int(input("Do you actually believe you can guess the number ? Then GOO! : \n"))
        GuessCount.append(PlayerGuess)
        if PlayerGuess<Unknown:
            print("No,yours is smaller!")
        elif PlayerGuess>Unknown:
            print("NO! Yours is bigger,think smaller.")
    print("  CONGRATULATIONS   !! \nYou finally found it!!")
    request=input("Also if you want to see your guess count I saved it. (yes/no) : ").lower()
    if request=="yes":
        print(GuessCount)
        print("You've tried "f"{len(GuessCount)}"" times.")
    elif request=="no":
        sys.exit()  
elif Start=="Exit":
    sys.exit()

    

