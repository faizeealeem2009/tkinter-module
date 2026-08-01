from tkinter import *
import csv
from tkinter import messagebox
with open("employees.csv","w",newline="") as f1:
    csvWriter=csv.writer(f1)
    csvWriter.writerow(["First Name","Last Name","City","Gender","Education","Experience","Job Profile","Department","Skill","Basic Salary"])


def submit_data():
    fname=firstname.get()
    lname=lastname.get()
    ct=city.get()
    gd=gender.get()
    ed=education.get()
    exp=experience.get()
    jb=job.get()
    dp=dep.get()
    sk=skill.get()
    bs=basic.get()

    empdata=[fname,lname,ct,gd,ed,exp,jb,dp,sk,bs]
    with open("employees.csv","a",newline="") as f1:
            csvWriter=csv.writer(f1)
            csvWriter.writerow(empdata)
            messagebox.showinfo("New Record","One record added to file!")
root=Tk()
root.title("HR Data Management")
#root.geometry("600x400")
root.resizable(False,False)


firstname=StringVar()
lastname=StringVar()
gender=StringVar()
city=StringVar()
education=StringVar()
experience=StringVar()
job=StringVar()
dep=StringVar()
skill=StringVar()
basic=IntVar()
L1=Label(root,text="HR Data Management",font=("Calibri",20,"bold"))
L1.grid(row=0,column=0,columnspan=2,padx=10,pady=10)

L2=Label(root,text="Enter First Name:",font=("Calibri",14,"normal"))
L2.grid(row=1,column=0,padx=10,pady=10)

L3=Label(root,text="Enter Last Name:",font=("Calibri",14,"normal"))
L3.grid(row=1,column=1,padx=10,pady=10)

E1=Entry(root,font=("Calibri",14,"normal"),textvariable=firstname)
E1.grid(row=2,column=0,padx=10,pady=10)

E2=Entry(root,font=("Calibri",14,"normal"),textvariable=lastname)
E2.grid(row=2,column=1,padx=10,pady=10)

L4=Label(root,text="Select Gender: ",font=("Calibri",16,"bold"))
L4.grid(row=3,column=0,columnspan=2,padx=10,pady=10)

L5=Label(root,text="Male ",font=("Calibri",14,"normal"))
L5.grid(row=4,column=0)

L8=Label(root,text="Female",font=("Calibri",14,"normal"))
L8.grid(row=4,column=1)

R1=Radiobutton(root,value="Male",variable=gender)
R1.grid(row=5,column=0)

R2=Radiobutton(root,value="Female",variable=gender)
R2.grid(row=5,column=1)

L9=Label(root,text="City:",font=("Calibri",14,"normal"))
L9.grid(row=6,column=0,padx=10,pady=10)

L10=Label(root,text="Education:",font=("Calibri",14,"normal"))
L10.grid(row=6,column=1,padx=10,pady=10)

E3=Entry(root,font=("Calibri",14,"normal"),textvariable=city)
E3.grid(row=7,column=0,padx=10,pady=10)

E4=Entry(root,font=("Calibri",14,"normal"),textvariable=education)
E4.grid(row=7,column=1,padx=10,pady=10)

L11=Label(root,text="Experience:",font=("Calibri",14,"normal"))
L11.grid(row=8,column=0,padx=10,pady=10)

L12=Label(root,text="Job Profile:",font=("Calibri",14,"normal"))
L12.grid(row=8,column=1,padx=10,pady=10)

E5=Entry(root,font=("Calibri",14,"normal"),textvariable=experience)
E5.grid(row=9,column=0,padx=10,pady=10)

E6=Entry(root,font=("Calibri",14,"normal"),textvariable=job)
E6.grid(row=9,column=1,padx=10,pady=10)

L11=Label(root,text="Department:",font=("Calibri",14,"normal"))
L11.grid(row=10,column=0,padx=10,pady=10)

L12=Label(root,text="Skills:",font=("Calibri",14,"normal"))
L12.grid(row=10,column=1,padx=10,pady=10)

E7=Entry(root,font=("Calibri",14,"normal"),textvariable=dep)
E7.grid(row=11,column=0,padx=10,pady=10)

E8=Entry(root,font=("Calibri",14,"normal"),textvariable=skill)
E8.grid(row=11,column=1,padx=10,pady=10)

L13=Label(root,text="Enter Basic Salary:",font=("Calibri",14,"normal"))
L13.grid(row=12,column=0,padx=10,pady=10)

E9=Entry(root,font=("Calibri",14,"normal"),textvariable=basic)
E9.grid(row=13,column=0,padx=10,pady=10)

B1=Button(root,text="Submit",command=submit_data,font=("Calibri",14,"bold"),bg="green",padx=50,pady=5)
B1.grid(row=14,column=0,padx=10,pady=10,columnspan=2)


root.mainloop()