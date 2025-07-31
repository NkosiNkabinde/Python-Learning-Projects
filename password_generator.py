import random
import string

def generate_password(min_length, number = True, special_characters = True):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    characters = letters
    if number:
        characters += digits
    if special_characters:
        characters += special_chars
    
    pwd= ""
    meets_criteria = False
    has_number = False
    has_special_char = False

    while not meets_criteria or len(pwd) < min_length:
        new_char= random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special_chars:
            has_special_char = True

        meets_criteria = True
        if number:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = has_number and has_special_char
    return pwd

        

min_length = int(input("Enter the minimum length: "))
has_number = input("Do you want numbers? (yes/no): ").lower() == "yes"
has_special_char = input("Do you want special characters? (yes/no): ").lower() == "yes"
pwd = generate_password(min_length, has_number, has_special_char)

print("The generated password is",   pwd)

