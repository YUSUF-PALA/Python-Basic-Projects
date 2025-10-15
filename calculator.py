import sys
import os
operations=["multiplication","division","addition","subtract"]
class calculator:
    def multiple(a,b):
        multiplication=a*b
        print("The result is "+str(multiplication))
    def addition(a,b):
        sum=a+b
        print("The result is "+str(sum))
    def subtraction(a,b):
        subs=a-b
        print("The result is "+str(subs))
    def division(a,b):
        div=a/b
        print("The result is "+str(div))



ChoosenOperation=input("Which operation do you want to make?  (multiplication/division/addition/subtract): ").lower()

if ChoosenOperation not in operations:
    print("❌ Undefined division (cannot divide by zero)!")
    restart = input("Do you want to make one more operation? (yes/no): ").lower()

    if restart == "yes":

        os.execl(sys.executable, sys.executable, *sys.argv)
    elif restart =="no":
        print("OK,Good bye..")


Number1=int(input("Enter the first number : "))
Number2=int(input("Enter the second number : "))
if ChoosenOperation=="multiplication":
    calculator.multiple(Number1,Number2)
elif ChoosenOperation=="division":
    if Number2==0:
        print("Undefined division!!")
        pass
    else:
        calculator.division(Number1,Number2)

elif ChoosenOperation=="addition":
    calculator.addition(Number1,Number2)
elif ChoosenOperation=="subtract":
    calculator.subtraction(Number1,Number2)




restart = input("Do you want to make one more operation? (yes/no): ").lower()

if restart == "yes":
    
    os.execl(sys.executable, sys.executable, *sys.argv)

elif restart =="no":
    print("OK,Good bye..")

    
