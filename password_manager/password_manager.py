# !! not a secure way to store passwords!!

pwd = input("What is the master password?: ")

while True:
    mode = input("Would you like to add a new password or view existing ones (add/view)?:  ").lower()
    
if mode == "view":
    pass
elif mode == "add":
    pass
else: