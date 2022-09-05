
from tkinter import *
from tkinter import messagebox

root  = Tk()
root.geometry('800x600')
root.title("Scale practice")

def rate():
    print(f"Your rating is {S1.get()}")
    messagebox.showinfo("Rating !!!",f"Your rating is {S1.get()}")


Label(root,text= "Welcome to my GUI ").pack()
Label(root,text= "Please Rate owr GUI ").pack()
S1 = Scale(root, from_=10 ,to = 100,orient=HORIZONTAL,width=20,length=500,tickinterval=5)
S1.pack()

Button(root,text= "Submit", command= rate,pady = 10).pack()


root.mainloop()


