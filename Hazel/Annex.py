import pyttsx3
import pyautogui 
import sounddevice 
import cv2
import playsound
import speech_recognition as sr
from tkinter import filedialog
from scipy.io.wavfile import write
from tkinter import *
# from tkinter import ttk
import requests,json 
import tkinter.scrolledtext as scrolledtext
import tkinter.messagebox as tmsg
import sqlite3
import datetime 
import os 
import subprocess 
import random
import smtplib
import psutil 
import math


class SetColor:
    '''
    Setting the colour of the screen and text as per user convenience.
    '''
    def __init__(self,scrollable_text):
        self.scrollable_text = scrollable_text

    def setBackground(self):
        bcolor=""
        SR=SpeakRecognition(self.scrollable_text)
        conn = sqlite3.connect('Hazel.db')
        mycursor=conn.cursor()

        while True:
            SR.speak("Available background colors are:")
            SR.updating_ST_No_newline('1.Blue\n2.Green\n3.sky blue\n4.Red\n5.Yellow\n6.Dark\n7.White')
            SR.speak("\n Tell the name of color from above list that you want to set as background")
            col_choice = SR.takeCommand().lower()
            if col_choice == ['blue','blu']:
                bcolor="blue"
                break
            elif col_choice in ['green','grin','gren']:
                bcolor="green"
                break
            elif col_choice in ['skyblue','sky blue','skie blue']:
                bcolor="sky blue"
                break
            elif col_choice in ['red']:
                bcolor="red"
                break
            elif col_choice in ['yellow','ellow']:
                bcolor="yellow"
                break
            elif col_choice in ['dark']:
                bcolor="black"
                break
            elif col_choice in ['white']:
                bcolor="white"
                break
            else:
                SR.speak("dont match with any choice.please tell index from given options")

        if bcolor:
            mycursor.execute('update colors set background=?',(bcolor,))
            conn.commit()
            conn.close()
            SR.speak("background color set successfully")

    def setForeground(self):
        SR=SpeakRecognition(self.scrollable_text)
        conn = sqlite3.connect('Hazel.db')
        mycursor=conn.cursor()

        while True:
            tcolor=""
            SR.speak("Available text colors are:")
            SR.updating_ST_No_newline('1.Blue\n2.Green\n3.Black\n4.Yellow\n5.White')
            SR.speak("Tell the name of color from above list that you want to set as background")
            col_choice = SR.takeCommand().lower()
            if col_choice == ['blue','blu']:
                tcolor = "blue"
                break
            elif col_choice in ['green','grin','gren']:
                tcolor="green"
                break
            elif col_choice in ['black']:
                tcolor="black"
                break
            elif col_choice in ['yellow','ellow']:
                tcolor="yellow"
                break
            elif col_choice in ['white']:
                tcolor="white"
                break
            else:
                SR.speak("dont match with any choice.please tell color from given options")

        if tcolor:
            mycursor.execute('update colors set foreground=?',(tcolor,))
            conn.commit()
            conn.close()
            SR.speak("text color set successfully")


class GetColor:
    '''
    Returning the colour of text and background
    during the starting of app to set it.
    '''
    def getBackground(self):
        try:
            conn = sqlite3.connect('Hazel.db')
            mycursor=conn.cursor()
            mycursor.execute('select background from colors')
            color = mycursor.fetchone()[0]
            conn.commit()
            conn.close()
            return color
        except Exception as e:
            pass

    def getForeground(self):
        try:
            conn = sqlite3.connect('Hazel.db')
            mycursor=conn.cursor()
            mycursor.execute('select foreground from colors')
            color = mycursor.fetchone()[0]
            conn.commit()
            conn.close()
            return color
        except Exception as e:
            pass


class SpeakRecognition:
    '''
    A class that will set the voice engine, take command from user,
    update the screen according to the command, clear the text in the
    screen,speak out the response with or without printing it in screen.
    '''
    def __init__(self,scrollable_text):
        self.scrollable_text = scrollable_text
     
    # database connection
    conn = sqlite3.connect('Hazel.db')
    mycursor=conn.cursor()

    engine=pyttsx3.init('sapi5')
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)

    scrollable_text=None

    def STS(self,scrollable_text):
        '''This is scrollable text setter '''
        self.scrollable_text=scrollable_text
        # print("hi")

    def updating_ST(self,data):
        '''Updating the scrollable text area with a preceding newline'''
        self.scrollable_text.configure(state='normal')
        self.scrollable_text.insert('end',data+'\n')
        self.scrollable_text.configure(state='disabled')
        self.scrollable_text.see('end')
        self.scrollable_text.update()
        # print("hi")

    def updating_ST_No_newline(self,data):
        '''Updating the scrollable text area without a preceding newline'''
        self.scrollable_text.configure(state='normal')
        self.scrollable_text.insert('end',data)
        self.scrollable_text.configure(state='disabled')
        self.scrollable_text.see('end')
        self.scrollable_text.update()

    def scrollable_text_clearing(self):
        '''Clear the texts in scrollable text area and set it to disabled state'''
        self.scrollable_text.configure(state='normal')
        self.scrollable_text.delete(1.0,'end')
        self.scrollable_text.configure(state='disabled')
        self.scrollable_text.update()

    def speak(self,audio):
        """It speaks the audio"""
        self.updating_ST(audio)
        self.engine.say(audio)
        self.engine.runAndWait()

    def nonPrintSpeak(self,audio):
        """it speaks audio without printing in screen"""
        self.engine.say(audio)
        self.engine.runAndWait()

    def takeCommand(self):
        """It take microphone input from the user and return string"""
        recog=sr.Recognizer()
        with sr.Microphone() as source:
            recog.adjust_for_ambient_noise(source)
            self.updating_ST("\nListening...")
            recog.pause_threshold = 1
            recog.energy_threshold = 2000
            # r.energy_threshold = 45.131829621150224
            #print(r.energy_threshold)
            audio=recog.listen(source)
        try:
            self.updating_ST("Recognizing...")
            query= recog.recognize_google(audio,language="en-in")
            self.updating_ST(f"You: {query}\n")
        except Exception as e:
            # print(e)
            self.updating_ST("Say that again please...")
            return 'None'
        return query


class Note:
    '''
    it takes the content of the text document as command and
    save it in the "Notes" folder as the making date as its
    filename
    '''
    def takeNote(self,data):
        date=datetime.datetime.now()
        filename=str(date).replace(':','-')+'-note.txt'
        a=os.getcwd()
        if not os.path.exists('Notes'):
            os.mkdir('Notes')
        os.chdir(a+r'\Notes')
        with open(filename,'w') as f:
            f.write(data)
        subprocess.Popen(['notepad.exe',filename])
        os.chdir(a)


class screenshot:
    '''
    it captures the current screen and save it with current 
    date and time as its filename in "Screenshots" folder
    '''
    def takeSS(self):
        img_captured=pyautogui.screenshot()
        a=os.getcwd()
        if not os.path.exists("Screenshots"):
            os.mkdir("Screenshots")
        os.chdir(a+'\Screenshots')
        ImageName='screenshot-'+str(datetime.datetime.now()).replace(':','-')+'.png'
        img_captured.save(ImageName)
        os.startfile(ImageName)
        os.chdir(a)


class VoiceRecorder: 
    '''
    it records the voice of user for 10 secs and
    save it in the "Recordings" folder as current 
    date and time as its filename
    '''
    def Record(self,scrollable_text):
        SR=SpeakRecognition(scrollable_text)
        SR.speak("This recording is of 10 seconds.")
        fs=44100
        second=10
        SR.updating_ST("Recording.....")
        record_voice=sounddevice.rec(int(second * fs),samplerate=fs,channels=2)
        sounddevice.wait()
        a=os.getcwd()
        if not os.path.exists("Recordings"):
            os.mkdir("Recordings")
        os.chdir(a+'\Recordings')
        write("Recording-"+str(datetime.datetime.now()).replace(':','-')+".wav",fs,record_voice)
        SR.speak("Voice is recorded in \'Recordings\' folder.")
        os.chdir(a)
        del SR


class camera:
    '''
    it captures the image of the user with system's
    webcam and save it in "Camera" folder with filename
    as current date and time
    '''
    def takePhoto(self):
        self.videoCaptureObject = cv2.VideoCapture(0)
        self.result = True
        a=os.getcwd()
        if not os.path.exists("Camera"):
            os.mkdir("Camera")
        os.chdir(a+'\Camera')
        self.ImageName="Image-"+str(datetime.datetime.now()).replace(':','-')+".jpg"
        while(self.result):
            self.ret,self.frame = self.videoCaptureObject.read()
            cv2.imwrite(self.ImageName,self.frame)
            self.result = False
        self.videoCaptureObject.release()
        cv2.destroyAllWindows()
        os.chdir(a)
        playsound.playsound("Sounds/camera-shutter-click.mp3")
        return "Camera\\"+self.ImageName


class TextToSpeech:
    '''
    This will open a new window as child window of assistant
    and take text input in a textarea.
    there will be 3 buttons
        --> Speak button for speaking the text typed in textarea
        --> Clear button for clearing the text in textarea
        --> Open button for selecting a file and write its contents in text area 
    '''
    def __init__(self):
        self.root=Tk()
        self.root.resizable(0,0)
        self.root.configure(background='white')
        self.root.title("Text to Speech")
        self.root.iconbitmap('Icons/text_to_speech.ico')
        #root widget
        self.text=scrolledtext.ScrolledText(self.root,width=30,height=10,wrap=WORD,padx=10,pady=10,borderwidth=5,relief=RIDGE)
        self.text.grid(row=0,columnspan=3)
        #buttons
        self.listen_btn=Button(self.root,text="Listen",width=7,command=self.txtspk).grid(row=2,column=0,ipadx=2)
        self.clear_btn=Button(self.root,text="Clear",width=7,command=lambda:self.text.delete(1.0,END)).grid(row=2,column=1,ipadx=2)
        self.open_btn=Button(self.root,text="Open",width=7,command=self.opentxt).grid(row=2,column=2,ipadx=2)
        self.root.focus_set()
        self.root.mainloop()

    def txtspk(self):
        SR=SpeakRecognition(None)
        SR.nonPrintSpeak(self.text.get(1.0,END))
        del SR

    def opentxt(self):
        self.root.focus_force()
        try:
            file_path=filedialog.askopenfilename(initialdir =r"C:\\Users\\ajayaju\\Documents",title="Select file",filetypes=(('text file',"*.txt"),("All files", "*.*")))
            with open(file_path,'r') as f:
                g=f.read()

            self.root.focus_force()
            self.text.delete(1.0,END)
            self.text.insert(INSERT,g)
            self.text.update()
            SR=SpeakRecognition(None)
            SR.nonPrintSpeak(g)
            del SR
        except FileNotFoundError as e:
            self.root.focus_force()
            pass


class StonePaperScissor:
    '''
    A class for playing stone paper scissor game.
    There will bw 3 rounds and user can select there option as 
    voice input, and computer will be the opponent and it will
    select its choice as random from a list.Those who win most rounds 
    will be the winner of the game.
    '''
    def start(self,scrollable_text):
        SR=SpeakRecognition(scrollable_text)
        list1=['stone','paper','scissor']
        while(True):
            SR.scrollable_text_clearing()
            SR.updating_ST("------------------------------------WELCOME-------------------------------------------")
            SR.speak("\n\nThis game contains 3 rounds, those who win maximum rounds will be winner of this game.")
            human_score=0
            computer_score=0
            i=0
            while(i<2):
                if i==2:
                    if(human_score>computer_score):
                        SR.speak("\nNo need of 3rd round because human's score is obviously greater thean computer's.\n")
                        break
                    elif(human_score<computer_score):
                        SR.speak("\nNo need of 3rd round because computer's score is obviously greater thean human's.\n")
                        break

                SR.updating_ST(87*"*")
                while(True):
                    SR.speak("Your choice please-")
                    user_ip=SR.takeCommand().lower()
                    if(('stone' in user_ip) or ('paper' in user_ip) or ('scissor' in user_ip) or ('cutter' in user_ip) or ('rock' in user_ip)):
                        if(user_ip=='cutter'):
                            user_ip='scissor'
                        if(user_ip=='rock'):
                            user_ip='stone'
                        break
                    else:
                        SR.speak("\nIt did not match with the option that we have. Please enter your choice again.")
                comp_ip=random.choice(list1)
                if(user_ip==comp_ip):
                    SR.speak("\nIt is a tie, so it is not considered as a round.\n")

                elif((user_ip=='stone' and comp_ip=='paper') or (user_ip=='paper' and comp_ip=='scissor') or (user_ip=='scissor' and comp_ip=='stone') ):
                    computer_score+=1
                    SR.speak("\nComputer win this round.\n")
                    SR.speak(f"\nComputre's choice was {comp_ip}.\n")
                    SR.updating_ST(87*"+")
                    i+=1
                elif((comp_ip=='stone' and user_ip=='paper') or (user_ip=='scissor' and comp_ip=='paper') or (user_ip=='stone' and comp_ip=='scissor')):
                    human_score+=1
                    SR.speak("\nHuman win this round.\n")
                    SR.speak(f"\nComputre's choice was {comp_ip}.\n")
                    SR.updating_ST(87*"+")
                    i+=1
            if(human_score==computer_score):
                SR.speak("\nIt is a tie.\n")
            elif(human_score>computer_score):
                SR.speak("\nHuman is the winner of this game.\n")
            else:
                SR.speak("\nComputer is the winner of this game.\n")
            SR.updating_ST(87*"*")
            SR.speak('If you want repeat this game then say REPEAT.')
            decision=SR.takeCommand().lower()
            if('repeat' not in decision or "don't" in decision):
                SR.speak("Getting out of this game to main thread.")
                break


class SettingWindow:
    '''
    Assistant's settings window. It can be opened by command or clicking
    the menu button named settings. Used for setting the speech_rate and
    volume of the assistant.
    '''

    def Apply(self):
        #Database connection
        conn = sqlite3.connect('Hazel.db')
        mycursor=conn.cursor()
        Speech_Rate=self.speech_rate_text_box.get()
        if not (Speech_Rate.isdigit()):
            tmsg.showinfo("Error.",f"Please enter integers.")
            self.setting.focus_force()
        else:
            mycursor.execute('update speech_rate set rate=?',(int(Speech_Rate),))
            volume=int((self.volume_slider.get()))
            mycursor.execute('update volume set vol=?',(volume,))
            conn.commit()
            conn.close()
            # print(f"{value} type is {type(value)}")
            tmsg.showinfo("Point to be noted.",f"Setting will be applied after reboot of this program.")
            self.setting.destroy()

    def settingWindow(self,root):
        #database connection
        conn = sqlite3.connect('Hazel.db')
        mycursor=conn.cursor()
        self.setting=Toplevel(root)
        canvas=Canvas(self.setting)
        canvas.create_line(0,143,400,143)
        canvas.create_line(0,146,400,146)
        canvas.pack()
        self.setting.title("Settings")
        self.setting.iconbitmap('Icons/setting.ico')
        self.setting.geometry("400x200+500+200")
        self.setting.resizable(0,0)
        self.volume=Label(self.setting,text="Hazel's Volume: ",borderwidth=0,font=('"Times New Roman"')).place(x=3,y=17)
        self.speech=Label(self.setting,text='Speech Rate[WPM]:',borderwidth=0,font=('"Times New Roman"')).place(x=3,y=77)
                
        '''Placing sliders and textboxes'''
        self.volume_slider=Scale(self.setting,from_=0,to=10,orient=HORIZONTAL)
        Integer_class=IntVar(self.setting,value=mycursor.execute('select rate from speech_rate').fetchone()[0])
        self.speech_rate_text_box=Entry(self.setting,textvariable=Integer_class)
        self.volume_slider.place(x=137,y=0)
        self.speech_rate_text_box.place(x=170,y=77)
        self.volume_slider.set((mycursor.execute('select vol from volume').fetchone()[0]))
        conn.commit()
        conn.close()
        self.Apply_Button=Button(self.setting,text="Apply",bg="green",fg="white",command=self.Apply).place(x=292,y=152)
        self.setting.mainloop()


class SystemInfo:
    '''
    A class for retrieving the system specs
    '''

    def convert_size(size_bytes):
        if size_bytes == 0:
            return "0B"
        size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
        i = int(math.floor(math.log(size_bytes, 1024)))
        p = math.pow(1024, i)
        s = round(size_bytes / p, 2)
        # print("%s %s" % (s, size_name[i]))
        return "%s %s" % (s, size_name[i])
    
    def system_stats(self,si):
        cpu_stats = str(psutil.cpu_percent())
        battery_percent = psutil.sensors_battery().percent
        memory_in_use = si.convert_size(psutil.virtual_memory().used)
        total_memory = si.convert_size(psutil.virtual_memory().total)
        final_res = f"Currently {cpu_stats} percent of CPU, {memory_in_use} of RAM out of total {total_memory}  is being used and battery level is at {battery_percent} percent"
        return final_res


class MailSend:
    '''
    A class for sending email messages
    '''

    def __init__(self, semail,spass,remail,msg):
        self.sender_mail = semail
        self.sender_passwd = spass
        self.receiver_mail = remail
        self.message = msg

    def mail(self):
        try:
            mail = smtplib.SMTP('smtp.gmail.com', 587)
            mail.ehlo()
            mail.starttls()
            mail.login(self.sender_mail, self.sender_password)
            mail.sendmail(self.sender_email, self.receiver_email, self.message)
            mail.close()
            return True
        except Exception as e:
            print(e)
            return False
            

class News:
    '''
    A class for retrieving the top 5 news of all catagories
    '''

    def __init__(self,scrollable_text):
        self.SR=SpeakRecognition(scrollable_text)

    def show(self):
        self.SR.speak("Showing top 5 news of today.")
        self.SR.scrollable_text_clearing()
        self.SR.updating_ST("-----------------------------Top 5 news of all categories.----------------------------")
        r=requests.get('http://newsapi.org/v2/top-headlines?country=in&apiKey=329416dc10ea4588a0a8f6b233116393')
        data=json.loads(r.content)
        for i in range(5):
            self.SR.updating_ST_No_newline(f'News {i+1}:  ')
            self.SR.speak(data['articles'][i]['title']+'\n')


class Weather:
    '''
    A class for retrieving the current weather information.
    Includes temperature,latitude,longitude,wind speed and
    description of weather.
    '''

    def show(self,scrollable_text):
        SR=SpeakRecognition(scrollable_text)
        base_url = "http://api.openweathermap.org/data/2.5/weather?q=Pune,IN&units=metric&appid=ea45752424c9cad83b4f5c836ced6b1a"
        data=requests.get(base_url).json()
        SR.scrollable_text_clearing()
        SR.speak("-----------------------------Weather Report of PUNE City------------------------------")
        SR.updating_ST("Temperature:   "+str(int(data['main']['temp']))+' Celsius\n'+
                        "Wind Speed:    "+str(data['wind']['speed'])+' m/s\n'+
                        "Latitude:      "+str(data['coord']['lat'])+
                        "\nLongitude:     "+str(data['coord']['lon'])+
                        "\nDescription:   "+str(data['weather'][0]['description'])+'\n')
