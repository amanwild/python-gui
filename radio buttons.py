from tkinter import *
from tkinter import messagebox

root  =Tk()

root.geometry('800x600')
root.title("Say My name")
Label(text="What is your name?")

def option():
    print(var.get())
    messagebox.showinfo("Names!!",f"Your name is {var.get()}")
    
var = StringVar()
var.set("Radio")

radio = Radiobutton(root,text="Aman",variable=var,value="AMAN").pack(anchor="w")
radio = Radiobutton(root,text="Samir",variable=var,value="Samir").pack(anchor="w")
radio = Radiobutton(root,text="Rajesh",variable=var,value="Rajesh").pack(anchor="w")
Button(root,text="Submit",pady= 10,command = option).pack()




root.mainloop()
