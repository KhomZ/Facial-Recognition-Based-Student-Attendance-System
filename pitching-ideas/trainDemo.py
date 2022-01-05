# from logging import root
# from os import close, path
# from tkinter import*
# from tkinter import ttk
# from PIL import Image, ImageTk
# from tkinter import messagebox
# import mysql.connector
# from mysql.connector import cursor
# import os
# import numpy as np
# import cv2
# from ntpath import join
# from tkinter import*
# from tkinter import ttk
# from PIL import Image,ImageTk
# from tkinter import messagebox
# import mysql.connector
# import cv2
# import os
# import numpy as np


# class Train:
#     def __init__(self,root):
#         self.root=root
#         self.root.geometry("1530x790+0+0")
#         self.root.title("Face Recognition System")


        
#         title_lbl=Label(self.root,text="TRAIN DATA SET",font=("times new roman",30,"bold"),bg="white",fg="Red")
#         title_lbl.place(x=0, y=0, width=1530,height=45)

#         img_top=Image.open(r"E:\6th sem\my_project\Face_reg\face_recognize_student_attendence_system\Images\NCIT.jpg")
#         img_top=img_top.resize((1530,325),Image.ANTIALIAS)  #Antialias lea high level image lai low level mah convert garxa
#         self.photoimg_top=ImageTk.PhotoImage(img_top)

#         f_lbl=Label(self.root,image=self.photoimg_top)
#         f_lbl.place(x=0, y=55,width=1530,height=325)

#         # Button....................

#         btn1 = Button(self.root, text="TRAIN DATA",command=self.train_classifier, cursor="hand2", font=("times new roman", 15, "bold"),
#                         bg="darkblue", fg="white")
#         btn1.place(x=0, y=380, width=1530, height=60)



#         img_bottom=Image.open(r"E:\6th sem\my_project\Face_reg\face_recognize_student_attendence_system\Images\developer.png")
#         img_bottom=img_bottom.resize((1530,325),Image.ANTIALIAS)  #Antialias lea high level image lai low level mah convert garxa
#         self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

#         f_lbl=Label(self.root,image=self.photoimg_bottom)
#         f_lbl.place(x=0, y=440,width=1530,height=325)


#     # def train_classifier(self):
#     #     data_dir=("Data")
#     #     path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

#     #     faces=[]
#     #     ids=[]


#     #     for image in path:
#     #         img= Image.open(image).convert('L')

#     #         imageNp=np.array(img,'uint8')
#     #         id =int(os.path.split(image)[1].split('.')[1])
#     #         faces.append(imageNp)
#     #         ids.append(id)
#     #         cv2.imshow("Training",imageNp)
#     #         cv2.waitKey(1)==13
#     #     ids=np.array(ids)
#     #         # ....................Train classifier....

#     #     clf=cv2.face.LBPHFaceRecognizer_create()
#     #     clf.train(faces,ids)
#     #     clf.Write("classifier.xml")
#     #     cv2.destroyAllWindows()
#     #     messagebox.showinfo("Result","Training dataset completed")
#     def train_classifier(self):
#         data_dir=("data")
#         path=[os.path.join(data_dir,file) for  file in os.listdir(data_dir)]

#         faces=[]
#         ids=[]
        
#         for image in path:
#             img=Image.open(image).convert('L')  # grAY SCALE image
#             imageNp=np.array(img,'uint8')
#             id=int(os.path.split(image)[1].split('.')[1])

#             faces.append(imageNp)
#             ids.append(id)
#             cv2.imshow("Training",imageNp)
#             cv2.waitKey(1)==13
#         ids=np.array(ids)
        
#         # Train the classifier and save 
#         clf=cv2.face.LBPHFaceRecognizer_create()
#         clf.train(faces,ids)
#         clf.write("classifier.xml")
#         cv2.destroyAllWindows()
#         messagebox.showinfo("Result","Training datasets completed !")
        

# if __name__=="__main__":
#     root=Tk()
#     obj=Train(root)
#     root.mainloop()

from ntpath import join
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np



class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("Algerian",20,"bold"),bg="lightgreen",fg="Blue")
        title_lbl.place(x=0,y=0,width=1366,height=35)
        
        # img_top=Image.open(r"E:\6th sem\my_project\Face_reg\face_recognize_student_attendence_system\Images\re2.jpg")
        img_top = Image.open(r"C:\Users\ACER\Desktop\myProj\Facial-Recognition-Based-Student-Attendance-System\Images\re2.jpg")
        img_top=img_top.resize((1366, 700),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=50,width=1366,height=650)
        
        # Button
        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("Algerian",25,"bold"),bg="green",fg="white")
        b1_1.place(x=500,y=450,width=300,height=150)
        
        # img_bottom=Image.open(r"E:\6th sem\my_project\Face_reg\face_recognize_student_attendence_system\Images\NCIT.jpg")
        # img_bottom=img_bottom.resize((1366, 300),Image.ANTIALIAS)
        # self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        # f_lbl=Label(self.root,image=self.photoimg_bottom)
        # f_lbl.place(x=0,y=390,width=1366,height=300)
        
    def train_classifier(self):
        # data_dir=(r"E:\6th sem\my_project\Face_reg\face_recognize_student_attendence_system\data")
        data_dir = (r"C:\Users\ACER\Desktop\myProj\Facial-Recognition-Based-Student-Attendance-System\data")
        path=[os.path.join(data_dir,file) for  file in os.listdir(data_dir)]

        faces=[]
        ids=[]
        
        for image in path:
            img=Image.open(image).convert('L')  # grAY SCALE image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        # Train the classifier and save 
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed !",parent=self.root)
        # self.root.destroy()



    
if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()