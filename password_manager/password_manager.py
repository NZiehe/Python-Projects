# !! not a secure way to store passwords!!
from cryptography.fernet import Fernet

#loads encrypted key
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key) # initializing encryption module


#creates key file
'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
'''

#Function prints all Usernames and Passwords
def view():
   with open("passwords.txt", "r") as f:
       for line in f.readlines():
           data = line.rstrip()
           user, passw = data.split("|")
           print("User:", user, ", Password:", fer.decrypt(passw.encode()).decode())

#Function adds a new Username|Passwords pair
def add():
   name = input("Account Name: ")
   pwd = input("Password: ")

   with open("passwords.txt", "a") as f:
       f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

#Encrypt Password


#Input
while True:
    mode = input("Would you like to add a new password or view existing ones (add/view)?, press q to quit!:  ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode")
        continue