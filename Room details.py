from tkinter import *      
from PIL import Image,ImageTk
from tkinter import ttk
from mysql.connector import *
import random
from tkinter import messagebox
from time import strptime
from datetime import datetime

class roombooking:
    def __init__(self,root):
        self.root=root
        self.root.title('Hotel Management System')
        self.root.geometry('1295x550+220+220')

        #************variables*********
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_avalrooms=StringVar()
        self.var_meal=StringVar()
        self.var_days=StringVar()
        self.var_paidtax=StringVar()
        self.var_subtotal=StringVar()
        self.var_total=StringVar()


        #title
        lbl_title=Label(self.root,text='WEL COME TO ROOM BOOKING',font=('times new roman',30,'bold'),bg='black',fg='gold',bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=40)

        #logo
        img2=Image.open(r'C:\Users\MAMATA\Desktop\pip\paradise.jpg')
        img2=img2.resize((100,40),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)

        #lable frame
        label_frameleft=LabelFrame(self.root,bd=2,relief=RIDGE,text='Room Booking',padx=2,font=('times new roman',12,'bold'))
        label_frameleft.place(x=5,y=50,width=425,height=490)


        #**************lables and entry****************
        #cust contact
        cust_contact=Label(label_frameleft,text='customer Contact',font=('times new roman',12,'bold'),padx=2,pady=6)
        cust_contact.grid(row=0,column=0,sticky=W)

        entry_contact=ttk.Entry(label_frameleft,textvariable=self.var_contact,width=20,font=('times new roman',13,'bold'))
        entry_contact.grid(row=0,column=1,sticky=W)

        #button fetch data
        btn_fetch_data=Button(label_frameleft,text='Fetch Data',command=self.fetch_contact,font=('arial', 8 ,'bold'),bg='black',fg='gold',width=8)
        btn_fetch_data.place(x=335,y=4)

        #chechk in date 
        checkin=Label(label_frameleft,text='Check in Date',font=('times new roman',12,'bold'),padx=2,pady=6)
        checkin.grid(row=1,column=0,sticky=W)

        txtcheckin=ttk.Entry(label_frameleft,textvariable=self.var_checkin,width=29,font=('times new roman',13,'bold'))
        txtcheckin.grid(row=1,column=1)


        #chech out date
        checkout=Label(label_frameleft,text='check out Date',font=('times new roman',12,'bold'),padx=2,pady=6)
        checkout.grid(row=2,column=0,sticky=W)

        txtcheckout=ttk.Entry(label_frameleft,textvariable=self.var_checkout,width=29,font=('times new roman',13,'bold'))
        txtcheckout.grid(row=2,column=1)


        #Room type
        room=Label(label_frameleft,text='Room type',font=('times new roman',12,'bold'),padx=2,pady=6)
        room.grid(row=3,column=0,sticky=W)

        conn=connect(host='localhost',username='root',passwd='8310728642',database='mam')
        my_cur=conn.cursor()
        my_cur.execute('select roomtype from details')
        rows=my_cur.fetchall()
        combo_room=ttk.Combobox(label_frameleft,textvariable=self.var_roomtype,font=('times new roman',13,'bold'),width=27,state='readonly')
        combo_room['value']=rows
        combo_room.current(0)
        combo_room.grid(row=3,column=1)
                           
        
        #available rooms
        avlroom=Label(label_frameleft,text='Available Rooms',font=('times new roman',12,'bold'),padx=2,pady=6)
        avlroom.grid(row=4,column=0,sticky=W)

        conn=connect(host='localhost',username='root',passwd='8310728642',database='mam')
        my_cur=conn.cursor()
        my_cur.execute('select Roomno from details')
        row=my_cur.fetchall()

        combo_avlroom=ttk.Combobox(label_frameleft,textvariable=self.var_avalrooms,font=('times new roman',13,'bold'),width=27,state='readonly')
        combo_avlroom['value']=row
        combo_avlroom.current(0)
        combo_avlroom.grid(row=4,column=1)

        
        #Meal
        lblmeal=Label(label_frameleft,text='Meal',font=('times new roman',12,'bold'),padx=2,pady=6)
        lblmeal.grid(row=5,column=0,sticky=W)

        txtlblmeal=ttk.Entry(label_frameleft,textvariable=self.var_meal,width=29,font=('times new roman',13,'bold'))
        txtlblmeal.grid(row=5,column=1)


        #no of days
        lblnoofdays=Label(label_frameleft,text='Number of days',font=('times new roman',12,'bold'),padx=2,pady=6)
        lblnoofdays.grid(row=6,column=0,sticky=W)

        txtlblnoofdays=ttk.Entry(label_frameleft,textvariable=self.var_days,width=29,font=('times new roman',13,'bold'))
        txtlblnoofdays.grid(row=6,column=1)


        #paid tax
        lblpaidtax=Label(label_frameleft,text='Paid Tax',font=('times new roman',12,'bold'),padx=2,pady=6)
        lblpaidtax.grid(row=7,column=0,sticky=W)
        txtpaidtax=ttk.Entry(label_frameleft,textvariable=self.var_paidtax,width=29,font=('times new roman',13,'bold'))
        txtpaidtax.grid(row=7,column=1)


        #sub total
        lblsubtot=Label(label_frameleft,text='Sub Total',font=('times new roman',12,'bold'),padx=2,pady=6)
        lblsubtot.grid(row=8,column=0,sticky=W)
        txtsubtot=ttk.Entry(label_frameleft,textvariable=self.var_subtotal,width=29,font=('times new roman',13,'bold'))
        txtsubtot.grid(row=8,column=1)

        
        #total cost
        lbltot=Label(label_frameleft,text='Total cost',font=('times new roman',12,'bold'),padx=2,pady=6)
        lbltot.grid(row=9,column=0,sticky=W)

        txtlbltot=ttk.Entry(label_frameleft,textvariable=self.var_total,width=29,font=('times new roman',13,'bold'))
        txtlbltot.grid(row=9,column=1)

        #****Bill button***
        btnbill=Button(label_frameleft,text='Bill',command=self.total,font=('arial', 10 ,'bold'),bg='black',fg='gold',width=9)
        btnbill.grid(row=10,column=0,padx=1,sticky=W)

        

        #***************buttons***********
        btn_frame=Frame(label_frameleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btn_add=Button(btn_frame,text='Add',command=self.add_data,font=('arial', 12 ,'bold'),bg='black',fg='gold',width=9)
        btn_add.grid(row=0,column=0,padx=1)

        btn_upd=Button(btn_frame,text='Update',command=self.update,font=('arial', 12 ,'bold'),bg='black',fg='gold',width=9)
        btn_upd.grid(row=0,column=1,padx=1)

        btn_delete=Button(btn_frame,text='Delete',command=self.delete,font=('arial', 12 ,'bold'),bg='black',fg='gold',width=9)
        btn_delete.grid(row=0,column=2,padx=1)

        btn_res=Button(btn_frame,text='Reset',command=self.reset,font=('arial', 12 ,'bold'),bg='black',fg='gold',width=9)
        btn_res.grid(row=0,column=3,padx=1)

        #********right side image*******
        img3=Image.open(r'C:\Users\MAMATA\Desktop\pip\bed.jpg')
        img3=img3.resize((520,310),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg1=Label(self.root,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg1.place(x=760,y=50,width=520,height=310)

        
        #********search systm********
        label_table=LabelFrame(self.root,bd=2,relief=RIDGE,text='View details And Search record',padx=2,font=('times new roman',12,'bold'))
        label_table.place(x=435,y=280,width=860,height=260)

        serby=Label(label_table,text='Search By',font=('arial',12,'bold'),fg='white',bg='red')
        serby.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar()
        combo_ser=ttk.Combobox(label_table,textvariable=self.search_var,font=('arial',12,'bold'),width=18,state='readonly')
        combo_ser['value']=('Contact','Room')
        combo_ser.current(0)
        combo_ser.grid(row=0,column=1,padx=2)
                                  
        self.txt_search=StringVar()                         
        entry_ser=ttk.Entry(label_table,textvariable=self.txt_search,width=24,font=('arial',13,'bold'))
        entry_ser.grid(row=0,column=2,padx=2)

        btn_Search=Button(label_table,text='Search',command=self.search,font=('arial', 11 ,'bold'),bg='black',fg='gold',width=9)
        btn_Search.grid(row=0,column=3,padx=2)

        btn_showall=Button(label_table,text='Show All',command=self.fetch_details,font=('arial',11,'bold'),bg='black',fg='gold',width=9)
        btn_showall.grid(row=0,column=4,padx=2)


        #*************show table************
        det_table=Frame(label_table,bd=2,relief=RIDGE)
        det_table.place(x=0,y=50,width=860,height=180)

        scroll_x=ttk.Scrollbar(det_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(det_table,orient=VERTICAL)

        self.room_details_table=ttk.Treeview(det_table,column=('contact','checkin','checkout','roomtype','avalrooms','meal','days'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_details_table.xview)
        scroll_y.config(command=self.room_details_table.yview)

        self.room_details_table.heading('checkin',text='Checkin date')
        self.room_details_table.heading('contact',text='Contact')
        self.room_details_table.heading('checkout',text='Checkout date ')
        self.room_details_table.heading('roomtype',text='Room types')
        self.room_details_table.heading('avalrooms',text='Available rooms')
        self.room_details_table.heading('meal',text='Meal')
        self.room_details_table.heading('days',text='No of dyas')
        
        self.room_details_table['show']='headings'

        self.room_details_table.column('contact',width=100)
        self.room_details_table.column('checkin',width=100)
        self.room_details_table.column('checkout',width=100)
        self.room_details_table.column('roomtype',width=100)
        self.room_details_table.column('avalrooms',width=100)
        self.room_details_table.column('meal',width=100)
        self.room_details_table.column('days',width=100)
        
        self.room_details_table.pack(fill=BOTH,expand=1)
        self.room_details_table.bind('<ButtonRelease-1>',self.get_cur)
        self.fetch_details()


    #*********************all data fetch********
    def fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("eror",'please enter contact number',parent=self.root)
        else:
            conn=connect(host='localhost',username='root',passwd='8310728642',database='mam')
            my_cur=conn.cursor()
            query=('select Name from customer where mobile=%s')
            value=(self.var_contact.get(),)
            my_cur.execute(query,value)
            row=my_cur.fetchone()

            if row==None:
                messagebox.showerror('error','This number not found',parent=self.root)
            else:
                conn.commit()
                conn.close()

                showdataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showdataframe.place(x=440,y=55,width=290,height=180)

                lblname=Label(showdataframe,text='Name:',font=('arila',12,'bold'))
                lblname.place(x=0,y=0)

                lbl=Label(showdataframe,text=row,font=('arila',12,'bold'))
                lbl.place(x=90,y=0)


                #gender
                conn=connect(host='localhost',username='root',passwd='8310728642',database='mam')
                my_cur=conn.cursor()
                query=('select Gender from customer where mobile=%s')
                value=(self.var_contact.get(),)
                my_cur.execute(query,value)
                row=my_cur.fetchone()

                lblGender=Label(showdataframe,text='Gender:',font=('arila',12,'bold'))
                lblGender.place(x=0,y=30)

                lbl2=Label(showdataframe,text=row,font=('arila',12,'bold'))
                lbl2.place(x=90,y=30)

                #email
                conn=connect(host='localhost',username='root',passwd='8310728642',database='mam')
                my_cur=conn.cursor()
                query=('select Email from customer where mobile=%s')
                value=(self.var_contact.get(),)
                my_cur.execute(query,value)
                row=my_cur.fetchone()

                lblGender=Label(showdataframe,text='Email:',font=('arila',12,'bold'))
                lblGender.place(x=0,y=60)

                lbl2=Label(showdataframe,text=row,font=('arila',12,'bold'))
                lbl2.place(x=90,y=60)

                #nationality
                conn=connect(host='localhost',username='root',passwd='8310728642',database='mam')
                my_cur=conn.cursor()
                query=('select Nationality from customer where mobile=%s')
                value=(self.var_contact.get(),)
                my_cur.execute(query,value)
                row=my_cur.fetchone()

                lblGender=Label(showdataframe,text='Nationality:',font=('arila',12,'bold'))
                lblGender.place(x=0,y=90)

                lbl2=Label(showdataframe,text=row,font=('arila',12,'bold'))
                lbl2.place(x=90,y=90)

                #address
                conn=connect(host='localhost',username='root',passwd='8310728642',database='mam')
                my_cur=conn.cursor()
                query=('select Address from customer where mobile=%s')
                value=(self.var_contact.get(),)
                my_cur.execute(query,value)
                row=my_cur.fetchone()

                lblGender=Label(showdataframe,text='Address:',font=('arila',12,'bold'))
                lblGender.place(x=0,y=120)

                lbl2=Label(showdataframe,text=row,font=('arila',12,'bold'))
                lbl2.place(x=90,y=120)
       
    # add data
    def add_data(self):
        if self.var_contact.get()=="" or self.var_checkin.get()=="":
            messagebox.showerror("error","all fields are required",parent=self.root)
        else:
            try:
                conn=connect(host='localhost',username='root',passwd='8310728642',database='mam')
                my_cur=conn.cursor()
                my_cur.execute('insert into room values(%s,%s,%s,%s,%s,%s,%s)',(self.var_contact.get(),\
                                                                                   self.var_checkin.get(),\
                                                                                   self.var_checkout.get(),\
                                                                                   self.var_roomtype.get(),\
                                                                                   self.var_avalrooms.get(),\
                                                                                   self.var_meal.get(),\
                                                                                   self.var_days.get()))
                conn.commit()
                self.fetch_details()
                conn.close()
                messagebox.showinfo("success",'Room Booked',parent=self.root)
            except Exception as es:
                messagebox.showwarning('warning',f'some thing went wrong:{str(es)}',parent=self.root)

    #fetch data
    def fetch_details(self):
        conn=connect(host='localhost',username='root',passwd='8310728642',database='mam')
        my_cur=conn.cursor()
        my_cur.execute('select * from room')
        rows=my_cur.fetchall()
        if len(rows)!=0:
            self.room_details_table.delete(*self.room_details_table.get_children())
            for i in rows:
                self.room_details_table.insert("",END,values=i)
            conn.commit()
        conn.close()


                    
    def get_cur(self,event=""):
        cur_row=self.room_details_table.focus()
        content=self.room_details_table.item(cur_row)
        row=content['values']

        self.var_contact.set(row[0]),self.var_checkin.set(row[1]),\
                                                                  self.var_checkout.set(row[2]),self.var_roomtype.set(row[3]),\
                                                                  self.var_avalrooms.set(row[4]),self.var_meal.set(row[5]),\
                                                                  self.var_days.set(row[6])


    #update fun
    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror('error','please enter mobile number',parent=self.root)
        else:
            conn=connect(host='localhost',username='root',passwd='8310728642',database='mam')
            my_cur=conn.cursor()
            my_cur.execute('update room set checkin=%s,checkout=%s,roomtype=%s,Room=%s,meal=%s,noofdays=%s  where contact=%s',\
                           (self.var_checkin.get(),\
                            self.var_checkout.get(),\
                            self.var_roomtype.get(),\
                            self.var_avalrooms.get(),\
                            self.var_meal.get(),\
                            self.var_days.get(),\
                            self.var_contact.get()))
            conn.commit()
            self.fetch_details()
            messagebox.showinfo('info','room details has been updated',parent=self.root)
            conn.close()


    #delete funcrion
    def delete(self):
        mdelete=messagebox.askyesno("hotel management system","do you want to delete this room ",parent=self.root)
        if mdelete>0:
            conn=connect(host='localhost',username='root',passwd='8310728642',database='mam')
            my_cur=conn.cursor()
            query="delete from room Where contact=%s"
            value=(self.var_contact.get(),)
            my_cur.execute(query,value)
        else:
            if not mdelete:
                return
        conn.commit()
        self.fetch_details()
        conn.close()


    #Reset function
    def reset(self):
        self.var_contact.set(""),\
                                   self.var_checkin.set(""),\
                                   self.var_checkout.set(""),\
                                   self.var_roomtype.set(""),\
                                   self.var_avalrooms.set(""),\
                                   self.var_meal.set(""),\
                                   self.var_days.set(""),\
                                   self.var_paidtax.set(''),\
                                   self.var_subtotal.set(''),\
                                   self.var_total.set('')

        


    def total(self):
        indate=self.var_checkin.get()
        outdate=self.var_checkout.get()
        indate=datetime.strptime(indate,"%d/%m/%Y")
        outdate=datetime.strptime(outdate,"%d/%m/%Y")
        self.var_days.set(abs(outdate-indate).days)

        if(self.var_meal.get()=="breakfast" and self.var_roomtype.get()=="deluxe"):
            q1=float(300)
            q2=float(800)
            q3=float(self.var_days.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            tax='Rs.'+str('%.2f'%((q5)*0.5))
            st='Rs.'+str('%.2f'%((q5)))
            tt='Rs.'+str('%.2f'%(q5+((q5)*0.1)))
            self.var_paidtax.set(tax)
            self.var_subtotal.set(st)
            self.var_total.set(tt)

        elif(self.var_meal.get()=="lunch" and self.var_roomtype.get()=="single"):
            q1=float(300)
            q2=float(600)
            q3=float(self.var_days.get())
            q4=float(q1+q2)
            q5=float((q3)+q4)
            tax='Rs.'+str('%.2f'%((q5)*0.09))
            st='Rs.'+str('%.2f'%((q5)))
            tt='Rs.'+str('%.2f'%(q5+((q5)*0.1)))
            self.var_paidtax.set(tax)
            self.var_subtotal.set(st)
            self.var_total.set(tt)

        elif(self.var_meal.get()=="dinner" and self.var_roomtype.get()=="double"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_days.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            tax='Rs.'+str('%.2f'%((q5)*0.09))
            st='Rs.'+str('%.2f'%((q5)))
            tt='Rs.'+str('%.2f'%(q5+((q5)*0.1)))
            self.var_paidtax.set(tax)
            self.var_subtotal.set(st)
            self.var_total.set(tt)


    #search funtion
    def search(self):
        conn=connect(host='localhost',username='root',passwd='8310728642',database='mam')
        my_cur=conn.cursor()
        my_cur.execute("select * from room where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cur.fetchall()
        if len(rows)!=0:
            self.room_details_table.delete(*self.room_details_table.get_children())
            for i in rows:
                self.room_details_table.insert("",END,values=i)
            conn.commit()
        conn.close()
                



    

        
            


    
                                       
                                       
                                       
                                       
                                      
        






if __name__=="__main__":
    root=Tk()
    obj=roombooking(root)
    root.mainloop()
    
