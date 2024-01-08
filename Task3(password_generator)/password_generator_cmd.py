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