from tkinter import *

def submit_data():
    pass


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

<<<<<<< HEAD
L9=Label(root,text="Select Hobbies:",font=("Calibri",16,"bold"))
L9.grid(row=8,column=0,columnspan=2)

C1=Checkbutton(root,text="Cricket",font=("Calibri",14,"bold"))
C1.grid(row=9,column=0)

C2=Checkbutton(root,text="Football",font=("Calibri",14,"bold"))
C2.grid(row=10,column=0)

C3=Checkbutton(root,text="Chess",font=("Calibri",14,"bold"))
C3.grid(row=11,column=0)

L10=Label(root,text="Type password: ",font=("Calibri",16,"bold"))
L10.grid(row=12,column=0,columnspan=2)

E5=Entry(root,font=("Calibri",14,"normal"),show="*")
E5.grid(row=13,column=0,padx=10,pady=10,columnspan=2)

L11=Label(root,text="Verify password: ",font=("Calibri",16,"bold"))
L11.grid(row=14,column=0,columnspan=2)

E6=Entry(root,font=("Calibri",14,"normal"),show="*")
E6.grid(row=15,column=0,padx=10,pady=10,columnspan=2)

B1=Button(root,text="Submit",command=submit_data,font=("Calibri",14,"bold"),padx=50,pady=5)
B1.grid(row=16,column=0,padx=10,pady=10,columnspan=2)

=======
L9=Label(root,text="Select Hobbies",font=("Calibri",16,"bold"))
L9.grid(row=8,column=0,columnspan=2)
>>>>>>> becd704d657258786d5a22b7005a43f2eb316fab
root.mainloop()