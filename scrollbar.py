from tkinter import *
root = Tk()

root.geometry('800x600')
root.title("scrollbar practice")

scrollbar = Scrollbar(root)
scrollbar.pack(side= RIGHT,fill =Y,padx=10)

list = Listbox(root,yscrollcommand=scrollbar.set)

for i in range(100):
    list.insert(END,i)
list.pack()
scrollbar.config(command=list.yview)

root.mainloop()