from tkinter import*
root=Tk()
root.geometry("600x600")
root.resizable(0,0)
var=IntVar()
"""r1=Radiobutton(root,text="Male",font=("Arial",15),variable=var,value=1)
r1.pack()
r2=Radiobutton(root,text="Female",font=("Arial",15),variable=var,value=2)
r2.pack()
r3=Radiobutton(root,text="Trans",font=("Arial",15),variable=var,value=3)
r3.pack()"""
c1=Checkbutton(root,text="Hindi")
c1.pack()
c2=Checkbutton(root,text="English")
c2.pack()
c3=Checkbutton(root,text="Sanskrit")
c3.pack()
c4=Checkbutton(root,text="Mathaili")
c4.pack()
c5=Checkbutton(root,text="Bhojpuri")
c5.pack()
c6=Checkbutton(root,text="Bangoli")
c6.pack()
root.mainloop()






