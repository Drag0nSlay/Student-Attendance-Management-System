from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2.face
import mysql.connector
from datetime import datetime
import cv2
import os
import numpy as np
import time

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Attendance Management System")

        title_lbl=Label(self.root,text="FACE DETECTOR",font=("times new roman",35,'bold'),bg="cyan",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #1st image
        img_top=Image.open(r"Images\DATA1.jpg")
        img_top=img_top.resize((650,700),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=650,height=700)

        #1st image
        img_bottom=Image.open(r"Images\loading1.jpg")
        img_bottom=img_bottom.resize((950,700),Image.LANCZOS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=650,y=55,width=950,height=700)

        #Button
        b1_1=Button(f_lbl,text="FACE RECOGNITION",command=self.face_recog,cursor="hand2",font=("times new roman",18,'bold'),bg="black",fg="white")
        b1_1.place(x=345,y=630,width=260,height=40)

        #=========== Attendance==================
    
    def mark_attendance(self, i, r, n, d):
    # Open the file in read and append mode
        with open("src/Attendance.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()  # Read all lines to avoid duplicate entries
            attendance_marked = False  # Flag to check if attendance is already marked

            for line in myDataList:
                entry = line.strip().split(",")  # Split each line by comma and strip whitespace

            # Check if the entry contains ID and Roll number to avoid duplicate attendance
                if len(entry) >= 2 and (i == entry[0] or r == entry[1]):
                    attendance_marked = True
                    break  # Exit loop if attendance is already marked

        # If attendance has not been marked, add the new entry
            if not attendance_marked:
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.write(f"{i},{r},{n},{d},{dtString},{d1},Present\n")  # Write new line without reopening file

        #face recognition================
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="MySQLAman",database="student_attendence")
                my_cursor=conn.cursor()

                my_cursor.execute("select Name from student where Student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n) if n else "Unknown"

                my_cursor.execute("select Roll from student where Student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r) if r else "Unknown"

                my_cursor.execute("select Dep from student where Student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d) if d else "Unknown"

                my_cursor.execute("select Student_id from student where Student_id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i) if i else "Unknown"

                if confidence>70:
                    cv2.putText(img,f"ID:{i}",(x,y-78),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)

                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    coord = [x, y, w, h]

                coord=[x,y,w,h]

            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("src/haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("src/classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Face Recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()
