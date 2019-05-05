from Tkinter import *
root=Tk()
icon=PhotoImage(file="satyam.gif")
lab=Label(root,image=icon)
lab.pack()
import os
def play():
    root.destroy()
    os.system("start 1.py")
def opening():
    os.system("start opening.mp3")
def Winners():
    root.destroy()
    os.system("start winners.py")
opening()
b1=Button(root,text="PLAY",command=play,font=('arial',24,'bold'),fg="white",bg="midnight blue",bd=10,width=18).place(relx=.50,rely=.8,anchor=CENTER)
b2=Button(root,text="QUIT",font=('arial',24,'bold'),fg="white",bg="midnight blue",bd=10,command=root.destroy,width=18).place(relx=.80,rely=.8,anchor=CENTER)
b3=Button(root,text="WINNERS",font=('arial',24,'bold'),fg="white",bg="midnight blue",bd=10,width=18,command=Winners).place(relx=.2,rely=.8,anchor=CENTER)
root.mainloop()
