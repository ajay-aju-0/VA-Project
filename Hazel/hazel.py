import wolframalpha
import datetime
import os 
import random
import requests
import sys 
import time
import threading 
import playsound
import getpass
import wikipedia
import webbrowser 
import pyautogui
import pyjokes
import Annex
import geocoder
from tkinter import *
from tkinter import scrolledtext
from PIL import ImageTk,Image
from functools import partial
from geopy.geocoders import Nominatim
from geopy.distance import great_circle



#****************************** LOCAL MEMORY ****************************************#


#==================== Memory for 'how are you' query ====================

howareyou= ['Good to hear from you! How may I help','I\'m fine, thank you. What can I do for you?',
            'Very Good, How may I help you','Wonderful thanks, What can I do for you?',
            'I\'m well, thank you, how can I help','So glad to hear your voice, How can I help you?',
            'I\'m doing great, thanks for asking. Anything I can help with'
        ]

#==================== setting browser paths =============================

chrome_path="C://Program Files//Google//Chrome//Application//chrome.exe %s"       #chrome path

edge_path ="C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe %s" #edge path

#==================== setting variables for background and text colours==

background = ""
foreground = ""


#********************************* LOCAL MEMORY END *********************************#



def there_exists(terms,query):
    '''Checking whether saved commands exists in given query or not'''
    for term in terms:
        if term in query:
                return True


def computational_intelligence(question):
    try:
        client = wolframalpha.Client("JPK4EE-L7KR3XWP9A")
        answer = client.query(question)
        answer = next(answer.results).text
        # print(answer)
        return answer
    except:
        SR.speak("Sorry sir I couldn't fetch your question's answer. Please try again ")
        return None


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
        SR.speak('Good morning')
    elif hour>=12 and hour<18:
        SR.speak('Good afternoon')
    elif hour>=18 and hour<20:
        SR.speak('Good evening')
    else:
        SR.speak('it\'s night time' )

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
            elif there_exists(['what is my name','tell me my name',"i don't remember my name","what's my name","who am i"],query):
                SR.speak("Your name is "+str(getpass.getuser()))


            # time and date
            elif there_exists(['the time'],query):
                strTime =datetime.datetime.now().strftime("%H:%M:%S")
                SR.speak(f"Sir, the time is {strTime}")
            elif there_exists(['the date'],query):  
                strDay=datetime.date.today().strftime("%B %d, %Y")
                SR.speak(f"Today is {strDay}")
            elif there_exists(['what day it is','what day is today','which day is today',"today's day name please",'the day'],query):
                SR.speak(f"Today is {datetime.datetime.now().strftime('%A')}")


            # display calendar
            elif there_exists(['show me calendar','display calendar','show calendar','open calender'],query):
                try:
                    todays_date = datetime.date.today()
                    obj = Annex.Calender(todays_date)
                    obj.showCalender()
                    SR.nonPrintSpeak('opening calender for you')
                except Exception as e:
                    SR.speak("not able to display calender,please try again later")
                break


            # calender events
            elif there_exists(['what do i have','do i have plans','am i busy','do i have plan'],query):
                try:
                    todays_date = datetime.date.today()
                    obj = Annex.Calender(todays_date)
                    service = obj.authenticate_google()
                    date = obj.get_date(query) 
                    if date:
                        return obj.get_events(date, service,scrollable_text)
                    else:
                        SR.speak("please mention a date or month to check events")
                except Exception as e:
                    SR.speak("unable to fetch your events.Please try later")


            # opening software applications
            elif there_exists(['open code','open visual studio code','open vs code','open vscode','launch code','launch visual studio code','launch vs code','launch vscode'],query):
                try:
                    os.startfile("C:\\Users\\ajayaju\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
                    SR.nonPrintSpeak('opening visual studio code')
                except Exception as e:
                    SR.speak('sorry i am not able to find the path of vs code,please make sure you installed it')
                break

            elif there_exists(['open wordpad','launch wordpad'],query):
                try:
                    os.startfile("C:\\Windows\\WinSxS\\amd64_microsoft-windows-wordpad_31bf3856ad364e35_10.0.22000.1_none_83fe16d971ae9831\\wordpad.exe")
                    SR.nonPrintSpeak('opening wordpad')
                except Exception as e:
                    SR.speak('sorry i am not able to find the path of wordpad,please make sure you installed it')
                break

            elif there_exists(['open microsoft word','open word','launch microsoft word','launch word'],query):
                try:
                    os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE")
                    SR.nonPrintSpeak('opening microsoft word')
                except Exception as e:
                    SR.speak('sorry i am not able to find the path of microsoft word,please make sure you installed it')
                break

            elif there_exists(['open powerpoint','open presentation','open powerpoint presentation','powerpoint presentation','launch powerpoint','launch presentation','launch powerpoint presentation'],query):
                try:
                    os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE")
                    SR.nonPrintSpeak('opening microsoft powerpoint presentation')
                except Exception as e:
                    SR.speak('sorry i am not able to find the path of powerpoint,please make sure you installed it')
                break

            elif there_exists(['open notepad plus plus','open notepad++','open notepad ++','notepad++','notepad ++','launch notepad plus plus','launch notepad++','launch notepad ++'],query):
                try:
                    os.startfile("C:\\Program Files\\Notepad++\\notepad++.exe")
                    SR.speak('Opening notepad++')
                except Exception as e:
                    SR.speak('sorry i am not able to find the path of notepad++,please make sure you installed it')
                break

            elif there_exists(['open notepad','start notepad','launch notepad'],query):
                try:
                    os.startfile("C:\\Windows\\notepad.exe")
                    SR.nonPrintSpeak('opening notepad')
                except Exception as e:
                    SR.speak('sorry i am not able to find the path of notepad,please make sure you installed it')
                break

            elif there_exists(['open ms paint','open mspaint','open microsoft paint','start microsoft paint','start ms paint','launch ms paint','launch mspaint','launch microsoft paint'],query):
                try:
                    os.startfile('C:\Windows\System32\mspaint.exe')
                    SR.speak("Opening Microsoft paint....")
                except Exception as e:
                    SR.speak('sorry i am not able to find the path of microsoft paint,please make sure you installed it')
                break

            elif there_exists(['open snipping tool','snipping tool','start snipping tool','launch snipping tool'],query):
                try:
                    os.startfile("C:\Windows\System32\SnippingTool.exe")
                    SR.speak("Opening snipping tool....")
                except Exception as e:
                    SR.speak('sorry i am not able to find the path of snipping tool,please make sure you installed it')
                break

            elif there_exists(['open file manager','file manager','open my computer','my computer','open file explorer','file explorer','open this pc','this pc','launch file manager','launch my computer','launch file explorer','launch this pc'],query):
                try:
                    os.startfile("C:\Windows\explorer.exe")
                    SR.speak("Opening File Explorer")
                except Exception as e:
                    SR.speak('sorry i am not able to open file explorer.i think the path doesn\'t exist')
                break

            elif there_exists(['powershell'],query):
                try:
                    os.startfile(r'C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe')
                    SR.speak("Opening powershell")
                except Exception as e:
                    SR.speak('sorry i am not able to open windows powershell.i think the path doesn\'t exist')
                break

            elif there_exists(['cmd','command prompt','command prom','commandpromt','launch commandprompt','launch command prompt'],query):
                try:
                    os.startfile(r'C:\\Windows\\System32\\cmd.exe')
                    SR.speak("Opening command prompt")
                except Exception as e:
                    SR.speak('sorry i am not able to open command prompt.i think the path doesn\'t exist')
                break

            elif there_exists(['show me performance of my system','open performance monitor','performance monitor','performance of my computer','performance of this computer','launch performance monitor'],query):
                try:
                    os.startfile("C:\\Windows\\System32\\perfmon.exe")
                    SR.speak("Opening performance monitor")
                except Exception as e:
                    SR.speak('sorry i am not able to open performance monitor.i think the path doesn\'t exist')
                break

            elif there_exists(['open settings','open control panel','open this computer setting Window','open computer setting Window','open computer settings','open setting','show me settings','open my computer settings','launch settings','launch control panel'],query):
                try:
                    os.startfile('C:\\Windows\\System32\\control.exe')
                    SR.speak("Opening settings...")
                except Exception as e:
                    SR.speak('sorry i am not able to open settings.i think the path doesn\'t exist')
                break

            elif there_exists(['open vlc','vlc media player','vlc player','launch vlc player'],query):
                try:
                    os.startfile(r"C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe")
                    SR.speak("Opening VLC media player")
                except Exception as e:
                    SR.speak('sorry i am not able to open vlc player.please make sure you installed it')
                break

            elif there_exists(['windows media player','launch windows media player'],query):
                try:
                    os.startfile(r"C:\\Program Files (x86)\\Windows Media Player\\wmplayer.exe")
                    SR.speak("Opening windows media player")
                except Exception as e:
                    SR.speak('sorry i am not able to open windows media player.please make sure the path exists')
                break

            elif there_exists(['open chrome','launch chrome','open google chrome','launch google chrome'],query):
                try:
                    os.startfile("C://Program Files//Google//Chrome//Application//chrome.exe")
                    SR.speak("Opening chrome browser")
                except Exception as e:
                    SR.speak('sorry i am not able to open chrome browser.please make sure you installed it')
                break

            elif there_exists(['open microsoft edge','microsoft edge','launch microsoft edge','edge browser'],query):
                try:
                    os.startfile("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")
                    SR.speak("Opening microsoft edge browser")
                except Exception as e:
                    SR.speak('sorry i am not able to open microsoft edge browser.please make sure you installed it')
                break


            #whatsapp message
            elif there_exists(['open whatsapp messeaging','send a whatsapp message','send whatsapp message','please send a whatsapp message'],query):
                whatsapp=Annex.WhatsApp(scrollable_text)
                whatsapp.send()
                del whatsapp


            # opening assistant settings
            elif there_exists(['open your setting','open your settings','open settiing window','show me setting window','open voice assistant settings'],query):
                try:
                    SR.speak("Opening my Setting window..")
                    sett_wind=Annex.SettingWindow()
                    sett_wind.settingWindow(root)
                except RuntimeError as r:
                    pass
                except Exception as e:
                    SR.speak('sorry i am not able to open my settings now.i will resolve the error and get back to you soon.')
                break

            
            # switching the windows
            elif there_exists(['switch the window','switch window'],query):
                try:
                    SR.speak("Okay sir, Switching the window")
                    pyautogui.keyDown("alt")
                    pyautogui.press("tab")
                    time.sleep(1)
                    pyautogui.keyUp("alt")
                except Exception as e:
                    SR.speak('not able to switch the window')
                break


            # system stats
            elif there_exists(['system stats','my system stats','system'],query):
                try:
                    info = Annex.SystemInfo()
                    sys_info = info.system_stats()
                    # print(sys_info)
                    SR.speak(sys_info)
                except Exception as e:
                    SR.speak('Not able to fetch system stats.Please try again later...')
                

            # system's current ip address
            elif there_exists(['ip address','show ip','tell system ip','what\'s my ip'],query):
                try:
                    ip = requests.get('https://api.ipify.org').text
                    # print(ip)
                    SR.speak(f"Your ip address is {ip}")
                except Exception as e:
                    SR.speak('failed to find ip address,please check again later')
                
            
            # bluetooth file sharing
            elif there_exists(['send some files through bluetooth','send file through bluetooth','bluetooth sharing','bluetooth file sharing','open bluetooth'],query):
                try:
                    SR.speak("Opening bluetooth...")
                    os.startfile(r"C:\\Windows\\System32\\fsquirt.exe")
                    SR.speak("bluetooth is enabled now you can send files through it")
                    SR.speak("opening file explorer for browsing files")
                    os.startfile("C:\Windows\explorer.exe")
                except Exception as e:
                    SR.speak('Not able to open bluetooth.try again after sometime...')
                break


            # # sending email's
            # elif there_exists(['email','send mail','send email'],query):
            #     sender_email = ''
            #     sender_password = ''

            #     try:
            #         SR.speak("Whom do you want to email sir ?")
            #         recipient = SR.takeCommand().lower()
            #         receiver_email = EMAIL_DIC.get(recipient)

            #         if receiver_email:
            #             SR.speak("What is the subject sir ?")
            #             subject = SR.takeCommand()
            #             SR.speak("What should I say?")
            #             message = SR.takeCommand()
            #             msg = 'Subject: {}\n\n{}'.format(subject, message)
            #             obj = Annex.MailSend(sender_email,sender_password,receiver_email,msg)
            #             if obj.mail():
            #                 SR.speak("Email has been successfully sent")
            #             else:
            #                 SR.speak("there was an error while sending the mail.")
            #                 SR.speak("please check your email settings and resolve it")
            #         else:
            #             SR.speak("I coudn't find the requested person's email in my database. Please try again with a different name")
            #     except:
            #         SR.speak("Sorry sir. Couldn't send your mail. Please try again")
            #     break

            #text to speech conversion
            elif there_exists(['text to speech','convert my notes to voice','convert my text into speech'],query):
                SR.speak("Opening Text to Speech mode")
                TS=Annex.TextToSpeech(scrollable_text)
                del TS
                break

            
            # wikipedia search
            elif there_exists(['search wikipedia for','from wikipedia'],query):
                try:
                    SR.speak("Searching wikipedia...")
                    if 'search wikipedia for' in query:
                        query=query.replace('search wikipedia for','')
                        results=wikipedia.summary(query,sentences=2)
                        SR.speak("According to wikipedia:\n")
                        SR.speak(results)
                        
                    elif 'from wikipedia' in query:
                        query=query.replace('from wikipedia','')
                        results=wikipedia.summary(query,sentences=2)
                        SR.speak("According to wikipedia:\n")
                        SR.speak(results)
                except wikipedia.exceptions.PageError as p:
                    SR.speak("sorry sir i am not able to find an answer for this in wikipedia")
                        
            elif there_exists(['wikipedia'],query):
                try:
                    SR.speak("Searching wikipedia....")
                    query=query.replace("wikipedia","")
                    results=wikipedia.summary(query,sentences=2)
                    SR.speak("According to wikipedia:\n")
                    SR.speak(results)
                except wikipedia.exceptions.PageError as p:
                    SR.speak("sorry sir i am not able to find an answer for this in wikipedia")

            # who is searcing mode
            elif there_exists(['who is','who the heck is','who the hell is','who is this','tell me about'],query):
                try:
                    if "wikipedia" in query:
                        query=query.replace("wikipedia","")
                    results=wikipedia.summary(query,sentences=1)
                    SR.speak("According to wikipdedia:  ")
                    SR.speak(results)
                except wikipedia.exceptions.PageError as p:
                    SR.speak("sorry sir i am not able to find an answer for this in wikipedia")
                
            # what is meant by
            elif there_exists(['what is meant by','what is mean by'],query):
                try:
                    results=wikipedia.summary(query,sentences=2)
                    SR.speak("According to wikipedia:\n")
                    SR.speak(results)
                except wikipedia.exceptions.PageError as p:
                    SR.speak("sorry sir i am not able to find an answer for this in wikipedia")
                

            # it will give online results for the query
            elif there_exists(['search something for me','to do a little search','open search mode','i want to search something'],query):
                SR.speak('What you want me to search for?')
                query=SR.takeCommand()
                SR.speak(f"Showing results for {query}")
                answer = computational_intelligence(query)
                SR.speak(answer)
                
            elif there_exists(['calculate','compute','+','-','*','x','/','plus','add','minus','subtract','divide','multiply','divided','multiplied'],query):
                answer = computational_intelligence(query)
                SR.speak(f"the result is {answer}")
                
            # what is the capital
            elif there_exists(['what is the capital of','capital of','capital city of'],query):
                answer = computational_intelligence(query)
                SR.speak(answer)
                
            # it will give the temperature
            elif there_exists(['temperature'],query):
                answer = computational_intelligence(query)
                SR.speak(answer)


            # google, youtube and location
            # playing on youtube 
            elif there_exists(['open youtube and play','on youtube'],query):
                import pywhatkit
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
                if os.path.exists(chrome_path.replace('%s','')):
                    webbrowser.get(chrome_path).open("https://www.youtube.com")
                else:
                    webbrowser.get(edge_path).open("https://www.youtube.com")
                break

            # opening google and search
            elif there_exists(['open google and search','google and search'],query):
                url='https://google.com/search?q='+query[query.find('for')+4:]
                if os.path.exists(chrome_path.replace('%s','')):
                    webbrowser.get(chrome_path).open(url)
                else:
                    webbrowser.get(edge_path).open(url)
                break
            elif there_exists(['open google'],query):
                SR.speak("Opening google")
                if os.path.exists(chrome_path.replace('%s','')):
                    webbrowser.get(chrome_path).open("https://www.google.com")
                else:
                    webbrowser.get(edge_path).open("https://www.google.com")
                break

            # finding location
            elif there_exists(['find location of','find the location of','show location of','find location for','find the location for','show location for'],query):
                if 'of' in query:
                    url='https://google.nl/maps/place/'+query[query.find('of')+3:]+'/&amp'
                    if os.path.exists(chrome_path.replace('%s','')):
                        webbrowser.get(chrome_path).open(url)
                    else:
                        webbrowser.get(edge_path).open(url)
                    break
                elif 'for' in query:
                    url='https://google.nl/maps/place/'+query[query.find('for')+4:]+'/&amp'
                    if os.path.exists(chrome_path.replace('%s','')):
                        webbrowser.get(chrome_path).open(url)
                    else:
                        webbrowser.get(edge_path).open(url)
                    break
            elif there_exists(["what is my exact location","What is my location","my current location","exact current location",'where is my'],query):
                url = "https://www.google.com/maps/search/Where+am+I+?/"
                SR.speak("Showing your current location on google maps...")
                if os.path.exists(chrome_path.replace('%s','')):
                    webbrowser.get(chrome_path).open(url)
                else:
                    webbrowser.get(edge_path).open(url)
                break
            elif there_exists(["where am i"],query):
                try:
                    ip_add = requests.get('https://api.ipify.org').text
                    url = 'https://get.geojs.io/v1/ip/geo/' + ip_add + '.json'
                    geo_requests = requests.get(url).json()
                    city = geo_requests['city']
                    state = geo_requests['region']
                    if city:
                        SR.speak(f"You must be somewhere in {city}")
                    else:
                        SR.speak(f"You must be somewhere in {state}")
                except Exception as e:
                    SR.speak("Sorry sir, I coundn't fetch your current location. Please try again")
                break
            elif there_exists(["where is"],query):
                place = query.split('where is ', 1)[1]
                try:
                    webbrowser.open("http://www.google.com/maps/place/" + place + "")
                    geolocator = Nominatim(user_agent="myGeocoder")
                    location = geolocator.geocode(place, addressdetails=True)
                    target_latlng = location.latitude, location.longitude
                    location = location.raw['address']
                    city = location.get('city', ''),
                    state = location.get('state', ''),
                    country = location.get('country', '')

                    current_loc = geocoder.ip('me')
                    current_latlng = current_loc.latlng
                    
                    distance = str(great_circle(current_latlng, target_latlng))
                    distance = str(distance.split(' ',1)[0])
                    distance = round(float(distance), 2)

                    if city:
                        res = f"{place} is in {state} state and country {country}. It is {distance} km away from your current location"
                        # print(res)
                        SR.speak(res)

                    else:
                        res = f"{state} is a state in {country}. It is {distance} km away from your current location"
                        # print(res)
                        SR.speak(res)
                except:
                    SR.speak("Sorry sir, I couldn't get the co-ordinates of the location you requested. Please try again")
                break


            # image search
            elif there_exists(['show me images of','images of','display images'],query):
                url="https://www.google.com/search?tbm=isch&q="+query[query.find('of')+3:]
                if os.path.exists(chrome_path.replace('%s','')):
                    webbrowser.get(chrome_path).open(url)
                else:
                    webbrowser.get(edge_path).open(url)
                break

            elif there_exists(['search for','do a little searching for','show me results for','show me result for','start searching for','do a little search for'],query):
                SR.speak("Searching.....")
                if 'do a little searching for' in query:
                    SR.speak(f"Showing results for {query.replace('do a little searching for','')}")
                elif 'do a little search for' in query:
                    SR.speak(f"Showing results for {query.replace('do a little search for','')}")
                elif 'search for' in query:
                    SR.speak(f"Showing results for {query.replace('search for','')}")           
                elif 'show me results for' in query:
                    SR.speak(f"Showing results for {query.replace('show me results for','')}")                   
                elif 'show me result for' in query:
                    SR.speak(f"Showing results for {query.replace('show me result for','')}")
                elif 'start searching for' in query:
                    SR.speak(f"Showing results for {query.replace('start searching for','')}")
                    
                url="https://www.google.com/search?tbm=isch&q="+query[query.find('for')+4:]
                if os.path.exists(chrome_path.replace('%s','')):
                    webbrowser.get(chrome_path).open(url)
                else:
                    webbrowser.get(edge_path).open(url)
                break


            #open mail
            elif there_exists(['email','send mail','send email','mail'],query):
                try:
                    if os.path.exists("C:\\Users\\ajayaju\\OneDrive\\Desktop\\Mail.lnk"):
                        os.startfile("C:\\Users\\ajayaju\\OneDrive\\Desktop\\Mail.lnk")
                    else:
                        url = "https://mail.google.com/"
                        if os.path.exists(chrome_path.replace('%s','')):
                            webbrowser.get(chrome_path).open(url)
                        else:
                            webbrowser.get(edge_path).open(url)
                except Exception as e:
                    SR.speak("i am not able to open mail now, please try after some time")
                break


            # top 5 news
            elif there_exists(['top 5 news','top five news','listen some news','news of today'],query):
                news=Annex.News(scrollable_text)
                news.show()


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
                

            # password generator
            elif there_exists(['suggest me a password','password suggestion','i want a password','give me a password','password generator'],query):
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


            # taking photo
            elif there_exists(['take a photo','take a selfie','take my photo','take photo','take selfie','one photo please','click a photo'],query):
                photo=Annex.camera()
                imgLocation=photo.takePhoto()
                os.startfile(imgLocation)
                del photo
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


            #flipping coin
            elif there_exists(["toss a coin","flip a coin","toss"],query):
                moves=["head", "tails"]
                cmove=random.choice(moves)
                playsound.playsound("Sounds/coinflip.mp3")
                SR.speak("It's a " + cmove)


            #Playing music
            elif there_exists(['play music','play some music for me','like to listen some music','play some music'],query):
                SR.speak("Playing musics")
                music_dir='C:\\Users\\ajayaju\\Music\\songs'
                songs=os.listdir(music_dir)
                # print(songs)
                index=random.randint(0,len(songs))
                # print(index)
                os.startfile(os.path.join(music_dir,songs[index]))
                break

            #image to sketch
            elif there_exists(['image to sketch','sketch an image','sketch image','create a sketch'],query):
                sketch = Annex.SketchImage(root,scrollable_text)
                SR.speak("select any image file to convert.")
                sketch.Imagesketch()
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
            elif there_exists(['change colour','change assistant colour','background colour','back ground colour','text colour'],query):
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
            

            #hiding and visibling all files in this folder
            elif there_exists(['hide all files','hide this folder'],query):
                os.system("attrib +h /s /d")
                SR.speak("Sir, all the files in this folder are now hidden")

            elif there_exists(['visible','make files visible'],query):
                os.system("attrib -h /s /d")
                SR.speak("Sir, all the files in this folder are now visible to everyone. I hope you are taking this decision in your own peace")


            #passing if nothing in the query
            elif there_exists(['none','no'],query):
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
        print(e.__class__)
        SR.speak('unable to start ,Please check your connection')
        sys.exit()


def startUp():
    SR.speak("Initializing")
    SR.speak("Starting all systems applications")
    SR.speak("Installing and checking all drivers")
    SR.speak("Caliberating and examining all the core processors")
    SR.speak("Checking the internet connection")
    SR.speak("Wait a moment sir")
    SR.speak("All drivers are up and running")
    SR.speak("All systems have been activated")
    SR.speak("Now I am online")
    SR.speak("click speak button to give me commands")
    


def generate(n):
    for i in range(n):
        yield i


# thread class
class MainframeThread(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        try:
            mainframe()
        except RuntimeError as r:
            pass


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
    foreground = col.getForeground()

    scrollable_text=scrolledtext.ScrolledText(root,state='disabled',height=15,width=72,wrap=WORD,relief='sunken',bd=5,bg=background,fg=foreground,font='"Times New Roman" 13')
    scrollable_text.place(x=10,y=10)

    Speak_label=Label(root,text="SPEAK:",fg="white",font='"Times New Roman" 15 ',borderwidth=0,bg='#2c4557')
    Speak_label.place(x=340,y=480)
    
    SR = Annex.SpeakRecognition(scrollable_text)

    mic_img=Image.open(r'C:\\Users\\ajayaju\\new virtual assistant\\Hazel\\Icons\\Mic.png')
    mic_img=mic_img.resize((55,55),Image.ANTIALIAS)
    mic_img=ImageTk.PhotoImage(mic_img)

    Listen_Button=Button(root,image=mic_img,borderwidth=0,activebackground='#2c4557',bg='#2c4557',command=Launching_thread)
    Listen_Button.place(x=450,y=470)

    startUp()

    myMenu=Menu(root)
    m1=Menu(myMenu,tearoff=0) #tearoff=0 means the submenu can't be teared off from the window
    m1.add_command(label='Commands List',command=commandsList)
    myMenu.add_cascade(label="Help",menu=m1)
    stng_win=Annex.SettingWindow()
    myMenu.add_cascade(label="Settings",command=partial(stng_win.settingWindow,root))
    myMenu.add_cascade(label="Clear Screen",command=clearScreen)
    root.config(menu=myMenu)

    root.mainloop()