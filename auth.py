import sqlite3
import bcrypt
from passwordgen import password_generator_initialization
from db import users_table_input, get_user
#from menus import secondary_menu


def login():
    while True:

        succesful_login = 0
        print('Welcome back!')
        username = input('Username: ')
        master_password = input('Password: ')

        user = get_user(username)
        if user is None:
            print("User does not exist!")
            return None, None
        else:
            user_id, db_username, db_password = user
            if bcrypt.checkpw(master_password.encode(), db_password.encode()):
                print("Login successful!")
                return user[0], master_password
            else:
                print("Wrong password!")
                return None, None

def register():
    print('Welcome!')
    username = input('Username: ')
    master_password = input('Password: ')

    hashed_password = hashing(master_password)

    users_table_input(username, hashed_password)

def hashing(value):
    value = value.encode()
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(value, salt)

    return hashed.decode()



            
            
