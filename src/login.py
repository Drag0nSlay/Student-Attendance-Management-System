from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import random
import time
import datetime
import mysql.connector
from time import strftime
import tkinter
import os
from student import Student
from data_model import Data_Model 
from face_recognition import Face_Recognition
from Attendance import Attendance
from developer import Developer
from help import Help
from main import Student_Attendance_Management

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()


class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        img1 = Image.open(r"Images\Login4.jpg")
        img1 = img1.resize((1530,750),Image.LANCZOS)
        self.photoImg1 = ImageTk.PhotoImage(img1)
        bg_lbl=Label(self.root,image=self.photoImg1)
        bg_lbl.place(x=0,y=0,width=1530,height=750)

        title=Label(bg_lbl,text="STUDENT ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",14,"bold"))
        title.place(x=0,y=120,width=1550,height=45)

        frame=Frame(self.root,bg='lightgreen')
        frame.place(x=610,y=170,width=340,height=450)

        img2=Image.open(r"Images\profile.png")
        img2=img2.resize((100,100),Image.LANCZOS)
        self.photoImg2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoImg2,bg="black",borderwidth=0)
        lblimg2.place(x=730,y=175,width=100,height=100)

        get_started=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="black",bg="lightgreen")
        get_started.place(x=95,y=100)

        #label
        usrname_lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="black",bg="lightgreen")
        usrname_lbl.place(x=70,y=155)

        self.txtusr=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtusr.place(x=40,y=180,width=270)

        passwd_lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="black",bg="lightgreen")
        passwd_lbl.place(x=70,y=225)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)

        #========icon images===========
        img3=Image.open(r"Images\profile.png")
        img3=img3.resize((25,25),Image.LANCZOS)
        self.photoImg3=ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.photoImg3,bg="black",borderwidth=0)
        lblimg3.place(x=650,y=323,width=25,height=25)

        img4=Image.open(r"Images\password.png")
        img4=img4.resize((25,25),Image.LANCZOS)
        self.photoImg4=ImageTk.PhotoImage(img4)
        lblimg4=Label(image=self.photoImg4,bg="black",borderwidth=0)
        lblimg4.place(x=650,y=394,width=25,height=25)

        #LoginButton
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

        #RegisterButton
        registerbtn=Button(frame,text="New User Registration",command=self.register_window,font=("times new roman",12,"bold"),borderwidth=0,fg="black",bg="lightgreen",activeforeground="white",activebackground="red")
        registerbtn.place(x=20,y=350,width=160)

        #ForgotPassword
        forgottn=Button(frame,text="Forgot Password?",command=self.forgot_password_window,font=("times new roman",12,"bold"),borderwidth=0,fg="black",bg="lightgreen",activeforeground="white",activebackground="blue")
        forgottn.place(x=10,y=390,width=160)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.txtusr.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all field required")

        elif self.txtusr.get()=="Aman" and self.txtpass.get()=="kothari":
            messagebox.showinfo("Success","Welcome to Student Attendance Management System")

        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="MySQLAman",database="mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                    self.txtusr.get(),
                                                                                    self.txtpass.get()
                                                                            ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username & password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only admin")
                if open_main:
                    self.new_window=Toplevel(self.root)
                    self.app=Student_Attendance_Management(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

            #reset password=================
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select Security Question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter your Answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please enter your new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="MySQLAman",database="mydata")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtusr.get(),self.combo_security_Q.get(),self.txt_security.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter correct answer",parent=self.root2)
            else:
                query1=("update register set password=%s where email=%s")
                value1=(self.txt_newpass.get(),self.txtusr.get())
                my_cursor.execute(query1,value1)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset, please login with new password",parent=self.root2)
                self.root2.destroy()

    
#============================forgot password window====================
    def forgot_password_window(self):
        if self.txtusr.get()=="":
            messagebox.showerror("Error","Please Enter the Email Address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="MySQLAman",database="mydata")
            my_cursor=conn.cursor()
            Query=("select * from register where email=%s")
            value=(self.txtusr.get(),)
            my_cursor.execute(Query,value)
            row=my_cursor.fetchone()
            #print(row)

            if row==None:
                messagebox.showerror("Error","Please enter the valid user name")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forgot Password",font=("times new roman",20,"bold"),fg="black",bg="lightgreen")
                l.place(x=0,y=10,relwidth=1)

                security_Q=Label(self.root2,text="Select Security Question",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_Q.place(x=50,y=80)

                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security_Q["values"]=("Select","Your Birth Place","Your Friend name","Your Pet name")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)



                security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_A.place(x=50,y=150)

                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_security.place(x=50,y=180,width=250)

                new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="black")
                new_password.place(x=50,y=220)

                self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_newpass.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),fg="white",bg="green")
                btn.place(x=100,y=290)

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        #============variables=================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_SecurityQ=StringVar()
        self.var_SecurityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        self.var_check=IntVar()

        img = Image.open(r"D:\SAM\Images\registration.jpg")
        img = img.resize((1600, 900), Image.LANCZOS)
        self.bg = ImageTk.PhotoImage(img)
        
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        #=======left image=========
        img1 = Image.open(r"D:\SAM\Images\registration2.jpg")
        img1 = img1.resize((1600, 900), Image.LANCZOS)
        self.bg1 = ImageTk.PhotoImage(img1)
        
        left_lbl1=Label(self.root,image=self.bg1)
        left_lbl1.place(x=50,y=100,width=470,height=550)

        #============main frame==========
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)

        #register label=========
        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="Orange")
        register_lbl.place(x=20,y=20)

        #Label & entry================
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=130,width=250)

        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        l_name.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)

        #------------------row2
        contact=Label(frame,text="Contact",font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)
        
        #-------------------row3
        security_Q=Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_Q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_SecurityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your Friend name","Your Pet name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)



        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_SecurityA,font=("times new roman",15))
        self.txt_security.place(x=370,y=270,width=250)

        #------------------row4
        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
        self.txt_pswd.place(x=50,y=340,width=250)

        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)

        #===============checkbox============
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Conditions",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)

        #======Buttons================
        img2=Image.open(r"D:\SAM\Images\register_btn.jpg")
        img2=img2.resize((200,55),Image.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        b1=Button(frame,image=self.photoimage2,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"))
        b1.place(x=10,y=420,width=200)

        img3=Image.open(r"D:\SAM\Images\login_btn.png")
        img3=img3.resize((200,200),Image.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        b1=Button(frame,image=self.photoimage3,command=self.return_login,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"))
        b1.place(x=330,y=370,width=200,height=150)


    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_SecurityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password & Confirm Password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms & conditions")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="MySQLAman",database="mydata")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exists, please try another email address")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_SecurityQ.get(),
                                                                                        self.var_SecurityA.get(),
                                                                                        self.var_pass.get()
                                                                                     ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Successfully")

    def return_login(self):
        self.root.destroy()

class Student_Attendance_Management:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Attendance Management System")

        #first image
        img=Image.open(r"Images\ABESIT.jpg")
        img=img.resize((500,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        #second image
        img1=Image.open(r"Images\face_header_sd.jpg")
        img1=img1.resize((500,130),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=550,height=130)

        #third image
        img2=Image.open(r"Images\abesit_front.jpg")
        img2=img2.resize((500,130),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)

        #bg image
        img3=Image.open(r"Images\bg.jpg")
        img3=img3.resize((1530,710),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="STUDENT ATTENDANCE MANAGEMENT SYSTEM ",font=("times new roman",35,'bold'),bg="orange",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #=========time================
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)

        lbl = Label(title_lbl, font=("times new roman",14,"bold"),background='orange',foreground='white')
        lbl.place(x=0, y=0, width=110, height=50)
        time()

        #student button
        img4=Image.open(r"Images\student.jpg")
        img4=img4.resize((1530,710),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,'bold'),bg="darkblue",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)

        #Detect Face button
        img5=Image.open(r"Images\Face_detect5.jpg")
        img5=img5.resize((1530,710),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Face Detector",command=self.face_data,cursor="hand2",font=("times new roman",15,'bold'),bg="darkblue",fg="white")
        b1_1.place(x=500,y=300,width=220,height=40)


        #Attendance  button
        img6=Image.open(r"Images\Attendance5.jpg")
        img6=img6.resize((1530,710),Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=800,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,'bold'),bg="darkblue",fg="white")
        b1_1.place(x=800,y=300,width=220,height=40)


        #Help button
        img7=Image.open(r"Images\Help2.jpg")
        img7=img7.resize((1530,710),Image.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help)
        b1.place(x=1100,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Help",cursor="hand2",command=self.help,font=("times new roman",15,'bold'),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=300,width=220,height=40)


        #Train Model button
        img8=Image.open(r"Images\Data_Model2.png")
        img8=img8.resize((1530,710),Image.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.data_model)
        b1.place(x=200,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Data Models",command=self.data_model,cursor="hand2",font=("times new roman",15,'bold'),bg="darkblue",fg="white")
        b1_1.place(x=200,y=580,width=220,height=40)


        #Images button
        img9=Image.open(r"Images\Images1.jpg")
        img9=img9.resize((1530,710),Image.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Images",cursor="hand2",command=self.open_img,font=("times new roman",15,'bold'),bg="darkblue",fg="white")
        b1_1.place(x=500,y=580,width=220,height=40)


        #Developer button
        img10=Image.open(r"Images\developer2.jpg")
        img10=img10.resize((1530,710),Image.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_info)
        b1.place(x=800,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_info,font=("times new roman",15,'bold'),bg="darkblue",fg="white")
        b1_1.place(x=800,y=580,width=220,height=40)


        #Exit button
        img11=Image.open(r"Images\exit1.png")
        img11=img11.resize((1530,710),Image.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.exit)
        b1.place(x=1100,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.exit,font=("times new roman",15,'bold'),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=580,width=220,height=40)

    def open_img(self):
        os.startfile("data")

    def exit(self):
        self.exit=tkinter.messagebox.askyesno("Student Attendance Management System","Are you sure want to leave this application?",parent=self.root)
        if self.exit>0:
            self.root.destroy()

        else:
            return

        #================Functions Buttons===========

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def data_model(self):
        self.new_window=Toplevel(self.root)
        self.app=Data_Model(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def developer_info(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)

if __name__ == "__main__":
    main()