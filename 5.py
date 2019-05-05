from Tkinter import *
import sqlite3
con=sqlite3.Connection('db')
cur=con.cursor()
root=Tk()
import tkMessageBox
icon=PhotoImage(file="main.gif")
root.geometry('1024x768')
l1=Label(root,image=icon).place(x=0,y=0)
l2=Label(root,text="What is the output of L[1:] if L = [1,2,3]?",font=('times',17,'bold'),bd=5,fg="white",bg="black").place(relx=.2,rely=.4)
import os

def Play():
    tkMessageBox.showinfo("CONGRATULATIONS","    YOU ARE THE NEW WINNER OF KBC")
    rt=Tk()
    Label(rt,text="Your Name=",font='times 30').grid(row=0,column=0)
    e=Entry(rt,font='times 25')
    e.grid(row=0,column=1)
    def ins():
        cur.execute('create table if not exists kbc(name varchar2(20))')
        cur.execute('insert into kbc values(?)',(e.get(),))
        rt.destroy()
        os.system("start winners.py")
        con.commit()
    Button(rt,text="Proceed",command=ins).grid(row=1,column=0)
    root.destroy()
    
def gameover():
    def asd():
        tkMessageBox.showinfo("GAME OVER","YOUR GAME IS OVER")
        root.destroy()
    l2=Label(root,text="GAME OVER",font=('times',17,'bold'),bd=8,fg="white",bg="black").after(500,asd)
    

button = Button(root, text="Click me!",command=Play)
img = PhotoImage(file="5_A.gif")
button.config(image=img,bd=-1)
button.place(relx=0.2,rely=0.6)

button1 = Button(root, text="Click me!",command=gameover)
img1 = PhotoImage(file="5_B.gif")
button1.config(image=img1,bd=-1)
button1.place(relx=.6,rely=.600)

button2 = Button(root, text="Click me!",command=gameover)
img2 = PhotoImage(file="5_C.gif")
button2.config(image=img2,bd=-1)
button2.place(relx=.2,rely=.7)

button3 = Button(root, text="Click me!",command=gameover)
img3 = PhotoImage(file="5_D.gif")
button3.config(image=img3,bd=-1)
button3.place(relx=.6,rely=.700)



root.mainloop()
