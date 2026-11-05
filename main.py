
import random

# Pick a random number between 1 and 5
secret = random.randint(1, 5)

# Track how many guesses the player makes
attempts = 0

# Tell the player the rules
print("Guess a number from 1 to 5.")

# Keep asking until the user guesses correctly
while True:
    guess = int(input("Your guess: "))
    attempts += 1

    # Check if the guess is correct
    if guess == secret:
        print("You win!")
        print("Attempts:", attempts)
        break
    elif guess < secret:
        print("Too low.")
    else:
        print("Too high.")
