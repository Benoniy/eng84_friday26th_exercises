age = 19
driver_license = True


def get_age():
    age_input = input("What is your age?: ")
    while not age_input.isdigit():
        age_input = input("Please enter you age using digits: ")
    return int(age_input)


def get_license():
    license_input = input("Do you have a driving license?: ")
    while not license_input.lower() in ("y", "n"):
        license_input = input("Please enter you answer using y or n: ")
    return license_input == "y"


while True:
    user_input = input("\nLets see if you can vote! (continue or exit): ")
    if user_input.lower().count("exit") > 0:
        break

    age = get_age()
    driver_license = get_license()

    if age < 16:
        print("You're too young, go back to school!")
        continue
    elif age < 18:
        print("You can't legally drink, but your mates/uncles might have your back (bigger 16)")
        if driver_license:
            print("You can legally drive")
    elif age > 17:
        print("You can legally drink")
        print("you can legally vote", end=" ")
        if driver_license:
            print("and you can legally drive")
        else:
            print("but you cant legally drive")
