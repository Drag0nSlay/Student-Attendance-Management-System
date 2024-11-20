from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from PIL import Image, ImageTk
import tkinter
from datetime import datetime
from time import strftime
import os
from student import Student
from data_model import Data_Model 
from face_recognition import Face_Recognition
from Attendance import Attendance
from developer import Developer
from chatbot1 import ChatBot

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

        #ChatBot Button
        img_chat=Image.open(r"Images\Chatbot1.jpg")
        img_chat=img_chat.resize((220,220),Image.LANCZOS)
        self.photoimg_chat=ImageTk.PhotoImage(img_chat)

        bChat=Button(bg_img,image=self.photoimg_chat,cursor="hand2",command=self.chatbot)
        bChat.place(x=1100,y=100,width=220,height=220)

        b1_Chat=Button(bg_img,text="ChatBot",cursor="hand2",command=self.chatbot,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_Chat.place(x=1100,y=300,width=220,height=40)

#======= Photo Sample Function================
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

    def chatbot(self):
        self.new_window=Toplevel(self.root)
        self.app=ChatBot(self.new_window)

if __name__ == "__main__":
    root=Tk()
    obj=Student_Attendance_Management(root)
    root.mainloop()
