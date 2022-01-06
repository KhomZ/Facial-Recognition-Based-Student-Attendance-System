from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk  # pip install
from tkinter import messagebox
import mysql.connector


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title('Registration Form')
        self.root.geometry("1600x500+0+0")

        # ***************variabletr
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

        # background img
        # self.bg = ImageTk.PhotoImage(
        #     file=r"E:\6th sem\my_project\Face_reg\face_recognize_student_attendence_system\img\5.jpg")
        self.bg = ImageTk.PhotoImage(
            file = r"C:\Users\ACER\Desktop\myProj\Facial-Recognition-Based-Student-Attendance-System\img\5.jpg")
        lbl_lbl = Label(self.root, image=self.bg)
        lbl_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        # #left image
        # self.bg1 = ImageTk.PhotoImage(
        #     file=r"E:\6th sem\my_project\Face_reg\face_recognize_student_attendence_system\img\6.jpg")
        self.bg1 = ImageTk.PhotoImage(
            file = r"C:\Users\ACER\Desktop\myProj\Facial-Recognition-Based-Student-Attendance-System\img\6.jpg")
        left_lbl = Label(self.root, image=self.bg1)
        left_lbl.place(x=50, y=100, width=470, height=550)
        # main frame
        frame = Frame(self.root, bg="white")
        frame.place(x=520, y=100, width=800, height=550)

        register_lbl = Label(frame, text="REGISTER HERE", font=(
            "times new roman", 20, "bold"), fg="green", bg="white")
        register_lbl.place(x=20, y=20)

        # ***lebal and entry
        # column 1
        fname = Label(frame, text="First and Middle Name", font=(
            "times new roman", 15, "bold"), bg="white")
        fname.place(x=50, y=100)

        self.fname_entry = ttk.Entry(
            frame, textvariable=self.var_fname, font=("times new roman", 15))
        self.fname_entry.place(x=50, y=130, width=250)

        lname = Label(frame, text="Last Name", font=(
            "times new roman", 15, "bold"), bg="white")
        lname.place(x=370, y=100)

        self.txt_lname = ttk.Entry(
            frame, textvariable=self.var_lname, font=("times new roman", 15))
        self.txt_lname.place(x=370, y=130, width=250)

        # column 2
        contact = Label(frame, text="Contact No", font=(
            "times new roman", 15, "bold"), bg="white")
        contact.place(x=50, y=170)

        self.txt_contact = ttk.Entry(
            frame, textvariable=self.var_contact, font=("times new roman", 15))
        self.txt_contact.place(x=50, y=200, width=250)

        email = Label(frame, text="Email", font=(
            "times new roman", 15, "bold"), bg="white")
        email.place(x=370, y=170)

        self.txt_email = ttk.Entry(
            frame, textvariable=self.var_email, font=("times new roman", 15))
        self.txt_email.place(x=370, y=200, width=250)

        # ...........column3
        security_Q = Label(frame, text="Select Security Question", font=(
            "times new roman", 15, "bold"), bg="white")
        security_Q.place(x=50, y=240)

        self.combo_security_Q = ttk.Combobox(frame, textvariable=self.var_securityQ, font=(
            "times new roman", 15, "bold"), state="readonly")
        self.combo_security_Q["values"] = ("Select", "Your Birth place", "your dad name", "your mother name")
        self.combo_security_Q.place(x=50, y=270, width=250)
        self.combo_security_Q.current(0)

        security_A = Label(frame, text="Security Answer", font=(
            "times new roman", 15, "bold"), bg="white")
        security_A.place(x=370, y=240)

        self.txt_security = ttk.Entry(
            frame, textvariable=self.var_securityA, font=("times new roman", 15))
        self.txt_security.place(x=370, y=270, width=250)

        # ......colum 5
        pswd = Label(frame, text="Password", font=(
            "times new roman", 15, "bold"), bg="white")
        pswd.place(x=50, y=310)

        self.txt_pswd = ttk.Entry(
            frame, textvariable=self.var_pass, font=("times new roman", 15))
        self.txt_pswd.place(x=50, y=340, width=250)

        confirm_pswd = Label(frame, text="Comfirm Password", font=(
            "times new roman", 15, "bold"), bg="white")
        confirm_pswd.place(x=370, y=310)

        self.txt_confirm_pswd = ttk.Entry(
            frame, textvariable=self.var_confpass, font=("times new roman", 15))
        self.txt_confirm_pswd.place(x=370, y=340, width=250)

        # ......check button
        self.var_check = IntVar()
        checkbtn = Checkbutton(frame, variable=self.var_check, text="I am Agree terms and conditions", font=(
            "times new roman", 12, "bold"), bg="white", onvalue=1, offvalue=0)
        checkbtn.place(x=50, y=380)

        # button

        # img = Image.open(
        #     r"E:\6th sem\my_project\Face_reg\face_recognize_student_attendence_system\img\7.jpg")
        img = ImageTk.PhotoImage(
            file = r"C:\Users\ACER\Desktop\myProj\Facial-Recognition-Based-Student-Attendance-System\img\7.jpg")
        img = img.resize((200, 50), Image.ANTIALIAS)
        self.photoimage = ImageTk.PhotoImage(img)
        b1 = Button(frame, command=self.register_data,
                    image=self.photoimage, borderwidth=0, cursor="hand2")
        b1.place(x=10, y=420, width=200)

        # img1 = Image.open(
        #     r"E:\6th sem\my_project\Face_reg\face_recognize_student_attendence_system\img\8.jpg")
        img1 = ImageTk.PhotoImage(
            file = r"C:\Users\ACER\Desktop\myProj\Facial-Recognition-Based-Student-Attendance-System\img\8.jpg")
        img1 = img1.resize((200, 50), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b1 = Button(frame, image=self.photoimage1,
                    borderwidth=0, cursor="hand2")
        b1.place(x=330, y=420, width=200)

# ...............function...................

    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "Select":
            messagebox.showerror("Error", "All fills are required",parent=self.root)
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror(
                "Error", "password and confirm password must be same")
        elif self.var_check.get() == 0:
            messagebox.showerror(
                "Error", "Please agree our terms and condition")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="root@khom123",database="khomdb")
            # conn = mysql.connector.connect(host="localhost", user="root", password="Keshav@123", database="mydata")
            my_cursor = conn.cursor()
            query = ("select * from register where email=%s")
            value = (self.var_email.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row!= None:
                messagebox.showerror("Error", "user already exist ,try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)", (

                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_securityQ.get(),
                    self.var_securityA.get(),
                    self.var_pass.get()
                ))
                messagebox.showinfo("Success","Registered Successfully")
            conn.commit()
            conn.close()
               


# object ko open garna
if __name__ == "__main__":
    root = Tk()
    app = Register(root)
    root.mainloop()
