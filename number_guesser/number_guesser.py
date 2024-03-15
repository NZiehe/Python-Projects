import random

top_range = input("Type a number: ")

if top_range.isdigit():
        top_range = int(top_range)

        if top_range <= 0:
                print("Please type a number larger than 0 next time!")
                quit()

else:
        print("Please type a number next time!")

random_number = random.randint(0, top_range)
counter = 1;

while True:
        guess = input("Guess the number: ")

        if guess.isdigit():
            guess = int(guess)
        else:
               print("Please Type a number between 0 and " + str(top_range))
               continue
        
        if guess == random_number:
                   print("Hoooray you guessed the number in " + str(counter) + " trys")
                   break
        else:
                    counter += 1