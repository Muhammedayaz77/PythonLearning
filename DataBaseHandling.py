import sqlite3

#db create and table create with if exist code
try:
    # to create connection and create db
    conn = sqlite3.connect('test_DataBase.db')
    #to create table
    conn.execute('''
            Create table student (
            st_id INT AUTO_INCREMENT PRIMARY KEY,
            st_name varchar(20),
            st_class varchar(20)
            )
        ''')
    conn.close()

except:
    print("created")


