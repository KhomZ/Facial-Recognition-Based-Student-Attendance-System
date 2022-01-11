
from logging import root
from os import SEEK_CUR, close
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from mysql.connector import cursor
import cv2
import datetime  
from time import strptime
import re
# from tkcalendar import Calendar
from tkcalendar import DateEntry
import pyttsx3


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 1 is for female voice and 0 is for male voice

def speak_va(transcribed_query):
    engine.say(transcribed_query)
    engine.runAndWait()


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        ##### Variables  #####
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        self.var_searchtxt=StringVar()
        self.var_search=StringVar()
       

      





    # #first image
    #     img=Image.open(r"E:\6th sem\my_project\Face_reg\face_recognize_student_attendence_system\Images\images.jpeg")
    #     img=img.resize((450,120),Image.ANTIALIAS)  #Antialias lea high level image lai low level mah convert garxa
    #     self.photoimg=ImageTk.PhotoImage(img)

    #     f_lbl=Label(self.root,image=self.photoimg)
    #     f_lbl.place(x=0, y=0,width=450,height=120)

    # #Second image
    #     img1=Image.open(r"E:\6th sem\my_project\Face_reg\face_recognize_student_attendence_system\Images\re2.jpg")
    #     img1=img1.resize((450,120),Image.ANTIALIAS)  #Antialias lea high level image lai low level mah convert garxa
    #     self.photoimg1=ImageTk.PhotoImage(img1)

    #     f_lbl=Label(self.root,image=self.photoimg1)
    #     f_lbl.place(x=450, y=0,width=450,height=120)

    #Third Image
        # img2=Image.open(r"E:\6th sem\my_project\Face_reg\face_recognize_student_attendence_system\Images\re1.jpg")
        # img2 = Image.open(r"C:\Users\ACER\Desktop\myProj\Facial-Recognition-Based-Student-Attendance-System\Images\re1.jpg")
        img2 = Image.open("Images/re1.jpg")
        img2 = img2.resize((1366,120),Image.ANTIALIAS)  #Antialias lea high level image lai low level mah convert garxa
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=0, y=0,width=1366,height=120)


    #Background image 
        # img3=Image.open(r"E:\6th sem\my_project\Face_reg\face_recognize_student_attendence_system\Images\face.jpg")
        # img3 = Image.open(r"C:\Users\ACER\Desktop\myProj\Facial-Recognition-Based-Student-Attendance-System\Images\re1.jpg")
        img3 = Image.open("Images/face.jpg")
        img3 = img3.resize((1530,730),Image.ANTIALIAS)  #Antialias lea high level image lai low level mah convert garxa
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0, y=130,width=1530,height=730)


        title_lbl=Label(bg_img,text="STUDENT DETAILS MANAGE SECTION",font=("Algerian",30,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1530,height=30)


        main_frame=Frame(bg_img,bd=2,bg="white",)
        main_frame.place(x=20,y=35,width=1480,height=600)

        # left label frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("Algerian",12,"bold"))
        left_frame.place(x=5,y=5,width=670,height=515)


        # img_left=Image.open(r"E:\6th sem\my_project\Face_reg\face_recognize_student_attendence_system\Images\NCIT.jpg")
        # img_left = Image.open(r"C:\Users\ACER\Desktop\myProj\Facial-Recognition-Based-Student-Attendance-System\Images\re1.jpg")
        img_left = Image.open("Images/NCIT.png")
        img_left = img_left.resize((660,100),Image.ANTIALIAS)  #Antialias lea high level image lai low level mah convert garxa
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=5, y=0,width=660,height=100)

     #current course information
        current_course_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=75,width=660,height=115)

    #Department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",13,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)


        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",13,"bold"),state="readonly",width=18)
        dep_combo["values"]=("Select Department","IT","Computer","Civil","Elx & Comm","Software")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

    #course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",13,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",13,"bold"),state="readonly",width=18)
        course_combo["values"]=("Select Course","AI","IPPR","CN","OOSE","TOC","CG","SNM")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)


    #Year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",13,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",13,"bold"),state="readonly",width=18)
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)


    #Semester
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",13,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",13,"bold"),state="readonly",width=18)
        # semester_combo["values"]=("Select Semester","Semester-I","Semester-II","Semester-III","Semester-IV","Semester-V","Semester-VI","Semester-VII","Semester-VIII")
        semester_combo["values"]=("Select Semester","Semester-I","Semester-III","Semester-V","Semester-VII")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)


     #class student information
        class_student_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=190,width=660,height=320)

    #studen ID 
        studentId_label=Label(class_student_frame,text="StudentID:",font=("times new roman",13,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,sticky=W)

        studentId_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=18,font=("times new roman",13,"bold"))
        studentId_entry.grid(row=0,column=1,padx=10,sticky=W)

        validate_id=self.root.register(self.checkid)
        studentId_entry.config(validate='key',validatecommand=(validate_id,'%P'))




    #student name
        studentName_label=Label(class_student_frame,text="Student Name:",font=("times new roman",13,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=18,font=("times new roman",13,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        # call back and validation
        validate_name=self.root.register(self.checkname)
        studentName_entry.config(validate='key',validatecommand=(validate_name,'%P'))





    #class division
        class_div_label=Label(class_student_frame,text="Class Division:",font=("times new roman",13,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",13,"bold"),state="readonly",width=16)
        div_combo["values"]=("Select Division","A","B")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=10,sticky=W)


    #roll_no
        roll_no_label=Label(class_student_frame,text="Roll No:",font=("times new roman",13,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=18,font=("times new roman",13,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        validate_roll=self.root.register(self.checkroll)
        roll_no_entry.config(validate='key',validatecommand=(validate_roll,'%P'))


    #Gender
        gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",13,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",13,"bold"),state="readonly",width=16)
        gender_combo["values"]=("Male","Female","Others")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=10,sticky=W)


    #DOB
        dob_label=Label(class_student_frame,text="DOB:",font=("times new roman",13,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        # dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=18,font=("times new roman",13,"bold"))
        # dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        cal = DateEntry(class_student_frame,textvariable=self.var_dob, width=23, year=2019, month=6, day=22, 
         background='darkblue', foreground='white', borderwidth=2)
        cal.grid(row=2,column=3,padx=10, pady=10)
      
        # validate_date=self.root.register(self.grad_date)
        # dob_entry.config(validate='key',validatecommand=(validate_date,'%P'))


        
    #Email
        email_label=Label(class_student_frame,text="Email:",font=("times new roman",13,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=18,font=("times new roman",13,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)



        email=Label(class_student_frame,text="*ex123@gmail.com",font=("times new roman",6,"bold"),fg="red",bg="white")
        # pswd.grid(row=8,column=1,padx=5,pady=5,sticky=W)
        email.place(x=150, y=149)


        # validate_email=self.root.register(self.checkemail)
        # email_entry.config(validate='key',validatecommand=(validate_email,'%P'))




    #Phone no
        phone_label=Label(class_student_frame,text="Phone No:",font=("times new roman",13,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=18,font=("times new roman",13,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)


        validate_phone=self.root.register(self.checkphone)
        phone_entry.config(validate='key',validatecommand=(validate_phone,'%P'))
    
   

    #Address
        address_label=Label(class_student_frame,text="Address:",font=("times new roman",13,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=18,font=("times new roman",13,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)



        validate_address=self.root.register(self.checkaddress)
        address_entry.config(validate='key',validatecommand=(validate_address,'%P'))
    

    

    #Teacher Name
        teacher_label=Label(class_student_frame,text="Teacher Name:",font=("times new roman",13,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teacher_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=18,font=("times new roman",13,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)


        validate_Teacher=self.root.register(self.checkTeachername)
        teacher_entry.config(validate='key',validatecommand=(validate_Teacher,'%P'))

      
    
    #radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=5,column=0)

        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="NO")
        radiobtn2.grid(row=5,column=1)

    #button frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=215,width=655,height=80)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=16,font=("times new roman",13,"bold"),bg="Green",fg="white")
        save_btn.grid(row=0,column=0)

        
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=16,font=("times new roman",13,"bold"),bg="Green",fg="white")
        update_btn.grid(row=0,column=1)

        
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=16,font=("times new roman",13,"bold"),bg="Green",fg="white")
        delete_btn.grid(row=0,column=2)

        
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=16,font=("times new roman",13,"bold"),bg="Green",fg="white")
        reset_btn.grid(row=0,column=3)

    #frame for take photo and update photo
        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=245,width=655,height=80)

        take_photo_btn=Button(btn_frame1,text="Take Photo Sample",command=self.generate_dataset,width=65,font=("times new roman",13,"bold"),bg="green",fg="white")
        take_photo_btn.grid(row=0,column=0)

        # update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=32,font=("times new roman",13,"bold"),bg="blue",fg="white")
        # update_photo_btn.grid(row=0,column=1)




 #Right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("Algerian",12,"bold"))
        right_frame.place(x=680,y=5,width=650,height=515)

        # img_right=Image.open(r"E:\6th sem\my_project\Face_reg\face_recognize_student_attendence_system\Images\NCIT.jpg")
        # img_right = Image.open(r"C:\Users\ACER\Desktop\myProj\Facial-Recognition-Based-Student-Attendance-System\Images\re1.jpg")
        img_right = Image.open("Images/mycollege1.jpeg")
        img_right = img_right.resize((650,75),Image.ANTIALIAS)  #Antialias lea high level image lai low level mah convert garxa
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(right_frame,image=self.photoimg_right)
        f_lbl.place(x=5, y=0,width=640,height=75)


##Search System
        # search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        # search_frame.place(x=5,y=75,width=640,height=70)

        # search_label=Label(search_frame,text="Search By:",font=("times new roman",15,"bold"),bg="red",fg="white")
        # search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        # search_combo=ttk.Combobox(search_frame,textvariable=self.var_search,font=("times new roman",13,"bold"),state="readonly",width=11)
        # search_combo["values"]=("Select","Roll_No","Phone_No")
        # search_combo.current(0)
        # search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)


        # search_entry=ttk.Entry(search_frame,width=17,textvariable=self.var_searchtxt,font=("times new roman",13,"bold"))
        # search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)
    


        # search_btn=Button(search_frame,text="Search",width=10,command=self.search_data,font=("times new roman",12,"bold"),bg="blue",fg="white")
        # search_btn.grid(row=0,column=3,padx=4)

        
        # showAll_btn=Button(search_frame,text="Show All",width=10,font=("times new roman",12,"bold"),bg="blue",fg="white")
        # showAll_btn.grid(row=0,column=4,padx=4)

        search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("Algerian",12,"bold"))
        search_frame.place(x=5,y=75,width=640,height=70)

        search_label=Label(search_frame,text="Search By:",font=("times new roman",15,"bold"),bg="Green",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,textvariable=self.var_search,font=("times new roman",13,"bold"),state="readonly",width=11)
        search_combo["values"]=("Select","Roll")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)


        search_entry=ttk.Entry(search_frame,textvariable=self.var_searchtxt,width=17,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)
    


        search_btn=Button(search_frame,text="Search",command=self.search_data,width=10,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        showAll_btn=Button(search_frame,text="Show All",width=10,command=self.show_all,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=4)



#Table frame
        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=150,width=640,height=350)


#scroll bar 
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=150)

        self.student_table.pack(fill=BOTH,expand=1)

        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        
        self.fetch_data()


# call back sytem
    def checkname(self,name):
        if name.isalnum():
            return True
        if name=='':
            return True
        else:
            speak_va('Invalid! Name Not allowed.')
            messagebox.showerror('Invalid','Not allowed' +name[-1])
    def checkname(self,name):
       for char in name:
           if  not (("A" <= char and char <= "Z") or ("a" <= char and char <= "z") or (char == " ")):
              return False
       return True
    
    def checkaddress(self,name):
       for char in name:
           if  not (("A" <= char and char <= "Z") or ("a" <= char and char <= "z") or (char == " ")):
              return False
       return True

    def checkTeachername(self,name):
       for char in name:
           if  not (("A" <= char and char <= "Z") or ("a" <= char and char <= "z") or (char == " ")):
              return False
       return True
       

    # # checkphone number

    def checkphone(self,phone):
        if len(phone) <=10:
          if phone.isdigit():
            return True
          if len(str(phone))==0:
            return True
          else:
              speak_va('Invalid phone number Format')
              messagebox.showerror('Invalid','Invalid entry. Please enter phone (example:9846200045)')
              return False
            
        else:
            speak_va('Alert!!! Invalid Phone Number')
            messagebox.showwarning('Alert','invalid phone. Please enter phone (example:9846200045)')
            return False

    #     # Id no ko validation 
    def checkid(self,id):
        if len(id) <=5:
          if id.isdigit():
            return True
          if len(str(id))==0:
            return True
          else:
              speak_va('Invalid ID. Please enter ID as integer value')
              messagebox.showerror('Invalid','Invalid entry ID. Please enter ID as integer value (example: ID :- 1 2 3 4 5 6 7...like this)')
              return False
        else:
            speak_va('Invalid ID.')
            messagebox.showwarning('Alert','invalid ID. Please Enter valid ID.')
            return False


    #     # Roll ko lagi validation
    def checkroll(self,roll):
        if len(roll) <=6:
          if roll.isdigit():
            return True
          if len(str(roll))==0:
            return True
          else:
              speak_va('Invalid Roll number. Please Enter your valid roll number.')
              messagebox.showerror('Invalid','Invalid entry enter Roll No (example: Roll No: 171346)')
              return False
        else:
            speak_va('Invalid Roll number.')
            messagebox.showwarning('Alert','invalid phone enter Roll No (example: Roll No: 171346)')
            return False
        
        cal = Calendar(root, selectmode = 'day',
               year = 2020, month = 5,
               day = 22)
        cal.pack(pady = 20)
        def grad_date():
           date.config(cal.get_date())





#    date of birthday

    # def checkdate(self,date_text):
    #     try:
    #         datetime.datetime.strptime(date_text, '%d/%m/%Y')
    #     except ValueError:
    #         messagebox.showerror('Invalid','Invalid entry')
            # raise ValueError("Incorrect data format, should be YYYY-MM-DD")

    # def checkemail(self,email):
    #     if len(email)>=7:
    #         if(re.match("^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)([a-zA-z]{2,5})$",email)!=None):
    #             return True
    #         if len(email)==0:
    #            return True
    #         else:
    #             messagebox.showwarning('Alert','Invalid email Enter valid email like keshav123@gmail.com ')
    #             return False
    #     else:
    #         messagebox.showinfo('Invalid',"Follow standard.")
    #         return False\



    # def checkemail(self,email):  

    #     regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    #     if(re.fullmatch(regex,email)):   
    #       return True  
    #     else:  
    #         messagebox.showinfo('Invalid',"Follow standard.")
    #         return False 
        




       
        
        
    



####function decleration ######
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            speak_va("Alert!!! All Fields are Mandatory.")
            messagebox.showerror("Error", "All fields Are Required",parent=self.root)

        elif not ("@" or ".com") in self.var_email.get():
            speak_va('Try valid email address!!')
            # speak_va("Invalid Email")
            messagebox.showerror("Error",'Invalid email Enter valid email like keshav123@gmail.com ',parent=self.root)
        else:
            try:
                # conn=mysql.connector.connect(host="localhost",username="root",password="Keshav@123",database="mydata")
                conn=mysql.connector.connect(host="localhost",username="root",password="root@khom123",database="khomdb")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_std_id.get(),
                                                                                                                self.var_std_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_radio1.get()


                                                                                                             ))
                conn.commit()
                self.fetch_data()
                conn.close()
                speak_va('Student Details has been added successfully.')
                messagebox.showinfo("Success","Student details has been added Sucessfully",parent=self.root)
            except Exception as es:
                speak_va('An Exception Occurred!')
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


######======Fetch data ==============#####
    def fetch_data(self):
        # conn=mysql.connector.connect(host="localhost",username="root",password="Keshav@123",database="mydata")
        conn=mysql.connector.connect(host="localhost",username="root",password="root@khom123",database="khomdb")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student1")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

#=================== get cursor ======================#
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])


#============= Update function =========================

    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            speak_va('Alert!!! All fields are required.')
            messagebox.showerror("Error", "All fields Are Required",parent=self.root)

        else:
            try:
                speak_va("Do you want to Update this Student's Details?")
                Upadate = messagebox.askyesno("Upadate","Do You Want To Update This Student Details",parent=self.root)
                if Upadate>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="root@khom123",database="khomdb")
                    # conn=mysql.connector.connect(host="localhost",username="root",password="Keshav@123",database="mydata")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student1 set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where id=%s",(

                                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                        self.var_semester.get(),
                                                                                                                                                                                        self.var_std_name.get(),
                                                                                                                                                                                        self.var_div.get(),
                                                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                        self.var_teacher.get(),
                                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                                        self.var_std_id.get()
                                                                                                                                                                                    ))   
                
                
                else:
                    if not Upadate:
                        return
                speak_va('Student Details updated successfully.')
                messagebox.showinfo("Success","Student Details updated Successfully.",parent=self.root)                                                                                                                                              
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                speak_va('An Exception Occurred!')
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)



# ===================Delete Function===================
    def delete_data(self):
        if self.var_std_id.get()=="":
            # speak_va('Student ID is mandatory')
            messagebox.showerror("Error","Student Id Must be Required",parent=self.root)
        else:
            try:
                speak_va("Do you want to Delete this Student's Details?")
                delete=messagebox.askyesno("Student Delete Page","Do You Want To Delete This Student Details",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="root@khom123",database="khomdb")
                    # conn=mysql.connector.connect(host="localhost",username="root",password="Keshav@123",database="mydata")
                    my_cursor=conn.cursor()
                    sql="delete from student1 where id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)

                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                speak_va('Student Details deleted successfully.')
                messagebox.showinfo("Delete","Student Details Successfully deleted",parent=self.root)

            except Exception as es:
                speak_va('An exception occurred!')
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


#============Reset Function =============================
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

# ..............Generate data set or take photo sample

    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            speak_va('All Fields are mandatory.')
            messagebox.showerror("Error", "All fields Are Required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="root@khom123",database="khomdb")
                # conn=mysql.connector.connect(host="localhost",username="root",password="Keshav@123",database="mydata")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student1")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1
                my_cursor.execute("update student1 set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where id=%s",(

                                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                        self.var_semester.get(),
                                                                                                                                                                                        self.var_std_name.get(),
                                                                                                                                                                                        self.var_div.get(),
                                                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                        self.var_teacher.get(),
                                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                                        self.var_std_id.get()==id+1
                                                                                                                                                                                    ))   
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # ..................load predefined data  face forntal from opencv.............
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)


                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                cap=cv2.VideoCapture(0)

                
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face =cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        # file_name_path="data/"+str(self.var_roll.get())+"."+str(id)+"."+str(img_id)+".jpg"
                        # file_name_path="data/"+str(Roll)+"."+str(id)+"."+str(img_id)+".jpg"
                        file_name_path="data/"+"user"+"."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()

                speak_va("Generation of Data Set completed.")
                messagebox.showinfo("Result","Generation of data set completed!!!",parent=self.root)
            except Exception as es:
                speak_va("An Exception occurred")
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)




     # search data     
    def search_data(self):
        if self.var_searchtxt.get()=="" or self.var_search.get()=="Select Option":
            messagebox.showerror("Error","Select Combo option and enter entry box",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="root@khom123",database="khomdb")
                # conn=mysql.connector.connect(host='localhost',username='root',password="Keshav@123",database="mydata")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student1 where " +str(self.var_search.get())+" LIKE '%"+str(self.var_searchtxt.get())+"%'")
                rows=my_cursor.fetchall()         
                if len(rows)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert("",END,values=i)
                    if rows==None:
                        speak_va("Data Not Found")
                        messagebox.showerror("Error","Data Not Found",parent=self.root)
                        conn.commit()
                conn.close()
            except Exception as es:
                speak_va("An Exception Occurred!")
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

            # show all 
    def show_all(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="root@khom123",database="khomdb")
        # conn=mysql.connector.connect(host="localhost",username="root",password="Keshav@123",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student1")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()


           



            

                


            # except Exception as es:
            #     messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)



if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()




# # Developer : team kyzen
# # Date : Saturday, April 10 2021

# from tkinter import *
# from tkinter import ttk
# from PIL import Image, ImageTk
# from tkinter import messagebox
# import mysql.connector


# class Student:
#     def __init__(self, root):
#         self.root = root
#         self.root.geometry("1450x720+0+0")
#         self.root.title("Face Recognition System")

#         # ==================================variables ========================================
#         self.var_dep = StringVar()
#         self.var_course = StringVar()
#         self.var_year = StringVar()
#         self.var_semester = StringVar()
#         self.var_std_id = StringVar()
#         self.var_std_name = StringVar()
#         self.var_sec = StringVar()
#         self.var_roll = StringVar()
#         self.var_gender = StringVar()
#         self.var_phone = StringVar()
#         self.var_address = StringVar()

#         # first image
#         img1 = Image.open("Images/scholarImages/smart-attendance.jpg")
#         img1 = img1.resize((450, 120), Image.ANTIALIAS)
#         self.photoimg1 = ImageTk.PhotoImage(img1)

#         f_lbl = Label(self.root, image=self.photoimg1)
#         f_lbl.place(x=0, y=0, width=450, height=120)

#         # second image
#         img2 = Image.open("Images/NCIT-building.jpg")
#         img2 = img2.resize((450, 120), Image.ANTIALIAS)
#         self.photoimg2 = ImageTk.PhotoImage(img2)

#         f_lbl = Label(self.root, image=self.photoimg2)
#         f_lbl.place(x=450, y=0, width=450, height=120)

#         # third image
#         img3 = Image.open("Images/scholarImages/Graduation-2014.jpg")
#         img3 = img3.resize((450, 120), Image.ANTIALIAS)
#         self.photoimg3 = ImageTk.PhotoImage(img3)

#         f_lbl = Label(self.root, image=self.photoimg3)
#         f_lbl.place(x=900, y=0, width=450, height=120)

#         # background image
#         img4 = Image.open("Images/face-recognition-logo.jpeg")
#         img4 = img4.resize((1350, 580), Image.ANTIALIAS)
#         self.photoimg4 = ImageTk.PhotoImage(img4)

#         bg_img = Label(self.root, image=self.photoimg4)
#         bg_img.place(x=0, y=120, width=1350, height=580)

#         title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM",
#                           font=("times new roman", 35, "bold"), bg="white", fg="magenta")
#         title_lbl.place(x=0, y=0, width=1350, height=45)  # using .place u can place things at any part of the window

#         main_frame = Frame(bg_img, bd=2)
#         main_frame.place(x=10, y=55, width=1330, height=570)

#         # left label frame
#         Left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Information", font=("Calibri", 12, "bold"))
#         Left_frame.place(x=10, y=10, width=650, height=500)

#         img_left = Image.open("Images/scholarImages/grad2.jpg")
#         img_left = img_left.resize((650, 80), Image.ANTIALIAS)
#         self.photoimg_left = ImageTk.PhotoImage(img_left)

#         f_lbl = Label(Left_frame, image=self.photoimg_left)
#         f_lbl.place(x=5, y=0, width=640, height=60)

#         current_course_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Current Course Information",
#                                 font=("Calibri", 12, "bold"), fg="green")
#         current_course_frame.place(x=5, y=60, width=640, height=90)

#         # Department
#         dep_label = Label(current_course_frame, text="Department :", font=("Calibri", 10, "bold"), bg="white", fg="blue")
#         dep_label.grid(row=0, column=0, padx=10, sticky=W)

#         dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep, font=("Calibri", 10, "bold"), state="readonly")
#         dep_combo["values"] = ("Select Department", "Computer", "IT", "Electronics", "Civil")
#         dep_combo.current(0)
#         dep_combo.grid(row=0, column=1, padx=2, pady=5, sticky=W)

#         # Course
#         course_label = Label(current_course_frame, text="Course :", font=("Calibri", 10, "bold"), bg="white", fg="blue")
#         course_label.grid(row=0, column=2, padx=10, sticky=W)

#         course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course, font=("Calibri", 10, "bold"), state="readonly")
#         course_combo["values"] = ("Select Course", "SNM", "OOSE", "DC", "ES", "NLP")
#         course_combo.current(0)
#         course_combo.grid(row=0, column=3, padx=10, pady=5, sticky=W)

#         # Year
#         year_label = Label(current_course_frame, text="Year :", font=("Calibri", 10, "bold"), bg="white", fg="blue")
#         year_label.grid(row=1, column=0, padx=10, sticky=W)

#         year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year, font=("Calibri", 10, "bold"), state="readonly")
#         year_combo["values"] = ("Select Year", "2021-22", "2022-23", "2023-24", "2024-25")
#         year_combo.current(0)
#         year_combo.grid(row=1, column=1, padx=2, pady=5, sticky=W)

#         # Semester
#         sem_label = Label(current_course_frame, text="Semester :", font=("Calibri", 10, "bold"), bg="white", fg="blue")
#         sem_label.grid(row=1, column=2, padx=10, sticky=W)

#         sem_combo = ttk.Combobox(current_course_frame, textvariable=self.var_semester, font=("Calibri", 10, "bold"), state="readonly")
#         sem_combo["values"] = ("Select Semester", "II", "IV", "VI", "VIII")
#         sem_combo.current(0)
#         sem_combo.grid(row=1, column=3, padx=10, pady=5, sticky=W)

#         #
#         # Student's Class Information
#         #
#         student_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Student's Class Information",
#                                           font=("Calibri", 12, "bold"), fg="green")
#         student_frame.place(x=5, y=150, width=640, height=300)

#         # studentID
#         studentID_label = Label(student_frame, text="StudentID:", font=("Calibri", 10, "bold"), bg="white",
#                           fg="blue")
#         studentID_label.grid(row=0, column=0, padx=10, sticky=W)

#         studentID_entry = ttk.Entry(student_frame, textvariable=self.var_std_id, width=20, font=("Calibri", 10, "bold"))
#         studentID_entry.grid(row=0, column=1, padx=10, sticky=W)

#         # student's Name
#         stdName_label = Label(student_frame, text="Name:", font=("Calibri", 10, "bold"), bg="white",
#                           fg="blue")
#         stdName_label.grid(row=0, column=2, padx=10, sticky=W)

#         stdName_entry = ttk.Entry(student_frame, textvariable=self.var_std_name, width=20, font=("Calibri", 10, "bold"))
#         stdName_entry.grid(row=0, column=3, padx=10, sticky=W)

#         # Section
#         section_label = Label(student_frame, text="Section:", font=("Calibri", 10, "bold"), bg="white",
#                           fg="blue")
#         section_label.grid(row=1, column=0, padx=10, sticky=W)

#         section_entry = ttk.Entry(student_frame, textvariable=self.var_sec, width=20, font=("Calibri", 10, "bold"))
#         section_entry.grid(row=1, column=1, padx=10, sticky=W)

#         # studentRollNo
#         studentRoll_label = Label(student_frame, text="RollNo:", font=("Calibri", 10, "bold"), bg="white",
#                           fg="blue")
#         studentRoll_label.grid(row=1, column=2, padx=10, sticky=W)

#         studentRoll_entry = ttk.Entry(student_frame, textvariable=self.var_roll, width=20, font=("Calibri", 10, "bold"))
#         studentRoll_entry.grid(row=1, column=3, padx=10, sticky=W)

#         # Gender
#         gender_label = Label(student_frame, text="Gender:", font=("Calibri", 10, "bold"), bg="white", fg="blue")
#         gender_label.grid(row=2, column=0, padx=10, sticky=W)

#         gender_combo = ttk.Combobox(student_frame, textvariable=self.var_gender, font=("Calibri", 10, "bold"), state="readonly")
#         gender_combo["values"] = ("Select Gender", "Male", "Female", "LGBTQ")
#         gender_combo.current(0)
#         gender_combo.grid(row=2, column=1, padx=10, pady=5, sticky=W)

#         # student's Contact Info
#         phone_label = Label(student_frame, text="Contact No.:", font=("Calibri", 10, "bold"), bg="white",
#                               fg="blue")
#         phone_label.grid(row=2, column=2, padx=10, sticky=W)

#         phone_entry = ttk.Entry(student_frame, textvariable=self.var_phone, width=20, font=("Calibri", 10, "bold"))
#         phone_entry.grid(row=2, column=3, padx=10, sticky=W)

#         # student's Address
#         address_label = Label(student_frame, text="Address:", font=("Calibri", 10, "bold"), bg="white",
#                               fg="blue")
#         address_label.grid(row=3, column=0, padx=10, sticky=W)

#         address_entry = ttk.Entry(student_frame, textvariable=self.var_address, width=20, font=("Calibri", 10, "bold"))
#         address_entry.grid(row=3, column=1, padx=10, sticky=W)

#         # ==================================Radio Buttons========================================
#         self.var_radio1 = StringVar()
#         radiobtn1 = ttk.Radiobutton(student_frame, variable=self.var_radio1, text="Capture Photo Sample", value="Yes")
#         radiobtn1.grid(row=6, column=0)
#         # self.var_radio2 = StringVar()
#         radiobtn2 = ttk.Radiobutton(student_frame, variable=self.var_radio1, text="No Photo Sample", value="No")
#         radiobtn2.grid(row=6, column=1)

#         # ==================================Buttons Frame========================================
#         btnFrame = Frame(student_frame, relief=RIDGE, bg="cyan")
#         btnFrame.place(x=0, y=180, width=640, height=40)

#         save_btn = Button(btnFrame, text="Save", command=self.add_data, width=13, font=('arial', 13, 'bold'), bg="red", fg="white")
#         save_btn.grid(row=0, column=0)

#         update_btn = Button(btnFrame, text="Update", width=13, font=('arial', 13, 'bold'), bg="red", fg="white")
#         update_btn.grid(row=0, column=1)

#         delete_btn = Button(btnFrame, text="Delete", width=13, font=('arial', 13, 'bold'), bg="red", fg="white")
#         delete_btn.grid(row=0, column=2)

#         reset_btn = Button(btnFrame, text="Reset", width=14, font=('arial', 13, 'bold'), bg="red", fg="white")
#         reset_btn.grid(row=0, column=3)

#         # ==================================Buttons Frame1========================================
#         btnFrame1 = Frame(student_frame, relief=RIDGE, bg="cyan")
#         btnFrame1.place(x=0, y=220, width=640, height=40)

#         capture_photo_btn = Button(btnFrame1, text="Capture Photo Sample", width=29, font=('arial', 13, 'bold'), bg="red", fg="white")
#         capture_photo_btn.grid(row=1, column=0)

#         update_photo_btn = Button(btnFrame1, text="Update Photo Sample", width=30, font=('arial', 13, 'bold'), bg="red", fg="white")
#         update_photo_btn.grid(row=1, column=1)

#         # right label frame
#         Right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details", font=("Calibri", 12, "bold"))
#         Right_frame.place(x=670, y=10, width=650, height=500)

#         img_right = Image.open("Images/scholarImages/high-school-grad.jpg")
#         img_right = img_right.resize((650, 80), Image.ANTIALIAS)
#         self.photoimg_right = ImageTk.PhotoImage(img_right)

#         f_lbl = Label(Right_frame, image=self.photoimg_right)
#         f_lbl.place(x=5, y=0, width=640, height=60)

#         # ==================================Search Systems========================================
#         search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, text="Search System",
#                                           font=("Calibri", 12, "bold"), fg="green")
#         search_frame.place(x=5, y=60, width=640, height=60)

#         search_label = Label(search_frame, text=" Search By: ", font=("Calibri", 10, "bold"), bg="blue",
#                             fg="white")
#         search_label.grid(row=0, column=0, padx=10, sticky=W)

#         search_combo = ttk.Combobox(search_frame, font=("Calibri", 10, "bold"), state="readonly", width=12)
#         search_combo["values"] = ("Select", "Roll_no", "Contact_no", "StdID")
#         search_combo.current(0)
#         search_combo.grid(row=0, column=1, padx=10, pady=5, sticky=W)

#         search_entry = ttk.Entry(search_frame, width=20, font=("Calibri", 10, "bold"))
#         search_entry.grid(row=0, column=2, padx=10, sticky=W)

#         search_btn = Button(search_frame, text="Search", width=10, font=('arial', 10, 'bold'), bg="red", fg="white")
#         search_btn.grid(row=0, column=3, padx=1)

#         showAll_btn = Button(search_frame, text="Show All", width=10, font=('arial', 10, 'bold'), bg="red", fg="white")
#         showAll_btn.grid(row=0, column=4, padx=1)

#         # ==================================Table Frame==========================================
#         table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
#         table_frame.place(x=5, y=120, width=640, height=330)

#         scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
#         scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

#         self.student_table = ttk.Treeview(table_frame, column=("dep", "course", "year", "sem", "id", "name", "section",
#                                                                "roll", "gender", "phone", "address", "photo"),
#                                           xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

#         scroll_x.pack(side=BOTTOM, fill=X)
#         scroll_y.pack(side=RIGHT, fill=Y)
#         scroll_x.config(command=self.student_table.xview)
#         scroll_y.config(command=self.student_table.yview)

#         self.student_table.heading("dep", text="Department")
#         self.student_table.heading("course", text="Course")
#         self.student_table.heading("year", text="Year")
#         self.student_table.heading("sem", text="Semester")
#         self.student_table.heading("id", text="StudentID")
#         self.student_table.heading("name", text="Name")
#         self.student_table.heading("section", text="Section")
#         self.student_table.heading("roll", text="RollNo")
#         self.student_table.heading("gender", text="Gender")
#         self.student_table.heading("phone", text="Phone")
#         self.student_table.heading("address", text="Address")
#         self.student_table.heading("photo", text="PhotoSampleStatus")
#         self.student_table["show"] = "headings"

#         self.student_table.column("dep", width=100)
#         self.student_table.column("course", width=100)
#         self.student_table.column("year", width=100)
#         self.student_table.column("sem", width=100)
#         self.student_table.column("id", width=100)
#         self.student_table.column("name", width=100)
#         self.student_table.column("section", width=100)
#         self.student_table.column("roll", width=100)
#         self.student_table.column("gender", width=100)
#         self.student_table.column("phone", width=100)
#         self.student_table.column("address", width=100)
#         self.student_table.column("photo", width=200)

#         self.student_table.pack(fill=BOTH, expand=1)

#     # ==================================Functions Declaration========================================
#     # validations
#     def add_data(self):
#         if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
#             messagebox.showerror("Error", "All Fields are mandatory", parent=self.root)
#             # here, parent=self.root shows the message explicitly in that window
#         else:
#             # pass
#             # messagebox.showinfo("Success", "Data Saved Successfully")
#             try:
#                 conn = mysql.connector.connect(host="localhost",
#                                                username="root",
#                                                password="Test@123",
#                                                database="face_recognizer")
#                 my_cursor = conn.cursor()
#                 my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
#                                   (
#                                       self.var_dep.get(),
#                                       self.var_course.get(),
#                                       self.var_year.get(),
#                                       self.var_semester.get(),
#                                       self.var_std_id.get(),
#                                       self.var_std_name.get(),
#                                       self.var_sec.get(),
#                                       self.var_roll.get(),
#                                       self.var_gender.get(),
#                                       self.var_phone.get(),
#                                       self.var_address.get(),
#                                       self.var_radio1.get()
#                                   ))
#                 conn.commit()
#                 conn.close()
#                 messagebox.showinfo("Done", "Student details have been added successfully", parent=self.root)

#             except Exception as es:
#                 messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)


# if __name__ == "__main__":
#     root = Tk()
#     obj = Student(root)
#     root.mainloop()

# # Project Type: Minor 6th Sem Project
# # Team : kyzen
# # College: NCIT (Nepal College of Information Technology)
# # University: Pokhara University

