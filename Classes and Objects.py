# from curses import window
from tkinter import *
from tkinter import messagebox

from setuptools import Command
class GUI(Tk):
    def __inti__(self):
        super().__init__()
        self.geometry("800x600")
        self.title("Hello World")
        
    def mystatus(self):
        self.var = StringVar()
        self.var.set("Ready")
        self.statusbar = Label(self,textvar = self.var,relief=SUNKEN,anchor="w")
        self.statusbar.pack(side =BOTTOM,fill=X)        
    def createbtn(self,inpute):
        Button(self,text=input,command=self.click).pack()
    
    def HW(self):
        messagebox.showinfo("Hello World","Welcome to the World")
    def button(self):
        self.label = Button(self,text="Submit",relief=SUNKEN,  command = self.HW )
        self.label.pack()
        
if __name__=='__main__':
    window = GUI()
    window.mystatus()
    window.button()
    window.mainloop()