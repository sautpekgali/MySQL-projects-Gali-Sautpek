import sqlite3
import pandas as pd
#connecting DB to specific object
conn = sqlite3.connect('INSTRUCTOR.db')

# cursor object - is used to call methods that execute the SQLite statements and fetch data from the queries.

cursor_obj = conn.cursor()

#creating table inside the database. Before that it is essential to check the absence of the table inside the DB.
# Drop the table if already exists. 
cursor_obj.execute("DROP TABLE IF EXISTS INSTRUCTOR")

# Creating table = Write SQL command to create a table;
table = """ create Table IF NOT EXISTS Instructor (ID INTEGER PRIMARY KEY NOT NULL,F_NAME VARCHAR(20), L_NAME VARCHAR(20), CITY VARCHAR(20), CCODE VARCHAR(2)); """

cursor_obj.execute(table)

print ("table is ready")

#insert data inside the table 

cursor_obj.execute(''' insert into Instructor values (1,'Gali','Sautpek','Almaty','KZ')''')
cursor_obj.execute('''INSERT INTO Instructor values (2,'Aizhan','Syzdykova','Abylaikhan','KZ')''')

#Next step is to retrieve the data that we inserted into Instructor table
retrieve = ('''Select * from Instructor''')
cursor_obj.execute(retrieve)


print("All data were retrieved")
output = cursor_obj.fetchall()
for i in output:
    print(i)

# If you want to fetch few rows from the table we use fetchmany(numberofrows) and mention the number how many rows you want to fetch
retrieve = ('''Select * from Instructor''')
cursor_obj.execute(retrieve)

first_row = cursor_obj.fetchmany(1)
for i in first_row:
    print (i)

# Fetch only FNAME from the table
retrieve = ('''Select F_NAME,L_NAME from Instructor''')
cursor_obj.execute(retrieve)

name = cursor_obj.fetchall()
for i in name:
    print (i)

# Now, what to write to change the city name of Gali? from Almaty to Astana
query_update = ('''Update instructor set city = 'Astana' where f_name = 'Gali';''')
cursor_obj.execute(query_update)

#Next, retrieve the changes
new_city = ('''select * from instructor''')
cursor_obj.execute(new_city)

results1 = cursor_obj.fetchall()
for row in results1:
    print (row)

# Retrieve the table using Pandas 
#retrieve the query results into a pandas dataframe

df = pd.read_sql_query("select * from instructor;", conn)
print(df)
#print just the LNAME for first row in the pandas data frame

print(df.shape) # to see the shape of the dataframe
# Close the connection
conn.close()