from asyncio import events
from lib2to3.pytree import Node

from tkinter import*
from tkinter.font import BOLD, Font
from tkinter import messagebox
from tkinter.filedialog import askopenfile 


from backend import*
from dataview import*


class ui:

    centrality_button = None
    centrality_button_c = None
    centrality_button_f = None

    girvan_button1=None
    girvan_button2=None

    pagerank_lab=None
    pagerank_button=None
    pagerank_button_c=None
    pagerank_button_f=None
    pagerank_ent=None

    backend = None
    loc_data = None

    choices_centrality=None

    def __init__(self, master):
        self.master = master
        
        master.title('Phân tích dữ liệu mạng xã hội')
        master.attributes('-fullscreen', True)
        self.drop_down_typegraph = StringVar()
        self.drop_down_centrality = StringVar()
        self.drop_down_community = StringVar()
        self.drop_down_link_prediction = StringVar()

        self.sl_node_centrality = StringVar()
        self.sl_node_pagerank=StringVar()

        top_bar = Frame(bg = "#465454", width="1366", height="56").place(x=0, y=0)
        top_lab = Label(self.master, text='Ứng dụng phân tích dữ liệu', anchor=W, font=('arial',15,'bold'),
                     width=22).place(x=540, y=15)

        bor1 = Frame(bg = "#465454", width="3", height="700").place(x=454, y=56)
        bor2 = Frame(bg = "#465454", width="3", height="700").place(x=909, y=56)
        bor3 = Frame(bg = "#465454", width="1366", height="3").place(x=0, y=100)

        bottom_bar = Frame(bg = "#465454", width="1366", height="60").place(x=0, y=730)

        exit_button = Button(self.master, text='Đóng', width=15, height=3,font=('arial',9,'bold'))
        exit_button.place(x =1250 ,y = 0)
        exit_button.bind('<Button-1>', self.closeGUI)
        
        open_button = Button(self.master, text='Chọn file dữ liệu', width=15, height=1,font=('arial',9,'bold'))
        open_button.place(x =0 ,y = 0)
        open_button.bind('<Button-1>',self.open_button_even)


    def body(self):
        
        lab0 = Label(self.master, text=self.loc_data, anchor=W, font=('arial',6,'bold'),
                     width=100).place(x=0, y=30)

        lab1 = Label(self.master, text='PHÂN TÍCH CÁC ĐỘ ĐO', anchor=W, font=('arial',10,'bold'),
                     width=24).place(x=140, y=70)
        lab2 = Label(self.master, text='PHÂN TÍCH BẰNG CÁC THUẬT TOÁN KHÁM PHÁ CỘNG ĐỒNG', anchor=W, font=('arial',10,'bold'),
                     width=50).place(x=485, y=70)

        lab3 = Label(self.master, text='DỰ ĐOÁN LIÊN KẾT TRONG MẠNG XÃ HỘI', anchor=W, font=('arial',10,'bold'),
                     width=40).place(x=1010, y=70)

        lab4 = Label(self.master, text='CHỌN ĐỘ ĐO', anchor=W, font=('arial',10,'bold'),
                     width=10).place(x=50, y=125)

        lab5 = Label(self.master, text='NHẬP SỐ LƯỢNG NODE HIỂN THỊ', anchor=W, font=('arial',10,'bold'),
                     width=27).place(x=50, y=250)
        
        lab6 = Label(self.master, text='CHỌN THUẬT TOÁN', anchor=W, font=('arial',10,'bold'),
                     width=27).place(x=500, y=125)

        lab7 = Label(self.master,bg = "#465454",fg='#ffffff', text='CHỌN LOẠI ĐỒ THỊ', anchor=W, font=('arial',10,'bold'),
                     width=15,height=2).place(x=900, y=15)

        lab8 = Label(self.master, text='CHỌN THUẬT TOÁN', anchor=W, font=('arial',10,'bold'),
                     width=27).place(x=970, y=125)

        choices_typegraph = { 'CÓ HƯỚNG', 'VÔ HƯỚNG'}
        self.drop_down_typegraph.set('CÓ HƯỚNG')
        self.drop_down_typegraph.trace('w',self.check_drop_down_typegraph)
        popupMenu = OptionMenu(self.master, self.drop_down_typegraph, *choices_typegraph).place(x = 1030 ,y = 16)
        
        self.choices_centrality = { 'DEGREE CENTRALITY','IN-DEGREE CENTRALITY','OUT-DEGREE CENTRALITY','BETWEENNESS CENTRALITY', 'CLOSENESS CENTRALITY', 'CLUSTERING COEFFICIENT'}
        self.drop_down_centrality.set('DEGREE CENTRALITY')
        self.drop_down_centrality.trace('w',self.check_drop_down_centrality)
        popupMenu = OptionMenu(self.master, self.drop_down_centrality, *self.choices_centrality).place(x = 150 ,y = 120)

        choices_community = { 'GIRVAN NEWMAN', 'PAGE RANK'}
        self.drop_down_community.set('PAGE RANK')
        self.drop_down_community.trace('w',self.check_drop_down_community)
        popupMenu = OptionMenu(self.master, self.drop_down_community, *choices_community).place(x = 650 ,y = 120)

        choices_link_prediction = { 'COMMON NEIGHBORS', 'PREFERENTIAL ATTACHMENT','ADAMIC/ADAR','KATZ'}
        self.drop_down_link_prediction.set('COMMON NEIGHBORS')
        self.drop_down_link_prediction.trace('w',self.check_drop_down_link_prediction)
        popupMenu = OptionMenu(self.master, self.drop_down_link_prediction, *choices_link_prediction).place(x = 1120 ,y = 120)

 
        d_allnetwork_button = Button(self.master, text='TRỰC QUAN HÓA MẠNG LIÊN KẾT', width=50, height=1,font=('arial',9,'bold'))
        d_allnetwork_button.place(x = 505 ,y = 737)
        d_allnetwork_button.bind('<Button-1>',self.d_allnetwork_button_event)

        self.centrality_button = Button(self.master, text='TRỰC QUAN HÓA MẠNG LIÊN KẾT ĐỘ ĐO DEGREE CENTRALITY', width=56, height=2,font=('arial',9,'bold'))
        self.centrality_button.place(x = 25 ,y = 170)
        self.centrality_button.bind('<Button-1>',self.centrality_button_event)

        self.centrality_button_c = Button(self.master, text='ĐỘ ĐO DEGREE CENTRALITY', width=30, height=2,font=('arial',9,'bold'))
        self.centrality_button_c.place(x = 110 ,y = 290)
        self.centrality_button_c.bind('<Button-1>',self.centrality_button_c_event)

        self.centrality_button_f = Button(self.master, text='TẦN SỐ VÀ XÁC SUẤT XUẤT HIỆN', width=30, height=2,font=('arial',9,'bold'))
        self.centrality_button_f.place(x = 110 ,y = 350)
        self.centrality_button_f.bind('<Button-1>',self.centrality_button_f_event)

        self.link_prediction_button = Button(self.master, text='PHÂN TÍCH', width=30, height=2,font=('arial',9,'bold'))
        self.link_prediction_button.place(x = 1040 ,y = 170)
        self.link_prediction_button.bind('<Button-1>',self.link_prediction_button_event)

        

        ent1 = Entry(self.master, textvariable=self.sl_node_centrality,
                     width=20).place(x=280, y=250)


        #pagerank_view
        self.pagerank_button = Button(self.master, text='TRỰC QUAN HÓA MẠNG LIÊN KẾT THEO PAGE RANK', width=56, height=2,font=('arial',9,'bold'))
        self.pagerank_button.place(x = 485 ,y = 170)
        self.pagerank_button.bind('<Button-1>',self.pagerank_button_even)

        self.pagerank_button_c = Button(self.master, text='PAGE RANK', width=30, height=2,font=('arial',9,'bold'))
        self.pagerank_button_c.place(x = 570 ,y = 290)
        self.pagerank_button_c.bind('<Button-1>',self.pagerank_button_c_event)

        self.pagerank_button_f = Button(self.master, text='TẦN SỐ VÀ XÁC SUẤT XUẤT HIỆN', width=30, height=2,font=('arial',9,'bold'))
        self.pagerank_button_f.place(x = 570 ,y = 350)
        self.pagerank_button_f.bind('<Button-1>',self.pagerank_button_f_event)


        self.pagerank_lab = Label(self.master, text='NHẬP SỐ LƯỢNG NODE HIỂN THỊ', anchor=W, font=('arial',10,'bold'),width=27)
        self.pagerank_lab.place(x=510, y=250)

        self.pagerank_ent = Entry(self.master, textvariable=self.sl_node_pagerank,width=20)
        self.pagerank_ent.place(x=740, y=250)

    def check_drop_down_link_prediction(self,*args):
        return
    
    def check_drop_down_typegraph(self,*args):
        if(self.drop_down_typegraph.get()=="VÔ HƯỚNG"):
            self.backend.set_type_graph(0)
            self.choices_centrality = { 'DEGREE CENTRALITY','BETWEENNESS CENTRALITY', 'CLOSENESS CENTRALITY', 'CLUSTERING COEFFICIENT'}
            self.drop_down_centrality.set('DEGREE CENTRALITY')
            self.drop_down_centrality.trace('w',self.check_drop_down_centrality)
            popupMenu = OptionMenu(self.master, self.drop_down_centrality, *self.choices_centrality).place(x = 150 ,y = 120)
        else:
            self.backend.set_type_graph(1)
            self.choices_centrality = { 'DEGREE CENTRALITY','IN-DEGREE CENTRALITY','OUT-DEGREE CENTRALITY','BETWEENNESS CENTRALITY', 'CLOSENESS CENTRALITY', 'CLUSTERING COEFFICIENT'}
            self.drop_down_centrality.set('DEGREE CENTRALITY')
            self.drop_down_centrality.trace('w',self.check_drop_down_centrality)
            popupMenu = OptionMenu(self.master, self.drop_down_centrality, *self.choices_centrality).place(x = 150 ,y = 120)
    
    def check_drop_down_centrality(self,*args):
        self.centrality_button['text']='TRỰC QUAN HÓA MẠNG LIÊN KẾT ĐỘ ĐO '+self.drop_down_centrality.get()
        self.centrality_button_c['text']='ĐỘ ĐO '+self.drop_down_centrality.get()

    def check_drop_down_community(self,*args):
        if(self.drop_down_community.get()=='GIRVAN NEWMAN'):
            try:
                self.pagerank_button.destroy()
                self.pagerank_button_c.destroy()
                self.pagerank_button_f.destroy()
                self.pagerank_ent.destroy()
                self.pagerank_lab.destroy()
                
                self.girvan_button1.destroy()
                self.girvan_button2.destroy()

                self.girvan_button1 = Button(self.master, text='KHAI PHÁ CỘNG ĐỒNG', width=56, height=2,font=('arial',9,'bold'))
                self.girvan_button1.place(x = 485 ,y = 170)
                self.girvan_button1.bind('<Button-1>',self.girvan_button1_event)

                self.girvan_button2 = Button(self.master, text='TRỰC QUAN HÓA MẠNG LIÊN KẾT THEO GIRVAN NEWMAN', width=56, height=2,font=('arial',9,'bold'))
                self.girvan_button2.place(x = 485 ,y = 230)
                self.girvan_button2.bind('<Button-1>',self.girvan_button2_event)
            except:
                self.girvan_button1 = Button(self.master, text='KHAI PHÁ CỘNG ĐỒNG', width=56, height=2,font=('arial',9,'bold'))
                self.girvan_button1.place(x = 485 ,y = 170)
                self.girvan_button1.bind('<Button-1>',self.girvan_button1_event)

                self.girvan_button2 = Button(self.master, text='TRỰC QUAN HÓA MẠNG LIÊN KẾT THEO GIRVAN NEWMAN', width=56, height=2,font=('arial',9,'bold'))
                self.girvan_button2.place(x = 485 ,y = 230)
                self.girvan_button2.bind('<Button-1>',self.girvan_button2_event)

        else:
            try:
                self.girvan_button1.destroy()
                self.girvan_button2.destroy()

                self.pagerank_button.destroy()
                self.pagerank_button_c.destroy()
                self.pagerank_button_f.destroy()
                self.pagerank_ent.destroy()
                self.pagerank_lab.destroy()
            
                self.pagerank_button = Button(self.master, text='TRỰC QUAN HÓA MẠNG LIÊN KẾT THEO PAGE RANK', width=56, height=2,font=('arial',9,'bold'))
                self.pagerank_button.place(x = 485 ,y = 170)
                self.pagerank_button.bind('<Button-1>',self.pagerank_button_even)

                self.pagerank_button_c = Button(self.master, text='PAGE RANK', width=30, height=2,font=('arial',9,'bold'))
                self.pagerank_button_c.place(x = 570 ,y = 290)
                self.pagerank_button_c.bind('<Button-1>',self.pagerank_button_c_event)

                self.pagerank_button_f = Button(self.master, text='TẦN SỐ VÀ XÁC SUẤT XUẤT HIỆN', width=30, height=2,font=('arial',9,'bold'))
                self.pagerank_button_f.place(x = 570 ,y = 350)
                self.pagerank_button_f.bind('<Button-1>',self.pagerank_button_f_event)


                self.pagerank_lab = Label(self.master, text='NHẬP SỐ LƯỢNG NODE HIỂN THỊ', anchor=W, font=('arial',10,'bold'),width=27)
                self.pagerank_lab.place(x=510, y=250)

                self.pagerank_ent = Entry(self.master, textvariable=self.sl_node_pagerank,width=20)
                self.pagerank_ent.place(x=740, y=250)
            except:
                self.pagerank_button = Button(self.master, text='TRỰC QUAN HÓA MẠNG LIÊN KẾT THEO PAGE RANK', width=56, height=2,font=('arial',9,'bold'))
                self.pagerank_button.place(x = 485 ,y = 170)
                self.pagerank_button.bind('<Button-1>',self.pagerank_button_even)

                self.pagerank_button_c = Button(self.master, text='PAGE RANK', width=30, height=2,font=('arial',9,'bold'))
                self.pagerank_button_c.place(x = 570 ,y = 290)
                self.pagerank_button_c.bind('<Button-1>',self.pagerank_button_c_event)

                self.pagerank_button_f = Button(self.master, text='TẦN SỐ VÀ XÁC SUẤT XUẤT HIỆN', width=30, height=2,font=('arial',9,'bold'))
                self.pagerank_button_f.place(x = 570 ,y = 350)
                self.pagerank_button_f.bind('<Button-1>',self.pagerank_button_f_event)


                self.pagerank_lab = Label(self.master, text='NHẬP SỐ LƯỢNG NODE HIỂN THỊ', anchor=W, font=('arial',10,'bold'),width=27)
                self.pagerank_lab.place(x=510, y=250)

                self.pagerank_ent = Entry(self.master, textvariable=self.sl_node_pagerank,width=20)
                self.pagerank_ent.place(x=740, y=250)

    def centrality_button_event(self,event):
        self.backend.d_type(self.drop_down_centrality.get())

    def centrality_button_c_event(self,event):
        try:
            if (int(self.sl_node_centrality.get())>self.backend.get_n_nodes()):
                messagebox.showerror('LỖI','SỐ LƯỢNG NODE TỐI ĐA LÀ '+str(self.backend.get_n_nodes()))
            else:
                data=self.backend.op_data_value(self.drop_down_centrality.get(),int(self.sl_node_centrality.get()))
                data_w=dataview(self.drop_down_centrality.get(),data,3)
                data_w.load_data_ver1(int(self.sl_node_centrality.get())-1)
        except:
            messagebox.showerror('LỖI','DỮ LIỆU BẠN NHẬP KHÔNG HỢP LỆ !')
    
    def centrality_button_f_event(self,event):
        data=self.backend.op_data_fre(self.drop_down_centrality.get())
        data_w=dataview(self.drop_down_centrality.get(),data,4)
        data_w.load_data_ver2()

    def girvan_button1_event(self,event):
        list_data=self.backend.girvan_newman_anal()
        view=view_discovery_algorithm(list_data)

    def girvan_button2_event(self,event):
        self.backend.d_grivan_newman()

    def pagerank_button_even(self,event):
        self.backend.d_page_rank()
    
    def pagerank_button_c_event(self,event):
        try:
            if (int(self.sl_node_pagerank.get())>self.backend.get_n_nodes()):
                messagebox.showerror('LỖI','SỐ LƯỢNG NODE TỐI ĐA LÀ '+str(self.backend.get_n_nodes()))
            else:
                data=self.backend.page_rank_anl(int(self.sl_node_pagerank.get()))
                data_w=dataview(self.drop_down_community.get(),data,3)
                data_w.load_data_ver1(int(self.sl_node_pagerank.get())-1)
        except:
            messagebox.showerror('LỖI','DỮ LIỆU BẠN NHẬP KHÔNG HỢP LỆ !')
    
    def pagerank_button_f_event(self,event):
        data=self.backend.page_rank_fre()
        data_w=dataview(self.drop_down_community.get(),data,4)
        data_w.load_data_ver2()
    
    def link_prediction_button_event(self,event):
        if(self.drop_down_link_prediction.get()=='COMMON NEIGHBORS' or self.drop_down_link_prediction.get()=='PREFERENTIAL ATTACHMENT' or self.drop_down_link_prediction.get()=='ADAMIC/ADAR'):
            data=self.backend.link_prediction(self.drop_down_link_prediction.get())
            data_w=dataview(self.drop_down_link_prediction.get(),data,0)
            data_w.load_data_ver3(len(data)-1)
        elif(self.drop_down_link_prediction.get()=='KATZ'):
            data=self.backend.link_prediction(self.drop_down_link_prediction.get())
            data_w=dataview(self.drop_down_link_prediction.get(),data,3)
            data_w.load_data_ver4(len(data)-1)
       
    
    def d_allnetwork_button_event(self,event):
        self.backend.d_allnetwork()

    def closeGUI(self, event):
        self.master.destroy()

    def open_button_even(self,event):
        file = askopenfile(mode ='r', filetypes =[('CSV File', '*.csv')]) 
        if file is not None: 
            try:
                self.loc_data = file.name
                if(self.backend == None):
                    self.backend=backend(self.loc_data)
                else:
                    self.backend=None
                    self.backend=backend(self.loc_data)
                self.body()
            except:
                messagebox.showerror('LỖI','FILE DỮ LIỆU KHÔNG HỢP LỆ !')

class view:    
    root=Tk()
    obj = ui(root)
    root.mainloop()
    
    def __init__(self) -> None:
        pass

