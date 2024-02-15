from tkinter import *
win=Tk()
win.title("products")
win.geometry("500x500+500+100")
win.state("zoomed")

def multiplication():
    a=int(producta.get())
    b=int(productb.get())
    c=a*b
    result.config(text=c)

producttiltle=Label(win,text="Multiplication")
producttiltle.grid(row=0,column=20,padx=200,pady=30)

message=Label(win,text="Enter a value 1:")
message.grid(row=1,column=20)

producta=Entry(win,width=60)
producta.grid(row=1,column=25)


message=Label(win,text="Enter a value 2:")
message.grid(row=2,column=20)

productb=Entry(win,width=60)
productb.grid(row=2,column=25)

result=Label(win,text=" ")
result.grid(row=3,column=30, pady=20)


click=Button(win,text="multiplication", command=multiplication)
click.grid(row=4, column=1)

win.mainloop()










# from tkinter import *

# win=Tk()

# win.title("Arithmatic Operations")
# win.geometry("500x500+500+100")
# win.state("zoomed")

# def addition():
#     a=int(tbEntrya.get())
#     b=int(tbEntryb.get())
#     #print(a+b)
#     c=a+b
#     labelouptut.config(text=c)

# def Subtraction():
#     a=int(tbEntrya.get())
#     b=int(tbEntryb.get())
#     #print(a+b)
#     c=a-b
#     labelouptut.config(text=c)



# labelTitle=Label(win,text="Arithmatic Operations")
# labelTitle.grid(row=0,column=20,padx=200, pady=30)

# label1msg=Label(win,text="Enter value a :")
# label1msg.grid(row=1,column=20)

# tbEntrya=Entry(win,width=60)
# tbEntrya.grid(row=1,column=25)


# label2msg=Label(win,text="Enter value b :")
# label2msg.grid(row=2,column=20, pady=20)

# tbEntryb=Entry(win,width=60)
# tbEntryb.grid(row=2,column=25,pady=20)


# labelouptut=Label(win,text="")
# labelouptut.grid(row=3,column=30, pady=20)


# btnAdd=Button(win,text="Addition", command=addition)
# btnAdd.grid(row=4, column=1)

# btnSubtract=Button(win,text="Subtraction",command=Subtraction)
# btnSubtract.grid(row=4,column=2)



# win.mainloop()