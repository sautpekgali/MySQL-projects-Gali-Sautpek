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

# Creating a table in the "gali" database

table1 = cursor.execute("CREATE TABLE IF NOT EXISTS instructor (id INT AUTO_INCREMENT PRIMARY KEY, FNAME VARCHAR (50),LNAME VARCHAR(50),CITY VARCHAR(15))")

print("Table 'instructor' created successfully.")
# Loading data into the "INSTRUCTOR" table

load1 = cursor.execute ("INSERT INTO instructor (id,FNAME,LNAME,CITY) values (2,'Aizhan','Syzdykova','Abylaikhan')")
connection.commit()

print("Data is loaded successfully.")

cursor.execute("Select * from instructor " )
rows = cursor.fetchall()
for i in rows:
    print(i)

cursor.close()
connection.close()