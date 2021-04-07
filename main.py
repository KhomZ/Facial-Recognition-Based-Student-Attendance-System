# Developer : team kyzen
# Date : 

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x730+0+0")
        self.root.title("Face Recognition System")

        img1 = Image.open("Images/PUbanner_2.jpg")
        img1 = img1.resize((500, 130), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=0, width=500, height=130)

        img2 = Image.open("Images/3faces.jpeg")
        img2 = img2.resize((500, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=500, y=0, width=500, height=130)

        img3 = Image.open("Images/ncit-wide2017-11-18.jpg")
        img3 = img3.resize((500, 130), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lbl = Label(self.root, image=self.photoimg3)
        f_lbl.place(x=1000, y=0, width=500, height=130)

        img4 = Image.open("Images/PUbanner_2.jpg")
        img4 = img4.resize((1500, 600), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        f_lbl = Label(self.root, image=self.photoimg4)
        f_lbl.place(x=0, y=130, width=1500, height=600)


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()

