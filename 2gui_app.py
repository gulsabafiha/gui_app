import tkinter as tk
from tkinter import ttk
from csv import DictWriter
import os
win=tk.Tk()
win.title('Loops')

#label block
name_label=ttk.Label(win,text='Enter your name : ')
name_label.grid(row=0,column=0,sticky=tk.W)
email_label=ttk.Label(win,text='Enter your email : ')
email_label.grid(row=1,column=0,sticky=tk.W)
age_label=ttk.Label(win,text='Enter your age : ')
age_label.grid(row=2,column=0,sticky=tk.W)
gender_label=ttk.Label(win,text='Select your gender : ')
gender_label.grid(row=3,column=0,sticky=tk.W)

#entrybox 
name_var=tk.StringVar()
name_entrybox=ttk.Entry(win,width=22,textvariable=name_var)
name_entrybox.grid(row=0,column=1)
email_var=tk.StringVar()
email_entrybox=ttk.Entry(win,width=22,textvariable=email_var)
email_entrybox.grid(row=1,column=1)
age_var=tk.StringVar()
age_entrybox=ttk.Entry(win,width=22,textvariable=age_var)
age_entrybox.grid(row=2,column=1)

gender_var=tk.StringVar()
gender_combobox=ttk.Combobox(win,width=19,textvariable=gender_var)
gender_combobox['values']=('Male','Female','Others')
gender_combobox.current(1)
gender_combobox.grid(row=3,column=1)

typ_var=tk.StringVar()
typ1=ttk.Radiobutton(win,text='student',value='student',variable=typ_var)
typ1.grid(row=4,column=0)
typ2=ttk.Radiobutton(win,text='Teacher',value='teacher',variable=typ_var)
typ2.grid(row=4,column=1)
typ3=ttk.Radiobutton(win,text='Others',value='others',variable=typ_var)
typ3.grid(row=4,column=2)

check_var=tk.IntVar()
check=ttk.Checkbutton(win,text='check if you want to subscribe our website')
check.grid(row=5,columnspan=2)

def l():
    username=name_var.get()
    useremail=email_var.get()
    userage=age_var.get()
    usertype=typ_var.get()
    usergender=gender_var.get()
    print(f"{username} your email is {useremail} and you are {userage} years old. and your are {usergender} ,you are a {usertype}")
    if check_var==0:
        subscribed='No'
    else:
        subscribed='Yes'
    with open('file2.txt','a') as f:
        f.write(f'{username},{userage},{useremail},{usergender},{usertype},{subscribed} /n')
    #write in csv file
    with open('f.csv','a',newline="") as f:
        dict_writer=DictWriter(f,fieldnames=['username','userage','useremail','usergender','usertype','subscribed'])
        if os.stat('f.csv').st_size==0:
            dict_writer.writeheader()
        if check_var.get()==0:
            subscribed='not subscribed'
        else:
            subscribed='yes subscribed'

        dict_writer.writerow({
            'username': username,
            'userage' : userage,
            'useremail':useremail,
            'usergender':usergender,
            'usertype':usertype,
            'subscribed': subscribed
        })


    name_entrybox.delete(0,tk.END)
    email_entrybox.delete(0,tk.END)
    age_entrybox.delete(0,tk.END)

    name_label.configure(foreground='blue')
    age_label.configure(foreground='purple')
    email_label.configure(foreground='orange')
    


submit=ttk.Button(win,text='Submit',command=l)
submit.grid(row=6,column=0)



win.mainloop()
