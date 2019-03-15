def data():
    import csv
    l=[]
    with open('book1.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            l.append([row['id'],row['name'],row['address'],row['email'],row['mnumber'],row['p_type'],row['d_name'],row['p_description'],row['c_name']])

    return l
    
def create_database():
    
    import sqlite3
    connection=sqlite3.connect("customer.db")

    crsr=connection.cursor()

    sql_command = """CREATE TABLE customer (    
    id int,
    name VARCHAR(20),
    address NVARCHAR(60),
    email nvarchar(50),
    mobno int,
    p_type NVARCHAR(100),
    d_type nvarchar(50),
    p_description nvarchar(200),
    c_name nvarchar(50),
    arrival_time int
    );"""

    crsr.execute(sql_command)

    connection.commit() 
    
    connection.close()

def fill_data_in_database():
    l=data()

    import sqlite3
    connection=sqlite3.connect("customer.db")

    crsr=connection.cursor()

    for i in range(len(l)):
        import maps
        hours,mins=maps.get_distance(l[i][2])
        if hours:
            t_time=int(hours)*60+int(mins)
            print(t_time)
        else:
            t_time=int(mins)    
            print(t_time)

        l[i][0]=int(l[i][0])
        l[i][4]=int(l[i][4])

        sql_command = """INSERT INTO customer VALUES (?,?,?,?,?,?,?,?,?,?);"""
        crsr.execute(sql_command,(l[i][0],l[i][1] , l[i][2],l[i][3], l[i][4],l[i][5],l[i][6],l[i][7],l[i][8],t_time))

    connection.commit() 
        
    connection.close()

create_database()
fill_data_in_database()