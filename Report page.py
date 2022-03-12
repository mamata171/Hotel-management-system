from tkinter import *      
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector 
import random
from tkinter import messagebox 

class Report:
    def __init__(self,root):
        self.root=root
        self.root.title('Hotel Management System')
        self.root.geometry('1295x550+230+220')

        #title
        lbl_title=Label(self.root,text='REPORT',font=('times new roman',30,'bold'),bg='black',fg='gold',bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=40)

        lbl_title=Label(self.root,text='Developer Details',font=('times new roman',20,'bold'),bg='black',fg='gold',bd=4,relief=RIDGE)
        lbl_title.place(x=50,y=50,width=230,height=30)

        lbl_title=Label(self.root,text='Johnson',font=('times new roman',20,'bold'),bd=4,relief=RIDGE)
        lbl_title.place(x=50,y=95,width=205,height=30)

        lbl_title=Label(self.root,text='From : America',font=('times new roman',17,'bold'),bd=4,relief=RIDGE)
        lbl_title.place(x=50,y=130,width=235,height=25)

        lbl_title=Label(self.root,text='Qualification : MCA',font=('times new roman',17,'bold'),bd=4,relief=RIDGE)
        lbl_title.place(x=50,y=165,width=240,height=25)

        lbl_title=Label(self.root,text='contact no. :9965847589',font=('times new roman',17,'bold'),bd=4,relief=RIDGE)
        lbl_title.place(x=50,y=195,width=275,height=30)

        lbl_title=Label(self.root,text='mail : john65@gmail.com : ',font=('times new roman',17,'bold'),bd=4,relief=RIDGE)
        lbl_title.place(x=50,y=235,width=275,height=30)

        #images
        img2=Image.open(r'C:\Users\MAMATA\Desktop\pip\lap2.jpg')
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=400,y=50,width=800,height=500)

        lbl_title=Label(self.root,text='Email : Mamata17@gmail.com',font=('times new roman',17,'bold'),bg='cyan',bd=4,relief=RIDGE)
        lbl_title.place(x=600,y=180,width=320,height=40)


        






        






if __name__=='__main__':
    root=Tk()
    obj=report(root)
    root.mainloop()
    
