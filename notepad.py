from cgitb import text
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import os
def newfile():
    global file
    root.title("Untitle - Notepad")
    file = None
    Textarea.delete(1.0,END)
def openfile():
    global file
    file = filedialog.askopenfilename(defaultextension=".txt",filetypes= [("All Files","*.*"),("Text Document","*.txt")])  
    if file =="":
        file =None
    else:
        root.title(os.path.basename(file)+"  - Notepad")
        Textarea.delete(1.0,END)
        f =open(file,"r")
        Textarea.insert(1.0,f.read())
        f.close()
def savefile():
    global file
    if file == None:
        file = filedialog.asksaveasfilename(initialfile='untitled.text',defaultextension=".txt",filetypes= [("All Files","*.*"),("Text Document","*.txt")])
        if file =="":
            file = None
        else:
            f = open(file,"w")
            f.write(Textarea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file)+" - Notepad")
            print("file saved")
    else:  
        f = open(file,"w")
        f.write(Textarea.get(1.0,END))
        f.close()
        
def quitapp():
    root.destroy()
def cutfile():
    
    Textarea.event_generate(("<<Cut>>"))

def copyfile():
    Textarea.event_generate(("<<Copy>>"))

def pastefile():
    Textarea.event_generate(("<<Paste>>"))

def aboutfile():
    messagebox.showinfo("about","This is a notepad")
def helpfile():
    pass


root = Tk()
root.geometry('800x600')
root.title("Untitled-Notebook")

Textarea = Text(root,font="lucida 13")
file = None
Textarea.pack(expand = True,fill = BOTH)

scrollbar = Scrollbar(Textarea)
scrollbar.pack(side = "right",fill = Y)
scrollbar.config(command=Textarea.yview)
Textarea.config(yscrollcommand= scrollbar.set)

Menubar = Menu(root)
fileMenu = Menu(Menubar,tearoff=0)
fileMenu.add_command(label = "New",command=newfile) 
fileMenu.add_command(label = "Open",command=openfile) 
fileMenu.add_command(label = "Save",command=savefile) 
fileMenu.add_separator()
fileMenu.add_command(label = "Exit",command=quitapp) 
Menubar.add_cascade(label="File",menu =fileMenu )


editMenu = Menu(Menubar,tearoff=0)
editMenu.add_command(label = "cut",command=cutfile) 
editMenu.add_command(label = "copy",command=copyfile) 
editMenu.add_command(label = "paste",command=pastefile) 
editMenu.add_separator()
editMenu.add_command(label = "Exit",command=quitapp) 
Menubar.add_cascade(label="Edit",menu =editMenu )


helpMenu = Menu(Menubar,tearoff=0)
helpMenu.add_command(label = "About",command=aboutfile) 
helpMenu.add_command(label = "help",command=helpfile) 
helpMenu.add_separator()
helpMenu.add_command(label = "Exit",command=quitapp) 
Menubar.add_cascade(label="Help",menu =helpMenu )

root.config(menu= Menubar)

root.mainloop()
 
 