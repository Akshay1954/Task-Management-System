import mysql.connector
from db.db import create_connection

def sign_up(username, password):
    conn, cursor = create_connection()
    
    with conn:
        try:
            cursor.execute("INSERT INTO users(username, password) VALUES(%s,%s)", (username, password))
            conn.commit()
            return True
        except mysql.connector.IntegrityError as e:
            return False

def login_user(username, password):
    conn, cursor = create_connection()
    
    cursor.execute("SELECT id FROM users WHERE username = %s AND password = %s",(username,password))
    user = cursor.fetchone()
    if user:
        return user[0]
    else:
        return None

    