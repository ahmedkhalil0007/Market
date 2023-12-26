# This was my first project when I was 7 years old
# This project was made to manage super market
import os
import tkinter
from tkinter import *
from math import *
from os import *
from random import *
from tkinter import messagebox
from tkinter import Toplevel,Button,Tk,Menu
class Super:
    def __init__(self, master=None):
        self.root = root
        self.root.geometry("1300x700+30+10")
        self.root.title("super-market: سوبر ماركت")
        self.root.resizable(False,False)
        self.root.iconbitmap("logo.ico")
        title = Label(self.root, text="مشروع سوبر مركيت",fg="white",bg="#0B2F3A",font=("tajawal ",15))
        title.pack(fill=X)     
    
        f1=Frame(root, bd=2 , width="388",height=170,bg="#0B2F3A")
        f1.place(x=961,y=45)

        self.bacoliat = StringVar()
        
        self.adoat = StringVar()
        self.kahraba =  StringVar()


        self.namo = StringVar()
        self.phono = StringVar()
        self.fatora = StringVar()

        
        self.q1=IntVar()
        self.q2=IntVar()
        self.q3=IntVar()
        self.q4=IntVar()
        self.q5=IntVar()
        self.q6=IntVar()
        self.q7=IntVar()
        self.q8=IntVar()
        self.q9=IntVar()
        self.q10=IntVar()
        self.q11=IntVar()
        self.q12=IntVar()
        self.q13=IntVar()
        self.q14=IntVar()
        self.q15=IntVar()
        self.q16=IntVar()
        self.q17=IntVar()
        self.q18=IntVar()

        self.qq1=IntVar()
        self.qq2=IntVar()
        self.qq3=IntVar()
        self.qq4=IntVar()
        self.qq5=IntVar()
        self.qq6=IntVar()
        self.qq7=IntVar()
        self.qq8=IntVar()
        self.qq9=IntVar()
        self.qq10=IntVar()
        self.qq11=IntVar()
        self.qq12=IntVar()
        self.qq13=IntVar()
        self.qq14=IntVar()
        self.qq15=IntVar()
        self.qq16=IntVar()
        self.qq17=IntVar()
        self.qq18=IntVar()

        self.qqq1=IntVar()
        self.qqq2=IntVar()
        self.qqq3=IntVar()
        self.qqq4=IntVar()
        self.qqq5=IntVar()
        self.qqq6=IntVar()
        self.qqq7=IntVar()
        self.qqq8=IntVar()
        self.qqq9=IntVar()
        self.qqq10=IntVar()
        self.qqq11=IntVar()
        self.qqq12=IntVar()
        self.qqq13=IntVar()
        self.qqq14=IntVar()
        self.qqq15=IntVar()
        self.qqq16=IntVar()


        self.namo = StringVar() 
        self.phono = StringVar()
        self.fatora = StringVar()

        x = randint(1,1000000)
        self.fatora.set(str(x))
        
        

        tit = Label(f1, text=": بيانات المشترى",font=("tajawal",13,"bold"),bg="#0B2F3A",fg="tomato")
        tit.place(x=175,y=0)

        his_name = Label(f1, text=(" اسم المشتري"),font=("tajawal",10),bg="#0B2F3A",fg="white")
        his_name.place(x=245,y=40)

        his_phone = Label(f1, text=("رقم المشتري"),font=("tajawal",10),bg="#0B2F3A",fg="white")
        his_phone.place(x=250,y=70)

        bill_num = Label(f1, text=(" رقم الفاتورة"),font=("tajawal",10),bg="#0B2F3A",fg="white")
        bill_num.place(x=250,y=100)
          
        Ent_name = Entry(f1,textvariable=self.namo, justify="center")
        Ent_name.place(x=90,y=42)

        Ent_phone = Entry(f1,textvariable=self.phono, justify="center")
        Ent_phone.place(x=90,y=72)

        Ent_bill = Entry(f1,textvariable=self.fatora, justify="center")
        Ent_bill.place(x=90,y=102)

        btn_customer = Button(f1, text="بحث", font=("tajawal",10),width=10,height=5,bg="white")
        btn_customer.place(x=1,y=40)

        titdd = Label(f1 ,text=" [الفواتىر] ",font=("tajawal",13,"bold"),bg="#0B2F3A",fg="gold")
        titdd.place(x=125,y=135)
       
        F3 = Frame(root, bd=2,width=338 , height=399, bg="white")
        F3.place(x=960,y=215)

        scrol_y = Scrollbar(F3, orient=VERTICAL)
        self.textarea = Text(F3 , yscrollcommand=scrol_y.set)
        scrol_y.pack(side=LEFT,fill=Y)
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH , expand=1)

      
        f4 = Frame(root, bd=2 , width="657",height=112,bg="#0B2F3A")
        f4.place(x=641,y=587)

        hesab = Button(f4, text="الحساب", width=13,height=1,font="tajawal",bg="#DBA901", command= lambda: self.total())
        hesab.place(x=537,y=10)

        fatora = Button(f4, text="تصدير الفاتورة",width=13 ,height=1,font="tajawal",bg="#DBA901",command = lambda: self.save())
        fatora.place(x=537,y=55)

        clear = Button(f4, text=" افراغ الحقول",width=13 ,height=1,font="tajawal",bg="#DBA901", command= lambda: self.clear())
        clear.place(x=417,y=10)

        exite = Button(f4, text="  اغلاق البرناج",width=13 ,height=1,font="tajawal",bg="#DBA901",command= lambda: self.close())
        exite.place(x=417,y=55)

        lblol = Label(f4, text="الحساب الكلي للبقوليات",font=("tajawal",13,"bold"),bg="#0B2F3A",fg="gold")
        lblol.place(x=220,y=10)

        lblol2 = Label(f4, text="الحساب اللوازم المنزلية",font=("tajawal",13,"bold"),bg="#0B2F3A",fg="gold")
        lblol2.place(x=220,y=40)

        lblol3 = Label(f4, text="الحساب ادوات الكهرباء",font=("tajawal",13,"bold"),bg="#0B2F3A",fg="gold")
        lblol3.place(x=220,y=70)

        ento1 = Entry(f4,textvariable=self.bacoliat, width=24)
        ento1.place(x=40,y=12)


        ento2 = Entry(f4,textvariable=self.adoat, width=24)
        ento2.place(x=40,y=42)

        ento3 = Entry(f4,textvariable=self.kahraba , width=24)
        ento3.place(x=40,y=72)

        ff1 = Frame(root, bd=2,width=318,height=664,bg="#0B2F3A")
        ff1.place(x=1,y=35)

        t = Label(ff1, text="البقوليات",font=("tajawal",13,"bold"),bg="#0B2F3A",fg="gold")
        t.place(x=122,y=0)

        bq1 = Label(ff1, text="الرز", font=("tajawal",13,"bold"),bg="#0B2F3A",fg="white")
        bq1.place(x=240,y=50)

        bq2 = Label(ff1, text="برغل", font=("tajawal",13,"bold"),bg="#0B2F3A",fg="white")
        bq2.place(x=240,y=80)

        bq3 = Label(ff1, text="فاصولياء", font=("tajawal",13,"bold"),bg="#0B2F3A",fg="white")
        bq3.place(x=240,y=110)

        bq4 = Label(ff1, text="عدس", font=("tajawal",13,"bold"),bg="#0B2F3A",fg="white")
        bq4.place(x=240,y=140)

        bq5 = Label(ff1, text="معكرونة", font=("tajawal",13,"bold"),bg="#0B2F3A",fg="white")
        bq5.place(x=240,y=170)

        bq6 = Label(ff1, text="فريكة", font=("tajawal",13,"bold"),bg="#0B2F3A",fg="white")
        bq6.place(x=240,y=200)

        bq7 = Label(ff1, text="حمص", font=("tajawal",13,"bold"),bg="#0B2F3A",fg="white")
        bq7.place(x=240,y=230)

        bq8 = Label(ff1, text="فول", font=("tajawal",13,"bold"),bg="#0B2F3A",fg="white")
        bq8.place(x=240,y=270)

        bq9 = Label(ff1, text="الملح", font=("tajawal",13,"bold"),bg="#0B2F3A",fg="white")
        bq9.place(x=240,y=300)

        bq10 = Label(ff1, text="سكر", font=("tajawal",13,"bold"),bg="#0B2F3A",fg="white")
        bq10.place(x=240,y=330)

        bq11 = Label(ff1, text="فلفل اسود", font=("tajawal",13,"bold"),bg="#0B2F3A",fg="white")
        bq11.place(x=240,y=370)

        bq12 = Label(ff1, text="فلفل احمر", font=("tajawal",13,"bold"),bg="#0B2F3A",fg="white")
        bq12.place(x=240,y=400)

        bq13 = Label(ff1, text="اللبيا", font=("tajawal",13,"bold"),bg="#0B2F3A",fg="white")
        bq13.place(x=240,y=430)

        bq14 = Label(ff1, text="الادمامي", font=("tajawal",13,"bold"),bg="#0B2F3A",fg="white")
        bq14.place(x=240,y=470)

        bq15 = Label(ff1, text="القمح", font=("tajawal",13,"bold"),bg="#0B2F3A",fg="white")
        bq15.place(x=240,y=500)

        bq16= Label(ff1, text="الشعير", font=("tajawal",13,"bold"),bg="#0B2F3A",fg="white")
        bq16.place(x=240,y=530)

        bq7 = Label(ff1, text="الشفان", font=("tajawal",13,"bold"),bg="#0B2F3A",fg="white")
        bq7.place(x=240,y=570)

        bq1 = Label(ff1, text="الذرة", font=("tajawal",13,"bold"),bg="#0B2F3A",fg="white")
        bq1.place(x=240,y=600)

        bqent1 = Entry(ff1,textvariable=self.q1, width=12)
        bqent1.place(x=70,y=50)

        bqent2 = Entry(ff1,textvariable=self.q2, width=12)
        bqent2.place(x=70,y=80)

        bqent3 = Entry(ff1,textvariable=self.q3, width=12)
        bqent3.place(x=70,y=110)

        bqent4 = Entry(ff1,textvariable=self.q4, width=12)
        bqent4.place(x=70,y=140)

        bqent5 = Entry(ff1,textvariable=self.q5, width=12)
        bqent5.place(x=70,y=170)

        bqent6 = Entry(ff1,textvariable=self.q6, width=12)
        bqent6.place(x=70,y=200)

        bqent7 = Entry(ff1,textvariable=self.q7, width=12)
        bqent7.place(x=70,y=230)

        bqent8 = Entry(ff1,textvariable=self.q8, width=12)
        bqent8.place(x=70,y=270)

        bqent9 = Entry(ff1,textvariable=self.q9, width=12)
        bqent9.place(x=70,y=300)

        bqent10 = Entry(ff1,textvariable=self.q10, width=12)
        bqent10.place(x=70,y=330)

        bqent11 = Entry(ff1,textvariable=self.q11, width=12)
        bqent11.place(x=70,y=370)

        bqent12 = Entry(ff1,textvariable=self.q12, width=12)
        bqent12.place(x=70,y=400)

        bqent13 = Entry(ff1,textvariable=self.q13, width=12)
        bqent13.place(x=70,y=430)

        bqent14 = Entry(ff1,textvariable=self.q14, width=12)
        bqent14.place(x=70,y=470)

        bqent15 = Entry(ff1,textvariable=self.q15, width=12)
        bqent15.place(x=70,y=500)

        bqent16 = Entry(ff1,textvariable=self.q16, width=12)
        bqent16.place(x=70,y=530)

        bqent17 = Entry(ff1,textvariable=self.q17, width=12)
        bqent17.place(x=70,y=570)

        bqent18 = Entry(ff1,textvariable=self.q18, width=12)
        bqent18.place(x=70,y=600)

        ff2 = Frame(root, bd=2,width=318,height=664,bg="#0B2F3A")
        ff2.place(x=321,y=35)

        t1 = Label(ff2, text="اللوازم المنزلية",font=("tajawal",13,"bold"),bg="#0B2F3A",fg="gold")
        t1.place(x=122,y=0)

        bq1 = Label(ff2, text="مصفاة", font=("tajawal",13,"bold"),bg="#0B2F3A",fg="white")
        bq1.place(x=240,y=50)

        bq2 = Label(ff2, text="صحن", font=("tajawal",13,"bold"),bg="#0B2F3A",fg="white")
        bq2.place(x=240,y=80)

        bq3 = Label(ff2, text="كاس", font=("tajawal",13,"bold"),bg="#0B2F3A",fg="white")
        bq3.place(x=240,y=110)

        bq4 = Label(ff2, text="ابريق", font=("tajawal",13,"bold"),bg="#0B2F3A",fg="white")
        bq4.place(x=240,y=140)

        bq5 = Label(ff2, text="سكين", font=("tajawal",13,"bold"),bg="#0B2F3A",fg="white")
        bq5.place(x=240,y=170)

        bq6 = Label(ff2, text="شوك", font=("tajawal",13,"bold"),bg="#0B2F3A",fg="white")
        bq6.place(x=240,y=200)

        bq7 = Label(ff2, text="طنجرة", font=("tajawal",13,"bold"),bg="#0B2F3A",fg="white")
        bq7.place(x=240,y=230)

        bq8 = Label(ff2, text="سلة", font=("tajawal",13,"bold"),bg="#0B2F3A",fg="white")
        bq8.place(x=240,y=270)

        bq9 = Label(ff2, text="ملاعق", font=("tajawal",13,"bold"),bg="#0B2F3A",fg="white")
        bq9.place(x=240,y=300)

        bq10 = Label(ff2, text="صينية", font=("tajawal",13,"bold"),bg="#0B2F3A",fg="white")
        bq10.place(x=240,y=330)

        bq11 = Label(ff2, text=" وعاء الخلط", font=("tajawal",13,"bold"),bg="#0B2F3A",fg="white")
        bq11.place(x=240,y=370)

        bq12 = Label(ff2, text=" فتاحة علب", font=("tajawal",13,"bold"),bg="#0B2F3A",fg="white")
        bq12.place(x=240,y=400)

        bq13 = Label(ff2, text="مقشرة", font=("tajawal",13,"bold"),bg="#0B2F3A",fg="white")
        bq13.place(x=240,y=430)

        bq14 = Label(ff2, text="لوح النقطيع", font=("tajawal",13,"bold"),bg="#0B2F3A",fg="white")
        bq14.place(x=240,y=470)

        bq15 = Label(ff2, text="حفارة", font=("tajawal",13,"bold"),bg="#0B2F3A",fg="white")
        bq15.place(x=240,y=500)

        bq16= Label(ff2, text="سلة قمامة", font=("tajawal",13,"bold"),bg="#0B2F3A",fg="white")
        bq16.place(x=240,y=530)

        bq7 = Label(ff2, text="منفضة", font=("tajawal",13,"bold"),bg="#0B2F3A",fg="white")
        bq7.place(x=240,y=570)

        bq1 = Label(ff2, text="اكياس", font=("tajawal",13,"bold"),bg="#0B2F3A",fg="white")
        bq1.place(x=240,y=600)


        bqent1 = Entry(ff2,textvariable=self.qq1, width=12)
        bqent1.place(x=70,y=50)

        bqent2 = Entry(ff2,textvariable=self.qq2, width=12)
        bqent2.place(x=70,y=80)

        bqent3 = Entry(ff2,textvariable=self.qq3, width=12)
        bqent3.place(x=70,y=110)

        bqent4 = Entry(ff2,textvariable=self.qq4, width=12)
        bqent4.place(x=70,y=140)

        bqent5 = Entry(ff2,textvariable=self.qq5, width=12)
        bqent5.place(x=70,y=170)

        bqent6 = Entry(ff2,textvariable=self.qq6, width=12)
        bqent6.place(x=70,y=200)

        bqent7 = Entry(ff2,textvariable=self.qq7, width=12)
        bqent7.place(x=70,y=230)

        bqent8 = Entry(ff2,textvariable=self.qq8, width=12)
        bqent8.place(x=70,y=270)

        bqent9 = Entry(ff2,textvariable=self.qq9, width=12)
        bqent9.place(x=70,y=300)

        bqent10 = Entry(ff2,textvariable=self.qq10, width=12)
        bqent10.place(x=70,y=330)

        bqent11 = Entry(ff2,textvariable=self.qq11, width=12)
        bqent11.place(x=70,y=370)

        bqent12 = Entry(ff2,textvariable=self.qq12, width=12)
        bqent12.place(x=70,y=400)

        bqent13 = Entry(ff2,textvariable=self.qq13, width=12)
        bqent13.place(x=70,y=430)

        bqent14 = Entry(ff2,textvariable=self.qq14, width=12)
        bqent14.place(x=70,y=470)

        bqent15 = Entry(ff2,textvariable=self.qq15, width=12)
        bqent15.place(x=70,y=500)

        bqent16 = Entry(ff2,textvariable=self.qq16, width=12)
        bqent16.place(x=70,y=530)

        bqent17 = Entry(ff2,textvariable=self.qq17, width=12)
        bqent17.place(x=70,y=570)

        bqent18 = Entry(ff2,textvariable=self.qq18, width=12)
        bqent18.place(x=70,y=600)

        ff3 = Frame(root, bd=2,width=318,height=550,bg="#0B2F3A")
        ff3.place(x=641,y=35)


        t1 = Label(ff3, text=" ادوات الكهرباء",font=("tajawal",13,"bold"),bg="#0B2F3A",fg="gold")
        t1.place(x=122,y=0)

        bq1 = Label(ff3, text="مكنسة", font=("tajawal",13,"bold"),bg="#0B2F3A",fg="white")
        bq1.place(x=240,y=50)

        bq2 = Label(ff3, text="تلفزيون", font=("tajawal",13,"bold"),bg="#0B2F3A",fg="white")
        bq2.place(x=240,y=80)

        bq3 = Label(ff3, text="غسالة", font=("tajawal",13,"bold"),bg="#0B2F3A",fg="white")
        bq3.place(x=240,y=110)

        bq4 = Label(ff3, text="مكرويف", font=("tajawal",13,"bold"),bg="#0B2F3A",fg="white")
        bq4.place(x=240,y=140)

        bq5 = Label(ff3, text="خلاط", font=("tajawal",13,"bold"),bg="#0B2F3A",fg="white")
        bq5.place(x=240,y=170)

        bq6 = Label(ff3, text="فرن غاز", font=("tajawal",13,"bold"),bg="#0B2F3A",fg="white")
        bq6.place(x=240,y=200)

        bq7 = Label(ff3, text="مقلاة كهرباء", font=("tajawal",13,"bold"),bg="#0B2F3A",fg="white")
        bq7.place(x=240,y=230)

        bq8 = Label(ff3, text="مروح سقف", font=("tajawal",13,"bold"),bg="#0B2F3A",fg="white")
        bq8.place(x=240,y=270)

        bq9 = Label(ff3, text="مروح ارضية", font=("tajawal",13,"bold"),bg="#0B2F3A",fg="white")
        bq9.place(x=240,y=300)

        bq10 = Label(ff3, text="تلفزيون32", font=("tajawal",13,"bold"),bg="#0B2F3A",fg="white")
        bq10.place(x=240,y=330)

        bq11 = Label(ff3, text=" تلفزيون43", font=("tajawal",13,"bold"),bg="#0B2F3A",fg="white")
        bq11.place(x=240,y=370)

        bq12 = Label(ff3, text="فلتر ماء", font=("tajawal",13,"bold"),bg="#0B2F3A",fg="white")
        bq12.place(x=240,y=400)

        bq13 = Label(ff3, text="غسالة اوتو", font=("tajawal",13,"bold"),bg="#0B2F3A",fg="white")
        bq13.place(x=240,y=430)

        bq14 = Label(ff3, text="مكواة", font=("tajawal",13,"bold"),bg="#0B2F3A",fg="white")
        bq14.place(x=240,y=470)

        bq15 = Label(ff3, text="مبردة", font=("tajawal",13,"bold"),bg="#0B2F3A",fg="white")
        bq15.place(x=240,y=500)

        bqent1 = Entry(ff3,textvariable=self.qqq1, width=12)
        bqent1.place(x=70,y=50)

        bqent2 = Entry(ff3,textvariable=self.qqq2, width=12)
        bqent2.place(x=70,y=80)

        bqent3 = Entry(ff3,textvariable=self.qqq3, width=12)
        bqent3.place(x=70,y=110)

        bqent4 = Entry(ff3,textvariable=self.qqq4, width=12)
        bqent4.place(x=70,y=140)

        bqent5 = Entry(ff3,textvariable=self.qqq5, width=12)
        bqent5.place(x=70,y=170)

        bqent6 = Entry(ff3,textvariable=self.qqq6, width=12)
        bqent6.place(x=70,y=200)

        bqent7 = Entry(ff3,textvariable=self.qqq7, width=12)
        bqent7.place(x=70,y=230)

        bqent8 = Entry(ff3,textvariable=self.qqq8, width=12)
        bqent8.place(x=70,y=270)

        bqent9 = Entry(ff3,textvariable=self.qqq9, width=12)
        bqent9.place(x=70,y=300)

        bqent10 = Entry(ff3,textvariable=self.qqq10, width=12)
        bqent10.place(x=70,y=330)

        bqent11 = Entry(ff3,textvariable=self.qqq11, width=12)
        bqent11.place(x=70,y=370)

        bqent12 = Entry(ff3,textvariable=self.qqq12, width=12)
        bqent12.place(x=70,y=400)

        bqent13 = Entry(ff3,textvariable=self.qqq13, width=12)
        bqent13.place(x=70,y=430)

        bqent14 = Entry(ff3,textvariable=self.qqq14, width=12)
        bqent14.place(x=70,y=470)

        bqent15 = Entry(ff3,textvariable=self.qqq15, width=12)
        bqent15.place(x=70,y=500)

       
        

    def total(self):
        
        print("q1 = ", self.q1.get())
        self.rez = self.q1.get() * 1.5
        print("rez = ",self.rez)
        self.borgel = self.q2.get() * 1.5
        self.fasolis = self.q3.get() * 1.5
        self.ades = self.q4.get() * 1.5
        self.makrona = self.q5.get() * 1.5
        self.frika = self.q6.get() * 1.5
        self.homes = self.q7.get() * 1.5
        self.fol = self.q8.get() * 1.5
        self.mlah = self.q9.get() * 1.5
        self.skar = self.q10.get() * 1.5
        self.flflahmar = self.q11.get() * 1.5
        self.flflasod = self.q12.get() * 1.5
        self.lobia = self.q13.get() * 1.5
        self.admami = self.q14.get() * 1.5
        self.qmah = self.q15.get() * 1.5
        self.shair = self.q16.get() * 1.5
        self.shofan = self.q17.get() * 1.5
        self.zara = self.q18.get() * 1.5
        self.totalito = float(
            self.rez +
            self.borgel +
            self.fasolis +
            self.ades +
            self.makrona +
            self.frika +
            self.homes +
            self.fol +
            self.mlah +
            self.skar +
            self.flflahmar +
            self.flflasod +
            self.lobia +
            self.admami +
            self.qmah +
            self.shair +
            self.shofan +
            self.zara + 0
            
        )
        print(" total =======", self.totalito)
        self.bacoliat.set(self.totalito)

        # اللوازم المنزلية
        print("qq1 = ", self.qq1.get())
        self.mesfaa = self.qq1.get() * 1.5
        print("mesafaa = ",self.mesfaa)
        self.sahn = self.qq2.get() * 1.5
        self.kas = self.qq3.get() * 1.5
        self.apreek = self.qq4.get() * 1.5
        self.seken = self.qq5.get() * 1.5
        self.shok = self.qq6.get() * 1.5
        self.tanger = self.qq7.get() * 1.5
        self.sl = self.qq8.get() * 1.5
        self.mlak = self.qq9.get() * 1.5
        self.sene = self.qq10.get() * 1.5
        self.qalt = self.qq11.get() * 1.5
        self.fatk = self.qq12.get() * 1.5
        self.mekshar = self.qq13.get() * 1.5
        self.loh = self.qq14.get() * 1.5
        self.hafar = self.qq15.get() * 1.5
        self.slh = self.qq16.get() * 1.5
        self.menh = self.qq17.get() * 1.5
        self.akes = self.qq18.get() * 1.5
        self.totalito2 = float(
            self.mesfaa +
            self.sahn +
            self.kas +
            self.apreek +
            self.seken + 
            self.shok +
            self.tanger +
            self.sl +
            self.mlak +
            self.sene +
            self.qalt +
            self.fatk +
            self.mekshar +
            self.loh +
            self.hafar +
            self.slh +
            self.menh +
            self.akes + 0


        )
        self.adoat.set(self.totalito2)


        
        print("qqq1 = ", self.qqq1.get())
        self.mkh = self.qqq1.get() * 1.5
        print("mkh = ",self.mkh)
        self.tv = self.qqq2.get() * 1.5
        self.shn = self.qqq3.get() * 1.5
        self.mk = self.qqq4.get() * 1.5
        self.flt = self.qqq5.get() * 1.5
        self.frn = self.qqq6.get() * 1.5
        self.mkl = self.qqq7.get() * 1.5
        self.mr = self.qqq8.get() * 1.5
        self.sr = self.qqq9.get() * 1.5
        self.tv32 = self.qqq10.get() * 1.5
        self.tv43 = self.qqq11.get() * 1.5
        self.fltr = self.qqq12.get() * 1.5
        self.at = self.qq13.get() * 1.5
        self.mekwa = self.qqq14.get() * 1.5
        self.mobrad = self.qqq15.get() * 1.5
        self.totalito3 = float(
            self.mkh +
            self.tv +
            self.shn +
            self.mk +
            self.flt + 
            self.frn +
            self.mkl +
            self.mr +
            self.sr +
            self.tv32 +
            self.tv43 +
            self.fltr +
            self.at +
            self.mekwa +
            self.mobrad +0

        )
        self.kahraba.set(self.totalito3)
        self.totalall = self.totalito + self.totalito2 + self.totalito3
        print("self.totalall", self.totalall)
        self.welcome()

    def welcome(self):
        self.textarea.delete("1.0",END)
        self.textarea.insert(END,"\t سوبر ماركت الخبير يرحب بكم")
        self.textarea.insert(END,"\n==================================")
        self.textarea.insert(END,f"\n\t B.NUM  :{self.fatora.get()}")
        self.textarea.insert(END,f"\n\t NAME   :{self.namo.get()}")
        self.textarea.insert(END,f"\n\t PHONE  :{self.phono.get()}")
        self.textarea.insert(END,"\n==================================")
        self.textarea.insert(END,f"\n             السعر          ")
        self.textarea.insert(END,"\n==================================")
        self.textarea.insert(END,f"\n{self.bacoliat.get()}\t      \t     البقوليات")
        self.textarea.insert(END,f"\n{self.adoat.get()}\t  \t  اللوازم المنزلية")
        self.textarea.insert(END,f"\n{self.kahraba.get()}\t    \t    ادوات الكهرباء")
        self.textarea.insert(END,"\n==================================")
        self.textarea.insert(END,f"\n{self.totalall}\t    \t    الاجمالي")
        self.textarea.insert(END,"\n==================================")

    def clear(self):
        self.q1.set(0)
        self.q2.set(0)
        self.q3.set(0)
        self.q4.set(0)
        self.q5.set(0)
        self.q6.set(0)
        self.q7.set(0)
        self.q8.set(0)
        self.q9.set(0)
        self.q10.set(0)
        self.q12.set(0)
        self.q13.set(0)
        self.q14.set(0)
        self.q15.set(0)
        self.q16.set(0)
        self.q17.set(0)
        self.q16.set(0)
        self.q17.set(0)
        self.q18.set(0)

        self.qq1.set(0)
        self.qq2.set(0)
        self.qq3.set(0)
        self.qq4.set(0)
        self.qq5.set(0)
        self.qq6.set(0)
        self.qq7.set(0)
        self.qq8.set(0)
        self.qq9.set(0)
        self.qq10.set(0)
        self.qq11.set(0)
        self.qq12.set(0)
        self.qq13.set(0)
        self.qq14.set(0)
        self.qq15.set(0)
        self.qq16.set(0)
        self.qq17.set(0)
        self.qq16.set(0)
        self.qq17.set(0)
        self.qq18.set(0)
        
        self.qqq1.set(0)
        self.qqq2.set(0)
        self.qqq3.set(0)
        self.qqq4.set(0)
        self.qqq5.set(0)
        self.qqq6.set(0)
        self.qqq7.set(0)
        self.qqq8.set(0)
        self.qqq9.set(0)
        self.qqq10.set(0)
        self.qqq11.set(0)
        self.qqq12.set(0)
        self.qqq13.set(0)
        self.qqq14.set(0)
        self.qqq15.set(0)

        self.bacoliat.set(0)
        self.adoat.set(0)
        self.kahraba.set(0)

        self.namo.set("")
        self.phono.set("")
        self.fatora.set("")


    def close(self):
        self.root.destroy()    
    



    def save(self):
        
        op = messagebox.askyesno("حفظ","هل تريد حفظ الفاتورة")
        if op > 0 :
            self.bb = (self.textarea.get("1.0",END))

            file_path =  r"C:\Users\AHMED\Desktop\Market\buy\\" + self.fatora.get() + ".txt"
            # Use the open() function with appropriate integer flags
            # 'w' corresponds to O_WRONLY|O_CREAT|O_TRUNC in the C API
            flags = os.O_WRONLY | os.O_CREAT | os.O_TRUNC
            mode = 0o777  # Octal permission mode, e.g., 777

            with os.fdopen(os.open(file_path, flags, mode), 'w', encoding='utf-8') as file:
                file.write(self.bb)
      



root = Tk()
ob = Super(root)
root.mainloop()