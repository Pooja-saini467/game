from tkinter import*
root=Tk()
root.geometry("300x300")
root.resizable(0,0)
l1=Label(root,text="Enter Name",font=("Arial",20))
e1=Entry(root,font=("Arial",20),fg="black")
l1.pack()
e1.pack()
root.mainloop()
