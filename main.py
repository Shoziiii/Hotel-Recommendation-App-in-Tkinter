from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import random
import pandas as pd
from PIL import ImageTk, Image


class menu:
    def __init__(self):
        self.root=Tk()
        self.root.title('Menu')
        self.root.geometry("800x600")
        self.root.configure(bg="#b3ecff")
        self.csv_file = pd.read_csv("hotel_data_set.csv")
        self.main_window()
    def main_window(self):
        self.photo=Image.open("logo.png")
        self.photo1=self.photo.resize((800,520),Image.ANTIALIAS)
        self.photo2=ImageTk.PhotoImage(self.photo1)
        Label(self.root,width=800,height=520,image=self.photo2,bd=0, highlightthickness=0, relief='ridge').place(x= 0,y = 0)
        Button(self.root,text='Welcome',relief = "groove",bg="#b3ecff",font=("Georgia 13 bold",14),command=self.welcome).place(x=300,y=540,width=200,height=40)
    def on_selection(self,*args):
        self.ima_num = random.randint(1,10)
        self.im = Image.open(f"{self.ima_num}.jpeg")
        self.im_width,self.im_height = self.im.size
        self.req_ratio = self.im_width/390
        self.req_width = int(self.im_width/self.req_ratio)
        self.req_height = int(self.im_height/self.req_ratio)
        self.photo3=self.im.resize((self.req_width,self.req_height),Image.ANTIALIAS)
        self.photo4=ImageTk.PhotoImage(self.photo3)
        Label(self.c_1,image=self.photo4,bd=0, highlightthickness=0,bg="#b3ecff", relief='ridge').place(x = 390+(400-self.req_width)/2,y = 10,width=self.req_width,height = self.req_height)
        self.updates()
        
    def filter(self):  
        self. li = []
        self.indi = 0      
        self.c_2 = Canvas(self.root,bg = "#b3ecff",bd=0, highlightthickness=0, relief='ridge').place(x = 0,y = 0, width = 800,height = 600 )
        Label(self.c_2,text='Minimum Price: ',font=("Georgia 13 bold",14),bg="#b3ecff").place(x=40,y=40)
        Label(self.c_2,text='Maximum Price: ',font=("Georgia 13 bold",14),bg="#b3ecff").place(x=40,y=80)
        Label(self.c_2,text='|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|',font=("Georgia 13 bold",5),bg="#b3ecff").place(x=380,y=1)
        self.p_min = IntVar()
        self.p_max = IntVar()
        Entry(self.c_2,textvariable = self.p_min).place(x=200,y=40,width=150,height=27)
        Entry(self.c_2,textvariable = self.p_max).place(x=200,y=80,width=150,height=27)
        self.s_min = IntVar()
        self.s_max = IntVar()
        Label(self.c_2,text='Minimum Stars: ',font=("Georgia 13 bold",14),bg="#b3ecff").place(x=40,y=340)
        Label(self.c_2,text='Maximum Stars: ',font=("Georgia 13 bold",14),bg="#b3ecff").place(x=40,y=380)
        Entry(self.c_2,textvariable = self.s_min).place(x=200,y=340,width=150,height=27)
        Entry(self.c_2,textvariable = self.s_max).place(x=200,y=380,width=150,height=27)
        Button(self.c_2,text='Sort by Price',relief = "groove",bg="#b3ecff",font=("Georgia 13 bold",14),command=self.asli_1).place(x=100,y=240,width=200,height=40)
        Button(self.c_2,text='Sort by Stars',relief = "groove",bg="#b3ecff",font=("Georgia 13 bold",14),command=self.asli_2).place(x=100,y=440,width=200,height=40)
        Button(self.c_2,text='<<Back',relief = "groove",bg="#b3ecff",font=("Georgia 13 bold",14),command=self.welcome).place(x=100,y=540,width=200,height=40)
        self.p_select = StringVar(self.c_2,"2")
        values = {"From Maximum to Minimum" : "1",
                "From Minimum to Maximum" : "2",}
        y = 130
        for (text, value) in values.items():
            Radiobutton(self.c_2, text = text, variable = self.p_select,value = value,font=("Georgia 13 bold",14)).place(x = 40, y = y)
            y+=40  
            
    def destry(self):
        if self.indi !=0:
            for i in self.li:
                i.config(text = "")
    def asli_2(self):
        self.destry()
        self.price_options = dict(self.csv_file["Number of stars"])
        if self.p_select.get() == "1":
            self.re_ord = {k: v for k, v in sorted(self.price_options.items(),reverse=True, key=lambda item: item[1])}
            yy = 20
            for k,v in self.re_ord.items():
                if v>=self.s_min.get() and v<=self.s_max.get():
                    self.h = self.csv_file["Hotel name"][k]
                    t = f"{self.h}: {v}"
                    xx = Label(self.c_2,text=t,font=("Georgia 13 bold",14),bg="#b3ecff")
                    xx.place(x=410,y=yy,width = 380)
                    self.li.append(xx)
                    yy+=40 
        if self.p_select.get() == "2":
            self.re_ord = {k: v for k, v in sorted(self.price_options.items(), key=lambda item: item[1])}
            yy = 20
            for k,v in self.re_ord.items():
                if v>=self.s_min.get() and v<=self.s_max.get():
                    self.h = self.csv_file["Hotel name"][k]
                    t = f"{self.h}: {v}"
                    xx = Label(self.c_2,text=t,font=("Georgia 13 bold",14),bg="#b3ecff")
                    xx.place(x=410,y=yy,width = 380)
                    self.li.append(xx)
                    yy+=40 
        self.indi+=1
    def asli_1(self):
        self.destry()
        self.price_options = dict(self.csv_file["Price"])
        if self.p_select.get() == "1":
            self.re_ord = {k: v for k, v in sorted(self.price_options.items(),reverse=True, key=lambda item: item[1])}
            yy = 20
            for k,v in self.re_ord.items():
                if v>=self.p_min.get() and v<=self.p_max.get():
                    self.h = self.csv_file["Hotel name"][k]
                    t = f"{self.h}: ${v}"   
                    xx = Label(self.c_2,text=t,font=("Georgia 13 bold",14),bg="#b3ecff")
                    xx.place(x=410,y=yy,width = 380)
                    self.li.append(xx)
                    yy+=40 
        if self.p_select.get() == "2":
            self.re_ord = {k: v for k, v in sorted(self.price_options.items(), key=lambda item: item[1])}
            yy = 20
            for k,v in self.re_ord.items():
                if v>=self.p_min.get() and v<=self.p_max.get():
                    self.h = self.csv_file["Hotel name"][k]
                    t = f"{self.h}: ${v}"
                    xx = Label(self.c_2,text=t,font=("Georgia 13 bold",14),bg="#b3ecff")
                    xx.place(x=410,y=yy,width = 380)
                    self.li.append(xx)
                    yy+=40 
        self.indi+=1
        
        
    def updates(self):
        Label(self.c_1,text='Number of Stars: ',font=("Georgia 13 bold",14),bg="#b3ecff").place(x=40,y=120)
        Label(self.c_1,text='Price: ',font=("Georgia 13 bold",14),bg="#b3ecff").place(x=40,y=170)
        Label(self.c_1,text='Gym Availability: ',font=("Georgia 13 bold",14),bg="#b3ecff").place(x=40,y=220)
        Label(self.c_1,text='Pool Availability: ',font=("Georgia 13 bold",14),bg="#b3ecff").place(x=40,y=320)
        Label(self.c_1,text='Bathtub Availability: ',font=("Georgia 13 bold",14),bg="#b3ecff").place(x=40,y=370)
        Label(self.c_1,text='Distinctive Features: ',font=("Georgia 13 bold",14),bg="#b3ecff").place(x=40,y=420)
        self.indexx = self.hotel_options.index(self.hotel_name.get())
        self.stars = self.csv_file["Number of stars"][self.indexx]
        self.price = self.csv_file["Price"][self.indexx]
        self.gym = self.csv_file["Gym availablility"][self.indexx]
        self.pool = self.csv_file["Pool availability"][self.indexx]
        self.btub = self.csv_file["Bathtub availablity "][self.indexx]
        self.dfeature = self.csv_file["Dstinctive features"][self.indexx]
        
        x = 220
        self.star_photo=ImageTk.PhotoImage(Image.open("star_2.png"))
        for i in range(int(self.stars)):
            Label(self.c_1,image = self.star_photo,bg="#b3ecff").place(x=x,y=120)
            x+=20
        
        Label(self.c_1,text=f"${self.price}",font=("Georgia 13 bold",14),bg="#b3ecff").place(x=220,y=170,width = 50)
        Label(self.c_1,text=self.gym,font=("Georgia 13 bold",14),bg="#b3ecff").place(x=220,y=220,width = 50)
        Label(self.c_1,text=self.pool,font=("Georgia 13 bold",14),bg="#b3ecff").place(x=220,y=320,width = 50)
        Label(self.c_1,text=self.btub,font=("Georgia 13 bold",14),bg="#b3ecff").place(x=220,y=370,width = 50)
        Label(self.c_1,text=self.dfeature,font=("Georgia 13 bold",14),bg="#b3ecff").place(x=0,y=460,width = 360)
    
    
    def welcome(self):
        self.c_1 = Canvas(self.root,bg = "#b3ecff",bd=0, highlightthickness=0, relief='ridge').place(x = 0,y = 0, width = 800,height = 600 )
        self.hotel_options = [i for i in self.csv_file["Hotel name"]]
        self.hotel_name = StringVar()
        self.hotel_name.set(self.hotel_options[0])
        self.hotel_name.trace("w",self.on_selection)
        Label(self.c_1,text='Select the Hotel : ',font=("Georgia 13 bold",14),bg="#b3ecff").place(x=40,y=40,width = 150)
        self.drop = OptionMenu( self.c_1 , self.hotel_name, *self.hotel_options ).place(x = 200,y = 40,width=175)
        Label(self.c_1,text='|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|',font=("Georgia 13 bold",5),bg="#b3ecff").place(x=380,y=1)
        
        Button(self.root,text='Filter',relief = "groove",bg="#b3ecff",font=("Georgia 13 bold",14),command=self.filter).place(x=100,y=540,width=200,height=40)

        
        
a = menu()
mainloop()
