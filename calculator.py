from tkinter import*
root=Tk()
root.geometry("600x600")
root.resizable(0,0)
x=DoubleVar()
y=DoubleVar()
z=DoubleVar()
e1=Entry(root,font=("Arial",20),textvariable=x)
"""e1.grid(row=0,column=1,pady=25)"""
e1.pack()
e2=Entry(root,font=("Arial",20),textvariable=y)
e2.pack()
def add():
    a=x.get()
    b=y.get()
    c=a+b
    z.set(c)
def minus():
    a=x.get()
    b=y.get()
    c=a-b
    z.set(c)
def multiply():
    a=x.get()
    b=y.get()
    c=a*b
    z.set(c)
b1=Button(root,text="+",font=("Arial",20),command=add)
b1.pack()
"""b1.grid(row=3,column=1,columnspan=2)"""
b2=Button(root,text="-",font=("Arial",20),command=minus)
b2.pack()
b3=Button(root,text="*",font=("Arial",20),command=multiply)
b3.pack()
e3=Entry(root,font=("Arial",20),textvariable=z)
e3.pack()
root.mainloop()

