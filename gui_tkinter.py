#python tkinter tutorial

#starter code for tkinter
# 1.
# import tkinter
# win=tkinter.Tk()
# 2.
# from tkinter import *
# win=Tk()
# 3.
import tkinter as tk
from tkinter import ttk #for creting buttons,lebels etc
from csv import DictWriter
import os
win=tk.Tk()
win.title('GUI')
#create lebel
name_label=ttk.Label(win,text='Enter your name : ')
name_label.grid(row=0,column=0,sticky=tk.W)

email_label=ttk.Label(win,text='Enter your Email : ')
email_label.grid(row=1,column=0,sticky=tk.W)

age_label=ttk.Label(win,text='Enter your age : ')
age_label.grid(row=2,column=0,sticky=tk.W)

gender_label=ttk.Label(win,text='Select your gender: ')
gender_label.grid(row=3,column=0,sticky=tk.W)

#entry box
name_var=tk.StringVar()
name_entrybox=ttk.Entry(win,width=22,textvariable=name_var)
name_entrybox.grid(row=0,column=1)
name_entrybox.focus()

email_var=tk.StringVar()
email_enterybox=ttk.Entry(win,width=22, textvariable=email_var)
email_enterybox.grid(row=1,column=1)

age_var=tk.StringVar()
age_entrybox=ttk.Entry(win,width=22,textvariable=age_var)
age_entrybox.grid(row=2,column=1)

#create combobox
gender_var=tk.StringVar()  
gender_combobox=ttk.Combobox(win,width=19,textvariable=gender_var,state='readonly')
gender_combobox['values']=('Male','Female','Others')
gender_combobox.current(0)
gender_combobox.grid(row=3,column=1)
#radio button
usertyp=tk.StringVar()
radiobtn1=ttk.Radiobutton(win,text='student',value='student',variable=usertyp)
radiobtn1.grid(row=4,column=0)

radiobtn2=ttk.Radiobutton(win,text='Teacher',value='teacher',variable=usertyp)
radiobtn2.grid(row=4,column=1)

radiobtn3=ttk.Radiobutton(win,text='Others',value='Others',variable=usertyp)
radiobtn3.grid(row=4,column=2)

#check button
check_var=tk.IntVar()
check1=ttk.Checkbutton(win,text='check if you want to subscribe to our newletter', variable=check_var)
check1.grid(row=5,columnspan=2)
#create buttons
def action():
    username=name_var.get()
    useremail=email_var.get()
    userage=age_var.get()
    print(f'{username} is {userage} years old, your email is {useremail}')
    usergender=gender_var.get()
    usertype=usertyp.get()
    if check_var.get()==0:
        subscribed='No'
    else:
        subscribed='Yes'
    print(usergender,usertype,subscribed)
    with open('file.txt','a') as f:
        f.write(f"{username},{userage},{useremail},{usergender},{usertype},{subscribed}/n")

    name_entrybox.delete(0,tk.END)
    age_entrybox.delete(0,tk.END)
    email_enterybox.delete(0,tk.END)

    name_label.configure(foreground='blue')
    age_label.configure(foreground='blue')
    email_label.configure(foreground='blue')

#write csv files
def action():
    username=name_var.get()
    useremail=email_var.get()
    userage=age_var.get()
    usergender=gender_var.get()
    usertype=usertyp.get()
    if check_var.get()==0:
        subscribed='No'
    else:
        subscribed='Yes'

        #write csv file
    with open('file.csv','a',newline="") as f:
        dict_writer=DictWriter(f,fieldnames=['userName','User Email address','user Age','user Type','Usergender','subscribe'])
        if os.stat('file.csv').st_size==0:
            dict_writer.writeheader()
            
        dict_writer.writerow(
            {
                'userName': username,
                'User Email address':useremail,
                'user Age' : userage,
                'user Type' : usertype,
                'Usergender' : usergender,
                'subscribe' : subscribed
            }
        )
    name_entrybox.delete(0,tk.END)
    age_entrybox.delete(0,tk.END)
    email_enterybox.delete(0,tk.END)
 

submit_button=ttk.Button(win,text='submit',command=action)
submit_button.grid(row=6,column=0)

win.mainloop()