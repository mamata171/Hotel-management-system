from tkinter import *      
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector 
import random
from tkinter import messagebox 

class cust_win:
    def __init__(self,root):
        self.root=root
        self.root.title('Hotel Management System')
        self.root.geometry('1295x550+230+220')
        
        #******variables***
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        
        self.var_cust_name=StringVar()
        self.var_father=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_address=StringVar()
        self.var_idproof=StringVar()
        self.var_idnumber=StringVar()
        


        #title
        lbl_title=Label(self.root,text='ADD CUSTOMER DETAILS',font=('times new roman',30,'bold'),bg='black',fg='gold',bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=40)

        #logo
        img2=Image.open(r'C:\Users\MAMATA\Desktop\pip\paradise.jpg')
        img2=img2.resize((100,40),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)

        #lable frame
        label_frameleft=LabelFrame(self.root,bd=2,relief=RIDGE,text='CUSTOMER DETAILS',padx=2,font=('times new roman',12,'bold'))
        label_frameleft.place(x=5,y=50,width=425,height=490)

        #lables and entries
        cust_ref=Label(label_frameleft,text='customer ref',font=('times new roman',12,'bold'),padx=2,pady=6)
        cust_ref.grid(row=0,column=0,sticky=W)

        entry_ref=ttk.Entry(label_frameleft,textvariable=self.var_ref,state='readonly',width=29,font=('times new roman',13,'bold'))
        entry_ref.grid(row=0,column=1)


        #customer name
        cname=Label(label_frameleft,text='Customer name',font=('times new roman',12,'bold'),padx=2,pady=6)
        cname.grid(row=1,column=0,sticky=W)

        entry_cname=ttk.Entry(label_frameleft,textvariable=self.var_cust_name,width=29,font=('times new roman',13,'bold'))
        entry_cname.grid(row=1,column=1)


        #father name
        Father_name=Label(label_frameleft,text='Father name',font=('times new roman',12,'bold'),padx=2,pady=6)
        Father_name.grid(row=2,column=0,sticky=W)

        entry_fn=ttk.Entry(label_frameleft,textvariable=self.var_father,width=29,font=('times new roman',13,'bold'))
        entry_fn.grid(row=2,column=1)


        #gender
        gen=Label(label_frameleft,text='Gender',font=('times new roman',12,'bold'),padx=2,pady=6)
        gen.grid(row=3,column=0,sticky=W)

        combo_gen=ttk.Combobox(label_frameleft,textvariable=self.var_gender,font=('times new roman',13,'bold'),width=27,state='readonly')
        combo_gen['value']=('Male','Female','Other')
        combo_gen.current(0)
        combo_gen.grid(row=3,column=1)
                           
        
        #postcode
        postcode=Label(label_frameleft,text='Postcode',font=('times new roman',12,'bold'),padx=2,pady=6)
        postcode.grid(row=4,column=0,sticky=W)

        entry_post=ttk.Entry(label_frameleft,textvariable=self.var_post,width=29,font=('times new roman',13,'bold'))
        entry_post.grid(row=4,column=1)


        #mobile
        mobile=Label(label_frameleft,text='Mobile',font=('times new roman',12,'bold'),padx=2,pady=6)
        mobile.grid(row=5,column=0,sticky=W)

        entry_mob=ttk.Entry(label_frameleft,textvariable=self.var_mobile,width=29,font=('times new roman',13,'bold'))
        entry_mob.grid(row=5,column=1)


        #email
        email=Label(label_frameleft,text='Email',font=('times new roman',12,'bold'),padx=2,pady=6)
        email.grid(row=6,column=0,sticky=W)

        entry_eml=ttk.Entry(label_frameleft,textvariable=self.var_email,width=29,font=('times new roman',13,'bold'))
        entry_eml.grid(row=6,column=1)


        #nationality
        nationality=Label(label_frameleft,text='Nationality',font=('times new roman',12,'bold'),padx=2,pady=6)
        nationality.grid(row=7,column=0,sticky=W)

        combo_nat=ttk.Combobox(label_frameleft,textvariable=self.var_nationality,font=('times new roman',13,'bold'),width=27,state='readonly')
        combo_nat['value']=('Indian','American','Britist')
        combo_nat.current(0)
        combo_nat.grid(row=7,column=1)


        #ID proof type
        idp=Label(label_frameleft,text='Id Proof Type',font=('times new roman',12,'bold'),padx=2,pady=6)
        idp.grid(row=8,column=0,sticky=W)

        combo_idp=ttk.Combobox(label_frameleft,textvariable=self.var_idproof,font=('times new roman',13,'bold'),width=27,state='readonly')
        combo_idp['value']=('Adharcard','Driving_licence','Passport')
        combo_idp.current(0)
        combo_idp.grid(row=8,column=1)


        #Id number
        id=Label(label_frameleft,text='Id Number',font=('times new roman',12,'bold'),padx=2,pady=6)
        id.grid(row=9,column=0,sticky=W)

        entry_id=ttk.Entry(label_frameleft,textvariable=self.var_idnumber,width=29,font=('times new roman',13,'bold'))
        entry_id.grid(row=9,column=1)


        #Address
        addr=Label(label_frameleft,text='Address',font=('times new roman',12,'bold'),padx=2,pady=6)
        addr.grid(row=10,column=0,sticky=W)

        entry_addr=ttk.Entry(label_frameleft,textvariable=self.var_address,width=29,font=('times new roman',13,'bold'))
        entry_addr.grid(row=10,column=1)


        #*****Buttons******
        btn_frame=Frame(label_frameleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btn_add=Button(btn_frame,text='Add',command=self.add_data,font=('arial', 12 ,'bold'),bg='black',fg='gold',width=9)
        btn_add.grid(row=0,column=0,padx=1)

        btn_upd=Button(btn_frame,text='Update',command=self.update,font=('arial', 12 ,'bold'),bg='black',fg='gold',width=9)
        btn_upd.grid(row=0,column=1,padx=1)

        btn_delete=Button(btn_frame,text='Delete',command=self.mdelete,font=('arial', 12 ,'bold'),bg='black',fg='gold',width=9)
        btn_delete.grid(row=0,column=2,padx=1)

        btn_res=Button(btn_frame,text='Reset',command=self.reset,font=('arial', 12 ,'bold'),bg='black',fg='gold',width=9)
        btn_res.grid(row=0,column=3,padx=1)


        #********tabel frame search systm********
        label_table=LabelFrame(self.root,bd=2,relief=RIDGE,text='View details And Search record',padx=2,font=('times new roman',12,'bold'))
        label_table.place(x=435,y=50,width=860,height=490)

        serby=Label(label_table,text='Search By',font=('arial',12,'bold'),fg='white',bg='red')
        serby.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar()
        combo_ser=ttk.Combobox(label_table,textvariable=self.search_var,font=('arial',12,'bold'),width=18,state='readonly')
        combo_ser['value']=('Mobile','ref')
        combo_ser.current(0)
        combo_ser.grid(row=0,column=1,padx=2)
                                  
        self.txt_search=StringVar()                         
        entry_ser=ttk.Entry(label_table,textvariable=self.txt_search,width=24,font=('arial',13,'bold'))
        entry_ser.grid(row=0,column=2,padx=2)

        btn_Search=Button(label_table,text='Search',command=self.search,font=('arial', 11 ,'bold'),bg='black',fg='gold',width=9)
        btn_Search.grid(row=0,column=3,padx=2)

        btn_showall=Button(label_table,text='Show All',command=self.fetch_details,font=('arial',11,'bold'),bg='black',fg='gold',width=9)
        btn_showall.grid(row=0,column=4,padx=2)


        #*******show data table*****
        det_table=Frame(label_table,bd=2,relief=RIDGE)
        det_table.place(x=0,y=50,width=860,height=350)

        scroll_x=ttk.Scrollbar(det_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(det_table,orient=VERTICAL)

        self.cust_details_table=ttk.Treeview(det_table,column=('ref','name','father name','gender','post','mobile','email','nationality','idproof','idnumber','address'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.cust_details_table.xview)
        scroll_y.config(command=self.cust_details_table.yview)

        self.cust_details_table.heading('ref',text='Refer no')
        self.cust_details_table.heading('name',text='Name')
        self.cust_details_table.heading('father name',text='Father name')
        self.cust_details_table.heading('gender',text='Gender')
        self.cust_details_table.heading('post',text='Postcode')
        self.cust_details_table.heading('mobile',text='Mobile')
        self.cust_details_table.heading('email',text='Email')
        self.cust_details_table.heading('nationality',text='Nationality')
        self.cust_details_table.heading('idproof',text='Id proof')
        self.cust_details_table.heading('idnumber',text='Id number')
        self.cust_details_table.heading('address',text='Address')

        self.cust_details_table['show']='headings'

        self.cust_details_table.column('ref',width=100)
        self.cust_details_table.column('name',width=100)
        self.cust_details_table.column('father name',width=100)
        self.cust_details_table.column('gender',width=100)
        self.cust_details_table.column('post',width=100)
        self.cust_details_table.column('mobile',width=100)
        self.cust_details_table.column('email',width=100)
        self.cust_details_table.column('nationality',width=100)
        self.cust_details_table.column('idproof',width=100)
        self.cust_details_table.column('idnumber',width=100)
        self.cust_details_table.column('address',width=100)

        self.cust_details_table.pack(fill=BOTH,expand=1)
        self.cust_details_table.bind('<ButtonRelease-1>',self.get_cur)
        self.fetch_details()
        
        

    def add_data(self):
        if self.var_mobile.get()=="" or self.var_father.get()=="":
            messagebox.showerror("error","all fields are required",parent=self.root)
        else:
            try:
               conn=mysql.connector.connect(host='localhost',username='root',passwd='8310728642',database='mam')
               my_cur=conn.cursor()
               my_cur.execute('insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(self.var_ref.get(),\
                                                                                               self.var_cust_name.get(),self.var_father.get(),self.var_gender.get(),\
                                                                                               self.var_post.get(),self.var_mobile.get(),self.var_email.get(),self.var_nationality.get(),\
                                                                                               self.var_idproof.get(),self.var_idnumber.get(),self.var_address.get()))
               
                  
               conn.commit()
               self.fetch_details()
               conn.close()
               messagebox.showinfo("success",'customer has been added',parent=self.root)
            except Exception as es:
                messagebox.showwarning('warning',f'some thing went wrong:{str(es)}',parent=self.root)


    def fetch_details(self):
        conn=mysql.connector.connect(host='localhost',username='root',passwd='8310728642',database='mam')
        my_cur=conn.cursor()
        my_cur.execute('select * from customer')
        rows=my_cur.fetchall()
        if len(rows)!=0:
            self.cust_details_table.delete(*self.cust_details_table.get_children())
            for i in rows:
                self.cust_details_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
                
                    
    def get_cur(self,event=""):
        cur_row=self.cust_details_table.focus()
        content=self.cust_details_table.item(cur_row)
        row=content['values']

        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_father.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_post.set(row[4]),
        self.var_mobile.set(row[5]),
        self.var_email.set(row[6]),
        self.var_nationality.set(row[7]),
        self.var_address.set(row[8]),
        self.var_idproof.set(row[9]),
        self.var_idnumber.set(row[10])
        
    def update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror('error','please enter mobile number',parent=self.root)
        else:
            conn=mysql.connector.connect(host='localhost',username='root',passwd='8310728642',database='mam')
            my_cur=conn.cursor()
            my_cur.execute('update customer set Name=%s,Father=%s,Gender=%s,Postcode=%s,Mobile=%s,Email=%s,Nationality=%s,Idproof=%s,Idnumber=%s,Address=%s where Ref=%s',\
                           (self.var_cust_name.get(),\
                            self.var_father.get(),\
                            self.var_gender.get(),\
                            self.var_post.get(),\
                            self.var_mobile.get(),\
                            self.var_email.get(),\
                            self.var_nationality.get(),\
                            self.var_idproof.get(),\
                            self.var_idnumber.get(),\
                            self.var_address.get(),\
                            self.var_ref.get()))
            conn.commit()
            self.fetch_details()
            messagebox.showinfo('info','customer details has been updated',parent=self.root)
            conn.close()

                                                                                                                                                                                                                                                                                      
        
    def  mdelete(self):
        mdelete=messagebox.askyesno("hotel management system","do you want to delete this customer",parent=self.root)
        if mdelete>0:
            conn=mysql.connector.connect(host='localhost',username='root',passwd='8310728642',database='mam')
            my_cur=conn.cursor()
            query="delete from customer Where Ref =%s"
            value=(self.var_ref.get(),)
            my_cur.execute(query,value)
        else:
            if not mdelete:
                return
        conn.commit()
        self.fetch_details()
        conn.close()


    def reset(self):
        self.var_cust_name.set(""),\
                                     self.var_father.set(""),\
                                     self.var_post.set(""),\
                                     self.var_mobile.set(""),\
                                     self.var_email.set(""),\
                                     self.var_idnumber.set(""),\
                                     self.var_address.set("")
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))


    def search(self):
        conn=mysql.connector.connect(host='localhost',username='root',passwd='8310728642',database='mam')
        my_cur=conn.cursor()
        my_cur.execute(" select * from customer where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cur.fetchall()
        if len(rows)!=0:
            self.cust_details_table.delete(*self.cust_details_table.get_children())
            for i in rows:
                self.cust_details_table.insert("",END,values=i)
            conn.commit()
        conn.close()
                
                                           
                    
                                   
        
    
                                                                      
        

   
        
        




        


        

        


if __name__=="__main__":
    root=Tk()
    obj=cust_win(root)
    root.mainloop()
    
                              
        
        






        
