import os
import pickle

class UserName:

    def __init__(self,username,name,password):
        self.user = {
            "username" : username,
            "name" : name,
            "pwd" : password
        }

       




    def dataprint(jl):
        print("Username:",jl.user["username"],"\nRealName:",jl.user["name"],"\nPassWord: *")

    def findUser(self,usern, pwd):
        if usern == self.user["username"] and pwd == self.user["pwd"]:
            return self.user
        else:
            return False

try:
    a_file = open("data.pkl", "rb")
    Data = pickle.load(a_file)
    print(Data)
    a_file.close()
except:
    Data = {
        "CatWoman": UserName("CatWoman", "Salina", "bruceisbat"),
        "Batman": UserName("Batman", "BW", "Catlove"),
        "SuperMan": UserName("SuperMan", "Clerk Kent", "Louis"),
        "AquaMan": UserName("AquaMan", "Arthur Curry", "mostpowerful"),
        "WonderWoman": UserName("WonderWoman", "Diana Prince", "Amazon"),
    }




def Exit():
    try:
        os.remove("data.pkl")
    except:
        print("Bye")
    finally:
        print(Data)
        f = open("data.pkl", "wb")
        pickle.dump(Data, f)
        f.close()




