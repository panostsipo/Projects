import sqlite3
import bcrypt


def login():
    while True:
        print('Welcome back!')
        username = input('Username: ')
        master_password = input('Password: ')

        user = get_user(username)
        if user is None:
            print("User does not exist!")
        else:
            user_id, db_username, db_password = user
            if bcrypt.checkpw(master_password.encode(), db_password.encode()):
                print("Login successful!")
                break
            else:
                print("Wrong password!")


def register():
    print('Welcome!')
    username = input('Username: ')
    master_password = input('Password: ')

    hashed_password = hashing(master_password)

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

def hashing(value):
    value = value.encode()
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(value, salt)
    return hashed.decode()
