  In this folder you could find basic commands and examples to connect SQL to Python for data analysis. 
In the begging of the each exmples we should set the connection between Python and SQL. This process can be done by importing necessary libraries and establishing cursor.
```python
import csv, sqlite3
con = sqlite3.connect("socioeconomic.db") # create a database and store the data inside socioeconomic1.db
cur = con.cursor() 
```
  Here, con = sqlite3.connect("socioeconomic.db") - creates a connection to a SQLite database named "socioeconomic.db" and establishes the connection between Python and SQL
cursor allows you to execute SQL commands and navigate through the results returned by queries such as creating tables, inserting data, updating data, or querying data from existing tables in the database.

Than, after establishing connection we can execute SQL commands. For eaxmple, we want to know how many community areas in Chicago have a hardship index greater than 50.0.
```python
cur.execute("Select count(*) from chicago_socioeconomic_data where hardship_index > 50") 
rows = cur.fetchall()

for i in rows:
    print (i)
con.close()
```
  Generally, we can use SQL commands in Python by many different ways. One of the main appoches is to illustrate the data on the graph. To do so, we should import necessery libraries and execure SQL commands:

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

income_vs_hardship = cur.execute("Select hardship_index, per_capita_income_ from chicago_socioeconomic_data ")

data = cur.fetchall()

df = pd.DataFrame(data, columns=['hardship_index','per_capita_income_']) 
plot = sns.jointplot(x = 'per_capita_income_', y = 'hardship_index', data = df)
plt.show()
```
  These simple examples were discribed and explained in details inside this repository. Feel free to download and ask questions if necessery. Thnak you! 
