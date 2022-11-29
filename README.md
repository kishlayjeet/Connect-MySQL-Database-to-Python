# Connect MySql database with Python  

In this section, I'll explain how to connect your MySQL database to Python and query it.

## Install "MySQL Connector"
To access the MySQL database, Python needs a MySQL driver. You must first install the `MySQL Connector` package on your computer.
```bash
  python -m pip install mysql-connector-python
```

## Import "MySQL Connector"
To access the MySQL database, import the MySQL connector library into your Python code.
```python
  import mysql.connector
```

## Create Connection
First, establish a connection to the database. Use your MySQL database's username and password in the Python code.
```python
  mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword"
  )
```
Now you can use SQL commands to query the database.

## Make Cursor
You must create or include a `cursor()` in your Python code in order to run MySQL queries.
```python
  mycursor = mydb.cursor()
```

## Creating a Database
To create a database in MySQL, use the `CREATE DATABASE` statement.
```python
  mycursor.execute("CREATE DATABASE mydatabase")
```

## Show Database
By using the `SHOW DATABASES` query to display every database on your system, you may verify that your database has been created.
```python
  mycursor.execute("SHOW DATABASES")
  
  for x in mycursor:
    print(x)
```
If the above code was executed without errors, you have successfully created a database. Now that your database has been created, you can also run another SQL command to query the database.

## Commit Changes
To save the changes in the database, use the `commit()` function.
```python
  mydb.commit()
```

## Close the Connection
In the end, you must close the cursor and the connection. 
```python
  mycursor.close()
  mydb.close()
```
You can also get code snippet from [here](https://github.com/kishlayjeet/Conenct-MySql-database-with-Python/blob/1ab44e07ea0d78122d00e01dc0ef1063f496df99/code-snippet.py).

## Authors

I am [Kishlay](https://www.github.com/kishlayjeet), and I have written this tutorial, but other people have also helped me with it.
If you have any trouble with this tutorial, please tell me about it, and I will make it better.
If you like this tutorial and this helped you out, then please give it a star.



## Feedback

If you have any feedback, please reach out to me at contact.kishlayjeet@gmail.com