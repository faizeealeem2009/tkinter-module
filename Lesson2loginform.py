from tkinter import *
from tkinter import messagebox
#import customtkinter as ctk

def login_function():
    if username.get()=="" or password.get()=="":
        messagebox.showerror("Blank Input","You can't leave username & password blank!")
    elif username.get()=="Aleem" and password.get()=="A@1234fa":
        messagebox.showinfo("Login successful","You enter correct username and password.")
    else:
        messagebox.showwarning("Input passwed","You entered"+username.get()+" "+password.get())

def showhide_pass():
    if showhide.get():
        E2.config(show="")
    else:
        E2.config(show="*")
    
window=Tk()
window.title("Login form")
window.geometry("500x300")
window.resizable(False,False)

username=StringVar()
password=StringVar()
showhide=BooleanVar()

L1=Label(window,text="Login form",font=("Arial",18,"bold"))
L1.pack(padx=10,pady=10)

L2=Label(window,text="Username:",font=("Arial",14,"normal"),pady=10)
L2.pack()

E1=Entry(window,font=("Arial",14,"bold"),textvariable=username)
E1.pack(padx=10)

L3=Label(window,text="Password:",font=("Arial",14,"normal"),pady=10)
L3.pack()

E2=Entry(window,font=("Arial",14,"bold"),textvariable=password,show="*")
E2.pack(padx=10)

C1=Checkbutton(window,text="Show/Hide Password",command=showhide_pass,variable=showhide)
C1.pack()

B1=Button(window,text="Login",font=("Arial",16,"bold"),padx=5,pady=5,bg="green",command=login_function)
B1.pack(pady=20)

#B1=Button(window, text="Login", font=("Arial",16,"bold"), bg="#28a745", fg="white", activebackground="#218838", activeforeground="white", relief="flat", bd=0, padx=20, pady=8, cursor="hand2", command=login_function)
#B1.pack()
#B1=ctk.CTkButton(window, text="Login", corner_radius=15, width=120, height=40, fg_color="green", command=login_function)
#B1.pack()

window.mainloop()