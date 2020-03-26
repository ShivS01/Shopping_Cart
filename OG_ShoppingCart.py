from tkinter import *
master = Tk()
thislist = ["perfume", "faces lipstick", "plecktrum", "jewellery box", "sanitizer", "lakme moisturizer", "addidas hoodie", "cover story jeans", "coffee mug", "vans sneakers"]
prices= [100, 150 ,60, 120, 40, 135, 1500, 900, 1100, 1000]
result=[0,0,0,0,0,0,0,0,0,0]
options=[IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar()]
cart=[0,0,0,0,0,0,0,0,0,0]
menu=[]
v = []
messageVar = Message(master, text = "                      shopping cart", width=250, font=50).grid(row=0, column=1, sticky=W)
for i in thislist:
    v.insert(thislist.index(i), IntVar())
    Checkbutton(master, text=i,  onvalue=1, offvalue=0, variable=v[thislist.index(i)]).grid(row=thislist.index(i)+1, column=1, sticky=W)
for j in prices:
    Label(master, text="                  ").grid(row=prices.index(j)+1, column=2, sticky=W)
    Label(master, text=j).grid(row=prices.index(j)+1, column=3, sticky=W)
def payment():
    import sqlite3 as lite
    import sys
    con = lite.connect('user.db')
    def save():
        s1=e1.get()
        s2=e2.get()
        s3=e3.get()
        n1=e4.get()
        n2=int(n1)
        master4 = Tk()
        Message(master4, text = "Your order has been Accepted", width=250, font=50).grid(row=0, column=1, sticky=W)
        Message(master4, text = "Order details are", width=250, font=50).grid(row=1, column=1, sticky=W)
        Message(master4, text = ("Name: "+s1), width=250, font=50).grid(row=2, column=1, sticky=W)
        Message(master4, text = ("Address: "+s2), width=250, font=50).grid(row=3, column=1, sticky=W)
        Message(master4, text = ("Email: "+s3), width=250, font=50).grid(row=4, column=1, sticky=W)
        Message(master4, text = ("Phone No.: "+n1), width=250, font=50).grid(row=5, column=1, sticky=W)
        with con:
            cur=con.cursor()
            cur.execute("INSERT INTO Users VALUES(?,?,?,?)",(s1,s2,s3,n2))
        master4.mainloop()
    master3 = Tk(className = "User Data")
    messageVar = Message(master3, text = "                      Confirmation", width=250, font=50).grid(row=0, column=1, sticky=W)
    Label(master3, text="Name").grid(row=1)
    Label(master3, text="Address").grid(row=2)
    Label(master3, text="Email").grid(row=3)
    Label(master3, text="Phone No.").grid(row=4)
    e1=Entry(master3)
    e2=Entry(master3)
    e3=Entry(master3)
    e4=Entry(master3)
    e1.grid(row=1, column=1)
    e2.grid(row=2, column=1)
    e3.grid(row=3, column=1)
    e4.grid(row=4, column=1)
    Button(master3, text='Save', command= save).grid(row=5, column=1, sticky=W)
    master3.mainloop()
def confirm():
    master2 = Tk()
    messageVar = Message(master2, text = "                      Your cart", width=250, font=50).grid(row=0, column=1, sticky=W)
    for i in range(0,10):
        if v[i].get()==1:
            def ok():
                res=0
                for i in range(0,10):
                    result[i]=(prices[i]*(options[i].get()))
                    Label(master2, text = result[i]).grid(row=i+1, column=5)
                    res=res+result[i]
                Label(master2, text=res).grid(row=13, column=5, sticky=W)
                for i in range(0,10):
                        menu.append(OptionMenu(master2, options[i], 1, 2, 3, 4, 5))
                        menu[i].grid(row=i+1, column=4)
            Label(master2, text=thislist[i]).grid(row=i+1, column=1, sticky=W)
            Label(master2, text="                  ").grid(row=i+1, column=2, sticky=W)
            Label(master2, text=prices[i]).grid(row=i+1, column=3, sticky=W)
    Label(master2, text="---------------------------").grid(row=12, column=1, sticky=W)
    Button(master2, text="Total", command= ok).grid(row=13, column=1, sticky=W)
    Button(master2, text="Place your order", command = payment).grid(row=14, column=1, sticky=W)
b1= Button(master, text= "<-----Confirm----->", command = confirm).grid(row=15, column=1, sticky=W)
mainloop() 
