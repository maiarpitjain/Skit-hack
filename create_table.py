def create_name_in_db():
    import sqlite3
    connection=sqlite3.connect("my.db")

    crsr=connection.cursor()

    sql_command = """CREATE TABLE employee (    
    fname VARCHAR(20),
    lname VARCHAR(20),
    email nvarchar(50),
    mobno int,
    address NVARCHAR(100),
    department nvarchar(50)
    );"""

    crsr.execute(sql_command)

    connection.commit() 
    
    connection.close()

create_name_in_db()