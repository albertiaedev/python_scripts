import sqlite3 #sqlite3 is the default database that's built-in Python

#Useful SQL commands#
 ###
#Create a client server
client = bigquery.Client() #When we're working with BigQuery

#Select specific entries
query = SELECT col FROM `folder.db.table`
        WHERE col='row'
        #if you want to select multiple columns, you can separate them with a comma ',' between the names
        #if you want to select all columns, you can use a '*' instead of a column name
        
#Count the entries in a column
COUNT()
#Put together all columns with the same value
GROUP BY
#Exclude entries with a certain criteria
HAVING
#Example:
SELECT col, COUNT(ID)
FROM `folder.db.table`
GROUP BY col
HAVING COUNT(ID)=n

