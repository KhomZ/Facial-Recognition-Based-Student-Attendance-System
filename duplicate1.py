import pandas as pd
import csv

# df = pd.read_csv(r"C:\Users\ACER\Desktop\myProj\Facial-Recognition-Based-Student-Attendance-System\customKyzen.csv", header=None)
df = pd.read_csv(r"Teamkyzen23.csv", header=None)


print(df)

# df.to_csv("example.csv", header=["Letter", "Number", "Symbol"], index=False)
# df.rename(columns={0: 'name', 1: 'id'}, inplace=True)
# df.columns = ['id' 'Roll' 'name' 'Dept' 'Time' 'Date' 'Status'] 

# df.to_csv(r"test1.csv", header = ['id', 'Roll', 'Name', 'Dept', 'Time', 'Date', 'Status'], index=False) 
df.to_csv(r"test1.csv", header = ['id', 'Roll', 'Name', 'Dept', 'Time', 'Date', 'Status'], index=False) 
# save to new csv file

# finaldata = pd.read_csv(r"C:\Users\ACER\Desktop\myProj\Facial-Recognition-Based-Student-Attendance-System\test1.csv")

finaldata = pd.read_csv(r"test1.csv")

# read CSV file
# results = pd.read_csv(r'test1.csv')
  
# count no. of lines
print("Number of lines present:-", len(finaldata))

# print(finaldata)