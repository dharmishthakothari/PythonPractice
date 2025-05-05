# W.A.P to create all the widgets using Tkinter. 
import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.title("Simple GUI")
lblFname=ttk.Label(root, text='First Name')
lblFname.grid(row=0,column=1)
e1=ttk.Entry(root)
e1.grid(row=0,column=2)

lblLname=ttk.Label(root, text='Last Name')
lblLname.grid(row=1,column=1)
e2=ttk.Entry(root)
e2.grid(row=1,column=2)


lblHobby = ttk.Label(root, text="Select Hobby ")
lblHobby.grid(row=2,column=1)

ival_reading=tk.IntVar()
checkRead=ttk.Checkbutton(root,text="Reading",variable=ival_reading)
checkRead.grid(row=2,column=2)

ival_drawing=tk.IntVar()
checkDraw=ttk.Checkbutton(root,text="Drawing",variable=ival_drawing)
checkDraw.grid(row=2,column=3)

lblGender=ttk.Label(root,text='Gender')
lblGender.grid(row=3,column=1)

gender_val=tk.StringVar(root,"1")
radioFemale=ttk.Radiobutton(root,text="Female",variable=gender_val,value='Female')
radioFemale.grid(row=3,column=2)

radioMale=ttk.Radiobutton(root,text="Male",variable=gender_val,value='Male')
radioMale.grid(row=3,column=3)

lblMonth=ttk.Label(root,text='Select Month')
lblMonth.grid(row=4,column=1)


n = tk.StringVar() 
select_month = ttk.Combobox(root, textvariable = n) 
  
# Adding combobox drop down list 
select_month['values'] = (' January',  
                          ' February', 
                          ' March', 
                          ' April', 
                          ' May', 
                          ' June', 
                          ' July', 
                          ' August', 
                          ' September', 
                          ' October', 
                          ' November', 
                          ' December') 
  
select_month.grid(column = 2, row = 4) 
select_month.current() 


button = ttk.Button(root, text="Click Me")
button.grid(row=5,)

root.mainloop()