import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="<your_username>",
  password="<your_password>",
  database="<your_database>"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM your_table")

# Fetch and print the results
for x in mycursor:
  print(x)
    
mydb.commit()

mycursor.close()
mydb.close()