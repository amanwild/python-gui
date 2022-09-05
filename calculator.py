from multiprocessing.sharedctypes import Value
from tkinter import * 
def click(event):
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value= eval(screen.get())
            except Exception as e:
                print(e)
                value = "Error"
        scvalue.set(value)
        screen.update()
    elif text == "C":
        scvalue.set("")
        screen.update
    else:
        scvalue.set(scvalue.get()  +text)
        screen.update()
    
root = Tk()
root.geometry("800x600")
root.title("My Calculator")

    
scvalue = StringVar()
scvalue.set("")
screen = Entry(root,textvar = scvalue,font = "lucida 30 bold")
screen.pack(fill=X,padx = 5,pady = 5,ipadx=20)


f= Frame(root,)
b= Button(f,text="7",font = "lucida 19 bold",padx=45,pady=5 )
b.pack(side=LEFT ,padx = 5,pady = 5)
b.bind("<Button-1>",click)
b= Button(f,text="8",font = "lucida 19 bold",padx=45,pady=5 )
b.pack(side=LEFT ,padx = 5,pady = 5)
b.bind("<Button-1>",click)
b= Button(f,text="9",font = "lucida 19 bold",padx=45,pady=5 )
b.pack(side=LEFT ,padx = 5,pady = 5)
b.bind("<Button-1>",click)
f.pack()




f= Frame(root,)
b= Button(f,text="4",font = "lucida 19 bold",padx=45,pady=5 )
b.pack(side=LEFT ,padx = 5,pady = 5)
b.bind("<Button-1>",click)
b= Button(f,text="5",font = "lucida 19 bold",padx=45,pady=5 )
b.pack(side=LEFT ,padx = 5,pady = 5)
b.bind("<Button-1>",click)
b= Button(f,text="6",font = "lucida 19 bold",padx=45,pady=5 )
b.pack(side=LEFT ,padx = 5,pady = 5)
b.bind("<Button-1>",click)
f.pack()
f= Frame(root,)
b= Button(f,text="1",font = "lucida 19 bold",padx=45,pady=5 )
b.pack(side=LEFT ,padx = 5,pady = 5)
b.bind("<Button-1>",click)
b= Button(f,text="2",font = "lucida 19 bold",padx=45,pady=5 )
b.pack(side=LEFT ,padx = 5,pady = 5)
b.bind("<Button-1>",click)
b= Button(f,text="3",font = "lucida 19 bold",padx=45,pady=5 )
b.pack(side=LEFT ,padx = 5,pady = 5)
b.bind("<Button-1>",click)
f.pack()
f= Frame(root,)
b= Button(f,text="C",font = "lucida 19 bold",padx=45,pady=5 )
b.pack(side=LEFT ,padx = 5,pady = 5)
b.bind("<Button-1>",click)
b= Button(f,text="0",font = "lucida 19 bold",padx=45,pady=5 )
b.pack(side=LEFT ,padx = 5,pady = 5)
b.bind("<Button-1>",click)
b= Button(f,text=".",font = "lucida 19 bold",padx=45,pady=5 )
b.pack(side=LEFT ,padx = 5,pady = 5)
b.bind("<Button-1>",click)
f.pack()
f= Frame(root,)
b= Button(f,text="-",font = "lucida 19 bold",padx=45,pady=5 )
b.pack(side=LEFT ,padx = 5,pady = 5)
b.bind("<Button-1>",click)
b= Button(f,text="+",font = "lucida 19 bold",padx=45,pady=5 )
b.pack(side=LEFT ,padx = 5,pady = 5)
b.bind("<Button-1>",click)
b= Button(f,text="=",font = "lucida 19 bold",padx=45,pady=5 )
b.pack(side=LEFT ,padx = 5,pady = 5)
b.bind("<Button-1>",click)
f.pack()
root.mainloop()