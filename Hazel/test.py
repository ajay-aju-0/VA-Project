import cv2
import matplotlib.pyplot as plt 
from tkinter import *
from tkinter import filedialog

file_path = ""

def openFile():
    global file_path
    file_path=filedialog.askopenfilename(initialdir =r"C:\\Users\\ajayaju\\OneDrive\\Pictures",title="Select file",filetypes=(("jpg","*.jpg"),("png","*.png"),("All files", "*.*")))
    with open(file_path,'r') as f:
        print(file_path)
        filename = f.name.split('/')[-1]
        print(filename)
        l2 = Label(root,text=filename)
        l2.place(x=36,y=20)

def submitFile():
    root.destroy()
    img = cv2.imread(file_path)
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

    inverted_gray_image = 255 - gray_image

    blurred_img = cv2.GaussianBlur(inverted_gray_image, (21,21),0) 

    inverted_blurred_img = 255 - blurred_img

    pencil_sketch_IMG = cv2.divide(gray_image, inverted_blurred_img, scale = 256.0)

    cv2.imwrite('sketch Image.png', pencil_sketch_IMG)

    # cv2.imshow('Pencil Sketch', pencil_sketch_IMG)

    cv2.waitKey(0)

    plt.figure(figsize=(14,8))
    plt.subplot(1,2,1)
    plt.title('Original image', size=18)
    plt.imshow(img)
    plt.axis('off')
    plt.subplot(1,2,2)
    plt.title('Sketch', size=18)
    rgb_sketch=cv2.cvtColor(pencil_sketch_IMG, cv2.COLOR_BGR2RGB)
    plt.imshow(rgb_sketch)
    plt.axis('off')
    plt.show()

    


# img_location = "C:\\Users\\ajayaju\\OneDrive\\Pictures\\Video Projects\\"
# filename = 'IMG-20210806-WA0139.jpg'

root = Tk()
root.resizable(0,0)
root.configure()
root.geometry("300x100+200+100")
root.title('image to sketch')
l1 = Label(root,text="file selected:")
l1.place(x=20,y=20)


open_btn=Button(root,text="Open",width=7,bg="blue",fg="black",font=("TimesNewRoman",10,'bold'),command=openFile).place(x=155,y=50)
submit = Button(root,text="submit",width=7,bg="green",fg="white",font=("TimesNewRoman",10,'bold'),command=submitFile).place(x=226,y=50)

# img = cv2.imread(img_location+filename)

root.mainloop()