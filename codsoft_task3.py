import string
import random

def generate_password():
    # Getting password length
    length = int(input("Enter password length: "))

    print('''Choose character set for password from these : 
            1. Digits
            2. Letters
            3. Special characters
            4. Exit''')

    character_list = ""

    def add_characters(choice):
        nonlocal character_list
        if choice == 1:
            character_list += string.ascii_letters
        elif choice == 2:
            character_list += string.digits
        elif choice == 3:
            character_list += string.punctuation
        elif choice != 4:
            print("Please pick a valid option!")

    for _ in range(3):  # Allow up to 3 choices
        choice = int(input("Pick a number "))
        add_characters(choice)
        if choice == 4:
            break
    else:
        print("You've reached the maximum number of choices.")

    password = [random.choice(character_list) for _ in range(length)]

    print("The random password is " + "".join(password))

if __name__ == "__main__":
    generate_password()
