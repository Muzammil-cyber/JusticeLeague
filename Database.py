class UserName:

    def __init__(self,no,username,name,password):
        self.user = {
            "id" : no,
            "username" : username,
            "name" : name,
            "pwd" : password

        }

    def dataprint(jl):
        print("id no.:",jl.user["id"],"\nUsername:",jl.user["username"],"\nRealName:",jl.user["name"],"\nPassWord: *")

    def findUser(self,usern, pwd):
        if usern == self.user["username"] and pwd == self.user["pwd"]:
            return self.user
        else:
            return False



Data = {
    "CatWoman" : UserName(0,"CatWoman","Salina","bruceisbat"),
    "Batman" : UserName(1,"Batman","BW","Catlove"),
    "SuperMan" : UserName(2,"SuperMan","Clerk Kent","Louis"),
    "AquaMan" : UserName(3,"AquaMan","Arthur Curry","mostpowerful"),
    "WonderWoman" : UserName(4,"WonderWoman","Diana Prince","Amazon"),
}
