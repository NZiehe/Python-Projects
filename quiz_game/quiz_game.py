print("Welcome to my computer quiz")

playing = input("Do you wanna play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :D")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
        print("Correct!")
        score +=1
else:
        print("Incorrect!")


answer = input("How many hands does a human have? ")
if answer.lower() == "two" or answer == "2":
        print("Correct!")
        score +=1
else:
        print("Incorrect!")


answer = input("do you need to understand lyric to enjoy music? ")
if answer.lower() == "no":
        print("Correct!")
        score +=1
else:
        print("Incorrect!")


answer = input("What is the name of my dog? ")
if answer.lower() == "yuno":
        print("Correct!")
        score +=1
else:
        print("Incorrect!")

print("You did score = " + str(score) + "/4\n Hope you had fun! \n \n bye bye")