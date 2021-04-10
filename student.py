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

        img_left = Image.open("Images/scholarImages/happy-students.jpg")
        img_left = img_left.resize((650, 120), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=640, height=120)

        current_course_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Current Course Information",
                                font=("Calibri", 12, "bold"), fg="blue")
        current_course_frame.place(x=5, y=125, width=640, height=140)

        dep_label = Label(current_course_frame, text="Department", font=("Calibri", 10, "bold"), bg="white", fg="blue")
        dep_label.grid(row=0, column=0, padx=5, pady=5)

        dep_combo = ttk.Combobox(current_course_frame, font=("Calibri", 10, "bold"), width=17, state="readonly")
        dep_combo["values"] = ("Select Department", "Computer", "IT", "Electronics", "Civil")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=5, pady=5)

        # right label frame
        Right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details", font=("Calibri", 12, "bold"))
        Right_frame.place(x=670, y=10, width=650, height=500)


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()

