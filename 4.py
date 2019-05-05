from Tkinter import *
root=Tk()
import tkMessageBox
icon=PhotoImage(file="main.gif")
root.geometry('1024x768')
l1=Label(root,image=icon).place(x=0,y=0)
l2=Label(root,text="Which of the following function convert a String to an object in python?",font=('times',17,'bold'),bd=5,fg="white",bg="black").place(relx=.1,rely=.4)
import os

def Play():
    root.destroy()
    os.system("start 5.py")
def gameover():
    def asd():
        tkMessageBox.showinfo("GAME OVER","YOUR GAME IS OVER")
        root.destroy()
    l2=Label(root,text="GAME OVER",font=('times',17,'bold'),bd=8,fg="white",bg="black").after(500,asd)
    

button = Button(root, text="Click me!",command=gameover)
img = PhotoImage(file="4_A.gif")
button.config(image=img,bd=-1)
button.place(relx=0.2,rely=0.6)

button1 = Button(root, text="Click me!",command=Play)
img1 = PhotoImage(file="4_B.gif")
button1.config(image=img1,bd=-1)
button1.place(relx=.6,rely=.600)

button2 = Button(root, text="Click me!",command=gameover)
img2 = PhotoImage(file="4_C.gif")
button2.config(image=img2,bd=-1)
button2.place(relx=.2,rely=.7)

button3 = Button(root, text="Click me!",command=gameover)
img3 = PhotoImage(file="4_D.gif")
button3.config(image=img3,bd=-1)
button3.place(relx=.6,rely=.700)



root.mainloop()
