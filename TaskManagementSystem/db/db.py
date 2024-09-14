import mysql.connector
from mysql.connector import errorcode

def create_connection():
    db_connection = mysql.connector.connect(
        user="YOUR MYSQL DB USERNAME",
        password="<YOUR MYSQL DB PASSWORD>",
        host="127.0.0.1",
        database="task"
    )
    return db_connection, db_connection.cursor()



def initialize_db():
    conn, cursor = create_connection()
    print(conn.is_connected())
    with conn:
        cursor.execute("CREATE TABLE IF NOT EXISTS users(id INT primary key auto_increment, username VARCHAR(255) unique not null, password text)")
        conn.commit()
        cursor.execute("CREATE TABLE IF NOT EXISTS tasks(id INT primary key auto_increment, user_id INT, task_title TEXT, task_description TEXT,status varchar(30) default 'pending', FOREIGN KEY (user_id) REFERENCES users(id))")
        conn.commit()
    
initialize_db()


