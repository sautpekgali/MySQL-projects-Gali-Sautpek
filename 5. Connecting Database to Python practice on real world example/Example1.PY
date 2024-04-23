import csv, sqlite3
import pandas as pd 

# connecting database to python using sqlite3

con = sqlite3.connect("database1")
#creating cursor for data manipulation 

cur = con.cursor()

df = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/FinalModule_Coursera_V5/data/ChicagoCensusData.csv")

# transfer csv data into database1, which we created recently 
df.to_sql("CENSUS_DATA", con, if_exists='replace', index=False,method="multi")
print('Data is loaded!')

df = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/FinalModule_Coursera_V5/data/ChicagoCrimeData.csv")
df.to_sql("CHICAGO_CRIME_DATA", con, if_exists='replace', index=False, method="multi")


#retrieve the data from database, and show table names with their headings 
cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
p = cur.fetchall()
for i in p:
    print (i)

#retrieve the the list of columns in SCHOOLS table and their column type (datatype) and length
cur.execute("SELECT name,type,length(type) FROM PRAGMA_TABLE_INFO('CHICAGO_CRIME_DATA')")
p1 = cur.fetchall()
for i in p1:
    print(i)

