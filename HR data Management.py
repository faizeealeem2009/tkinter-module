from tkinter import *
from tkinter import ttk
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
    skill=""
    if skill1.get():
        skill+="Python "
    else:
        pass
    if skill2.get():
        skill+="Excel "
    else:
        pass
    if skill3.get():
        skill+="Graphic Designing "
    else:
        pass
    bs=basic.get()
    
    empdata=[fname,lname,ct,gd,ed,exp,jb,dp,skill,bs]
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

experience=StringVar()
selected=list(range(16))
experience.set(selected[2])


sel_educ=["HSC","B.Com","B.Voc","BCA","B.Sc","M.Sc","B.E","MCA"]
education.set(sel_educ[2])

skill1=BooleanVar()
skill2=BooleanVar()
skill3=BooleanVar()

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

L10=Label(root,text="Select Education:",font=("Calibri",14,"normal"))
L10.grid(row=6,column=1)

E3=Entry(root,font=("Calibri",14,"normal"),textvariable=city)
E3.grid(row=7,column=0,padx=10,pady=10)

E4=ttk.Combobox(root,font=("Calibri",14,"normal"),textvariable=education,values=sel_educ)
E4.grid(row=7,column=1)

L11=Label(root,text="Select Experience:",font=("Calibri",14,"normal"))
L11.grid(row=8,column=0)

L12=Label(root,text="Job Profile:",font=("Calibri",14,"normal"))
L12.grid(row=8,column=1,padx=10,pady=10)

E5=ttk.Combobox(root,font=("Calibri",14,"normal"),textvariable=experience,values=selected)
E5.grid(row=9,column=0)

E6=Entry(root,font=("Calibri",14,"normal"),textvariable=job)
E6.grid(row=9,column=1,padx=10,pady=10)

L11=Label(root,text="Department:",font=("Calibri",14,"normal"))
L11.grid(row=10,column=0,padx=10,pady=10)

L12=Label(root,text="Enter Basic Salary:",font=("Calibri",14,"normal"))
L12.grid(row=10,column=1,padx=10,pady=10)

E7=Entry(root,font=("Calibri",14,"normal"),textvariable=dep)
E7.grid(row=11,column=0,padx=10,pady=10)

E8=Entry(root,font=("Calibri",14,"normal"),textvariable=basic)
E8.grid(row=11,column=1,padx=10,pady=10)

L13=Label(root,text="Select Skills:",font=("Calibri",14,"bold"))
L13.grid(row=12,column=0,columnspan=2)

cb1=Checkbutton(root,text="Python",font=("Calibri",14,"bold"),variable=skill1)
cb1.grid(row=13,column=0)

cb2=Checkbutton(root,text="Excel",font=("Calibri",14,"bold"),variable=skill2)
cb2.grid(row=13,column=1)

cb3=Checkbutton(root,text="Graphic Designing",font=("Calibri",14,"bold"),variable=skill3)
cb3.grid(row=13,column=2)



B1=Button(root,text="Submit",command=submit_data,font=("Calibri",14,"bold"),bg="green",padx=50,pady=5)
B1.grid(row=14,column=0,padx=10,pady=10,columnspan=2)


root.mainloop()