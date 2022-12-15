import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="<your_username>",
  password="<your_password>",
  database="<your_database>"
)

mycursor = mydb.cursor()

mycursor.execute('''CREATE TABLE employee(  
    EmployeeID int,  
    Name varchar(255),  
    Email varchar(255));
''')

mycursor.execute('''
  INSERT INTO employee (EmployeeID, Name, Email) 
    VALUES (101, 'Mark', 'mark@company.com'),
           (102, 'Robert', 'robert@company.com'),
           (103, 'Spencer', 'spencer@company.com');
''')

mydb.commit()

mycursor.execute("SELECT * FROM your_table")
for x in mycursor:
  print(x)

mycursor.close()
mydb.close()