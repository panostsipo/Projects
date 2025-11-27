from auth import login, register
from db import database_check, users_passwords_table_input, show_user_passwords
from passwordgen import password_generator_initialization
from crypto_engine import encrypt_password

def main_menu():

    database_check()

    while True:
        print('1. Login')
        print('2. Register')
        print('3. Quit')

        choice = input('Choose:')

        if choice == '1':
            user_id, master_password = login()
            if user_id:
                secondary_menu(user_id, master_password)
        elif choice == '2':
            register()
        elif choice == '3':
            print('Quitting...')
            break
        else:
            print('Please choose one of the option below')

def secondary_menu(user_id, master_password):
    while True:
        print("1. Save password")
        print("2. View saved passwords")
        print("3. Delete password")
        print("4. Logout")

        choice = input("Choose: ")
        if choice == '1':
            item_info(user_id, master_password)
        elif choice == '2':
            show_user_passwords(user_id)
        elif choice == '4':
            break

def item_info(user_id, master_password):
    item_name = input("Item's name: ")
    item_username = input("Item's username: ")
    user_choice = input("Would you like to generate a password? [Y/N] ").strip().upper()
    if user_choice == "Y":
        password = password_generator_initialization()
    else:
        password = input("Type in your password: ")
    
    encrypted_password = encrypt_password(master_password, password)

    users_passwords_table_input(user_id, item_name, item_username, encrypted_password)
