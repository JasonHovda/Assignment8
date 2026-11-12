import random

# Pick a random number between 1 and 5
secret = random.randint(1, 5)

# Track how many guesses the player makes
attempts = 0

# Tell the player the rules
print("Guess a number from 1 to 5.")
print("You have 3 guesses!")

# Keep asking until the player runs out of guesses
while attempts < 3:
    guess = int(input("Your guess: "))
    attempts += 1

    if guess == secret:
        print("You win!")
        print("Attempts:", attempts)
        break
    elif guess < secret:
        print("Too low.")
    else:
        print("Too high.")

# Check if the player used all 3 guesses
if guess != secret:
    print("Game over! You ran out of guesses.")
    print("The correct number was:", secret)