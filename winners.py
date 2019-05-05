from Tkinter import *
import os
import sqlite3
con=sqlite3.Connection('db')
cur=con.cursor()
root=Tk()
root.configure(bg='black')
root.geometry('1024x768')
cur.execute('select * from kbc')
c=cur.fetchall()
print c
for i in c:
    Label(root,text=i,bg='white',fg='blue').pack()
    



def Retry():
    root.destroy()
    os.system("start KBC.py")
l2=Label(root,text="WINNERS",font=('times',50,'bold'),bd=5,fg="white",bg="black").place(relx=.350,rely=.000)
b1=Button(root,text="QUIT",font=('arial',10,'bold'),fg="white",bg="midnight blue",bd=10,command=root.destroy,width=18).place(relx=.85,rely=.85,anchor=CENTER)
b2=Button(root,text="RETRY",font=('arial',10,'bold'),fg="white",bg="midnight blue",bd=10,command=Retry,width=18).place(relx=.15,rely=.85,anchor=CENTER)
root.mainloop()
