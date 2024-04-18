import mysql.connector

#Entering credentials to connect to the database.
host = "127.0.0.1"
user = "root"
password = "Gali6134!"
database = "sys"

#Establishing Connection between MySQL Xampp example and Python.
connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)
# After establishing a connection, create a cursor object to execute SQL queries:
cursor = connection.cursor()

cursor.execute("Select * from petrescue")

rows = cursor.fetchall()
for i in rows:
    print(i)

cursor.close()
connection.close()