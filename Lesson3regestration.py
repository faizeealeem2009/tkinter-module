from tkinter import *

root=Tk()
root.title("Student Regestration Form")
#root.geometry("600x400")
root.resizable(False,False)

gender=StringVar()


L1=Label(root,text="Student Regestration Form",font=("Calibri",20,"bold"))
L1.grid(row=0,column=0,columnspan=2,padx=10,pady=10)

L2=Label(root,text="Enter First Name:",font=("Calibri",14,"normal"))
L2.grid(row=1,column=0,padx=10,pady=10)

L3=Label(root,text="Enter Last Name:",font=("Calibri",14,"normal"))
L3.grid(row=1,column=1,padx=10,pady=10)

E1=Entry(root,font=("Calibri",14,"normal"))
E1.grid(row=2,column=0,padx=10,pady=10)

E2=Entry(root,font=("Calibri",14,"normal"))
E2.grid(row=2,column=1,padx=10,pady=10)

L4=Label(root,text="Enter Address: ",font=("Calibri",14,"normal"))
L4.grid(row=3,column=0,padx=10,pady=10)

L5=Label(root,text="Enter City Name:",font=("Calibri",14,"normal"))
L5.grid(row=3,column=1,padx=10,pady=10)

E3=Entry(root,font=("Calibri",14,"normal"))
E3.grid(row=4,column=0,padx=10,pady=10)

E4=Entry(root,font=("Calibri",14,"normal"))
E4.grid(row=4,column=1,padx=10,pady=10)

L6=Label(root,text="Select Gender: ",font=("Calibri",16,"bold"))
L6.grid(row=5,column=0,columnspan=2,padx=10,pady=10)

L7=Label(root,text="Male ",font=("Calibri",14,"normal"))
L7.grid(row=6,column=0)

L8=Label(root,text="Female",font=("Calibri",14,"normal"))
L8.grid(row=6,column=1)

R1=Radiobutton(root,value="Male",textvariable=gender)
R1.grid(row=7,column=0)

R2=Radiobutton(root,value="Female",textvariable=gender)
R2.grid(row=7,column=1)


root.mainloop()