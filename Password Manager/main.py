from auth import login, register

def main_menu():
    while True:
        print('1. Login')
        print('2. Register')
        print('3. Quit')

        choice = input('Choose:')

        if choice == '1':
            login()
            print("test=================================================")

        elif choice == '2':
            register()

        elif choice == '3':
            print('Quitting...')
            break

        else:
            print('Please choose one of the option below')



main_menu()