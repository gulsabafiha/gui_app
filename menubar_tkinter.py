import tkinter as tk
from tkinter import ttk
win=tk.Tk()
win.title('Menubar tutorial')
def func():
    print('funtion has been called')

#*******simple menubar*******
# menubar=tk.Menu(win)
# menubar.add_command(label='save',command=func)
# menubar.add_command(label='save As', command=func)
# menubar.add_command(label='Copy',command=func)

#dropdown menubar
main_menu=tk.Menu(win)
file_menu=tk.Menu(main_menu,tearoff=0)
edit_menu=tk.Menu(main_menu,tearoff=0)

file_menu.add_command(label='New File',command=func)
file_menu.add_command(label='New Window',command=func)
file_menu.add_separator()
file_menu.add_command(label='Save  File',command=func)
file_menu.add_command(label='Open File',command=func)

edit_menu.add_command(label='Undo',command=func)
edit_menu.add_command(label='Redo',command=func)

main_menu.add_cascade(label='File',menu=file_menu)
main_menu.add_cascade(label='Edit',menu=edit_menu)

win.config(menu=main_menu)



win.mainloop()