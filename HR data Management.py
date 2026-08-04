from tkinter import *
from tkinter import ttk
import csv
from tkinter import messagebox
''' 
with open("employees.csv","w",newline="") as f1:
    writer=csv.writer(f1)
    writer.writerow(["First Name","Last Name","Gender","City","Education","Experience","Job Profile","Department","Basic Salary","Skills","Gross Salary","Allowances","Tax","Net Salary"])
    f1.close()
'''

def submit_data():
    basic_salary_value=int(salary.get())
    allowances=basic_salary_value*0.2
    gross_salary=(allowances + basic_salary_value)*12
    if gross_salary >= 1200000:
        tax=gross_salary*0.1
    elif gross_salary >= 800000:
        tax=gross_salary*0.08
    elif gross_salary >= 600000:
        tax=gross_salary*0.06
    elif gross_salary >= 400000:
        tax=gross_salary*0.04
    else:
        tax=0
    net_salary=gross_salary - tax
    selected_skill=[]
    if skill1.get():
        selected_skill.append("Python")
    if skill2.get():
        selected_skill.append("Excel")
    if skill3.get():
        selected_skill.append("Graphic Designing")

    with open("employees.csv","a",newline="") as csvfile:
        writer=csv.writer(csvfile)
        writer.writerow([
            firstname.get(),
            lastname.get(),
            gender.get(),
            city.get(),
            education.get(),
            experience.get(),
            job.get(),
            dep.get(),
            basic_salary_value,
            selected_skill,
            gross_salary,
            allowances,
            tax,
            net_salary,
        ])
        csvfile.close()
    messagebox.showinfo("Success","Employee data submitted successfully.")

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
salary=StringVar()

experience=StringVar()
select_exp=list(range(16))
experience.set(select_exp[2])


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

E5=ttk.Combobox(root,font=("Calibri",14,"normal"),textvariable=experience,values=select_exp)
E5.grid(row=9,column=0)

E6=Entry(root,font=("Calibri",14,"normal"),textvariable=job)
E6.grid(row=9,column=1,padx=10,pady=10)

L11=Label(root,text="Department:",font=("Calibri",14,"normal"))
L11.grid(row=10,column=0,padx=10,pady=10)

L12=Label(root,text="Enter Basic Salary:",font=("Calibri",14,"normal"))
L12.grid(row=10,column=1,padx=10,pady=10)

E7=Entry(root,font=("Calibri",14,"normal"),textvariable=dep)
E7.grid(row=11,column=0,padx=10,pady=10)

E8=Entry(root,font=("Calibri",14,"normal"),textvariable=salary)
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