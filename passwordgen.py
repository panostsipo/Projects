import random

def password_generator(settings):

    # Character groups
    groups = {
        "lower": list("abcdefghijklmnopqrstuvwxyz"),
        "upper": list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
        "num":   list("0123456789"),
        "sym":   list("!@#$%^&*-_=+?")
    }

    pool = []            # all allowed characters
    password_list = []   # final password characters

    # Add selected groups to pool + guarantee one from each
    for key, group in groups.items():
        if settings[key] == "Y":
            pool.extend(group)                     # add entire group to pool
            password_list.append(random.choice(group))  # guarantee one from each

    # Fill the rest of the password with random pool choices
    while len(password_list) < settings["length"]:
        password_list.append(random.choice(pool))

    # Shuffle so fixed characters are not in order
    random.shuffle(password_list)

    # Convert to string
    password = "".join(password_list)

    print("Generated password:", password)

def user():
    #Asks user for password length and checks if its 8 or more caracters
    while True:
        length = input("Minimum password length is 8: ")
        if length.isdigit() and int(length) >= 8:
            length = int(length)
            break

    #Asks the user if he wants numbers, symbols, lowercase and uppercase caracters, checks if he chose atleast 1 and if he his input is valid
    print("You have to choose at least 1")
    while True:

        lower = input("Do you want lowercase? [Y/N] ").strip().upper()
        upper = input("Do you want uppercase? [Y/N] ").strip().upper()
        num = input("Do you want numbers? [Y/N] ").strip().upper()
        sym = input("Do you want symbols? [Y/N] ").strip().upper()

        #valid input is only Y or N
        valid_inputs = {lower, upper, num, sym}
        if all(x in ("Y", "N") for x in valid_inputs):
            #check that at least one is Y
            if lower == "Y" or upper == "Y" or num == "Y" or sym == "Y":
                break
            else:
                print("You must choose at least one category!") 
        else:
            print("Error: Please enter only Y or N.")

    #Creating a dictionary to pass the variables
    return {'length': length, 'lower': lower, 'upper': upper, 'num': num, 'sym': sym}

def main():
    #Settings = the return of the user function (the dictionary)
    settings = user()
    password_generator(settings)


main()