import os
import sqlite3


#file_path = "C:\Users\Panos\Desktop\Password Manager\database.db"

def database_check():
    if os.path.exists("database.db"):
        print("Database exist")
    else:
        print("Initializing database...")
        database_initialization()

def database_initialization():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        master_password TEXT
    );
    """)

    # Create passwords table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users_passwords (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        item_name TEXT,
        username TEXT,
        password TEXT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(id)
    );
    """)

    conn.commit()
    conn.close()

    print("Database initialized!")

def users_table_input(username, hashed_password):
    # Connect to database
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # Insert the new user into the users table
    cursor.execute("""
        INSERT INTO users (username, master_password)
        VALUES (?, ?)
    """, (username, hashed_password))

    # Save changes
    conn.commit()

    # Get the ID of the newly created user
    user_id = cursor.lastrowid

    # Close connection
    conn.close()

    return user_id

def users_passwords_table_input(user_id, item_name, item_username, password):
    # Connect to database
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # Insert the new user into the users table
    cursor.execute("""
        INSERT INTO users_passwords (user_id, item_name, username, password)
        VALUES (?, ?, ?, ?)
    """, (user_id, item_name, item_username, password))

    # Save changes
    conn.commit()
    # Close connection
    conn.close()

#Used to check if the user exists and return the users data
def get_user(username):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, username, master_password
        FROM users
        WHERE username = ?
    """, (username,))

    user = cursor.fetchone()

    conn.close()

    return user   # returns (id, username, password) OR None

def show_user_passwords(user_id):
    # Connect to database
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # Insert the new user into the users table
    cursor.execute("""
        SELECT * 
        FROM users_passwords
        WHERE user_id = ? 
    """, (user_id,))

    rows = cursor.fetchall()

    # Close connection
    conn.close()
    print("-" * 30)  # separator line
    for row in rows:
        # unpack tuple
        id, user_id, item_name, item_username, password = row
        
        # print in readable format
        print(f"Item name: {item_name}")
        print(f"Username: {item_username}")
        print(f"Password: {password}")
        print("-" * 30)  # separator line

    return rows

    