from tkinter import *
from tkinter import messagebox
import csv
'''
with open("register.csv","w",newline="") as f1:
    csvWriter=csv.writer(f1)
    csvWriter.writerow(["First Name","Last Name","Address","City","Gender","Hobbies","Password"])

'''
def submit_data():
    if fname.get()=="" or lname.get()=="" or address.get()=="" or city.get()=="" or passvalue1.get()=="" or passvalue2.get()=="":
        messagebox.showerror("Invalid or missing Input","Please Enter All the values!")
    elif passvalue1.get()!=passvalue2.get():
        messagebox.showwarning("Password Warning","Password Does not Match!")
    else:
        firstname=fname.get()
        lastname=lname.get()
        add=address.get()
        ct=city.get()
        gd=gender.get()
        hobbies=""
        if cricket.get():
            hobbies+="Cricket "
        else:
            pass

        if Football.get():
            hobbies+="Football "
        else:
            pass

        if chess.get():
            hobbies+="Chess "
        else:
            pass

        passwd=passvalue1.get()

        regdata=[firstname,lastname,gd,add,ct,hobbies,passwd]

        with open("register.csv","a",newline="") as f1:
            csvWriter=csv.writer(f1)
            csvWriter.writerow(regdata)
            messagebox.showinfo("New Record","One record added to file!")
            E1.delete(0,END)
            E2.delete(0,END)
            E3.delete(0,END)
            E4.delete(0,END)
            E5.delete(0,END)
            E6.delete(0,END)

def showhidepass1():
    if mypass1.get():
        E5.config(show="")
    else:
        E5.config(show="*")

def showhidepass2():
    if mypass2.get():
        E6.config(show="")
    else:
        E6.config(show="*")
root=Tk()
root.title("Student Regestration Form")
#root.geometry("600x400")
root.resizable(False,False)

gender=StringVar()
mypass1=BooleanVar()
mypass2=BooleanVar()
fname=StringVar()
lname=StringVar()
address=StringVar()
city=StringVar()
cricket=BooleanVar()
Football=BooleanVar()
chess=BooleanVar()
passvalue1=StringVar()
passvalue2=StringVar()

L1=Label(root,text="Student Regestration Form",font=("Calibri",20,"bold"))
L1.grid(row=0,column=0,columnspan=2,padx=10,pady=10)

L2=Label(root,text="Enter First Name:",font=("Calibri",14,"normal"))
L2.grid(row=1,column=0,padx=10,pady=10)

L3=Label(root,text="Enter Last Name:",font=("Calibri",14,"normal"))
L3.grid(row=1,column=1,padx=10,pady=10)

E1=Entry(root,font=("Calibri",14,"normal"),textvariable=fname)
E1.grid(row=2,column=0,padx=10,pady=10)

E2=Entry(root,font=("Calibri",14,"normal"),textvariable=lname)
E2.grid(row=2,column=1,padx=10,pady=10)

L4=Label(root,text="Enter Address: ",font=("Calibri",14,"normal"))
L4.grid(row=3,column=0,padx=10,pady=10)

L5=Label(root,text="Enter City Name:",font=("Calibri",14,"normal"))
L5.grid(row=3,column=1,padx=10,pady=10)

E3=Entry(root,font=("Calibri",14,"normal"),textvariable=address)
E3.grid(row=4,column=0,padx=10,pady=10)

E4=Entry(root,font=("Calibri",14,"normal"),textvariable=city)
E4.grid(row=4,column=1,padx=10,pady=10)

L6=Label(root,text="Select Gender: ",font=("Calibri",16,"bold"))
L6.grid(row=5,column=0,columnspan=2,padx=10,pady=10)

L7=Label(root,text="Male ",font=("Calibri",14,"normal"))
L7.grid(row=6,column=0)

L8=Label(root,text="Female",font=("Calibri",14,"normal"))
L8.grid(row=6,column=1)

R1=Radiobutton(root,value="Male",variable=gender)
R1.grid(row=7,column=0)

R2=Radiobutton(root,value="Female",variable=gender)
R2.grid(row=7,column=1)

L9=Label(root,text="Select Hobbies:",font=("Calibri",16,"bold"))
L9.grid(row=8,column=0,columnspan=2)

C1=Checkbutton(root,text="Cricket",font=("Calibri",14,"bold"),variable=cricket)
C1.grid(row=9,column=0)

C2=Checkbutton(root,text="Football",font=("Calibri",14,"bold"),variable=Football)
C2.grid(row=10,column=0)

C3=Checkbutton(root,text="Chess",font=("Calibri",14,"bold"),variable=chess)
C3.grid(row=11,column=0)

L10=Label(root,text="Type password: ",font=("Calibri",16,"bold"))
L10.grid(row=12,column=0,columnspan=2)

E5=Entry(root,font=("Calibri",14,"normal"),show="*",textvariable=passvalue1)
E5.grid(row=13,column=0,padx=10,pady=10)

C4=Checkbutton(root,text="Show/Hide Password",variable=mypass1,font=("Calibri",14,"bold"),command=showhidepass1)
C4.grid(row=13,column=1)

L11=Label(root,text="Verify password: ",font=("Calibri",16,"bold"))
L11.grid(row=14,column=0,columnspan=2)

E6=Entry(root,font=("Calibri",14,"normal"),show="*",textvariable=passvalue2)
E6.grid(row=15,column=0,padx=10,pady=10)

C5=Checkbutton(root,text="Show/Hide Password",variable=mypass2,font=("Calibri",14,"bold"),command=showhidepass2)
C5.grid(row=15,column=1)

B1=Button(root,text="Submit",command=submit_data,font=("Calibri",14,"bold"),bg="green",padx=50,pady=5)
B1.grid(row=16,column=0,padx=10,pady=10,columnspan=2)

root.mainloop()
