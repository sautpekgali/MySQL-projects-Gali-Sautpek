import csv,sqlite3
import pandas as pd 

#connecting and creating databases
connect1 = sqlite3.connect('FinalDB.db')

cursor = connect1.cursor()

#Reading and loading tables into FinalDb  database.

table1 = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/FinalModule_Coursera_V5/data/ChicagoCensusData.csv?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork20127838-2021-01-01")

table1.to_sql("CENSUS_DATA", connect1, if_exists='replace',index=False,method='multi')

table3 = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/FinalModule_Coursera_V5/data/ChicagoCrimeData.csv?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork20127838-2021-01-01")
table3.to_sql("CHICAGO_CRIME_DATA",connect1,if_exists='replace',index=False,method='multi')

print('data is loaded')

query0 = "SELECT name,type,length(type) FROM PRAGMA_TABLE_INFO('CHICAGO_CRIME_DATA')"
pdf0 = pd.read_sql(query0,connect1)
print(pdf0)

query1 = "SELECT count(*) from CHICAGO_CRIME_DATA"

pdf = pd.read_sql(query1,connect1)
print (pdf)



query2 = "SELECT name,type,length(type) FROM PRAGMA_TABLE_INFO('CENSUS_DATA')"
pdf2 = pd.read_sql(query2,connect1)
print(pdf2)

#List community area names and numbers with per capita income less than 11000.

query3 = "SELECT  COMMUNITY_AREA_NAME, PER_CAPITA_INCOME as Numbers from CENSUS_DATA where PER_CAPITA_INCOME<11000 "
pdf3 = pd.read_sql(query3,connect1)
print(pdf3)

#List all case numbers for crimes involving minors?(children are not considered minors for the purposes of crime analysis)

query4 = "SELECT CASE_NUMBER from CHICAGO_CRIME_DATA "
pdf4 = pd.read_sql(query4,connect1)
print(pdf4)


#List all kidnapping crimes involving a child?
query5 = "SELECT CASE_NUMBER \
FROM CHICAGO_CRIME_DATA \
WHERE PRIMARY_TYPE = 'KIDNAPPING' AND DESCRIPTION LIKE '%CHILD%' "
pdf5 = pd.read_sql(query5,connect1)
print(pdf5)

#List the kind of crimes that were recorded at schools.
query6 = "SELECT CASE_NUMBER FROM CHICAGO_CRIME_DATA WHERE LOCATION_DESCRIPTION like '%school%' "
pdf6 = pd.read_sql(query6,connect1)
print(pdf6)

#List 5 community areas with highest % of households below poverty line

query7 = "select COMMUNITY_AREA_NAME,PERCENT_HOUSEHOLDS_BELOW_POVERTY\
      from CENSUS_DATA order by PERCENT_HOUSEHOLDS_BELOW_POVERTY desc limit 5 "
pdf7 = pd.read_sql(query7,connect1)
print(pdf7)

#Which community area is most crime prone? Display the coumminty area number only.
query8 = "select COMMUNITY_AREA_Number from CHICAGO_CRIME_DATA where ward = (select max(ward) from CHICAGO_CRIME_DATA) "
pdf8 = pd.read_sql(query8,connect1)
print(pdf8)

#Use a sub-query to find the name of the community area with highest hardship index
query9 = "SELECT COMMUNITY_AREA_NAME from CENSUS_DATA where  HARDSHIP_INDEX =(select max(HARDSHIP_INDEX) from CENSUS_DATA) "
pdf9 = pd.read_sql(query9,connect1)
print(pdf9)


