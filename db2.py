def create_name_in_db():
    import sqlite3
    connection=sqlite3.connect("my23.db")

    crsr=connection.cursor()

    sql_command = """CREATE TABLE emp (    
    name VARCHAR(20));"""

    crsr.execute(sql_command)

    connection.commit() 
    
    connection.close()

def send_name_in_db(name):
    import sqlite3
    connection=sqlite3.connect("my23.db")
    crsr=connection.cursor()
    
    crsr.execute("INSERT INTO emp VALUES (?)",(name,))

    connection.commit() 
    
    connection.close()
#create_name_in_db()
send_name_in_db('arpit')
