# Define some placeholder values
age = 19
driver_license = True


# Gets the age of the user
def get_age():
    age_input = input("What is your age?: ")
    while not age_input.isdigit():
        age_input = input("Please enter you age using digits: ")
    return int(age_input)


# Gets the license status of the user
def get_license():
    license_input = input("Do you have a driving license?: ")
    while not license_input.lower() in ("y", "n"):
        license_input = input("Please enter you answer using y or n: ")
    return license_input == "y"


# Makes the program continuous
while True:
    # Give the user an opportunity to exit the program
    user_input = input("\nLets see if you can vote! (continue or exit): ")
    if user_input.lower().count("exit") > 0:
        break

    # Get the users age and license status
    age = get_age()
    driver_license = get_license()

    if age < 16:  # If the user is too young to do anything
        print("You're too young, go back to school!")
        continue
    elif age < 18:  # If the user is just old enough to potentially drive but not drink
        print("You can't legally drink, but your mates/uncles might have your back (bigger 16)")
        if driver_license:
            print("You can legally drive")
    elif age > 17:  # If the user is old enough to drink and vote and potentially drive
        print("You can legally drink")
        print("You can legally vote", end=" ")
        if driver_license:
            print("and you can legally drive")
        else:
            print("but you cant legally drive")
