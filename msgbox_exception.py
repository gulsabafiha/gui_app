import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as m_box
win=tk.Tk()
win.title('MSG')
label_frame=ttk.LabelFrame(win,text='Contact detail')
label_frame.grid(row=0,column=0,padx=40,pady=10)

name_label=ttk.Label(label_frame,text='Enter your name please: ')
name_label.grid(row=0,column=0,padx=5,pady=5,sticky=tk.W)
age_label=ttk.Label(label_frame,text='Enter your age please: ')
age_label.grid(row=0, column=1,padx=5,pady=5,sticky=tk.W)

name_var=tk.StringVar()
name_entrybox=ttk.Entry(label_frame,width=36,textvariable=name_var)
name_entrybox.grid(row=1,column=0,padx=5,pady=5,sticky=tk.W)
age_var=tk.StringVar()
age_entrybox=ttk.Entry(label_frame,width=36,textvariable=age_var)
age_entrybox.grid(row=1,column=1,padx=5,pady=5,sticky=tk.W)

def submit():
    # m_box.showerror('title','content of this message box !!')
    name=name_var.get()
    age=age_var.get()
    if name=="" or age=="":
        m_box.showerror('Error','please fill both name and age.')
    else:
        try:
            age=int(age)
        except ValueError:
            m_box.showwarning('title','please enter your age in number.')
        else:
            if age<18:
                m_box.showwarning('title','you are not avobe 18,visit this content at your own risk')
            print(f"{name} : {age}")



submit_btn=ttk.Button(win,text="submit",command=submit)
submit_btn.grid(row=2,columnspan=2,padx=40)


win.mainloop()