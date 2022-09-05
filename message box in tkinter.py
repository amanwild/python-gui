from tkinter import *
from tkinter import messagebox as mb


root = Tk()
root.geometry('800x600')
root.title("message box practice")

def ask():
    print("ask a Quetions?")
    a= mb.showinfo("what?","bol kya problem h")
    
mainmenu = Menu(root)
m1 = Menu(mainmenu,tearoff= 0)
m1.add_command(label="open",command= ask)
m1.add_command(label="close",command= ask)
m1.add_separator()
m1.add_command(label="read",command= ask)
m1.add_command(label="write",command= ask)
root.config(menu=mainmenu)
mainmenu.add_cascade(label = ("file"),menu=m1)

m2 = Menu(mainmenu,tearoff= 0)
m2.add_command(label="open",command= ask)
m2.add_command(label="close",command= ask)
m2.add_separator()
m2.add_command(label="read",command= ask)
m2.add_command(label="write",command= ask)
root.config(menu=mainmenu)
mainmenu.add_cascade(label = ("file"),menu=m2)
root.mainloop()

