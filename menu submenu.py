from tkinter import *

root = Tk()
root.geometry('800x600')
root.title("python GUI")

def myfunc():
    print("hello aman sahu, welcom to python GUI")
# #non dropdown commands
# menubar = Menu(root)
# menubar.add_command(label = "file" ,command= myfunc )
# menubar.add_command(label = "Edit" ,command= myfunc )
# menubar.add_command(label = "View" 0,command= myfunc )
# root.config(menu =menubar)


menubar = Menu(root)

m1 = Menu(menubar)
m1.add_command(label = "open project " ,command= myfunc)
m1.add_command(label = "Edit project" ,command= myfunc)
m1.add_command(label = "View project" ,command= myfunc)
root.config(menu= menubar)
menubar.add_cascade(label = "file" , menu= m1)

m2 = Menu(menubar,tearoff= 0)
m2.add_command(label = "open book " ,command= myfunc)
m2.add_command(label = "Edit book" ,command= myfunc)
m2.add_command(label = "View book" ,command= myfunc)
root.config(menu= menubar)
menubar.add_cascade(label = "book" , menu= m2)

m2 = Menu(menubar,tearoff= 0)
m2.add_command(label = "open book " ,command= myfunc)
m2.add_command(label = "Edit book" ,command= myfunc)
m2.add_command(label = "View book" ,command= myfunc)
root.config(menu= menubar)
menubar.add_cascade(label = "book" , menu= m2)

m3 = Menu(menubar,tearoff= 0)
m3.add_command(label = "open book " ,command= myfunc)
m3.add_command(label = "Edit book" ,command= myfunc)
m3.add_command(label = "View book" ,command= myfunc)
root.config(menu= menubar)
menubar.add_cascade(label = "book" , menu= m3)

m4 = Menu(menubar,tearoff= 0)
m4.add_command(label = "open book " ,command= myfunc)
m4.add_command(label = "Edit book" ,command= myfunc)
m4.add_command(label = "View book" ,command= myfunc)
root.config(menu= menubar)
menubar.add_cascade(label = "book" , menu= m4)

m5 = Menu(menubar,tearoff= 0)
m5.add_command(label = "open book " ,command= myfunc)
m5.add_command(label = "Edit book" ,command= myfunc)
m5.add_command(label = "View book" ,command= myfunc)
root.config(menu= menubar)
menubar.add_cascade(label = "book" , menu= m5)

root.mainloop()