from tkinter import *
from tkinter.ttk import *
from modules.tkcalendar import ttkCalendar
from forms.products import FormProducts
from forms.invoices import FormInvoices
from forms.addinvoice import FormAddInvoice
from modules.tktooltip import CreateToolTip

class FormMenu:
    """This is the main form that shows after user login.
    Contains
    =========
    --> Label shows login Company name.
    --> Three Buttons
        --> Products:   OnClick Shows FormProducts,
        --> Invoices:   OnClick Shows FormInvoices,
        --> Customers:  OnClick shows FormCustomers
    --> A background Image
    """
    def __init__(self,master):
        self.frame=master
        master.title("Shopping Cart V-1.0")
        self.frm_invoices=None
        self.frm_calendar=None
        self._init_menu()
        self._init_widgets()
        
    def _init_menu(self):
       # self.frame.bind("<KeyPress>",self.keypressed)
        
        self.menu = Menu(self.frame)
        self.frame.config(menu=self.menu)
        filemenu = Menu(self.menu)
        self.menu.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="Products...", command=self.products_click)
        filemenu.add_command(label="Invoices...", command=self.invoices_click)
        filemenu.add_command(label="Create Invoice...", command=self.addinvoice_click)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.frame.quit)
        helpmenu = Menu(self.menu)
        self.menu.add_cascade(label="Help", menu=helpmenu)
        helpmenu.add_command(label="About...", command=self.about_click)

    def about_click(self):
        w=Toplevel()
        w.title("About")
        lbl1=Label(w,text="Welcome to Shopping Cart 1.0")
        lbl1.pack(side="top",padx=10,pady=10)
        lbl3=Label(w,text="Team Members : Shivanshu, Harsha, Hemanth, Pranav")
        lbl3.pack(side="top",padx=10,pady=10)
        lbl3=Label(w,text="https://github.com/ShivS01/Shopping_Cart")
        lbl3.pack(side="top",padx=10,pady=10)
        
    def _init_widgets(self):
        #initiate toolbar
        self.toolbar = Frame(self.frame)

        imgdir="images/24x24/"

        self.toolbar.imghome=PhotoImage(file=imgdir+"home.png")
        self.toolbar.imgcalc=PhotoImage(file=imgdir+"calc.png")
        self.toolbar.imgcalander=PhotoImage(file=imgdir+"date.png")
        self.toolbar.imgexit=PhotoImage(file=imgdir+"exit.png")
        self.toolbar.imghelp=PhotoImage(file=imgdir+"help.png")

        butcompany=Button(self.toolbar,image=self.toolbar.imghome,command="")
        butcompany.pack(side=LEFT,padx=2)
        CreateToolTip(butcompany, text='Choose a company')

        butcalc=Button(self.toolbar,image=self.toolbar.imgcalc,command=self.calc_click)
        butcalc.pack(side=LEFT,padx=2)
        CreateToolTip(butcalc, text='Open Calculator')


        butcalendar=Button(self.toolbar,image=self.toolbar.imgcalander,command=self.calendar_click)
        butcalendar.pack(side=LEFT,padx=2)
        CreateToolTip(butcalendar, text='Open Calender')

        butexit=Button(self.toolbar,image=self.toolbar.imgexit,command=self.frame.quit)
        butexit.pack(side=RIGHT,padx=2)
        CreateToolTip(butexit, text='Exit')


        buthelp=Button(self.toolbar,image=self.toolbar.imghelp,command=self.about_click)
        buthelp.pack(side=RIGHT,padx=2)
        CreateToolTip(buthelp, text='Help')


        self.toolbar.pack(side='top',fill='x')
                
        #buttons frame
        #--------------------------------------------
        style = Style()
        style.configure("BW.TLabel", foreground="white", background="black")
        self.buttons = Label(self.frame, style="BW.TLabel",borderwidth=0,anchor='e')

        #button products
        self.btnproducts = Button(self.buttons,command=self.products_click)
        self.imgprdt=PhotoImage(file="images/products1.png")#self.btnproducts['font']=("Helvetica", 16)
        self.btnproducts['image']=self.imgprdt
        self.btnproducts.pack(side='top')#, fill='x')
        lbl1=Label(self.buttons,text="Products", style="BW.TLabel").pack()

        #button invoices
        self.btninvoices = Button(self.buttons, command=self.invoices_click)
        self.imginv=PhotoImage(file="images/invoices.png")
        self.btninvoices['image']=self.imginv
        self.btninvoices.pack(side='top')
        lbl2=Label(self.buttons,text="Invoices", style="BW.TLabel").pack()

        #button customers
        self.btncustomers = Button(self.buttons, command=self.addinvoice_click)
        self.imgcust=PhotoImage(file="images/customers.png")
        self.btncustomers['image']=self.imgcust
        self.btncustomers.pack(side='top')
        lbl3=Label(self.buttons,text="Create Invoice", style="BW.TLabel").pack()

        self.buttons.pack(side='left',expand=YES)

        #background label
        #-------------------------------------------
        self.imgback=PhotoImage(file="images/logo4.png")
        self.lblbackground= Label(self.frame, style="BW.TLabel",borderwidth=0,anchor='w')

        #Second Col -- in widgets
        self.lblbackground.pack(side='left',fill=BOTH,expand=YES)
        self.lblbackground['image'] = self.imgback


    def calc_click(self):
        import os
        try: os.startfile('calc.exe')
        except: print ('calculator doesnt exist')

    #calendar-------
    def calendar_click(self):
        if self.frm_calendar==None:
            self.frm_calendar=ttkCalendar(master=self.frame)
        elif self.frm_calendar.flag: #frm_products currently opened
            print ('already a window exists')
            return 0
        else:
            self.frm_calendar=ttkCalendar(master=self.frame)
            
        self.frame.wait_window(self.frm_calendar.top)
        print (self.frm_calendar.datepicked)

        ''''
    def keypressed(self,e):
        #33 p, 31 i, 54 c
        if e.keycode == 33: self.products_click()
        elif e.keycode == 31: self.invoices_click()
        elif e.keycode == 54: self.addinvoice_click()
        '''
    def products_click(self):
        print("products")
        self.frame.withdraw()
        self.frm_products=FormProducts()
        self.frame.wait_window(self.frm_products.frame)
        self.frame.deiconify()
        
    def invoices_click(self):
        print ("invoices")
        self.frame.withdraw()
        self.frm_invoices=FormInvoices()
        self.frame.wait_window(self.frm_invoices.frame)
        self.frame.deiconify()

    def addinvoice_click(self):        
        print ("add_invoice")
        self.frame.withdraw()
        self.frm_invoices=FormAddInvoice()
        self.frame.wait_window(self.frm_invoices.frame)
        self.frame.deiconify()
