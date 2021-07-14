import Database as data
print("Welcome To Justice League")
def signin():
    user = input("UserName: ")
    pwd = input("Password: ")

    Verify(user, pwd)
def Verify(user,pwd):
    try:
        found = data.Data[user].findUser(user, pwd)
    except:
        found = False

    #
    if found == False:
        print("Wrong UserName or PassWord")
        create = int(input("Wanna Create a New Account press 2 or wanna Try Again press 1 or press 0 to Exit"))
        while create != 1 and create !=2 and create != 0:
            create = int(input("Enter 1 to Try Again or Enter 2 to Create a Account or Enter 0 to EXIT"))
        if create == 1:
            signin()
        elif create == 2: signup()
        else: print("Bye-Bye")


    else:
        txt = "Welcome to Justice League Tower\n          {}\nPersonal Detail:\nReal Name:{}"
        print(txt.format(found['username'], found['name']))
        signout = input("Press ENTER to SignOut\n")
        while signout != "":
           signout = input("Just Press the ENTER button")
        main()

def main():
    user = int(input("Enter 1 for SignIn and 2 for Signup and 0 to Exit\n"))
    while user != 1 and user != 2 and user != 0:
        user = int(input("For SignIn enter 1 and for SignUp enter 2, Dumba*s\n"))
    if user == 1:
        signin()
    elif user == 2:
        signup()
    else:
        print("!!!Bye-Bye!!!")
def signup():
    user = input("Enter New UserName: ")
    pwd = input("Enter New Password: ")
    cpwd = input("Confirm your PassWord: ")
    while pwd != cpwd:
        print("PassWord didnt Match Try Again")
        pwd = input("Enter New Password: ")
        cpwd = input("Confirm your PassWord: ")
    realname = input("Enter Your Name: ")
    newuser = data.Data.setdefault(user,data.UserName(user,realname,pwd))

    data.Data[user].dataprint()
    print("Account Created")
    main()

main()
