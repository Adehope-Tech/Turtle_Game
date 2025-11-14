import random

print("--- Welcome to 'Guess the Number' ---")
secret_number = random.randint(1, 20)
print("I'm thinking of a number between 1 and 20. You have 5 guesses.")

guess = 0
guess_count = 0
guess_limit = 5
out_of_guesses = False

while guess != secret_number and not out_of_guesses:
    if guess_count < guess_limit:
        try:
            guess = int(input("Take a guess: "))
            guess_count += 1
            if guess < secret_number:
                print("Too low!")
            elif guess > secret_number:
                print("Too high!")
        except ValueError:
            print("Please enter a valid number.")
    else:
        out_of_guesses = True

if out_of_guesses:
    print(f"You're out of guesses! The number was {secret_number}.")
else:
    print(f"You got it in {guess_count} guesses! The number was {secret_number}.")