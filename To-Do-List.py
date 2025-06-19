from tkinter import *
from tkinter import messagebox

#setting up the window
a=Tk()
a.title("JESUS LOVES YOU")
a.geometry("800x600")

#Building Widgets
l1=Label(a,text="enter your tasks/To-Do")
l1.pack(pady=200)
e1=Entry(a)
e1.pack()
#adding
def add():
    try:
        EN1=e1.get()
        list_var.insert(END,EN1)
    except:
        i="enter something "
        messagebox.showerror("ERROR",i)
#deleting
def delete():
    try:
        selected=list_var.curselection()
        list_var.delete(selected[0])
    except:
        k="enter a valid number"
        messagebox.showerror("ERROR",k)
e2=Entry(a)
e2.pack()
b1=Button(a,text="add",command=add)
b1.pack(pady=20)
b2=Button(a,text="delete",command=delete)
b2.pack()
l2=Label(a,text="enter which task you wanna delete(enter the task number)")
l2.pack()
list_var=Listbox(a)
list_var.pack(pady=400)

a.mainloop()
