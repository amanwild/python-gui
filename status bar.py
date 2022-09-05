# from lib2to3.refactor import _BottomMatcher
from tkinter import *
root = Tk()

root.geometry('800x600')
root.title("Status bar")

def updt():
    status.set("Busy...")
    label.update()
    import time
    time.sleep(1)
    status.set("Ready Now")
    label.update()
    time.sleep(1)
    status.set("Busy...")
    label.update()
    time.sleep(1)
    status.set("Ready Now")
    label.update()
    time.sleep(1)
    status.set("Busy...")
    label.update()
    time.sleep(1)
    status.set("Ready Now")
    label.update()
    time.sleep(1)
    status.set("Busy...")
    label.update()
    time.sleep(1)
    status.set("Ready Now")
    label.update()

status = StringVar()
status.set("Ready")
label = Label(root,textvariable=status,relief=SUNKEN,anchor="w")
label.pack(side = BOTTOM,fill  = X)
Button(root, text="upadate",command=updt).pack()


root.mainloop()