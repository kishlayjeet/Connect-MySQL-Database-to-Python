# Connect Python to the MySQL database.

In this section, I'll explain how you can connect your MySQL database to Python and query it.
To connect MySQL with Python, you will need to have both MySQL and Python installed on your system.

## Setup `MySQL Connector`

To access the MySQL database, Python needs a MySQL driver called `MySQL Connector`, So you must first install the MySQL connector package on your computer.
The MySQL connector package is available on the [Python Package Index (PyPI)](https://pypi.org), and it can be easily installed using the `pip` package manager.

You can do this by running the following command in your terminal:

```bash
  pip install mysql-connector-python
```

## Import `MySQL Connector`

Import the MySQL connector module into your Python code.
This module provides a Python API for connecting to and interacting with a MySQL database.

To import the module, use the following syntax:

```python
  import mysql.connector
```

## Creating a Database:

For purposes of example, we will need a sample database. To do so, follow the below steps:

- First, open a MySQL client tool like MySQL Workbench or use a terminal.
- Second login to the database using your credentials.
- Finally, run the following command to create a database (for example, company).

```mysql
  CREATE DATABASE company;
```

## Make a connection

Create a new MySQLConnection object by calling the `connect()` function from the mysql.connector module.
This function takes a number of parameters that specify details about the database you want to connect to, such as the hostname, username, password, and database name.

- Use your MySQL's username, password, and database in the Python code.
  For example:

```python
  mydb = mysql.connector.connect(
    host="localhost",
    user="<your_username>",
    password="<your_password>",
    database="<your_database>"
  )
```

Once you have successfully established a connection to the database, you can start running SQL queries and performing other operations.

## Make a Cursor

You must create or include a cursor in your python code in order to run MySQL queries.

```python
  mycursor = mydb.cursor()
```

A cursor is a pointer to the result set of a query, and it is used to iterate over the rows of the result set.
Cursors are useful for breaking up large result sets into smaller pieces and processing them one row at a time.

## Execute a SQL query

By using the `SELECT` query to display every record in your table.

```python
  mycursor.execute("SELECT * FROM your_table")

  # Fetch and print the results
  for x in mycursor:
    print(x)
```

If the above code was executed without errors, you have successfully viewed table records.
Now that your cursor is working, you can also run another SQL command to query the database.

## Commit the Changes

It's important to remember to save your changes to the database using the `commit()` function every time you run the code.

```python
  mydb.commit()
```

## Close the Connection and the Cursor.

And finally, once you're done, you need to close the cursor and the connection.

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
