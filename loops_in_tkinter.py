import tkinter as tk
from tkinter import ttk
win=tk.Tk()
win.title('Loop')
label=['what is your name: ','what is your age: ','what is your gender: ','country: ','state :','City :']
for i in range(len(label)):
    cur_label='label'+ str(i)
    cur_label=ttk.Label(win,text=label[i])
    cur_label.grid(row=i,column=0,sticky=tk.W)

#entrybox
name_var=tk.StringVar()
user_info={
    'name':tk.StringVar(), 
    'age':tk.StringVar(),
    'gender':tk.StringVar(),
    'country':tk.StringVar(),
    'state':tk.StringVar(),
    'city':tk.StringVar()
}
counter=0
for i in user_info:
    cur_entrybox='entrybox'+ str(i)
    cur_entrybox=ttk.Entry(win,width=22,textvariable=user_info[i])
    cur_entrybox.grid(row=counter,column=1)
    counter+=1
def l():
    print(user_info('name').get())
    print(user_info('age').get())
    print(user_info('gender').get())
    print(user_info('country').get())
    print(user_info('state').get())
    print(user_info('city').get())
    
submit=ttk.Button(win,text='submit',command=l)
submit.grid(row=7,columnspan=2)


win.mainloop()