# Developer : team kyzen
# Date : Saturday, April 10 2021

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1450x720+0+0")
        self.root.title("Face Recognition System")


        # first image
        img1 = Image.open("Images/scholarImages/smart-attendance.jpg")
        img1 = img1.resize((450, 120), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=0, width=450, height=120)

        # second image
        img2 = Image.open("Images/NCIT-building.jpg")
        img2 = img2.resize((450, 120), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=450, y=0, width=450, height=120)

        # third image
        img3 = Image.open("Images/scholarImages/Graduation-2014.jpg")
        img3 = img3.resize((450, 120), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lbl = Label(self.root, image=self.photoimg3)
        f_lbl.place(x=900, y=0, width=450, height=120)

        # background image
        img4 = Image.open("Images/face-recognition-logo.jpeg")
        img4 = img4.resize((1350, 580), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=120, width=1350, height=580)

        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM",
                          font=("times new roman", 35, "bold"), bg="white", fg="magenta")
        title_lbl.place(x=0, y=0, width=1350, height=45)  # using .place u can place things at any part of the window

        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=10, y=55, width=1330, height=570)

        # left label frame
        Left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Information", font=("Calibri", 12, "bold"))
        Left_frame.place(x=10, y=10, width=650, height=500)

        img_left = Image.open("Images/scholarImages/grad2.jpg")
        img_left = img_left.resize((650, 80), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=640, height=60)

        current_course_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Current Course Information",
                                font=("Calibri", 12, "bold"), fg="green")
        current_course_frame.place(x=5, y=60, width=640, height=90)

        # Department
        dep_label = Label(current_course_frame, text="Department :", font=("Calibri", 10, "bold"), bg="white", fg="blue")
        dep_label.grid(row=0, column=0, padx=10, sticky=W)

        dep_combo = ttk.Combobox(current_course_frame, font=("Calibri", 10, "bold"), state="readonly")
        dep_combo["values"] = ("Select Department", "Computer", "IT", "Electronics", "Civil")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=5, sticky=W)

        # Course
        course_label = Label(current_course_frame, text="Course :", font=("Calibri", 10, "bold"), bg="white", fg="blue")
        course_label.grid(row=0, column=2, padx=10, sticky=W)

        course_combo = ttk.Combobox(current_course_frame, font=("Calibri", 10, "bold"), state="readonly")
        course_combo["values"] = ("Select Course", "SNM", "OOSE", "DC", "ES", "NLP")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Year
        year_label = Label(current_course_frame, text="Year :", font=("Calibri", 10, "bold"), bg="white", fg="blue")
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(current_course_frame, font=("Calibri", 10, "bold"), state="readonly")
        year_combo["values"] = ("Select Year", "2021-22", "2022-23", "2023-24", "2024-25")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=5, sticky=W)

        # Semester
        sem_label = Label(current_course_frame, text="Semester :", font=("Calibri", 10, "bold"), bg="white", fg="blue")
        sem_label.grid(row=1, column=2, padx=10, sticky=W)

        sem_combo = ttk.Combobox(current_course_frame, font=("Calibri", 10, "bold"), state="readonly")
        sem_combo["values"] = ("Select Semester", "II", "IV", "VI", "VIII")
        sem_combo.current(0)
        sem_combo.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        #
        # Student's Class Information
        #
        student_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Student's Class Information",
                                          font=("Calibri", 12, "bold"), fg="green")
        student_frame.place(x=5, y=150, width=640, height=300)

        # studentID
        studentID_label = Label(student_frame, text="StudentID:", font=("Calibri", 10, "bold"), bg="white",
                          fg="blue")
        studentID_label.grid(row=0, column=0, padx=10, sticky=W)

        studentID_entry = ttk.Entry(student_frame, width=20, font=("Calibri", 10, "bold"))
        studentID_entry.grid(row=0, column=1, padx=10, sticky=W)

        # student's Name
        stdName_label = Label(student_frame, text="Name:", font=("Calibri", 10, "bold"), bg="white",
                          fg="blue")
        stdName_label.grid(row=0, column=2, padx=10, sticky=W)

        stdName_entry = ttk.Entry(student_frame, width=20, font=("Calibri", 10, "bold"))
        stdName_entry.grid(row=0, column=3, padx=10, sticky=W)

        # Section
        section_label = Label(student_frame, text="Section:", font=("Calibri", 10, "bold"), bg="white",
                          fg="blue")
        section_label.grid(row=1, column=0, padx=10, sticky=W)

        section_entry = ttk.Entry(student_frame, width=20, font=("Calibri", 10, "bold"))
        section_entry.grid(row=1, column=1, padx=10, sticky=W)

        # studentRollNo
        studentRoll_label = Label(student_frame, text="RollNo:", font=("Calibri", 10, "bold"), bg="white",
                          fg="blue")
        studentRoll_label.grid(row=1, column=2, padx=10, sticky=W)

        studentRoll_entry = ttk.Entry(student_frame, width=20, font=("Calibri", 10, "bold"))
        studentRoll_entry.grid(row=1, column=3, padx=10, sticky=W)

        # Gender
        gender_label = Label(student_frame, text="Gender:", font=("Calibri", 10, "bold"), bg="white", fg="blue")
        gender_label.grid(row=2, column=0, padx=10, sticky=W)

        gender_combo = ttk.Combobox(student_frame, font=("Calibri", 10, "bold"), state="readonly")
        gender_combo["values"] = ("Select Gender", "Male", "Female", "LGBTQ")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # student's Contact Info
        phone_label = Label(student_frame, text="Contact No.:", font=("Calibri", 10, "bold"), bg="white",
                              fg="blue")
        phone_label.grid(row=2, column=2, padx=10, sticky=W)

        phone_entry = ttk.Entry(student_frame, width=20, font=("Calibri", 10, "bold"))
        phone_entry.grid(row=2, column=3, padx=10, sticky=W)

        # student's Address
        address_label = Label(student_frame, text="Address:", font=("Calibri", 10, "bold"), bg="white",
                              fg="blue")
        address_label.grid(row=3, column=0, padx=10, sticky=W)

        address_entry = ttk.Entry(student_frame, width=20, font=("Calibri", 10, "bold"))
        address_entry.grid(row=3, column=1, padx=10, sticky=W)

        # ==================================Radio Buttons========================================
        radiobtn1 = ttk.Radiobutton(student_frame, text="Capture Photo Sample", value="Yes")
        radiobtn1.grid(row=6, column=0)

        radiobtn2 = ttk.Radiobutton(student_frame, text="No Photo Sample", value="Yes")
        radiobtn2.grid(row=6, column=1)

        # ==================================Buttons Frames========================================
        btnFrame = Frame(student_frame, relief=RIDGE, bg="cyan")
        btnFrame.place(x=0, y=180, width=640, height=80)

        save_btn = Button(btnFrame, text="Save", font=('arial', 13, 'bold'), bg="red", fg="green")
        save_btn.grid(row=0, column=0)

        # right label frame
        Right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details", font=("Calibri", 12, "bold"))
        Right_frame.place(x=670, y=10, width=650, height=500)


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()

