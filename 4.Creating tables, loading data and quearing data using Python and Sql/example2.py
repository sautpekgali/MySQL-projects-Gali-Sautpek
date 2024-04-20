import pandas as pd
import mysql.connector

#Entering credentials to connect to the database.
host = "127.0.0.1"
user = "root"
password = "Gali6134!"
database = "gali"

#Establishing Connection between MySQL Xampp example and Python.
connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)
# After establishing a connection, create a cursor object to execute SQL queries:
cursor = connection.cursor()

query1 = "SELECT * FROM instructor where id = 1"

pdf = pd.read_sql(query1,connection)

print (pdf)

pdf.shape

cursor.close()
connection.close()
