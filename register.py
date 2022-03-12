from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from mysql.connector import *

class register:
    def __init__(self,root):
        self.root2=root
        self.root2.title('Register')
        self.root2.geometry('900x700+0+0')

       #*******vaiables****
        self.fname=StringVar()
        self.lname=StringVar()
        self.contact=StringVar()
        self.email=StringVar()
        self.sq=StringVar()
        self.sa=StringVar()
        self.passw=StringVar()
        self.cp=StringVar()


         #***********main frame******
        frame=Frame(self.root2,bg='white')
        frame.place(x=10,y=50,width=800,height=550)

        reg_lbl=Label(frame,text='REGISTER HERE',font=('times new roman',20,'bold'),fg='darkgreen')
        reg_lbl.place(x=20,y=20)


        #********label and entry******

        #first row
        fname=Label(frame,text='First Name',font=('times new roman',15,'bold'),bg='white')
        fname.place(x=50,y=100)

        fname_entry=ttk.Entry(frame,textvariable=self.fname,font=('times new roman',15))
        fname_entry.place(x=50,y=130,width=250)

        lname=Label(frame,text='Last Name',font=('times new roman',15,'bold'),bg='white')
        lname.place(x=370,y=100)

        lname_entry=ttk.Entry(frame,textvariable=self.lname,font=('times new roman',15))
        lname_entry.place(x=370,y=130,width=250)


        #second row
        con=Label(frame,text='Contact No',font=('times new roman',15,'bold'),bg='white')
        con.place(x=50,y=170)

        c_entry=ttk.Entry(frame,textvariable=self.contact,font=('times new roman',15))
        c_entry.place(x=50,y=200,width=250)


        email=Label(frame,text='Email',font=('times new roman',15,'bold'),bg='white')
        email.place(x=370,y=170)

        e_entry=ttk.Entry(frame,textvariable=self.email,font=('times new roman',15))
        e_entry.place(x=370,y=200,width=250)


        #third row
        sec=Label(frame,text='Select security question',font=('times new roman',15,'bold'),bg='white')
        sec.place(x=50,y=240)

        self.combo_sec=ttk.Combobox(frame,textvariable=self.sq,font=('times new roman',15,'bold'),state='readonly')
        self.combo_sec['values']=('select','your birth place','your bestfriend name','your pet name')
        self.combo_sec.current(0)
        self.combo_sec.place(x=50,y=270,width=250)
        

        sec_ans=Label(frame,text='Security Answer',font=('times new roman',15,'bold'),bg='white')
        sec_ans.place(x=370,y=240)

        sec_entry=ttk.Entry(frame,textvariable=self.sa,font=('times new roman',15))
        sec_entry.place(x=370,y=270,width=250)

        #fourth row
        passw=Label(frame,text='Password',font=('times new roman',15,'bold'),bg='white')
        passw.place(x=50,y=310)

        p_entry=ttk.Entry(frame,textvariable=self.passw,font=('times new roman',15))
        p_entry.place(x=50,y=340,width=250)


        cp=Label(frame,text='Confirm password',font=('times new roman',15,'bold'),bg='white')
        cp.place(x=370,y=310)

        e_entry=ttk.Entry(frame,textvariable=self.cp,font=('times new roman',15))
        e_entry.place(x=370,y=340,width=250)


        #************checkbox****
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text='I Agree The Terms And Conditions',font=('times new roman',12),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)


        #butoons
        img=Image.open(r'C:\Users\MAMATA\Desktop\pip\reg.jpg')
        img=img.resize((200,60),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage1,borderwidth=0,command=self.register_data,cursor='hand2',font=('times new roman',15,'bold'))
        b1.place(x=10,y=420,width=200)

             
        img1=Image.open(r'C:\Users\MAMATA\Desktop\pip\last.jpg')
        img1=img1.resize((200,63),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img1)
        b2=Button(frame,image=self.photoimage2,borderwidth=0,cursor='hand2',font=('times new roman',15,'bold'))
        b2.place(x=350,y=420,width=200)


    #function declaration
    def register_data(self):
        if self.fname.get()=="" or self.email.get()=="" or self.sq.get()=='selct':
            messagebox.showerror('error','All fields required',parent=self.root2)
        elif self.passw.get()!=self.cp.get():
            messagebox.showerror('error','Password and confirm password must be same',parent=self.root2)
        elif self.var_check.get()==0:
             messagebox.showerror('error','Please agree our terms and conditions',parent=self.root2)
        else:
            conn=connect(host='localhost',user='root',password='8310728642',database='mam')
            cur=conn.cursor()
            query=('select * from register where email=%s')
            value=(self.email.get(),)
            cur.execute(query,value)

            row=cur.fetchone()
            if row!=None:
                messagebox.showerror('error','User already exits,please try another email',parent=self.root2)
            else:
                cur.execute('insert into register values(%s,%s,%s,%s,%s,%s,%s)',(\
                    self.fname.get(),self.lname.get(),\
                    self.contact.get(),self.email.get(),\
                    self.sq.get(),self.sa.get(),self.passw.get()))
            conn.commit()
            conn.close()
            messagebox.showinfo('info','Registerd successfully',parent=self.root2)
        
        


        
        

        



        
        

        

            



        
        

        
        




if __name__=='__main__':
    root=Tk()
    app=register(root)
    root.mainloop()
    
        
