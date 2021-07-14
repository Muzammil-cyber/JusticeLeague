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



Data = {
    "CatWoman" : UserName("CatWoman","Salina","bruceisbat"),
    "Batman" : UserName("Batman","BW","Catlove"),
    "SuperMan" : UserName("SuperMan","Clerk Kent","Louis"),
    "AquaMan" : UserName("AquaMan","Arthur Curry","mostpowerful"),
    "WonderWoman" : UserName("WonderWoman","Diana Prince","Amazon"),
}
