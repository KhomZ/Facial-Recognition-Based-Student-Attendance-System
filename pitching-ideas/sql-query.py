import mysql.connector


conn=mysql.connector.connect(host="localhost",username="root",password="root@khom123",database="khomdb")
my_cursor=conn.cursor()
my_cursor.execute("select * from student1")
myresult=my_cursor.fetchall()
print(myresult)
# print('\n')

conn.commit()
# self.fetch_data()
conn.close()