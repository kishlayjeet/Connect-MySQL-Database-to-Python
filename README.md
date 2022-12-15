# Connect MySQL database to Python.

In this section, I'll explain how you can connect your MySQL database to Python and query it.
To connect MySQL with Python, you will need to have both [MySQL](https://dev.mysql.com/downloads/) and [Python](https://www.python.org/downloads/) installed on your system.

## Setup MySQL

To access the MySQL database, Python needs a MySQL driver called `MySQL Connector`, So you must first install the MySQL connector package on your computer.
The MySQL connector package is available on the [Python Package Index (PyPI)](https://pypi.org), and it can be easily installed using the `pip` package manager.

You can do this by running the following command in your terminal:

```bash
  pip install mysql-connector-python
```

## Import MySQL connector

Import the MySQL connector module into your Python code.
This module provides a Python API for connecting to and interacting with a MySQL database.

To import the module, use the following syntax:

```python
  import mysql.connector
```

## Creating a Database:

For purposes of example, we will need a sample database in MySQL that you can connect to.
If you don't have a database to do so, follow the below steps:

- First, open a MySQL client tool like [MySQL Workbench](https://dev.mysql.com/downloads/workbench/) or use a terminal.
- Second login to the database using your credentials.
- Finally, run the following command to create a database (for example, company).

```mysql
  CREATE DATABASE company;
```

## Make a Connection

Create a new MySQLConnection object by calling the `connect()` function from the mysql.connector module.
This function takes a number of parameters that specify details about the database you want to connect to, such as:

- `host`: the IP address or hostname of the MySQL server. By default, this is localhost.
- `user`: the username that you want to use to connect to MySQL.
- `password`: the password associated with the username.
- `database`: the name of the database that you want to connect to.

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

## Create a Table

By using the `CREATE TABLE` statement, it creates a new table called `employee` with three columns:

| EmployeeID | Name | Email |
| :--------- | :--- | :---- |

```python
  mycursor.execute('''CREATE TABLE employee(
      EmployeeID int,
      Name varchar(255),
      Email varchar(255));
  ''')
```

Now your table has been created.

## Insert some Records

By using the `INSERT INTO` statement to insert some records into your employee table, you just created

```python
  mycursor.execute('''
    INSERT INTO employee (EmployeeID, Name, Email)
      VALUES (101, 'Mark', 'mark@company.com'),
             (102, 'Robert', 'robert@company.com'),
             (103, 'Spencer', 'spencer@company.com');
  ''')
```

## Commit the Changes

It's important to remember to save your changes to the database using the `commit()` method every time you run the query.

```python
  mydb.commit()
```

This is necessary because MySQL uses a transactional storage engine, which means that changes are not visible to other connections until they are committed.

## Fetch the Record

Now, you have to use the `execute()` method of the cursor object to execute a `SELECT` statement that retrieves all rows from the employee table.
Then you have to use a for loop to iterate over the rows returned by the query and print them to the console.

```python
  mycursor.execute("SELECT * FROM your_table")

  for x in mycursor:
    print(x)
```

If the above code was executed without errors, you have successfully viewed table records.
Now that your cursor is working, you can also run other SQL commands to query the database.

## Close the Connection

And finally, once you're done, you need to close the cursor and the connection to free up resources and prevent potential issues.

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
