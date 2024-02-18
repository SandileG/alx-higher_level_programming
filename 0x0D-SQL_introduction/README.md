## Introduction to SQL

# Database:

A database is a structured collection of data organized for efficient retrieval, storage, and manipulation. It acts as a central repository for storing and managing various types of information.
Relational Database:

A relational database is a type of database that organizes data into tables, where each table represents a distinct entity or concept. Relationships between tables are established using keys, enabling efficient querying and manipulation of data.

# SQL:

SQL stands for Structured Query Language. It is a standard programming language used to communicate with and manage relational databases. SQL enables users to perform tasks such as querying data, defining database structures, and manipulating data within the database.
MySQL:

MySQL is an open-source relational database management system (RDBMS) that uses SQL as its query language. It is widely used for building web applications and other types of software due to its performance, reliability, and scalability.

# Creating a Database in MySQL:

To create a database in MySQL, you can use the CREATE DATABASE statement followed by the desired database name. For example:
sql
Copy code
CREATE DATABASE database_name;

# DDL and DML:

DDL stands for Data Definition Language, which includes SQL commands used to define and modify database structures, such as creating, altering, or dropping tables and indexes.
DML stands for Data Manipulation Language, which includes SQL commands used to manipulate data within tables, such as inserting, updating, deleting, and querying data.

# Creating or Altering a Table:

To create a table in MySQL, you can use the CREATE TABLE statement followed by the table name and column definitions. For example:
sql
Copy code
CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    ...
);
To alter an existing table in MySQL, you can use the ALTER TABLE statement followed by the desired alterations, such as adding, modifying, or dropping columns.

# Selecting Data from a Table:

To select data from a table in MySQL, you can use the SELECT statement followed by the desired columns and table name. For example:
sql
Copy code
SELECT column1, column2 FROM table_name WHERE condition;

# Inserting, Updating, or Deleting Data:

To insert data into a table, you can use the INSERT INTO statement followed by the table name and values to be inserted.
To update data in a table, you can use the UPDATE statement followed by the table name and the new values.
To delete data from a table, you can use the DELETE FROM statement followed by the table name and a condition specifying which rows to delete.

# Subqueries:

Subqueries, also known as nested queries or inner queries, are SQL queries nested within another query. They allow you to retrieve data from multiple tables or perform complex operations by using the result of one query as input for another.

# Using MySQL Functions:

MySQL provides a wide range of built-in functions for performing various operations on data. These functions can be used in SQL queries to manipulate, aggregate, or transform data. Examples include mathematical functions, string functions, date and time functions, and aggregate functions like SUM, COUNT, and AVG.
