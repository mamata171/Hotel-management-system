from tkinter import *      
from PIL import Image , ImageTk
from customer import cust_win
from room import roombooking
from details import roomdetails
from time import strftime
from report import Report

class Hotelmanagementsystem:
    def __init__(self,root):
        self.root=root
        self.root.title('Hotel Management System')
        self.root.geometry('1550x800')

        img1=Image.open(r'C:\Users\MAMATA\Desktop\pip\hotel1.png')
        img1=img1.resize((1550,140),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=140)

        # LOGO
        img2=Image.open(r'C:\Users\MAMATA\Desktop\pip\paradise.jpg')
        img2=img2.resize((230,140),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=230,height=140)
        
        #title
        lbl_title=Label(self.root,text='HOTEL MANAGEMENT SYSTEM',font=('times new roman',40,'bold'),bg='black',fg='gold',bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=50)

        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl=Label(self.root,font=('times new roman',20,'bold'),bg='black',fg='gold')
        lbl.place(x=30,y=140,width=150)
        time()

        # frame for below labels ,main frame
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)

        #label menu
        menu=Label(main_frame,text='MENU',font=('times new roman',20,'bold'),bg='black',fg='gold',bd=4,relief=RIDGE)
        menu.place(x=0,y=0,width=230)

        #another frame below menu for buttons
        button_frame=Frame(main_frame,bd=4,relief=RIDGE)
        button_frame.place(x=0,y=35,width=228,height=190)

        #buttons
        cust_butt=Button(button_frame,text='CUSTOMER',command=self.cust_details,width=22,font=('times new roman',14,'bold'),bg='black',fg='gold',bd=0,relief=RIDGE,cursor='hand2')
        cust_butt.grid(row=0,column=0,pady=1)

        room_butt=Button(button_frame,text='ROOM',width=22,command=self.Roombooking,font=('times new roman',14,'bold'),bg='black',fg='gold',bd=0,relief=RIDGE,cursor='hand2')
        room_butt.grid(row=1,column=0,pady=1)

        det_butt=Button(button_frame,text='DETAILS',command=self.Roomdet,width=22,font=('times new roman',14,'bold'),bg='black',fg='gold',bd=0,relief=RIDGE,cursor='hand2')
        det_butt.grid(row=2,column=0,pady=1)

        REP_butt=Button(button_frame,text='REPORT',command=self.report,width=22,font=('times new roman',14,'bold'),bg='black',fg='gold',bd=0,relief=RIDGE,cursor='hand2')
        REP_butt.grid(row=3,column=0,pady=1)

        logout_butt=Button(button_frame,text='LOGOUT',command=self.logout,width=22,font=('times new roman',14,'bold'),bg='black',fg='gold',bd=0,relief=RIDGE,cursor='hand2')
        logout_butt.grid(row=4,column=0,pady=1)

        # middle image
        img3=Image.open(r'C:\Users\MAMATA\Desktop\pip\slide3.jpg')
        img3=img3.resize((1310,590),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg1=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg1.place(x=225,y=0,width=1310,height=590)

        #below second frame images
        img4=Image.open(r'C:\Users\MAMATA\Desktop\pip\outside.jpg')
        img4=img4.resize((230,210),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lblimg2=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lblimg2.place(x=0,y=225,width=230,height=210)

        img5=Image.open(r'C:\Users\MAMATA\Desktop\pip\food.jpg')
        img5=img5.resize((230,190),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        lblimg3=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        lblimg3.place(x=0,y=420,width=230,height=190)


    def cust_details(self):
            self.new_window=Toplevel(self.root)
            self.app=cust_win(self.new_window)

    def Roombooking(self):
            self.new_window=Toplevel(self.root)
            self.app=roombooking(self.new_window)


    def Roomdet(self):
            self.new_window=Toplevel(self.root)
            self.app=roomdetails(self.new_window)



    def report(self):
            self.new_window=Toplevel(self.root)
            self.app=Report(self.new_window)


        

    def logout(self):
        self.root.destroy()



        
if __name__ == "__main__":
     root =  Tk()
     obj = Hotelmanagementsystem(root)
     root.mainloop()
    
        
