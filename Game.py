import random

print("--- Welcome to 'Guess the Number' ---")
# Set the number to guess
secret_number = random.randint(1, 20)
print("I'm thinking of a number between 1 and 20.")

guess = 0
# Loop until the user guesses correctly
while guess != secret_number:
    try:
        guess = int(input("Take a guess: "))
        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
    except ValueError:
        print("Please enter a valid number.")

print(f"You got it! The number was {secret_number}.")