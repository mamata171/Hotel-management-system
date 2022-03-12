from tkinter import *      
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector 
import random
from tkinter import messagebox
from time import strptime
from datetime import datetime

class roomdetails:
    def __init__(self,root):
        self.root=root
        self.root.title('ROOM DETAILS')
        self.root.geometry('1295x550+230+220')


        #title
        lbl_title=Label(self.root,text='ROOM DETAILS',font=('times new roman',30,'bold'),bg='black',fg='gold',bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=40)

        #logo
        img2=Image.open(r'C:\Users\MAMATA\Desktop\pip\paradise.jpg')
        img2=img2.resize((100,40),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)

        #lable frame
        label_frameleft=LabelFrame(self.root,bd=2,relief=RIDGE,text='Room details',padx=2,font=('times new roman',12,'bold'))
        label_frameleft.place(x=8,y=50,width=500,height=400)

        #floor label
        lbl_floor=Label(label_frameleft,text='Floor',font=('times new roman',12,'bold'),padx=4,pady=6)
        lbl_floor.grid(row=0,column=0)

        self.var_floor=StringVar()
        entry_floor=ttk.Entry(label_frameleft,textvariable=self.var_floor,width=20,font=('times new roman',13,'bold'))
        entry_floor.grid(row=0,column=1)

        #room number
        lbl_rno=Label(label_frameleft,text='Room number',font=('times new roman',12,'bold'),padx=4,pady=6)
        lbl_rno.grid(row=2,column=0)

        self.var_rno=StringVar()
        entry_rno=ttk.Entry(label_frameleft,textvariable=self.var_rno,width=20,font=('times new roman',13,'bold'))
        entry_rno.grid(row=2,column=1,padx=20)

        #room type
        lbl_rt=Label(label_frameleft,text='Room type',font=('times new roman',12,'bold'),padx=4,pady=6)
        lbl_rt.grid(row=3,column=0)

        self.var_rt=StringVar()
        entry_rt=ttk.Entry(label_frameleft,textvariable=self.var_rt,width=20,font=('times new roman',13,'bold'))
        entry_rt.grid(row=3,column=1,padx=20)

        #images
        img3=Image.open(r'C:\Users\MAMATA\Desktop\pip\single.jpg')
        img3=img3.resize((250,200),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg=Label(self.root,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg.place(x=8,y=180,width=250,height=200)

        img4=Image.open(r'C:\Users\MAMATA\Desktop\pip\room2.jpg')
        img4=img4.resize((260,200),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lblimg=Label(self.root,image=self.photoimg4,bd=4,relief=RIDGE)
        lblimg.place(x=250,y=180,width=260,height=200)



        #***************buttons***********
        btn_frame=Frame(label_frameleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=330,width=412,height=40)

        btn_add=Button(btn_frame,text='Add',command=self.add_data,font=('arial', 12 ,'bold'),bg='black',fg='gold',width=9)
        btn_add.grid(row=0,column=0,padx=1)

        btn_upd=Button(btn_frame,text='Update',command=self.update,font=('arial', 12 ,'bold'),bg='black',fg='gold',width=9)
        btn_upd.grid(row=0,column=1,padx=1)

        btn_delete=Button(btn_frame,text='Delete',command=self.delete,font=('arial', 12 ,'bold'),bg='black',fg='gold',width=9)
        btn_delete.grid(row=0,column=2,padx=1)

        btn_res=Button(btn_frame,text='Reset',command=self.reset,font=('arial', 12 ,'bold'),bg='black',fg='gold',width=9)
        btn_res.grid(row=0,column=3,padx=1)

        #********search systm********
        label_table=LabelFrame(self.root,bd=2,relief=RIDGE,text='Show Room Details',padx=2,font=('times new roman',12,'bold'))
        label_table.place(x=550,y=50,width=500,height=400)

        scroll_x=ttk.Scrollbar(label_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(label_table,orient=VERTICAL)

        self.room_details_table=ttk.Treeview(label_table,column=('floor','roomno','roomtype'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        self.room_details_table.heading('floor',text='Floor ')
        self.room_details_table.heading('roomno',text='Room no')
        self.room_details_table.heading('roomtype',text='Room type ')
        
        self.room_details_table['show']='headings'

        self.room_details_table.column('floor',width=100)
        self.room_details_table.column('roomno',width=100)
        self.room_details_table.column('roomtype',width=100)
        
        
        self.room_details_table.pack(fill=BOTH,expand=1)
        self.room_details_table.bind('<ButtonRelease-1>',self.get_cur)
        self.fetch_details()
        


    def add_data(self):
        if self.var_floor.get()=="" or self.var_rt.get()=="":
            messagebox.showerror("error","all fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',passwd='8310728642',database='mam')
                my_cur=conn.cursor()
                my_cur.execute('insert into details values(%s,%s,%s)',(self.var_floor.get(),\
                                                                                   self.var_rno.get(),\
                                                                                   self.var_rt.get()))
                                                                                   
                conn.commit()
                self.fetch_details()
                conn.close()
                messagebox.showinfo("success",'New Room added successfully',parent=self.root)
            except Exception as es:
                messagebox.showwarning('warning',f'some thing went wrong:{str(es)}')


    #fetch data
    def fetch_details(self):
        conn=mysql.connector.connect(host='localhost',username='root',passwd='8310728642',database='mam')
        my_cur=conn.cursor()
        my_cur.execute('select * from details')
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

        self.var_floor.set(row[0]),self.var_rno.set(row[1]),\
                                                              self.var_rt.set(row[2])


    #update fun
    def update(self):
        if self.var_floor.get()=="":
            messagebox.showerror('error','please enter floor number',parent=self.root)
        else:
            conn=mysql.connector.connect(host='localhost',username='root',passwd='8310728642',database='mam')
            my_cur=conn.cursor()
            my_cur.execute('update details set floor=%s,roomtype=%s where Roomno=%s',\
                           (self.var_floor.get(),\
                            self.var_rt.get(),\
                            self.var_rno.get()))
                            
            conn.commit()
            self.fetch_details()
            messagebox.showinfo('info','room details has been updated')
            conn.close()

    #delete funcrion
    def delete(self):
        mdelete=messagebox.askyesno("hotel management system","do you want to delete this room ",parent=self.root)
        if mdelete>0:
            conn=mysql.connector.connect(host='localhost',username='root',passwd='8310728642',database='mam')
            my_cur=conn.cursor()
            query="delete from details Where Roomno=%s"
            value=(self.var_rno.get(),)
            my_cur.execute(query,value)
        else:
            if not mdelete:
                return
        conn.commit()
        self.fetch_details()
        conn.close()


    #Reset function
    def reset(self):
        self.var_floor.set(""),\
                                   self.var_rno.set(""),\
                                   self.var_rt.set("")
                                   








if __name__=="__main__":
    root=Tk()
    obj=roomdetails(root)
    root.mainloop()
    
