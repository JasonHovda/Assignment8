
import random

def playGame():
    numbers = [1, 2, 3, 4, 5]
    secretNumber = random.choice(numbers)
    attempts = 0

    print("Welcome to the Number Guessing Game!")

    while True:
        guess = int(input("Guess a number between 1 and 5: "))
        attempts += 1

        if guess == secretNumber:
            print("Correct, You guessed the number!")
            print("Total attempts:", attempts)
            break
        elif guess < secretNumber:
            print("Too low, Try again.")
        else:
            print("Too high!,Try again.")

playGame()
