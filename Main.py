import Database as data
print("Welcome To Justice League")
user = input("UserName: ")
pwd = input("Password: ")
found = True

try:
   found = data.Data[user].findUser(user,pwd)
except:
   found = False


if found == False:
   print("Wrong UserName or PassWord")
else:
  txt = "Welcome to Justice League Tower\n          {}\nPersonal Detail:\nReal Name:{}"
  print(txt.format(found['username'],found['name']))
