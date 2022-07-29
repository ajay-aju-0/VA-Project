from tkinter import *
from tkinter import scrolledtext 
from PIL import ImageTk,Image

if __name__=="__main__":
    root=Tk()
    root.configure(background="grey")
    # root.geometry("{}x{}+{}+{}".format(745,360,int(root.winfo_screenwidth()/2 - 745/2),int(root.winfo_screenheight()/2 - 360/2)))
    root.geometry("{}x{}+{}+{}".format(745,450,int(root.winfo_screenwidth()/2-745/2),int(root.winfo_screenheight()/2-450/2)))
    root.resizable(0,0)
    root.title("Hazel")
    root.configure(bg='#2c4557')
    scrollable_text=scrolledtext.ScrolledText(root,state='disabled',height=20,width=87,relief='sunken',bd=5,wrap=WORD,bg='#add8e6',fg='#800000',font='"Times New Roman" 15 ')
    scrollable_text.place(x=10,y=10)
    mic_img=Image.open(r'C:\\Users\\ajayaju\\new virtual assistant\\Hazel\\Mic.png')
    mic_img=mic_img.resize((55,55),Image.ANTIALIAS)
    mic_img=ImageTk.PhotoImage(mic_img)
    Speak_label=Label(root,text="SPEAK:",fg="white",font='"Times New Roman" 15 ',borderwidth=0,bg='#2c4557')
    Speak_label.place(x=270,y=370)
    Listen_Button=Button(root,image=mic_img,borderwidth=0,activebackground='#2c4557',bg='#2c4557')
    Listen_Button.place(x=340,y=350)
    myMenu=Menu(root)
    m1=Menu(myMenu,tearoff=0) #tearoff=0 means the submenu can't be teared off from the window
    m1.add_command(label='Commands List')
    myMenu.add_cascade(label="Help",menu=m1)
    myMenu.add_cascade(label="Settings")
    myMenu.add_cascade(label="Clear Screen")
    root.config(menu=myMenu)
    root.mainloop()