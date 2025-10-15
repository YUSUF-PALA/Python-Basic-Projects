import sys
import os
Answer=["yes","no"]
def ask_yes_no(prompt):
    while True:
        answer = input(prompt).lower()
        if answer in Answer:
            return answer
        print("❌ Invalid input! Please enter 'yes' or 'no'.")

def withdraw():
    leftAmount=int(input("How many dollars you want to withdraw : "))
    if leftAmount<NewBank_obj.Balance:
        NewBank_obj.Balance -= leftAmount
        print("Current balance :"f"{NewBank_obj.Balance}"" $")
    else:
        print("Not enough money!!")

def deposite():
    deposited=int(input("How many dollars you deposited : "))
    NewBank_obj.Balance += deposited
    print("Current balance :"f"{NewBank_obj.Balance}"" $")

def DisplayInfo():
    print("User Full Name : "f"{NewBank_obj.UserName.capitalize()}")
    print("Current balance : "f"{NewBank_obj.Balance}")
    


class BankAccount:
    def __init__(self,BankName,UserName,AccountNo,Balance):
        self.BankName=BankName
        self.UserName=UserName
        self.AccountNo=AccountNo
        self.Balance=Balance

UserAction=False
ActionCheck=input("Do you want to enter and display your account information? : (yes/no)").lower()

if ActionCheck=="yes":
    UserAction=True
elif ActionCheck=="no":
    UserAction=False
    print("Okay,Good bye!!!!")
    sys.exit()
else: 
    user_choice = ask_yes_no("Do you want to restart? (yes/no): ")
    if user_choice == "yes":
        os.execl(sys.executable, sys.executable, *sys.argv)#Taken from AI
    else:
        sys.exit()
NewBank_obj=BankAccount(input("What bank do you use? : "),input("What is your user name : "),int(input("Enter your account number : ")),int(input("Balance : ")))
Choose=input("What do you want to do : \n1.Withdraw \n2.Deposite \n3.Display Account Info \n4.Cancel \n||Please choose as a number(1,2,3,4) : ")

request=None

if Choose=="1":
    withdraw()
    request=input("Do you want to see your account infos : (yes/no)").lower()
    if request == "yes":
        DisplayInfo()
    elif request== "no":
        pass
        
    
    
elif Choose=="2":
    deposite()
    request=input("Do you want to see your account infos : (yes/no)").lower()
    if request == "yes":
        DisplayInfo()
    elif request== "no":
        pass
        
elif Choose=="3":
    print(NewBank_obj.BankName,NewBank_obj.UserName,NewBank_obj.AccountNo,NewBank_obj.Balance)
elif Choose=="4":
    sys.exit()

    


