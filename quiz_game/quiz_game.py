print("Welcome to my computer quiz")

playing = input("Do you wanna play? ")

if playing.lower != "yes":
    quit()

print("Okay! Let's play :D")

answer = input("What does CPU stand for? ")
if answer.lower == "central processing unit":
        print("Correct!")
else:
        print("Incorrect!")


answer = input("How many hands does a human have? ")
if answer.lower == "two" or answer == "2":
        print("Correct!")
else:
        print("Incorrect!")


answer = input("do you need to understand lyric to enjoy music? ")
if answer.lower == "no":
        print("Correct!")
else:
        print("Incorrect!")


answer = input("What is the name of my dog? ")
if answer.lower == "yuno":
        print("Correct!")
else:
        print("Incorrect!")

print("Hope you had fun! \n \n bye bye")