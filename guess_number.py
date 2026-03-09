import random

secret_number = random.randint(1, 10)
guess_number = 1

while guess_number <=  3:
    guess = int(input("Guess: "))

    if guess > secret_number:
        print("High!")
    elif guess < secret_number:
        print("Low!")
    else:
        print("You won!!!")
        break

    guess_number += 1
else:
    print("sorry you failed!")
