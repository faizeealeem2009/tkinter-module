from tkinter import *
from tkinter import messagebox

def greetings():
    messagebox.showinfo("Greetings!","Good Morning! "+username.get())
window=Tk()
window.title("First GUI application")
window.geometry("600x400")
window.resizable(False,False)
username=StringVar()
L1=Label(text="First GUI Application",font=("Arial",19,"bold"))
L1.pack()

L2=Label(text="Enter user name: ",font=("Arial",15,"bold"))
L2.pack()

E1=Entry(font=("Arial",14,"normal"),textvariable=username)
E1.pack()

B1=Button(text="Click Here!",font=("Arial",14,"bold"),command=greetings)
B1.pack()

window.mainloop()