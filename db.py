import sqlite3
connection=sqlite3.connect("my.db")

crsr=connection.cursor()


sql_command = """INSERT INTO emp VALUES (23, "Rishabh", "Bansal", "M", "2014-03-28");"""
crsr.execute(sql_command)

sql_command = """INSERT INTO emp VALUES (1, "Bill", "Gates", "M", "1980-10-28");"""
crsr.execute(sql_command)

connection.commit() 
  
connection.close()


