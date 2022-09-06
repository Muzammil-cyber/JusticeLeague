import datetime as dt
import io
import os
import pickle
import random
import webbrowser as wb
from random import randint
from time import sleep
from tkinter import *
from tkinter import ttk, messagebox, colorchooser, filedialog
from urllib.request import urlopen
import requests as req
import speech_recognition as sr
import wikipedia as wiki
import wolframalpha as wa
from PIL import ImageTk, Image
from PyDictionary import PyDictionary as Dic
from googlesearch import search
from resizeimage import resizeimage


class UserName:

    def __init__(self, username, Fname, Lname, password, dob, sex, AssistantName="Mark 6", ):
        self.user = {
            "username": username,
            "First Name": Fname,
            "Last Name": Lname,
            "pwd": password,
            "Date of Birth": dob,
            "Gender": sex,
            "AI data": AssistantName
        }

    def dataprint(self):
        print("Username:", self.user["username"], "\nRealName:", self.user["First Name"] + " " + self.user["Last Name"],
              "\nPassWord: *")

    def findUser(self, usern, pwd):
        if usern == self.user["username"] and pwd == self.user["pwd"]:
            return self.user
        else:
            return False

    def Change(self, change, New):
        self.user[change] = New

    def AINameChange(self, AssistantName):
        self.user["AI data"] = AssistantName


try:
    a_file = open("data.pkl", "rb")
    Data = pickle.load(a_file)
    # print(Data)
    a_file.close()
except:
    Data = {
        "CatWoman": UserName("CatWoman", "Salina", "Cyile", "bruceisbat", "11-11-2012", "F"),
        "Batman": UserName("Batman", "Bruce", "Wayne", "Catlove", "11-11-2012", "M"),
        "SuperMan": UserName("SuperMan", "Clerk", "Kent", "Louis", "11-11-2012", "M"),
        "AquaMan": UserName("AquaMan", "Arthur", "Curry", "mostpowerful", "11-11-2012", "M"),
        "WonderWoman": UserName("WonderWoman", "Diana", "Prince", "Amazon", "11-11-2012", "F"),
        "W": UserName("W", "Diana", "Prince", "a", "11-11-2012", "F")
    }


def Exit():
    try:
        os.remove("data.pkl")
    except:
        print("Bye")
    finally:
        f = open("data.pkl", "wb")
        pickle.dump(Data, f)
        f.close()


def SignUp(fname, lname, user, passw, cpass, dob, gender, NAR):
    if NAR:
        if passw == cpass and passw != "":
            PP = messagebox.askyesno("Privacy Polices", "We have no Polices, have fun")
            if PP:
                try:
                    Data.setdefault(user,
                                    UserName(str(user), str(fname), str(lname), str(passw), str(dob), str(gender)))
                    Exit()
                except:
                    messagebox.showerror("Error", "An UnExpected Error Occurred")
        else:
            messagebox.showerror("PassWord Not Match", "Your Password doesn't match")
    else:
        messagebox.showerror("Robot Found", "You're a Robot?")


def NameChange(ID):
    dlg = Toplevel()
    dlg.title("Name Setting")
    dlg.lift()
    dlg.grab_set()
    fName = StringVar()
    lName = StringVar()
    fName.set(Data[ID].user["First Name"])
    lName.set(Data[ID].user["Last Name"])
    ttk.Label(dlg, text=f"Current Name: " + Data[ID].user["First Name"] + " " + Data[ID].user["Last Name"]).grid(row=0,
                                                                                                                 column=0)
    ttk.Label(dlg, text="New First Name: ").grid(row=1, column=0)
    ttk.Entry(dlg, textvariable=fName).grid(row=1, column=1, columnspan=2)
    ttk.Label(dlg, text="New Last Name: ").grid(row=2, column=0)
    ttk.Entry(dlg, textvariable=lName).grid(row=2, column=1, columnspan=2)
    ttk.Button(dlg, text="Apply", command=lambda: (
        Data[ID].Change("First Name", fName.get()), Data[ID].Change("Last Name", lName.get()), dlg.destroy(),
        Login(ID, Data[ID].user["pwd"]))).grid(row=3, column=2, sticky="e")


def UserNameChange(ID):
    dlg = Toplevel()
    dlg.title("UserName Setting")
    dlg.lift()
    dlg.grab_set()
    var = StringVar()
    var.set(ID)
    ttk.Label(dlg, text=f"Old Username: {ID}").grid(row=0, column=0)
    ttk.Label(dlg, text="New Username: ").grid(row=1, column=0)
    ttk.Entry(dlg, textvariable=var).grid(row=1, column=1, columnspan=2)
    # data["username"] = var.get()
    ttk.Button(dlg, text="Apply", command=lambda: (ChangeID(ID, var.get()), dlg.destroy())).grid(row=2, column=2,
                                                                                                 sticky="e")


def ChangeID(OldID, NewID):
    Data.setdefault(NewID, UserName(NewID, Data[OldID].user["First Name"], Data[OldID].user["Last Name"],
                                    Data[OldID].user["pwd"], Data[OldID].user["Date of Birth"],
                                    Data[OldID].user["Gender"], Data[OldID].user["AI Data"]
                                    ))
    Data.pop(OldID)
    Login(NewID, Data[NewID].user["pwd"])


def DOBChange(ID):
    dlg = Toplevel()
    dlg.title("DOB Setting")
    dlg.lift()
    dlg.grab_set()
    DOB = Data[ID].user["Date of Birth"].split("-")
    day = StringVar()
    month = StringVar()
    year = StringVar()
    day.set(DOB[0])
    month.set(DOB[1])
    year.set(DOB[2])
    ttk.Label(dlg, text=f"Current Date of Birth: " + Data[ID].user["Date of Birth"]).grid(row=0, column=0, columnspan=3)
    ttk.Label(dlg, text="Date: ").grid(row=1, column=0)
    ttk.Spinbox(dlg, from_=1, to=30, textvariable=day).grid(row=1, column=1)
    ttk.Label(dlg, text="Month: ").grid(row=2, column=0)
    ttk.Spinbox(dlg, from_=1, to=31, textvariable=month).grid(row=2, column=1)
    ttk.Label(dlg, text="Year: ").grid(row=3, column=0)
    ttk.Spinbox(dlg, from_=1920, to=2023, textvariable=year).grid(row=3, column=1)
    ttk.Button(dlg, text="Apply", command=lambda: (
        Data[ID].Change("Date of Birth", f"{day.get()}-{month.get()}-{year.get()}"), dlg.destroy(),
        Login(ID, Data[ID].user["pwd"]))).grid(row=4, column=2)


def GenChange(ID):
    dlg = Toplevel()
    dlg.title("DOB Setting")
    dlg.lift()
    dlg.grab_set()
    var = StringVar()
    var.set(Data[ID].user["Gender"])
    ttk.Radiobutton(dlg, text="Male", variable=var, value="Μ").grid(row=0, column=0)
    ttk.Radiobutton(dlg, text="FeMale", variable=var, value="F").grid(row=0, column=1)
    ttk.Button(dlg, text="Apply", command=lambda: (
        Data[ID].Change("Gender", var.get()), dlg.destroy(), Login(ID, Data[ID].user["pwd"]))).grid(row=1,
                                                                                                    column=1)


def PassWordChange(ID):
    dlg = Toplevel()
    dlg.title("PWD Setting")
    dlg.lift()
    dlg.grab_set()
    var = StringVar()
    var.set(Data[ID].user["pwd"])
    ttk.Label(dlg, text=f"Current PassWord: " + Data[ID].user["pwd"]).grid(row=0, column=0)
    ttk.Entry(dlg, textvariable=var).grid(row=1, column=0)
    ttk.Button(dlg, text="Apply", command=lambda: (
        Data[ID].Change("pwd", var.get()), dlg.destroy(), Login(ID, Data[ID].user["pwd"]))).grid(row=3, column=1)


def WeatherLocation():
    loc = req.get("http://ip-api.com/json").json()
    weaApiKey = "a786c740192c5d9c2cab10255c49ef33"
    weatherDetail = req.get(
        "https://api.openweathermap.org/data/2.5/weather?q={},{}&appid={}&units=metric".format(loc["city"],
                                                                                               loc['countryCode'],
                                                                                               weaApiKey)).json()
    return weatherDetail, loc


def UpdateWeather():
    global weather, location, img
    weather, location = WeatherLocation()
    img = urlopen("http://openweathermap.org/img/wn/{}@2x.png".format(weather["weather"][0]["icon"])).read()
    img = ImageTk.PhotoImage(Image.open(io.BytesIO(img)))
    weaIcon.config(image=img)
    weaCity.config(text=location["city"] + ", " + location['countryCode'])
    weaTemp.config(text=weather["main"]["temp"])
    weaDisc.config(text=weather["weather"][0]["main"])


def CallAssitant(ID):
    username = ID
    assname = Data[ID].user["AI data"]

    SpeakPrint("How may I help you?")
    command = ask().lower()
    if command == "":
        SpeakPrint("Sorry I couldn't hear that Try Again")
    if "good bye" in command or "bye" in command or "stop" in command or "exit" in command or "shutdown" in command:
        SpeakPrint(f"Bye Bye, {assname} Shutting Down")
    elif "sleep" in command and "go" in command:

        chat.insert(END, "For how long(sec)")
        x = ask()
        while x == "":
            chat.insert(END, "For how long(sec)?")
            x = ask()
        num = []
        for y in x.split():
            if y.isdigit():
                num.append(y)
        SpeakPrint(f"Going to sleep for {num[0]} sec")
        sleep(int(num[0]))
    elif "what is your name" in command or "who are you" in command:
        SpeakPrint(f"My name is {assname}")
    elif "change your name" in command:
        SpeakPrint("What will you like to call me")
        assname = ask()
        while assname == "":
            assname = ask()
        SpeakPrint(f"From now onwards my name is {assname}")
        Data[ID].AINameChange(assname)
    elif "what is my name" in command or "do you know my name" in command:
        SpeakPrint(f"Your name is {username}")
    elif "call me" in command or "change my name to" in command:
        SpeakPrint("You can do that here")
        UserNameChange(ID)
    elif "change my name" in command:
        SpeakPrint("What should i call you?")
        username = ask()
        while username == "":
            username = ask()
        ChangeID(ID, username)
        SpeakPrint(f"From now onwards I will call you {username}")
    elif "on a date" in command:
        SpeakPrint(random.choice(["I will rather deactivate then go out with you", "Nah I'm good"]))
    elif "date" in command or "time" in command or "day" in command:
        if "day" in command or "date" in command:
            date = dt.datetime.today().strftime("%A %d %B %Y")
            SpeakPrint(f"Today is {date}")
        if "time" in command:
            time = dt.datetime.today().strftime('%I:%M%p')
            SpeakPrint(f"The time is {time}")
    elif "calculate" in command:
        command = command.replace("calculate ", "")
        app_id = "EVYHEV-GP3W4RJPA5"
        client = wa.Client(app_id)
        res = client.query(command)
        ans = next(res.results).text
        SpeakPrint(ans)
    elif "ask" in command:
        SpeakPrint('I can answer to computational and geographical questions and what question do you want to ask now')
        command = ask()
        app_id = "EVYHEV-GP3W4RJPA5"
        client = wa.Client(app_id)
        res = client.query(command)
        ans = next(res.results).text
        SpeakPrint(ans)
    elif "open" in command:
        if "chrome" in command or "google" in command:
            os.system("open -a \"google chrome\"")
        elif "utorrent" in command and ".com" not in command:
            os.system("open -a utorrent")
        else:
            command = command.replace("open ", "")
            if ".com" not in command and os.path.exists(f"/Applications/{command}.app"):
                app = command.replace(" ", "\ ")
                os.system(f"open /Applications/{app}.app")
            else:
                site = command.replace(".com", "")
                site = site.replace(" ", "")
                url = f"https://www.{site}.com/"
                wb.open(url)
            SpeakPrint(f"opening {command}")
    elif "good morning" in command or "good evening" in command or "good afternoon" in command:
        greet(ID)
    elif "hello" in command or "hi" in command or "hey" in command:
        SpeakPrint(random.choice(["Hello", "Hi", "Hey", "Bonjour", "Hiya"]))
    elif "you single" in command or "you married" in command:
        SpeakPrint(random.choice(["I am single", "I'm married to the idea of helping people",
                                  "I'm Happy to say i feel whole all on my own\nPlus, I never have to share my desert",
                                  "I wanna keep that private \n\"PRIVACY\""]))
    elif "marry me" in command:
        SpeakPrint(random.choice(
            ["NO", "I will rather deactivate then marry you", "Sorry not POSSIBLE", "LOL"
                                                                                    "\N{rolling on the floor laughing} "
                                                                                    "NO"]))
    elif "how are you" in command:
        SpeakPrint(random.choice(["I am Fine", "I am doing great", "I'm happy to be here", ]))
    elif "am i hot" in command:
        SpeakPrint(random.choice(["Hot as a tin roof under the sun", "Sorry I don't have a thermometer"]))
    elif "weather" in command:
        SpeakPrint("Weather of which City?")
        city = ask()
        app_id = "a786c740192c5d9c2cab10255c49ef33"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={app_id}&units=metric"
        res = req.get(url)
        ans = res.json()
        if ans["cod"] != 404:
            temp = ans["main"]["temp"]
            humidity = ans["main"]["humidity"]
            des = ans["weather"][0]["main"]
            temph = ans["main"]["temp_max"]
            templ = ans["main"]["temp_min"]
            feel = ans["main"]["feels_like"]
            chat.insert(END, "Temp:", temp, "ªC")
            chat.insert(END, "High:", temph, "ªC Low:", templ, "ªC")
            chat.insert(END, "Feels like:", feel, "ªC")
            chat.insert(END, "Humidity:", humidity)
            chat.insert(END, "Description:", des)

        else:
            SpeakPrint("City Not Found")
    elif "make" in command and "note" in command:
        f = open(ID + "AI.txt", "w")
        cmd = "n"
        datetime = dt.datetime.today().strftime("%A %d %B %Y %I:%M%p")
        # noinspection PyUnboundLocalVariable
        while "n" in cmd or text == "" or "don't" in cmd:
            SpeakPrint("What should i Write?")
            text = ask()
            chat.insert(END, text)
            print("Should i save it")
            cmd = ask().lower()
        f.write(datetime + " " + text)
        f.close()
    elif "read" in command and "note" in command:
        try:
            f = open("Note.txt", "r")
            chat.insert(END, "Your Note:", f.read())
            f.close()
        except:
            SpeakPrint("You don't have any note")
    elif 'delete' in command and "note" in command:
        try:
            os.remove("Note.txt")
            SpeakPrint("Note Deleted")
        except:
            SpeakPrint("You don't have any note")
    elif "news" in command or "headline" in command:
        api_id = "f06509ec428d41f1b3e4824b273b1e10"
        url = f"https://newsapi.org/v2/top-headlines?language=en&apiKey={api_id}"
        res = req.get(url)
        ans = res.json()
        try:
            x = 0
            for news in ans["articles"]:
                title_news = news["title"]
                des_news = news['description']
                url_news = news['url']
                source = news["source"]["name"]
                SpeakPrint("Top Headlines for you:")
                chat.insert(END, title_news)
                chat.insert(END, des_news)
                chat.insert(END, source)
                chat.insert(END, "See more:", url_news)

        except Exception as e:
            chat.insert(END, e)
            SpeakPrint("No New News")
    elif "define" in command or ("what does" in command and "means" in command) or "meaning of" in command:
        command = command.replace("define ", "")
        command = command.replace("what does", "")
        command = command.replace("means", "")
        command = command.replace("meaning of ", "")
        defi = Dic.meaning(command, disable_errors=True)
        try:
            x = 1
            noun = defi["Noun"]
            chat.insert(END, "Noun:")
            for y in noun:
                if x == 1:
                    SpeakPrint(f"{x}.\n{y}")
                else:
                    chat.insert(END, f"{x}.\n{y}")
                x += 1
        except:
            pass
        try:
            verb = defi["Verb"]
            chat.insert(END, "Verb:")
            x = 1
            for y in verb:
                if x == 1:
                    SpeakPrint(f"{x}.\n{y}")
                else:
                    chat.insert(END, f"{x}.\n{y}")
                x += 1
        except:
            pass
        try:
            adj = defi["Adjective"]
            chat.insert(END, "Adjective:")
            x = 1
            for y in adj:
                if x == 1:
                    SpeakPrint(f"{x}.\n{y}")
                else:
                    chat.insert(END, f"{x}.\n{y}")
                x += 1
        except:
            pass
    elif "wikipedia" in command:
        command = command.replace("wikipedia ", "")
        chat.insert(END, wiki.summary(command, sentences=3))

    else:
        try:
            chat.insert(END, "On the Web:")
            for res in search(command, start=0, stop=5, pause=2):
                chat.insert(END, res)
        except:
            SpeakPrint("Sorry I can't do that")

    pass


def SpeakPrint(txt):
    chat.insert(END, f"Bot: {txt}")


def greet(ID):
    username = ID
    assname = Data[ID].user["AI data"][0]
    hour = dt.datetime.now().hour
    if 0 <= hour < 12:
        SpeakPrint("Hello,Good Morning " + username)
    elif 12 <= hour < 18:
        SpeakPrint("Hello,Good Afternoon " + username)
    else:
        SpeakPrint("Hello,Good Evening " + username)
    SpeakPrint(f"I am your Assistant {assname}")


def ask():
    r = sr.Recognizer()
    with sr.Microphone() as source:

        chat.insert(END, "Listening...")
        audio = r.listen(source)

        try:
            cmd = r.recognize_google(audio, language='en-in')
            chat.insert(END, f"user said:{cmd}\n")

        except Exception as error:
            chat.insert(END, error)
            # speakprint("Sorry, I couldn't understand that.")
            return ""

        return cmd


def SaveNote(ID, data):
    file_name = ID + ".txt"
    try:
        os.remove(file_name)
    finally:
        with open(file_name, "w") as note:
            note.write(data)


def RetrieveNote(ID):
    data = ""
    file_name = ID + ".txt"
    if os.path.exists(file_name):
        with open(file_name, "r") as note:
            data = note.read()
    return data


def BtnClick(event):
    global tool, color, points
    points = []
    if event == "line":
        tool = 1
    elif event == "connect line":
        tool = 2
    elif event == "square":
        tool = 3
    elif event == "cut line":
        tool = 4
    elif event == "spray":
        tool = 5
    else:
        color = event


def click(event):
    global tool, color, points
    if tool == 1 or tool == 3:
        points.append(event.x)
        points.append(event.y)
    elif tool == 2:
        points.append(event.x)
        points.append(event.y)
        if len(points) >= 4:
            sketchpad.create_line(points, fill=color)


def drag(event):
    global tool, color, points

    if tool == 4:
        points.append(event.x)
        points.append(event.y)
    if len(points) >= 4:
        sketchpad.create_line(points, fill=color)
    if tool == 5:
        for r in range(50):
            rpixelx = randint(event.x - 20, event.x + 20)
            rpixely = randint(event.y - 20, event.y + 20)
            if (rpixelx - event.x) ** 2 + (rpixely - event.y) ** 2 <= 20 ** 2:
                sketchpad.create_line(rpixelx, rpixely, rpixelx + 1, rpixely + 1, fill=color)


def release(event):
    global tool, color, points

    if tool == 1:
        points.append(event.x)
        points.append(event.y)
        sketchpad.create_line(points, fill=color)
        points = []
    elif tool == 3:
        points.append(event.x)
        points.append(event.y)
        sketchpad.create_rectangle(points, fill=color)
        points = []
    elif tool == 4 or tool == 5:
        points = []


def delete(event):
    sketchpad.delete("all")


def ChangeColor():
    cusColor = colorchooser.askcolor(title="Custom Color")
    cosColor.set(str(cusColor[1]))
    style.map("Custom.TButton",
              background=[('pressed', '!disabled', cusColor[1]), ('active', cusColor[1]), ("!disabled", cusColor[1])])
    customColorBtn.config(style="Custom.TButton")
    BtnClick(cosColor.get())


def Upload():
    file: tuple = filedialog.askopenfilenames(title="Select File")
    files = {}
    for x in range(0, len(file)):
        files.setdefault(f"files[{x}]", open(file[x], 'rb'))

    response = req.post('https://tmp.ninja/upload.php', files=files).json()
    for x in range(0, len(file)):
        List.insert(END, x & ". File: " + response["files"][x]["name"])
        List.insert(END, "Link: " + response["files"][x]["url"])
        List.insert(END, "")

    scrolly.config(command=List.yview)


def Login(ID, Pass):
    try:
        found = Data[ID].findUser(ID, Pass)
        if not found:
            messagebox.showerror("Not Found", "Incorrect ID or PassWord")
            return
    except:
        messagebox.showerror("Not Found", "Incorrect ID or PassWord")
        return

    SUPFrame.destroy()
    SINFrame.destroy()

    root.title(found["username"])

    root.geometry("1050x576")
    root.config(bg="#6B7C7F", padx=11, pady=28)

    # LOG INFO FRAME
    logcard = ttk.Frame(root, height=150, width=432, padding=(5, 5))
    logcard.grid(row=0, column=0, sticky="n", padx=12)
    logcard.grid_propagate(False)
    # Pic = Imag()
    PPic = Label(logcard, image=Pic)
    PPic.grid(row=0, column=0, rowspan=5, padx=5)
    Uname = ttk.Label(logcard, text=found["username"], font=("Kungfont", 23))
    Uname.grid(row=0, column=1, columnspan=2, sticky="w")
    ttk.Label(logcard, text="Name: ", font=("Bold Baskerville", 20)).grid(row=1, column=1, sticky="w")
    ttk.Label(logcard, text="PassWord: ", font=("Bold Baskerville", 20)).grid(row=2, column=1, sticky="w")
    ttk.Label(logcard, text="Gender: ", font=("Bold Baskerville", 20)).grid(row=3, column=1, sticky="w")
    ttk.Label(logcard, text="Date Of Birth: ", font=("Bold Baskerville", 20)).grid(row=4, column=1, sticky="w")
    name = ttk.Label(logcard, text="{} {}".format(found["First Name"], found["Last Name"]), font=("Baskerville", 20))
    name.grid(row=1, column=2, sticky=W)
    pwd = ttk.Label(logcard, text="********", font=("Baskerville", 20))
    pwd.grid(row=2, column=2, sticky=W)
    Gen = ttk.Label(logcard, text=found["Gender"], font=("Baskerville", 20))
    Gen.grid(row=3, column=2, sticky=W)
    DOB = ttk.Label(logcard, text=found["Date of Birth"], font=("Baskerville", 20))
    DOB.grid(row=4, column=2, sticky=W)
    UserNameedit = Button(logcard, image=editB, command=lambda: UserNameChange(found["username"]), background="#D4D6D5")
    UserNameedit.grid(row=0, column=2)
    nameedit = Button(logcard, image=editB, command=lambda: (NameChange(found["username"])), background="#D4D6D5")
    nameedit.grid(row=1, column=3, sticky="e")
    pwdedit = Button(logcard, image=editB, command=lambda: PassWordChange(found["username"]), background="#D4D6D5")
    pwdedit.grid(row=2, column=3, sticky="e")
    Genedit = Button(logcard, image=editB, command=lambda: GenChange(found["username"]), background="#D4D6D5")
    Genedit.grid(row=3, column=3, sticky=E)
    DOBedit = Button(logcard, image=editB, command=lambda: DOBChange(found["username"]), background="#D4D6D5")
    DOBedit.grid(row=4, column=3, sticky=E)

    # WEATHER CARD
    weaCard.grid(row=0, column=1, padx=12, sticky=N)

    # ASSISTANT FRAME

    assFrame.grid(row=0, column=2, rowspan=2, padx=12, sticky=N)
    actBtn = ttk.Button(assFrame, image=actimg, command=lambda : CallAssitant(ID))
    actBtn.pack(side=BOTTOM, anchor=CENTER)
    greet(ID)

    # ACTIVITY FRAME
    accNote.grid(row=1, column=0, columnspan=2, pady=20, padx=11, sticky=W)
    accNote.grid_propagate(False)
    # notebook
    note = Text(noteFrame, relief="sunken", height=16, width=100, borderwidth=3, insertwidth=4)
    note.insert(END, RetrieveNote(found["username"]))
    note.grid(row=0, column=0, pady=5, padx=5)
    ttk.Button(noteFrame, text="Save", command=lambda: SaveNote(found["username"], note.get(1.0, "end-1c"))).grid(row=1,
                                                                                                                  column=0)
    # sketchpad
    sketchpad.pack(padx=10, pady=10, anchor="center", expand=True, fill="both")
    # file transfer FT

    root.protocol("WM_DELETE_WINDOW", Exit())


def CAA():
    logid.set("")
    pasw.set("")

    CAAWin = Toplevel(root)
    CAAWin.geometry("600x750")
    CAAWin.config(bg="#6B7C7F", padx=40, pady=64)
    CAAWin.title("Create An Account")
    CAAstyle = ttk.Style()
    CAAstyle.theme_use("default")
    Fname = StringVar()
    Lname = StringVar()
    cpass = StringVar()
    CAAstyle.map("Title.Label",
                 font=[("!disabled", ("Optima", 21))],
                 foreground=[("!disabled", "black")],
                 background=[("!disabled", "transparent")]
                 )

    CAAstyle.map("Sub.Label",
                 font=[("!disabled", ("Optima", 12))],
                 foreground=[("!disabled", "#CFD5DF")],
                 background=[("!disabled", "transparent")]
                 )
    CAAstyle.map("Cre.TButton",
                 background=[("disabled", "grey"), ("!disabled", "#CFD5DF")],
                 foreground=[("disabled", "white"), ("!disabled", "black")],
                 font=[("disabled", ("optima", 21)), ("!disabled", ("optima", 21))],
                 height=[("disabled", 32), ("!disabled", 32)],
                 # width=[("disabled", "149px"), ("!disabled", "149px")]
                 )
    CAAstyle.map("TCheckbutton",
                 background=[("!disabled", "#6B7C7F")],
                 font=[("!disabled", ("Baskerville", 18))],
                 foreground=[("!disabled", "#CFD5DF")],
                 indicatorbackground=[("!disabled", "#6B7C7F")]
                 )
    CAAstyle.map("TRadiobutton",
                 background=[("!disabled", "#6B7C7F")],
                 font=[("!disabled", ("Baskerville", 18))],
                 foreground=[("!disabled", "#CFD5DF")],
                 indicatorbackground=[("!disabled", "#6B7C7F")],
                 )
    CAAstyle.map("Back.TButton",
                 font=[("disabled", ("optima", 21)), ("!disabled", ("optima", 21))],
                 foreground=[("disabled", "white"), ("!disabled", "black")],
                 background=[("disabled", "grey"), ("!disabled", "#858EA4")]
                 )

    NameLabel = ttk.Label(CAAWin, text="Full Name", style="Title.Label")
    NameLabel.grid(row=1, column=1, sticky="w")

    FnameFeild = ttk.Entry(CAAWin, width=16, textvariable=Fname)
    FnameFeild.grid(row=2, column=1, sticky="w")
    FnameLabel = ttk.Label(CAAWin, text="First Name", style="Sub.Label")
    FnameLabel.grid(row=3, column=1, sticky="w")
    LnameFeild = ttk.Entry(CAAWin, width=16, textvariable=Lname)
    LnameFeild.grid(row=2, column=2, padx=10, sticky="w")
    LnameLabel = ttk.Label(CAAWin, text="Surname", style="Sub.Label")
    LnameLabel.grid(row=3, column=2, sticky="w", padx=10)

    ttk.Label(CAAWin, style="Title.Label").grid(row=4, column=1, pady=14)

    UnameLabel = ttk.Label(CAAWin, text="UserName", style="Title.Label")
    UnameLabel.grid(row=5, column=1, sticky="w")
    UnameFeild = ttk.Entry(CAAWin, width=16, textvariable=logid)
    UnameFeild.grid(row=6, column=1, sticky="w")

    ttk.Label(CAAWin, style="Title.Label").grid(row=7, column=1, pady=12)

    PassLabel = ttk.Label(CAAWin, text="PassWord", style="Title.Label")
    PassLabel.grid(row=8, column=1, sticky="w")
    PassFeild = ttk.Entry(CAAWin, width=18, textvariable=pasw)
    PassFeild.grid(row=9, column=1, sticky="w")

    CPassLabel = ttk.Label(CAAWin, text="Confirm PassWord", style="Title.Label")
    CPassLabel.grid(row=8, column=2, sticky="w", padx=10)
    CPassFeild = ttk.Entry(CAAWin, width=18, textvariable=cpass)
    CPassFeild.grid(row=9, column=2, padx=10, sticky="w")

    ttk.Label(CAAWin, style="Title.Label").grid(row=10, column=1, pady=12)

    DOBLabel = ttk.Label(CAAWin, text="Date of Birth", style="Title.Label")
    DOBLabel.grid(row=11, column=1, sticky="w")
    year = StringVar()
    year.set(str(dt.date.today().year))
    date = StringVar()
    date.set(str(dt.date.today().day))
    month = StringVar()
    month.set(str(dt.date.today().month))
    seldate = Spinbox(CAAWin, from_=1, to=31, textvariable=date, width=4)
    seldate.grid(row=12, column=1, sticky="w")
    ttk.Label(CAAWin, text="Day", style="Sub.Label").grid(row=13, column=1, sticky="w")
    selmonth = Spinbox(CAAWin, from_=1, to=12, textvariable=month, width=3)
    selmonth.grid(row=12, column=1, sticky="w", padx=70)
    ttk.Label(CAAWin, text="Month", style="Sub.Label").grid(row=13, column=1, sticky="w", padx=70)
    selyear = Spinbox(CAAWin, from_=1900, to=dt.date.today().year, textvariable=year, width=6)
    selyear.grid(row=12, column=1, sticky="w", padx=125, columnspan=2)
    ttk.Label(CAAWin, text="Year", style="Sub.Label").grid(row=13, column=1, sticky="w", padx=125, columnspan=2)

    ttk.Label(CAAWin, style="Title.Label").grid(row=14, column=1, pady=12)

    Gender = StringVar()
    GenLabel = ttk.Label(CAAWin, text="Gender", style="Title.Label")
    GenLabel.grid(row=15, column=1, sticky="w")
    ttk.Radiobutton(CAAWin, text="Male", variable=Gender, value="M").grid(row=16, column=1, sticky="w")
    ttk.Radiobutton(CAAWin, text="Female", variable=Gender, value="F").grid(row=16, column=1, columnspan=2, padx=70,
                                                                            sticky="w")

    ttk.Label(CAAWin, style="Title.Label").grid(row=17, column=1, pady=12)

    NAR = BooleanVar()
    ttk.Checkbutton(CAAWin, text="I am not a Robot", variable=NAR, onvalue=True, offvalue=False).grid(row=18, column=1,
                                                                                                      sticky="w")

    ttk.Label(CAAWin, style="Title.Label").grid(row=19, column=1, pady=12)

    # First Name, Last Name, UserName, PassWord, Confirm PassWord, DOB(date, month, year), Gender, NAR
    CreButton = ttk.Button(CAAWin, text="Create", style="Cre.TButton", width=10,
                           command=lambda: (SignUp(Fname.get(), Lname.get(), logid.get(), pasw.get(), cpass.get(),
                                                   dt.date(int(year.get()), int(month.get()), int(date.get())), Gender,
                                                   NAR.get()), Exit(), CAAWin.destroy(), root.state("normal")))
    CreButton.grid(row=20, column=3, sticky="e")
    back = ttk.Button(CAAWin, text="Back", width=6, style="Back.TButton",
                      command=lambda: (Exit(), CAAWin.destroy(), root.state("normal")))
    back.grid(row=20, column=2, sticky="e", padx=10)
    CAAWin.grab_set()
    CAAWin.wait_visibility()


if __name__ == '__main__':
    root = Tk()
    root.geometry("640x480")
    root.title("Warner Bros.")
    style = ttk.Style()
    style.theme_use("default")


    def Imag():
        if not os.path.exists("Username.png"):
            with open('Asset 3.png', 'r+b') as f:
                with Image.open(f) as IMAGE:
                    cover = resizeimage.resize_cover(IMAGE, [105, 132])
                    cover.save('Username.png', IMAGE.format)
        return 'Username.png'


    Pic = ImageTk.PhotoImage(Image.open(Imag()))
    editB = ImageTk.PhotoImage(Image.open("Asset 2.png"))

    style.map("TButton",
              foreground=[('pressed', 'white'), ('active', 'white'), ("!disabled", "white")],
              background=[('pressed', '!disabled', '#598080'), ('active', '#84B2B2'), ("!disabled", "#598080")],
              font=[("!disabled", ("PT Sans Caption", 18))]

              )
    style.map("CAA.TButton",
              font=[("!disabled", ("Noteworthy", 20))]
              )
    style.map("FP.TButton",
              font=[("!disabled", ("PT Sans Caption", 2))]
              )

    logid = StringVar()
    logid.set("")
    pasw = StringVar()
    pasw.set("")
    SINFrame = ttk.Frame(root, height=341, width=237, relief="groove", borderwidth="5", padding=(8, 8))
    SINFrame.grid(column=0, row=1, padx=35)
    SINFrame.grid_propagate(False)

    SINLabel = ttk.Label(SINFrame, text="Sign In", font=("PT Serif", 24), padding=(0, 5))
    SINLabel.grid(column=0, row=0, columnspan=3)

    LOGLabel = ttk.Label(SINFrame, text="Login ID:", font=("PT Sans Caption", 14), padding=(0, 30, 0, 0), anchor="s")
    LOGLabel.grid(column=0, row=1, columnspan=2, sticky="w")
    LOGFeild = ttk.Entry(SINFrame, width=18, textvariable=logid)
    LOGFeild.grid(row=2, column=0, padx=25, columnspan=3)

    PASLabel = ttk.Label(SINFrame, text="PassWord:", font=("PT Sans Caption", 14))
    PASLabel.grid(column=0, row=3, columnspan=2, sticky="w")
    PASField = ttk.Entry(SINFrame, width=18, textvariable=pasw, show="X")
    PASField.grid(column=0, row=4, padx=25, columnspan=3)

    FPBUT = ttk.Button(SINFrame, width=2, text="", style="FP.TButton")
    FPBUT.grid(row=5, column=0, sticky="e", pady=10)
    FPLabel = ttk.Label(SINFrame, text="Forgot Password")
    FPLabel.grid(row=5, column=1, sticky="w", columnspan=2)

    LOGBUT = ttk.Button(SINFrame, text="Login", style="TButton",
                        command=lambda: Login(logid.get(), pasw.get()))
    LOGBUT.grid(row=6, column=2, pady=10)

    SUPFrame = ttk.Frame(root, height=341, width=237, relief="groove", borderwidth="5", padding=(8, 8))
    SUPFrame.grid(column=1, row=1, padx=35)
    SUPFrame.grid_propagate(False)

    SUPLabel = ttk.Label(SUPFrame, justify="center", text="Sign Up", font=("PT Serif", 24), padding=(0, 5))
    SUPLabel.grid(column=1, row=0, columnspan=1, padx=20)

    CAAButton = ttk.Button(SUPFrame, text="Create an Account", style="CAA.TButton", command=CAA)
    CAAButton.grid(row=1, column=0, columnspan=3, padx=25, pady=80)

    root.protocol("WM_DELETE_WINDOW", Exit())

    # WEATHER CARD
    weaCard = ttk.Labelframe(root, text="Weather", labelanchor="nw", height=150, width=275, padding=5)
    weaCard.grid_propagate(False)
    weather, location = WeatherLocation()
    image = urlopen("http://openweathermap.org/img/wn/{}@2x.png".format(weather["weather"][0]["icon"])).read()
    img = ImageTk.PhotoImage(Image.open(io.BytesIO(image)))
    weaIcon = ttk.Label(weaCard, image=img)
    weaIcon.grid(column=0, row=0, rowspan=2)
    weaDisc = ttk.Label(weaCard, text=weather["weather"][0]["main"], font=("Georgia", 18))
    weaDisc.grid(row=2, column=0)
    weaTemp = ttk.Label(weaCard, text=weather["main"]["temp"], font=("Digital-7", 60))
    weaTemp.grid(row=0, column=1, sticky="s")
    ttk.Label(weaCard, text="°C", font=("Marker Felt", 20)).grid(row=0, column=2)
    weaCity = ttk.Label(weaCard, text=location["city"] + ", " + location['countryCode'], font=("Marker Felt", 18))
    weaCity.grid(row=2, column=1, columnspan=2, rowspan=2)
    ttk.Button(weaCard, text="⬆", command=UpdateWeather, width=2).grid(row=0, column=4, padx=5)

    # ASSISTANT FRAME
    style.map("Assistant.TButton",
              background=[("disabled", "#81B2E2"), ("!disabled", "#81B2E2")]
              )
    assFrame = ttk.Labelframe(root, text="Assistant", labelanchor="nw", height=511, width=255)
    assFrame.pack_propagate(False)
    chatFrame = ttk.Frame(assFrame, height=450, width=250)
    chatFrame.pack(fill=BOTH, side=TOP)

    scroll = ttk.Scrollbar(chatFrame)
    scroll.pack(side=RIGHT, fill=Y)
    chat = Listbox(chatFrame, relief="sunken", yscrollcommand=scroll.set,width=40,height=20)
    chat.pack(side=LEFT)
    scroll.config(command=chat.yview())
    actimg = ImageTk.PhotoImage(Image.open("Asset 4.png"))

    # ACTIVITY FRAME
    accNote = ttk.Notebook(root, height=317, width=727)
    # Notepad
    noteFrame = ttk.Frame(accNote)
    accNote.add(noteFrame, text="NoteBook")
    # Sketchpad
    tool = 1
    color = "black"
    points = []
    sketchFrame = ttk.Frame(accNote)
    accNote.add(sketchFrame, text="SketchPad")
    sketchpad = Canvas(sketchFrame, relief="sunken", borderwidth=5)
    cosColor = StringVar()
    cosColor.set("green")
    style.map("Black.TButton",
              background=[('pressed', '!disabled', 'black'), ('active', 'black'), ("!disabled", "black")])
    style.map("Blue.TButton",
              background=[('pressed', '!disabled', 'blue'), ('active', 'blue'), ("!disabled", "blue")])
    style.map("Red.TButton",
              background=[('pressed', '!disabled', 'red'), ('active', 'red'), ("!disabled", "red")])
    style.map("Custom.TButton",
              background=[('pressed', '!disabled', cosColor.get()), ('active', cosColor.get()),
                          ("!disabled", cosColor.get())])

    selPalette = Frame(sketchFrame)
    selPalette.pack(side="bottom")
    ttk.Button(selPalette, command=lambda: BtnClick("black"), style="Black.TButton", width=2).grid(row=0, column=0)
    ttk.Button(selPalette, command=lambda: BtnClick("blue"), style="Blue.TButton", width=2).grid(row=0, column=1)
    ttk.Button(selPalette, command=lambda: BtnClick("red"), style="Red.TButton", width=2).grid(row=0, column=2)
    customColorBtn = ttk.Button(selPalette, command=lambda: BtnClick(cosColor.get()), style="Custom.TButton", width=2)
    customColorBtn.grid(row=0, column=3)
    ttk.Button(selPalette, text="Custom", command=ChangeColor).grid(row=0, column=4)
    ttk.Button(selPalette, text="𑁋", command=lambda: BtnClick("line"), width=3).grid(row=0, column=5)
    ttk.Button(selPalette, text="◻️", command=lambda: BtnClick("square"), width=2).grid(row=0, column=6)
    ttk.Button(selPalette, text="＿|", command=lambda: BtnClick("connect line"), width=2).grid(row=0, column=7)
    ttk.Button(selPalette, text="٭", command=lambda: BtnClick("cut line"), width=2).grid(row=0, column=8)
    ttk.Button(selPalette, text="spray", command=lambda: BtnClick("spray"), width=6).grid(row=0, column=9)
    delete(0)
    root.bind("c", delete)
    sketchpad.bind("<Button-1>", click)
    sketchpad.bind("<B1-Motion>", drag)
    sketchpad.bind("<ButtonRelease-1>", release)
    # File Transfer Tmp.ninja
    ftFrame = ttk.Frame(accNote)
    accNote.add(ftFrame, text="File Transfer")
    detailFrame = ttk.Frame(ftFrame)
    detailFrame.pack(side=TOP, fill=BOTH)
    scrolly = ttk.Scrollbar(detailFrame, orient="vertical")
    scrolly.pack(side="right", fill="y")
    List = Listbox(detailFrame, yscrollcommand=scrolly.set, height=15, width=79)
    List.pack(side="left", fill=BOTH)
    uploadBtn = ttk.Button(ftFrame, text="Upload", command=Upload)
    uploadBtn.pack(side=BOTTOM, anchor="center")
    scrolly.config(command=List.yview)

    root.mainloop()
