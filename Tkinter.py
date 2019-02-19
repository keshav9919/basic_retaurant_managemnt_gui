from tkinter import *
import time
import random
root=Tk()
operator = " "
text_input=StringVar()
f1=Frame(root,height=50,width=1600,bg="powder blue",relief=SUNKEN)
f1.pack(side=TOP)
f2=Frame(root,width=800,height=700,relief=SUNKEN)
f2.pack(side=LEFT)
f3=Frame(root,width=300,height=700,bg="powder blue",relief=SUNKEN)
f3.pack(side=RIGHT)
l=Label(f1,text="Restaurant Management System",font=("Arial",50,'bold'),fg="blue",anchor='w')
l.grid(row=0,column=0)
l2=time.asctime(time.localtime(time.time()))
l=Label(f1,text=l2,font=("Arial",20,'bold'),fg="blue",anchor='w')
l.grid(row=1,column=0)
#===================================functions============================
def btnclick(n):
    global operator
    operator=operator+str(n)

    text_input.set(operator)
def btnclear():
    global operator
    operator=""
    text_input.set(operator)
def btnequal():
    global operator
    sumup=str(eval(operator))
    text_input.set(sumup)
    operator=""
def rendom():
    x=str(random.randint(20000,80000))
    ref.set(x)
    v1=float(fries.get())
    v2=float(veg.get())
    v3=float(chicken_meal.get())
    v4 = float(burger_meal.get())
    v5 = float(cheese_meal.get())
    v6 = float(non_veg.get())
    v7 = float(drinks.get())

    c1=v1*20
    c2 = v2 * 20
    c3 = v3 * 30
    c4 = v4 * 40
    c5 = v5 * 50
    c6 = v6 * 60
    c7 = v7 * 70

    csotofmeal="Rs",str('%.2f' %(c1+c2+c3+c4+c5+c6+c7))
    paytax=(c1+c2+c3+c4+c5+c6+c7)*0.2
    TotalCost=c1+c2+c3+c4+c5+c6+c7
    serCharge=TotalCost/99
    service="Rs",str("%.2f" %serCharge)
    overallcost="Rs",str("%.2f" %(serCharge+TotalCost+paytax))
    paidtax="Rs",str("%.2f" %paytax)

    service_charge.set(service)
    cost_of_meal.set(csotofmeal)
    gst.set(paidtax)
    sub_total.set(csotofmeal)
    total_cost.set(overallcost)




def reset():
    ref.set("")
    fries.set("")
    veg.set("")
    chicken_meal.set("")
    burger_meal.set("")
    cheese_meal.set("")
    non_veg.set("")
    drinks.set("")
    cost_of_meal.set("")
    service_charge.set("")
    gst.set("")
    sub_total.set("")
    total_cost.set("")
def quit():
    root.destroy()


#=====================================calculator======================================================
txt_display=Entry(f3,bd=30,textvariable=text_input,bg="powder blue",insertwidth=4)
txt_display.grid(columnspan=10)
btn7=Button(f3,padx=16,pady=16,text="7",bd=8,fg="black",bg="powder blue",font=("Arial",20,"bold"),command=lambda :btnclick(7)).grid(row=2,column=0)#+++doubt++++
btn8=Button(f3,padx=16,pady=16,text="8",bd=8,fg="black",bg="powder blue",font=("Arial",20,"bold"),command=lambda :btnclick(8)).grid(row=2,column=1)#+++doubt++++
btn9=Button(f3,padx=16,pady=16,text="9",bd=8,fg="black",bg="powder blue",font=("Arial",20,"bold"),command=lambda :btnclick(9)).grid(row=2,column=2)#+++doubt++++
btnadd=Button(f3,padx=16,pady=16,text="+",bd=8,fg="black",bg="powder blue",font=("Arial",20,"bold"),command=lambda :btnclick("+")).grid(row=2,column=3)#+++doubt++++
#========================================================================================================================================
btn4=Button(f3,padx=16,pady=16,text="4",bd=8,fg="black",bg="powder blue",font=("Arial",20,"bold"),command=lambda :btnclick(4)).grid(row=3,column=0)#+++doubt++++
btn5=Button(f3,padx=16,pady=16,text="5",bd=8,fg="black",bg="powder blue",font=("Arial",20,"bold"),command=lambda :btnclick(5)).grid(row=3,column=1)#+++doubt++++
btn6=Button(f3,padx=16,pady=16,text="6",bd=8,fg="black",bg="powder blue",font=("Arial",20,"bold"),command=lambda :btnclick(6)).grid(row=3,column=2)#+++doubt++++
btnsub=Button(f3,padx=16,pady=16,text="-",bd=8,fg="black",bg="powder blue",font=("Arial",20,"bold"),command=lambda :btnclick("-")).grid(row=3,column=3)#+++doubt++++
#=============================================================================================================================================
btn1=Button(f3,padx=16,pady=16,text="1",bd=8,fg="black",bg="powder blue",font=("Arial",20,"bold"),command=lambda :btnclick(1)).grid(row=4,column=0)#+++doubt++++
btn2=Button(f3,padx=16,pady=16,text="2",bd=8,fg="black",bg="powder blue",font=("Arial",20,"bold"),command=lambda :btnclick(2)).grid(row=4,column=1)#+++doubt++++
btn3=Button(f3,padx=16,pady=16,text="3",bd=8,fg="black",bg="powder blue",font=("Arial",20,"bold"),command=lambda :btnclick(3)).grid(row=4,column=2)#+++doubt++++
btnmul=Button(f3,padx=16,pady=16,text="x",bd=8,fg="black",bg="powder blue",font=("Arial",20,"bold"),command=lambda :btnclick("*")).grid(row=4,column=3)#+++doubt++++
#====================================================================================================================================================================
btn0=Button(f3,padx=16,pady=16,text="0",bd=8,fg="black",bg="powder blue",font=("Arial",20,"bold"),command=lambda :btnclick(0)).grid(row=5,column=0)#+++doubt++++
btnC=Button(f3,padx=16,pady=16,text="C",bd=8,fg="black",bg="powder blue",font=("Arial",20,"bold"),command=lambda :btnclear()).grid(row=5,column=1)#+++doubt++++
btneq=Button(f3,padx=16,pady=16,text="=",bd=8,fg="black",bg="powder blue",font=("Arial",20,"bold"),command=lambda:btnequal()).grid(row=5,column=2)#+++doubt++++
btndiv=Button(f3,padx=16,pady=16,text="/",bd=8,fg="black",bg="powder blue",font=("Arial",20,"bold"),command=lambda :btnclick("/")).grid(row=5,column=3)#+++doubt++++
#==============================================================================================================================================================
ref=StringVar()
fries=StringVar()
veg=StringVar()
chicken_meal=StringVar()
burger_meal=StringVar()
cheese_meal=StringVar()
non_veg=StringVar()
drinks=StringVar()
cost_of_meal=StringVar()
service_charge=StringVar()
gst=StringVar()
sub_total=StringVar()
total_cost=StringVar()



lblref=Label(f2,text="Reference",font=("Arial",16,"bold"),bd=16).grid(row=0,column=0)
refentry=Entry(f2,textvariable=ref,insertwidth=4,bd=10,justify='right',font=("Arial",20,'bold'),bg="powder blue").grid(row=0,column=1)
lblfry=Label(f2,text="Large Fries",font=("Arial",16,"bold"),bd=16).grid(row=1,column=0)
fryentry=Entry(f2,textvariable=fries,insertwidth=4,bd=10,justify='right',font=("Arial",20,'bold'),bg='powder blue').grid(row=1,column=1)
lblveg=Label(f2,text="Veg Meal",font=("Arial",16,"bold"),bd=16).grid(row=2,column=0)
vegentry=Entry(f2,textvariable=veg,insertwidth=4,bd=10,justify='right',font=("Arial",20,'bold'),bg="powder blue").grid(row=2,column=1)
lblchicken=Label(f2,text="Chicken Meal",font=("Arial",16,"bold"),bd=16).grid(row=3,column=0)
chickenentry=Entry(f2,textvariable=chicken_meal,insertwidth=4,bd=10,justify='right',font=("Arial",20,'bold'),bg="powder blue").grid(row=3,column=1)
lblburger=Label(f2,text="Burger Meal",font=("Arial",16,"bold"),bd=16).grid(row=4,column=0)
burgerentry=Entry(f2,textvariable=burger_meal,insertwidth=4,bd=10,justify='right',font=("Arial",20,'bold'),bg="powder blue").grid(row=4,column=1)
lblcheese=Label(f2,text="Cheese Meal",font=("Arial",16,"bold"),bd=16).grid(row=5,column=0)
cheeseentry=Entry(f2,textvariable=cheese_meal,insertwidth=4,bd=10,justify='right',font=("Arial",20,'bold'),bg="powder blue").grid(row=5,column=1)
lblnonveg=Label(f2,text="Non-Veg Meal",font=("Arial",16,"bold"),bd=16).grid(row=6,column=0)
nonvegentry=Entry(f2,textvariable=non_veg,insertwidth=4,bd=10,justify='right',font=("Arial",20,'bold'),bg="powder blue").grid(row=6,column=1)
#=====================
lbldrinks=Label(f2,text="Drinks",font=("Arial",16,"bold"),bd=16).grid(row=0,column=3)
drinksentry=Entry(f2,textvariable=drinks,insertwidth=4,bd=10,justify='right',font=("Arial",20,'bold'),bg="powder blue").grid(row=0,column=4)
lblcost0fmeal=Label(f2,text="Cost of Meal",font=("Arial",16,"bold"),bd=16).grid(row=1,column=3)
costentry=Entry(f2,textvariable=cost_of_meal,insertwidth=4,bd=10,justify='right',font=("Arial",20,'bold'),bg="powder blue").grid(row=1,column=4)
lblservice=Label(f2,text="Service Charge",font=("Arial",16,"bold"),bd=16).grid(row=2,column=3)
service_charge_entry=Entry(f2,textvariable=service_charge,insertwidth=4,bd=10,justify='right',font=("Arial",20,'bold'),bg="powder blue").grid(row=2,column=4)
lblgst=Label(f2,text="GST",font=("Arial",16,"bold"),bd=16).grid(row=3,column=3)
gstentry=Entry(f2,textvariable=gst,insertwidth=4,bd=10,justify='right',font=("Arial",20,'bold'),bg="powder blue").grid(row=3,column=4)
lblsubtotal=Label(f2,text="Sub Total",font=("Arial",16,"bold"),bd=16).grid(row=4,column=3)
drinksentry=Entry(f2,textvariable=sub_total,insertwidth=4,bd=10,justify='right',font=("Arial",20,'bold'),bg="powder blue").grid(row=4,column=4)
lbtotal_cost=Label(f2,text="Total Cost",font=("Arial",16,"bold"),bd=16).grid(row=5,column=3)
total_cost_entry=Entry(f2,textvariable=total_cost,insertwidth=4,bd=10,justify='right',font=("Arial",20,'bold'),bg="powder blue").grid(row=5,column=4)
#===============================
tobut=Button(f2,padx=10,pady=5,font=("Arial",20,'bold'),bd=10,text="Total",bg="powder blue",command=lambda:rendom()).grid(row=7,column=1)
reset_button=Button(f2,padx=10,pady=5,font=("Arial",20,'bold'),bd=10,text="Reset",bg="powder blue",command=lambda:reset()).grid(row=7,column=3)
exit_bitton=Button(f2,padx=10,pady=5,font=("Arial",20,'bold'),bd=10,text="Exit",bg="powder blue",command=lambda:quit()).grid(row=7,column=4)
root.mainloop()
