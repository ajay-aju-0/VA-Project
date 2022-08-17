import datetime
import wikipedia 
import webbrowser 
import os 
import random
import requests
import sys 
import time
import threading 
import playsound
from tkinter import *
from tkinter import scrolledtext
from PIL import ImageTk,Image
from functools import partial
import wolframalpha
import getpass
import pywhatkit 
import pyautogui
import pyjokes
import Annex
from config.config import *

'''
* add games like pong,snake,and blocks game
* if possible add image to sketch also.....
'''

try:
    app = wolframalpha.Client(wolframalpha_id) # API key for wolframalpha
except Exception as e:
    pass


#==================== Memory for Greetings ====================================

morning = ['Good Morning!!!','Isn\'t it a beautiful day today?','May this day bring new opportunities and successes for you. Good morning!',
            'This is not just another day. It is yet another chance to make your dreams come true. Get up and get started. Good morning!',
            'Wishing you a day full of sunny smiles and happy thoughts. Good morning!','Enjoy life now! Good morning!!!',
            'Good morning. Wake up and be awesome!','Just the thought of you brightens up my morning. Good morning!',
            'Morning comes whether you set the alarm or not. Wake up, sleepyhead!','As the day begins, remember that I am your friend…you’re welcome!'
        ]

afternoon = ['Good Afternoon!','Thinking of you today — have a good afternoon!','A wish for a wonderful afternoon for you and yours!',
             'Here\'s a wish for a fun afternoon and the gentle breeze that comes with it.','Half of the day is over; have a marvelous afternoon and enjoy the rest of the day!',
             'Remember, every day I am wishing you the best morning, afternoon, and night!','Today, there will be a beautiful sunset after you have a good afternoon!',
             'Wishing you a happy day and a fabulous afternoon!','May this afternoon bring you delightful surprises.',
             'The afternoon is when the day starts to slow down. Enjoy yourself!'
        ]

evening = ['Good Evening!!','Lots of love for this sweet evening.','Zestful energetic evening',
           'Zestful exciting evening!','Hey delightful evening.','Mesmerizing evening for you.',
           'This evening is as adorable as you.'
        ]

night = ['It is a night time.','Night time code time!!','This night is dark as your IDE\'s theme.',
         'Hey, Owl how is your work going?','Night men are smart men.','Nothing like a nighttime stroll to give you ideas..',
         'I like the night. Without the dark, we\'d never see the stars.Night is to see dreams and day is to make them true.',
         'The darkest night produce the brightest stars.','The nighttime of the body is the daytime of the soul.',
         'Night is beautiful when you are happy, calming when you are stressed and lonesome when you are missing someone.',
         'Night time is the time when our thinking and feeling gains it peakness!'
        ]

#============================================================================


#==================== Memory for 'how are you' query ==========================

howareyou= ['Good to hear from you! How may I help','I\'m fine, thank you. What can I do for you?',
            'Very Good, How may I help you','Wonderful thanks, What can I do for you?',
            'I\'m well, thank you, how can I help','So glad to hear your voice, How can I help you?',
            'I\'m doing great, thanks for asking. Anything I can help with'
        ]

#============================================================================


#================ EMAIL dictionary for sending emails =======================

EMAIL_DIC = {
    'myself': 'ajaypadmanabhan01@gmail.com',
    'my official email': 'ajaypadmanabhan01@gmail.com',
}

#============================================================================


#setting chrome path
chrome_path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"


#setting variables for background and text colours
background = ""
foreground = ""


def there_exists(terms,query):
    '''Checking whether saved commands exists in given query or not'''
    for term in terms:
        if term in query:
                return True


def commandsList():
    '''show the command to which voice assistant is registered with'''
    os.startfile('Commands List.txt')


def clearScreen():
    '''clearing the scrollable textbox'''
    SR.scrollable_text_clearing()


#Greeting the user at the start
def greet():
    ''' greeting according to time '''
    hour=int(datetime.datetime.now().hour)
    if hour>=4 and hour<12:
        greet = random.choice(morning)
        SR.speak(greet)
    elif hour>=12 and hour<18:
        greet = random.choice(afternoon)
        SR.speak(greet)
    elif hour>=18 and hour<20:
        greet = random.choice(evening)
        SR.speak(greet)
    else:
        greet = random.choice(night)
        SR.speak(greet)

    SR.speak("\nMyself Hazel. How may I help you?")


def mainframe():
    """Logic for executing task based on query"""
    SR.scrollable_text_clearing()
    greet()
    try:
        while(True):
            query = SR.takeCommand().lower()  #converted the command in lower case for ease of matching
    

            # Asking for name
            if there_exists(["what is your name","what's your name","tell me your name",'who are you'],query):
                SR.speak("My name is Hazel and I'm here to serve you.")  


            # How are you
            elif there_exists(['how are you'],query):
                reply = random.choice(howareyou)
                SR.updating_ST_No_newline(reply+'😃\n')
                SR.nonPrintSpeak(reply)


            # what is my name
            elif there_exists(['what is my name','tell me my name',"i don't remember my name"],query):
                SR.speak("Your name is "+str(getpass.getuser()))


            # time and date
            elif there_exists(['the time'],query):
                strTime =datetime.datetime.now().strftime("%H:%M:%S")
                SR.speak(f"Sir, the time is {strTime}")
            elif there_exists(['the date'],query):  
                strDay=datetime.date.today().strftime("%B %d, %Y")
                SR.speak(f"Today is {strDay}")
            elif there_exists(['what day it is','what day is today','which day is today',"today's day name please"],query):
                SR.speak(f"Today is {datetime.datetime.now().strftime('%A')}")


            # display calendar
            elif there_exists(['show me calendar','display calendar'],query):
                todays_date = datetime.date.today()
                # SR.updating_ST(calendar.calendar(todays_date.year))
                obj = Annex.Calender(todays_date)
                obj.showCalender()
                break


            # opening software applications
            elif there_exists(['open code','open visual studio code','open vs code','open vscode'],query):
                SR.nonPrintSpeak('opening visual studio code')
                codepath = "C:\\Users\\ajayaju\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codepath)
                break

            elif there_exists(['open wordpad'],query):
                SR.nonPrintSpeak('opening wordpad')
                codepath = "C:\\Windows\\WinSxS\\amd64_microsoft-windows-wordpad_31bf3856ad364e35_10.0.22000.1_none_83fe16d971ae9831\\wordpad.exe"
                os.startfile(codepath)
                break

            elif there_exists(['open microsoft word','open word'],query):
                SR.nonPrintSpeak('opening microsoft word')
                codepath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
                os.startfile(codepath)
                break

            elif there_exists(['open powerpoint','open presentation','open powerpoint presentation','powerpoint presentation'],query):
                SR.nonPrintSpeak('opening microsoft powerpoint presentation')
                codepath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
                os.startfile(codepath)
                break

            elif there_exists(['open notepad','start notepad'],query):
                SR.nonPrintSpeak('opening notepad')
                codepath = "C:\\Windows\\notepad.exe"
                os.startfile(codepath)
                break

            elif there_exists(['open file manager','file manager','open my computer','my computer','open file explorer','file explorer','open this pc','this pc'],query):
                SR.speak("Opening File Explorer")
                os.startfile("C:\Windows\explorer.exe")
                break

            elif there_exists(['powershell'],query):
                SR.speak("Opening powershell")
                os.startfile(r'C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe')
                break

            elif there_exists(['cmd','command prompt','command prom','commandpromt',],query):
                SR.speak("Opening command prompt")
                os.startfile(r'C:\\Windows\\System32\\cmd.exe')
                break

            elif there_exists(['show me performance of my system','open performance monitor','performance monitor','performance of my computer','performance of this computer'],query):
                SR.speak("Opening performance monitor")
                os.startfile("C:\\Windows\\System32\\perfmon.exe")
                break

            elif there_exists(['open settings','open control panel','open this computer setting Window','open computer setting Window'   ,'open computer settings','open setting','show me settings','open my computer settings'],query):
                SR.speak("Opening settings...")
                os.startfile('C:\\Windows\\System32\\control.exe')
                break

            elif there_exists(['open your setting','open your settings','open settiing window','show me setting window','open voice assistant settings'],query):
                SR.speak("Opening my Setting window..")
                sett_wind=Annex.SettingWindow()
                sett_wind.settingWindow(root)
                break

            elif there_exists(['open vlc','vlc media player','vlc player'],query):
                SR.speak("Opening VLC media player")
                os.startfile(r"C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe")
                break
            
            # switching the windows
            elif there_exists(['switch the window','switch window'],query):
                SR.speak("Okay sir, Switching the window")
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")


            # system stats
            elif there_exists(['system','system stats','my system stats'],query):
                info = Annex.SystemInfo()
                sys_info = info.system_stats()
                # print(sys_info)
                SR.speak(sys_info)
                break


            # system's current ip address
            elif there_exists(['ip address','ip'],query):
                ip = requests.get('https://api.ipify.org').text
                # print(ip)
                SR.speak(f"Your ip address is {ip}")
                break
            

            # bluetooth file sharing
            elif there_exists(['send some files through bluetooth','send file through bluetooth','bluetooth sharing','bluetooth file sharing','open bluetooth'],query):
                SR.speak("Opening bluetooth...")
                os.startfile(r"C:\\Windows\\System32\\fsquirt.exe")
                SR.speak("bluetooth is enabled now you can send files through it")
                SR.speak("opening file explorer for browsing files")
                os.startfile("C:\Windows\explorer.exe")
                break


            # sending email's
            elif there_exists(['email','send mail'],query):
                sender_email = email
                sender_password = email_password

                try:
                    SR.speak("Whom do you want to email sir ?")
                    recipient = SR.takeCommand().lower()
                    receiver_email = EMAIL_DIC.get(recipient)

                    if receiver_email:
                        SR.speak("What is the subject sir ?")
                        subject = SR.takeCommand()
                        SR.speak("What should I say?")
                        message = SR.takeCommand()
                        msg = 'Subject: {}\n\n{}'.format(subject, message)
                        obj = Annex.MailSend(sender_email,sender_password,receiver_email,msg)
                        if obj.mail():
                            SR.speak("Email has been successfully sent")
                        else:
                            SR.speak("there was an error while sending the mail.")
                            SR.speak("please check your email settings and resolve it")
                    else:
                        SR.speak("I coudn't find the requested person's email in my database. Please try again with a different name")
                except:
                    SR.speak("Sorry sir. Couldn't send your mail. Please try again")
                break

            
            # wikipedia search
            elif there_exists(['search wikipedia for','from wikipedia'],query):
                SR.speak("Searching wikipedia...")
                if 'search wikipedia for' in query:
                    query=query.replace('search wikipedia for','')
                    results=wikipedia.summary(query,sentences=2)
                    SR.speak("According to wikipedia:\n")
                    SR.speak(results)
                    break
                elif 'from wikipedia' in query:
                    query=query.replace('from wikipedia','')
                    results=wikipedia.summary(query,sentences=2)
                    SR.speak("According to wikipedia:\n")
                    SR.speak(results)
                    break
            elif there_exists(['wikipedia'],query):
                SR.speak("Searching wikipedia....")
                query=query.replace("wikipedia","")
                results=wikipedia.summary(query,sentences=2)
                SR.speak("According to wikipedia:\n")
                SR.speak(results)
                break


            # who is searcing mode
            elif there_exists(['who is','who the heck is','who the hell is','who is this'],query):
                query=query.replace("wikipedia","")
                results=wikipedia.summary(query,sentences=1)
                SR.speak("According to wikipdedia:  ")
                SR.speak(results)
                break
                

            # what is meant by
            elif there_exists(['what is meant by','what is mean by','what is'],query):
                results=wikipedia.summary(query,sentences=2)
                SR.speak("According to wikipedia:\n")
                SR.speak(results)
                break

            
            # it will give online results for the query
            elif there_exists(['search something for me','to do a little search','search mode','i want to search something'],query):
                SR.speak('What you want me to search for?')
                query=SR.takeCommand()
                SR.speak(f"Showing results for {query}")
                try:
                    res=app.query(query)
                    SR.speak(next(res.results).text)
                except:
                    print("Sorry, but there is a little problem while fetching the result.")
                break

            elif there_exists(['calculate'],query):
                try:
                    res=app.query(query)
                    SR.speak(next(res.results).text)
                except:
                    print("Sorry, but there is a little problem while fetching the result.")
                break

            # what is the capital
            elif there_exists(['what is the capital of','capital of','capital city of'],query):
                try:
                    res=app.query(query)
                    SR.speak(next(res.results).text)
                except:
                    print("Sorry, but there is a little problem while fetching the result.")
                break


            # google, youtube and location
            # playing on youtube 
            elif there_exists(['open youtube and play','on youtube'],query):
                if 'on youtube' in query:
                    SR.speak("Opening youtube")
                    pywhatkit.playonyt(query.replace('on youtube',''))
                else:
                    SR.speak("Opening youtube")
                    pywhatkit.playonyt(query.replace('open youtube and play ',''))
                break
            elif there_exists(['play some songs on youtube','i would like to listen some music','i would like to listen some songs','play songs on youtube'],query):
                SR.speak("Opening youtube")
                pywhatkit.playonyt('play random songs')
                break
            elif there_exists(['open youtube','access youtube'],query):
                SR.speak("Opening youtube")
                webbrowser.get(chrome_path).open("https://www.youtube.com")
                break

            # opening google and search
            elif there_exists(['open google and search','google and search'],query):
                url='https://google.com/search?q='+query[query.find('for')+4:]
                webbrowser.get(chrome_path).open(url)
                break
            elif there_exists(['open google'],query):
                SR.speak("Opening google")
                webbrowser.get(chrome_path).open("https://www.google.com")
                break

            # finding location
            elif there_exists(['find location of','show location of','find location for','show location for'],query):
                if 'of' in query:
                    url='https://google.nl/maps/place/'+query[query.find('of')+3:]+'/&amp'
                    webbrowser.get(chrome_path).open(url)
                    break
                elif 'for' in query:
                    url='https://google.nl/maps/place/'+query[query.find('for')+4:]+'/&amp'
                    webbrowser.get(chrome_path).open(url)
                    break
            elif there_exists(["what is my exact location","What is my location","my current location","exact current location"],query):
                url = "https://www.google.com/maps/search/Where+am+I+?/"
                webbrowser.get().open(url)
                SR.speak("Showing your current location on google maps...")
                break
            elif there_exists(["where am i"],query):
                Ip_info = requests.get('https://api.ipdata.co?api-key=test').json()
                loc = Ip_info['region']
                SR.speak(f"You must be somewhere in {loc}")

            # image search
            elif there_exists(['show me images of','images of','display images'],query):
                url="https://www.google.com/search?tbm=isch&q="+query[query.find('of')+3:]
                webbrowser.get(chrome_path).open(url)
                break
            elif there_exists(['search for','do a little searching for','show me results for','show me result for','start searching for'],query):
                SR.speak("Searching.....")
                if 'search for' in query:
                    SR.speak(f"Showing results for {query.replace('search for','')}")
                    pywhatkit.search(query.replace('search for',''))
                elif 'do a little searching for' in query:
                    SR.speak(f"Showing results for {query.replace('do a little searching for','')}")
                    pywhatkit.search(query.replace('do a little searching for',''))
                elif 'show me results for' in query:
                    SR.speak(f"Showing results for {query.replace('show me results for','')}")
                    pywhatkit(query.replace('show me results for',''))
                elif 'start searching for' in query:
                    SR.speak(f"Showing results for {query.replace('start searching for','')}")
                    pywhatkit(query.replace('start searching for',''))
                break


            # top 5 news
            elif there_exists(['top 5 news','top five news','listen some news','news of today'],query):
                news=Annex.News(scrollable_text)
                news.show()
                break


            # jokes
            elif there_exists(['tell me joke','tell me a joke','tell me some jokes','i would like to hear some jokes',"i'd like to hear some jokes",
                            'can you please tell me some jokes','i want to hear a joke','i want to hear some jokes','please tell me some jokes',
                            'would like to hear some jokes','tell me more jokes'],query):
                SR.speak(pyjokes.get_joke(language="en", category="all"))
                query_for_future=query
            elif there_exists(['one more','one more please','tell me more','i would like to hear more of them','once more','once again','more','again'],query) and (query_for_future is not None):
                SR.speak(pyjokes.get_joke(language="en", category="all"))


            # weather report
            elif there_exists(['weather report','weather'],query):
                Weather=Annex.Weather()
                Weather.show(scrollable_text)
                break


            # it will give the temperature
            elif there_exists(['temperature'],query):
                try:
                    res=app.query(query)
                    SR.speak(next(res.results).text)
                except:
                    print("Internet Connection Error")
                break


            # password generator
            elif there_exists(['suggest me a password','password suggestion','i want a password','give me a password'],query):
                m3=Annex.PasswordGenerator()
                m3.givePSWD(scrollable_text,root)
                del m3
                break


            # making note
            elif there_exists(['make a note','take note','take a note','note it down','make note','remember this as note','open notepad and write'],query):
                SR.speak("What would you like to write down?")
                data=SR.takeCommand()
                n=Annex.Note()
                n.takeNote(data)
                SR.speak("I have a made a note of that.")
                
            # closing the notepad
            elif there_exists(['close the note','close notepad'],query):
                SR.speak("Okay sir, closing notepad")
                os.system("taskkill /f /im notepad.exe")
                break


            # taking photo
            elif there_exists(['take a photo','take a selfie','take my photo','take photo','take selfie','one photo please','click a photo'],query):
                takephoto=Annex.camera()
                imgLocation=takephoto.takePhoto()
                os.startfile(imgLocation)
                del takephoto
                SR.speak("Captured picture is stored in Camera folder.")
                break


            # screenshot
            elif there_exists(['take screenshot','take a screenshot','screenshot please','capture my screen'],query):
                SR.speak("Taking screenshot")
                SS=Annex.screenshot()
                SS.takeSS()
                SR.speak('Captured screenshot is saved in Screenshots folder.')
                del SS
                break


            #voice recorder
            elif there_exists(['record my voice','start voice recorder','voice recorder'],query):
                VR=Annex.VoiceRecorder()
                VR.Record(scrollable_text)
                del VR
                break


            #text to speech conversion
            elif there_exists(['text to speech','convert my notes to voice'],query):
                SR.speak("Opening Text to Speech mode")
                TS=Annex.TextToSpeech()
                del TS
                break


            #flipping coin
            elif there_exists(["toss a coin","flip a coin","toss"],query):
                moves=["head", "tails"]
                cmove=random.choice(moves)
                playsound.playsound('Sounds/quarter spin flac.mp3')
                SR.speak("It's " + cmove)
                break


            #Playing music
            elif there_exists(['play music','play some music for me','like to listen some music'],query):
                SR.speak("Playing musics")
                music_dir='C:\\Users\\ajayaju\\Music'
                songs=os.listdir(music_dir)
                # print(songs)
                index=random.randint(0,50)
                os.startfile(os.path.join(music_dir,songs[index]))
                break


            #play game
            elif there_exists(['would like to play some games','play some games','would like to play some game','want to play some games','want to play game','want to play games','play games','open games','play game','open game'],query):
                SR.speak("We have only 2 game right now.\n")
                SR.updating_ST_No_newline('1.')
                SR.speak("Stone Paper Scissor")
                SR.updating_ST_No_newline('2.')
                SR.speak("Snake")
                SR.updating_ST_No_newline('3.')
                SR.speak("Pong")
                SR.speak("\nTell us your choice:")
                while(True):
                    query=SR.takeCommand().lower()
                    if ('stone' in query) or ('paper' in query):
                        SR.speak("Opening stone paper scissor...")
                        sps=Annex.StonePaperScissor()
                        sps.start(scrollable_text)
                        break
                    elif ('snake' in query):
                        SR.speak("Opening snake game...")
                        from Games.Snake.snake import start
                        start()
                        break
                    elif ('pong' in query):
                        SR.speak("Opening pong game...")
                        from Games.Pong.pong import start
                        start()
                        break
                    else:
                        SR.speak("It did not match the option that we have. \nPlease say it again.")
                break


            #changing the background and foreground color
            elif there_exists(['change colour','change assistant colour','background colour','text colour'],query):
                col = Annex.SetColor(scrollable_text)
                while True:
                    SR.speak("which color do you want to change,background or text or both")
                    choice = SR.takeCommand().lower()
                    if there_exists(['background','background colour','back ground','back ground colour'],choice):
                        col.setBackground()
                        SR.speak("restart to take changes effect")
                        break
                    elif there_exists(['text','foreground','foreground colour','fore ground','fore ground colour','forground','forground colour','for ground colour','for ground'],choice):
                        col.setForeground()
                        SR.speak("restart to take changes effect")
                        break
                    elif there_exists(['both'],choice):
                        col.setBackground()
                        col.setForeground()
                        SR.speak("restart to take changes effect")
                        break
                    elif there_exists(['nothing','no','none'],choice):
                        break
                    else:
                        SR.speak("choice doesn't match any......please retry")
                break
            

            #hiding and visibling all files in this folder
            elif there_exists(['hide all files','hide this folder'],query):
                os.system("attrib +h /s /d")
                SR.speak("Sir, all the files in this folder are now hidden")

            elif there_exists(['visible','make files visible'],query):
                os.system("attrib -h /s /d")
                SR.speak("Sir, all the files in this folder are now visible to everyone. I hope you are taking this decision in your own peace")


            #passing if nothing in the query
            elif there_exists(['none'],query):
                pass
    

            #Stopping the listening
            elif there_exists(['stop the flow','stop the execution','halt','halt the process','stop the process','stop listening','stop the listening','stop'],query):
                SR.speak("Listening halted.")
                break
        

            #Halting the assistant
            elif there_exists(['exit','quit','shutdown','shut up','goodbye','shut down','good bye','offline','bye'],query):
                SR.speak("shutting down")
                sys.exit()

            else:
                SR.speak("Sorry it did not match with any commands that i'm registered with. Please say it again.")

    except RuntimeError as r:
        pass

    except Exception as e:
        SR.speak('unable to start ,Please check your connection')
        sys.exit()




def generate(n):
    for i in range(n):
        yield i


# thread class
class MainframeThread(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        # print(threadID,name)
    def run(self):
        # print("running..")
        mainframe()


def Launching_thread():
    """
    creating thread for smooth execution of the assistant
    """
    Thread_ID=generate(1000)
    global MainframeThread_object
    MainframeThread_object=MainframeThread(Thread_ID.__next__(),"Mainframe")
    MainframeThread_object.start()



if __name__=="__main__":
    #tkinter code
    root=Tk()
    root.configure(background="grey")
    # root.geometry("{}x{}+{}+{}".format(1000,450,int(root.winfo_screenwidth()/2 - 745/2),int(root.winfo_screenheight()/2 - 450/2)))
    root.geometry("1000x550+200+100")
    root.resizable(0,0)
    root.title("Hazel")
    root.configure(bg='#2c4557')
    col = Annex.GetColor()
    background = col.getBackground()
    # print(background)
    foreground = col.getForeground()
    # print(foreground)
    scrollable_text=scrolledtext.ScrolledText(root,state='disabled',height=15,width=72,wrap=WORD,relief='sunken',bd=5,bg=background,fg=foreground,font='"Times New Roman" 13')
    scrollable_text.place(x=10,y=10)
    mic_img=Image.open(r'C:\\Users\\ajayaju\\new virtual assistant\\Hazel\\Mic.png')
    mic_img=mic_img.resize((55,55),Image.ANTIALIAS)
    mic_img=ImageTk.PhotoImage(mic_img)
    Speak_label=Label(root,text="SPEAK:",fg="white",font='"Times New Roman" 15 ',borderwidth=0,bg='#2c4557')
    Speak_label.place(x=340,y=480)
    # print(scrollable_text)
    SR = Annex.SpeakRecognition(scrollable_text)
    Listen_Button=Button(root,image=mic_img,borderwidth=0,activebackground='#2c4557',bg='#2c4557',command=Launching_thread)
    Listen_Button.place(x=450,y=470)
    myMenu=Menu(root)
    m1=Menu(myMenu,tearoff=0) #tearoff=0 means the submenu can't be teared off from the window
    m1.add_command(label='Commands List',command=commandsList)
    myMenu.add_cascade(label="Help",menu=m1)
    stng_win=Annex.SettingWindow()
    myMenu.add_cascade(label="Settings",command=partial(stng_win.settingWindow,root))
    myMenu.add_cascade(label="Clear Screen",command=clearScreen)
    root.config(menu=myMenu)
    root.mainloop()