# Python code to demonstrate SQL to fetch data. 

# importing the module 
import sqlite3 

# connect withe the myTable database 
connection = sqlite3.connect("customer.db") 

# cursor object 
crsr = connection.cursor() 

# execute the command to fetch all the data from the table emp 
crsr.execute("SELECT * FROM customer") 

# store all the fetched data in the ans variable 
ans= crsr.fetchall() 

# loop to print all the data 
for i in ans: 
	print(i) 
