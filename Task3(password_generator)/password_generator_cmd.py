import string
import random

def generate_password(length):
    characters = str(string.ascii_letters+string.digits+string.punctuation)
    char_lst = []
    for char in characters:
        char_lst.append(char)
    random.shuffle(char_lst)
    password = ""
    for password_character in range(length):
        password += random.choice(char_lst)
    print(password)

def get_length_of_pswd():
    global length
    while True:
        try:
            length = int(input("Enter the length of Password: "))
            if length > 0:
                return length
            else:
                print("Length must be greater than 0.")
            break
        except ValueError:
            print("Enter Valid Input!")

def main():
    length = get_length_of_pswd()
    print()
    print("",end="\t\t")
    generate_password(length)
    print()
    print("",end="\t\t")

    while True:
        prompt = input("""Options:
        1. Generate another password
        2. Change the length of the password
        0. Exit
        Choose an option (0, 1, 2): """)
        if prompt == "1":
            print()
            print("",end="\t\t")
            generate_password(length)
            print()
            print("",end="\t\t")
        elif prompt == "2":
            length = get_length_of_pswd()
            print()
            print("",end="\t\t")
            generate_password(length)
            print()
            print("",end="\t\t")
        elif prompt == "0":
            break
        else:
            print()
            print("",end="\t\t")
            print("Invalid Input!")
            print()
            print("",end="\t\t")

    print("\nThank you!")

if __name__ == "__main__":
    main()