from tkinter import*
import random
import time
import datetime
from tkinter import messagebox


root=Tk()
root.geometery("1400x1400+0+0")
root.title("Restaurant Management System")
root.configure(background='black')



heading=Frame(root,width=1350,height=100,relief="raise",bd=14)
heading.pack(side=TOP)
heading=Label(heading,font=('aria',62,'bold'),text="Restaurnt Mangement System")
heading.grid(row=0,column=0)


bottomframe=Frame(root,width=1350,height=100,bd=14,relief="raise")
bottomframe.pack(side=BOTTOM)


frame1=Frame(bottomframe, width=300, height=550, bd=14, relief="raise")
frame1.pack(side=LEFT)


frame2=Frame(bottomframe, width=300, height=550, bd=14, relief="raise")
frame2.pack(side=LEFT)


frame3=Frame(bottomframe, width=300, height=550, bd=14, relief="raise")
frame3.pack(side=LEFT)


frame4=Frame(bottomframe, width=300, height=550, bd=14, relief="raise")
frame4.pack(side=RIGHT)




def qExit ():
    qExit =messagebox.askyesno("Quit System","Do you want to exit?")

    if (qExit>0):
        root.destroy ()
        return

btnExit=Button(frame3,padx=25,pady=15,bd=10,fg="black",font=('arial'))



def qReset ():
    PaidTax.set("")
    SubTotal.set("")
    TotalCost.set("")
    CostOfBeverages.set("")
    CostOfFoods.set("")
    ServiceCharge.set("")
    txtReceipt.delete("1.0",END)



    E_Burger.set("0")
    E_Pizza.set("0")
    E_Sandwich.set("0")
    E_Salad.set("0")


    E_Coffee.set("0")
    E_Tea.set("0")
    E_Mojita.set("0")
    E_Shake.set("0")


    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)


    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)

    txtBurger.configure(State="disabled")
    txtPizza.configure(State="disabled")
    txtSandwich.configure(State="disabled")
    txtSalad.configure(State="disabled")
   

    txtCoffee.configure(State="disabled")
    txtTea.configure(State="disabled")
    txtMojita.configure(State="disabled")
    txtShake.configure(State="disabled")


btnReset=Button(frame3,padx=15,pady=15,bd=10,fg="black",font=('arial'))


def checkButton ():
    if(var1.get () ==1):
        txtBurger.configure(state = "normal")
    elif(var1.get ()==0):
        txtBurger.configure(state = "disabled")
        E_Burger.set("0")


    if(var2.get () ==1):
        txtPizza.configure(state = "normal")
    elif(var2.get ()==0):
        txtPizza.configure(state = "disabled")
        E_Pizza.set("0")



    if(var3.get () ==1):
        txtSandwich.configure(state = "normal")
    elif(var3.get ()==0):
        txtSandwich.configure(state = "disabled")
        E_Sandwich.set("0")


    if(var4.get () ==1): 
        txtSalad.configure(state = "normal")
    elif(var4.get ()==0):
        txtSalad.configure(state = "disabled")
        E_Salad.set("0")


    if(var5.get () ==1):
        txtCoffee.configure(state = "normal")
    elif(var5.get ()==0):
        txtCoffee.configure(state = "disabled")
        E_Coffee.set("0")


    if(var6.get () ==1):
        txtTea.configure(state = "normal")
    elif(var6.get ()==0):
        txtTea.configure(state = "disabled")
        E_Tea.set("0")


    if(var7.get () ==1):
        txtMojita.configure(state = "normal")
    elif(var7.get ()==0):
        txtMojita.configure(state = "disabled")
        E_Mojita.set("0")

    if(var8.get () ==1):
        txtShake.configure(state = "normal")
    elif(var8.get ()==0):
        txtShake.configure(state = "disabled")
        E_Shake.set("0")



def CostOfItem ():
    Item1= float (E_Burger.get())
    Item2= float (E_Pizza.get())
    Item3= float (E_Sandwich.get())
    Item4= float (E_Salad.get())


    Item5= float (E_Coffee.get())
    Item6= float (E_Tea.get())
    Item7= float (E_Mojita.get())
    Item8= float (E_Shake.get())



    PriceOfBeverages=(Item1*10) + (Item2*20) + (Item3*30) + (Item4*40)
    PriceOfFoods=(Item5*15)+(Item6*20)+(Item7*25)+(Item8*30)


    BeveragesPrice=""+ str('%.2f'%(PriceOfBeverages))
    FoodsPrice=""+ str('%.2f'%(PriceOfFoods))


    CostOfBeverages.set(BeveragesPrice)


    

    


     

     

        

    

        






