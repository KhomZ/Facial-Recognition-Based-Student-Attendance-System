import pandas as pd
import csv
df = pd.read_csv(r"E:\6th sem\my_project\Face_reg\face_recognize_student_attendence_system\Teamkyzen23.csv", header=None)
# df.rename(columns={0: 'name', 1: 'id'}, inplace=True)
df.columns = ['name1' 'name2' 'name3'] 
df.to_csv(r"E:\6th sem\my_project\Face_reg\face_recognize_student_attendence_system\test1.csv", index=False) # save to new csv file