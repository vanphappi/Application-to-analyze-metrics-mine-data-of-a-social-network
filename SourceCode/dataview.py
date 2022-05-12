from tkinter import *
import tkinter.ttk as ttk
import pandas as pd

class dataview:

    type_c=None
    data=None
    num_col=None

    root=None
    tree=None

    def __init__(self,type_c,data,num_col):
        self.type_c=type_c
        self.data=data
        self.num_col=num_col

        self.root = Tk()
        self.root.title('GIÁ TRỊ '+self.type_c)
        width = 800
        height = 400
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        self.root.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self.root.resizable(0, 0)
        if(self.num_col==3):
            self.body_ver1()
        elif(self.num_col==4):
            self.body_ver2()
        else:
            self.body_ver3()

    
    
    def body_ver1(self):
        TableMargin = Frame(self.root, width=500)
        TableMargin.pack(side=TOP)
        scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
        scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
        self.tree = ttk.Treeview(TableMargin, columns=("STT", "NODE",self.type_c), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        scrollbary.config(command=self.tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=self.tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        self.tree.heading('STT', text="", anchor=W)
        self.tree.heading('NODE', text="NODE", anchor=W)
        self.tree.heading(self.type_c, text=self.type_c, anchor=W)
        self.tree.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree.column('#1', stretch=NO, minwidth=0, width=200)
        self.tree.column('#2', stretch=NO, minwidth=0, width=200)
        self.tree.column('#3', stretch=NO, minwidth=0, width=200)
        self.tree.pack()

    def body_ver2(self):
        TableMargin = Frame(self.root, width=500)
        TableMargin.pack(side=TOP)
        scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
        scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
        self.tree = ttk.Treeview(TableMargin, columns=("STT",self.type_c,"FREQUENCY","PROBABILITY",), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        scrollbary.config(command=self.tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=self.tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        self.tree.heading('STT', text="", anchor=W)
        self.tree.heading(self.type_c, text=self.type_c, anchor=W)
        self.tree.heading("FREQUENCY", text="FREQUENCY", anchor=W)
        self.tree.heading("PROBABILITY", text="PROBABILITY", anchor=W)
        self.tree.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree.column('#1', stretch=NO, minwidth=0, width=200)
        self.tree.column('#2', stretch=NO, minwidth=0, width=200)
        self.tree.column('#3', stretch=NO, minwidth=0, width=200)
        self.tree.column('#4', stretch=NO, minwidth=0, width=200)
        self.tree.pack()

    def body_ver3(self):
        TableMargin = Frame(self.root, width=500)
        TableMargin.pack(side=TOP)
        scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
        scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
        self.tree = ttk.Treeview(TableMargin, columns=("STT", "NODE PAIR (NOT CONNECT)",self.type_c), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        scrollbary.config(command=self.tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=self.tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        self.tree.heading('STT', text="", anchor=W)
        self.tree.heading('NODE PAIR (NOT CONNECT)', text="NODE PAIR (NOT CONNECT)", anchor=W)
        self.tree.heading(self.type_c, text=self.type_c, anchor=W)
        self.tree.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree.column('#1', stretch=NO, minwidth=0, width=200)
        self.tree.column('#2', stretch=NO, minwidth=0, width=200)
        self.tree.column('#3', stretch=NO, minwidth=0, width=200)
        self.tree.pack()
         

    def load_data_ver1(self,num):
        node=self.data['NODE'].tolist()
        type = self.data[self.type_c].tolist()
        while(num>=0):
            self.tree.insert("", 0, values=(num,node[num],type[num]))
            num -= 1
        self.root.mainloop()

    def load_data_ver2(self):
        type = self.data[self.type_c].tolist()
        fre = self.data["FREQUENCY"].tolist()
        pro = self.data["PROBABILITY"].tolist()
        num=len(type)-1
        while(num>=0):
            self.tree.insert("", 0, values=(num,type[num],fre[num],pro[num]))
            num -= 1
        self.root.mainloop()

    def load_data_ver3(self,num):
        while(num>=0):
            self.tree.insert("", 0, values=(num,str(self.data[num][0])+'-'+str(self.data[num][1]),self.data[num][2]))
            num -= 1
        self.root.mainloop()

    def load_data_ver4(self,num):
        while(num>=0):
            self.tree.insert("", 0, values=(num,self.data[num][0],self.data[num][1]))
            num -= 1
        self.root.mainloop()    

class view_discovery_algorithm:
    def __init__(self,list_data):
        root = Tk()
        root.title("KẾT QUẢ KHAI PHÁ CỘNG ĐỒNG BẰNG GIRVAN NEWMAN")
        width = 800
        height = 400
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        root.geometry("%dx%d+%d+%d" % (width, height, x, y))
        root.resizable(0, 0)

        TableMargin = Frame(root, width=500)
        TableMargin.pack(side=TOP)
        scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
        scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
       
        #root.geometry("250x170")
        T = Text(TableMargin,width=800,height=400)
        
        scrollbary.config(command=T.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=T.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        T.pack()
        num=len(list_data)-1
        while(num>=0):
            T.insert('1.0',list_data[num]+'\n')
            num -= 1
        root.mainloop()