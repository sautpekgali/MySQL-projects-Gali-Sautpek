import pandas as pd
import csv, sqlite3
import matplotlib.pyplot as plt
import seaborn as sns

con = sqlite3.connect("socioeconomic1.db") # create a database and store the data inside socioeconomic1.db
cur = con.cursor() 

df = pd.read_csv('https://data.cityofchicago.org/resource/jcxq-k9xf.csv')
df.to_sql("chicago_socioeconomic_data", con, if_exists='replace', index=False,method="multi")

#Execute SQL command using Python:  How many community areas in Chicago have a hardship index greater than 50.0?

cur.execute("Select count(*) from chicago_socioeconomic_data where hardship_index > 50") 
rows = cur.fetchall()

for i in rows:
    print (i)


#Execute SQL command using Python: What is the maximum value of hardship index in this dataset?

cur.execute("Select MAX(hardship_index) FROM chicago_socioeconomic_data ")
rows = cur.fetchall()

for i in rows:
    print (i)



#Execute SQL command using Python: Which community area which has the highest hardship index? (Using sub-query)
cur.execute("Select community_area_name FROM chicago_socioeconomic_data where hardship_index = (select  MAX(hardship_index) FROM chicago_socioeconomic_data )")
rows = cur.fetchall()

for i in rows:
    print (i)

#Execute SQL command using Python: Which Chicago community areas have per-capita incomes greater than $60,000?

cur.execute("Select community_area_name FROM chicago_socioeconomic_data where per_capita_income_ > 60000")
rows = cur.fetchall()
for i in rows:
    print (i)

# Creating scatter plot using two variables such as per_capita_income_ and hardship_index:

income_vs_hardship = cur.execute("Select hardship_index, per_capita_income_ from chicago_socioeconomic_data ")

data = cur.fetchall()

df = pd.DataFrame(data, columns=['hardship_index','per_capita_income_']) 

con.close()

plot = sns.jointplot(x = 'per_capita_income_', y = 'hardship_index', data = df)
plt.show()


