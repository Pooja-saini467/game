from tkinter import*
root=Tk()
root.geometry("600x600")
root.resizable(0,0)
var=IntVar()
r1=Radiobutton(root,text="Male",font=("Arial",15),variable=var,value=1)
r1.pack()
r2=Radiobutton(root,text="Female",font=("Arial",15),variable=var,value=2)
r2.pack()
r3=Radiobutton(root,text="Trans",font=("Arial",15),variable=var,value=3)
r3.pack()
