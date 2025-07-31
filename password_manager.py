from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open ("key.key", "wb") as key_file:
        key_file.write(key)'''


def load_key():
    file= open ("key.key", "rb")
    key = file.read()
    file.close
    return key


master_pwd = input("What is the master password? ")
key = load_key()
fer  = Fernet(key)

def view():
    with open("password.txt", "at") as f:
        for line in f.readlines():
            data = (line.rstrip())
            user , passw = data.split("|")
            print("User:", user, "| Passoword:" ,fer.decrypt(passw.encode()).decode())


def add():
    name = input("Account Name:  ")
    pwd = input("Password: ")

    with open("passwords.txt", "a") as f:
        f.write(name + ":" + fer.encrypt(pwd.encode()).decode()+ "\n")




while True:
    mode = input("Would you like to add a new password or view existing ones? (add/view) or q to quit: ").lower()
    if mode == "q":
        break

    if mode == "add":
        name = input("What is the name of the password? ")
        add()
    elif mode == "view":
        print("You have chosen to view existing passwords.")
        view()
    else:
        print("Invalid choice. Please choose 'add' or 'view'.")




    

