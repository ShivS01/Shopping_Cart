#tb.py

from tkinter import *
from tkinter.ttk import *
from modules.tktooltip import *
def _init_toolbar(tbmaster):
    
    '''TOOLBAR CONTAINS ADD, EDIT, DELETE AND FIND BUTTONS
        the argment is a class and it must have:
        tbmaster.frame              :- a root window class
        tbmaster.btn_add_click()    :- a method
        tbmaster.btn_edit_click()
        tbmaster.btn_delete_click()
        tbmaster.btn_find_click()
        '''
    tbmaster.tb=Frame(tbmaster.frame,borderwidth=1)#,relief=)
    tbmaster.tb.pack(side=TOP,fill=X)#####
    imgdir="images/16x16/"
    tbmaster.btn_add=Button(tbmaster.tb,command=tbmaster.btn_add_click)
    tbmaster.imgadd=PhotoImage(file=imgdir+"add.png")
    tbmaster.btn_add['image']=tbmaster.imgadd
    tbmaster.btn_add.pack(side=LEFT,padx=4,pady=4)
    CreateToolTip(tbmaster.btn_add, text='Add a Product')
    
    tbmaster.btn_edit=Button(tbmaster.tb,command=tbmaster.btn_edit_click)
    tbmaster.imgedit=PhotoImage(file=imgdir+"edit2.png")
    tbmaster.btn_edit['image']=tbmaster.imgedit
    tbmaster.btn_edit.pack(side=LEFT,padx=4,pady=4)
    CreateToolTip(tbmaster.btn_edit, text='Edit a Product')

    
    tbmaster.btn_delete=Button(tbmaster.tb,command=tbmaster.btn_del_click)
    tbmaster.imgdel=PhotoImage(file=imgdir+"delete.png")
    tbmaster.btn_delete['image']=tbmaster.imgdel
    tbmaster.btn_delete.pack(side=LEFT,padx=4,pady=4)
    CreateToolTip(tbmaster.btn_delete, text='Delete a Product')

    
    tbmaster.btn_find=Button(tbmaster.tb,command=tbmaster.tb_btnfind_click)
    tbmaster.imgfind=PhotoImage(file=imgdir+"find.png")
    tbmaster.btn_find['image']=tbmaster.imgfind
    tbmaster.btn_find.pack(side=LEFT,padx=4,pady=4)
    CreateToolTip(tbmaster.btn_find, text='Find a Product')

    
    tbmaster.tb_entryfind=Entry(tbmaster.tb)
    tbmaster.tb_entryfind.pack(side=LEFT,padx=4,pady=4)

