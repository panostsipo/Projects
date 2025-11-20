import sqlite3


def login():
    print('Welcome back!')
    username = input('Username: ')
    master_password = input('Password: ')

    user = get_user(username)
    if user is None:
        print("User does not exist!")
    else:
        user_id, db_username, db_password = user
        if master_password == db_password:
            print("Login successful!")
        else:
            print("Wrong password!")


def register():
    print('Welcome!')
    username = input('Username: ')
    master_password = input('Password: ')

    # Connect to database
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # Insert the new user into the users table
    cursor.execute("""
        INSERT INTO users (username, master_password)
        VALUES (?, ?)
    """, (username, master_password))

    # Save changes
    conn.commit()

    # Get the ID of the newly created user
    user_id = cursor.lastrowid

    # Close connection
    conn.close()

    return user_id


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

