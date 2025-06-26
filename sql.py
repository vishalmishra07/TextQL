import sqlite3

## Connection to sqlite
connection=sqlite3.connect("student.db")


## Create a cursor object to insert record,create table,retrive result == can retrieve anything
cursor = connection.cursor()

## create the Student table
table_info = '''CREATE TABLE IF NOT EXISTS STUDENT(name TEXT, course TEXT, section TEXT, marks INT)'''

cursor.execute(table_info)


## Insert some more records

cursor.execute(''' Insert Into STUDENT values('krish Sharma','Data Sciene','A',90)''')
cursor.execute(''' Insert Into STUDENT values('Vishal Mishra','Data Science','D',100)''')
cursor.execute(''' Insert Into STUDENT values('Smarth Phutela','DEVOPS','C',99)''')
cursor.execute(''' Insert Into STUDENT values('Shubhangi Shah','Full Stack Developer','A',60)''')
cursor.execute(''' Insert Into STUDENT values('Ria Rathore','DEVOPS','B',70)''')


##Display all the records
print("The inserted records are: ")
data=cursor.execute('''Select * From STUDENT''')

for row in data:
    print(row)
    
    
## commit and close connection
connection.commit()
connection.close()