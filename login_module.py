import mysql.connector

def connect_db():
    
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="yeshsql",
        database="stock_db"
    )
    return conn

def login(cursor):
    print("=== Login ===")
    username = input("Username: ")
    password = input("Password: ")
    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
    if cursor.fetchone():
        print("Login successful!\n")
        return True
    else:
        print("Invalid credentials.\n")
        return False

