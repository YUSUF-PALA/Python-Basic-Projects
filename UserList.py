UserName=[]
UserPassword=[]
UserName.append(input("Enter your Name : "))
UserPassword.append(input("Enter password : "))
UserInformation=UserName + UserPassword
for info in UserInformation:
    print(info)
