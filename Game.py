import tkinter as tk
import random

class GuessingGame:
    def __init__(self, master):
        self.master = master
        master.title("Guess the Number")
        master.geometry("300x150")

        self.secret_number = random.randint(1, 100)
        self.guess_count = 0
        self.guess_limit = 7

        self.label = tk.Label(master, text="Guess a number between 1 and 100:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.guess_button = tk.Button(master, text="Guess", command=self.check_guess)
        self.guess_button.pack()

        self.feedback = tk.Label(master, text="")
        self.feedback.pack()

        self.reset_button = tk.Button(master, text="Reset", command=self.reset_game, state=tk.DISABLED)
        self.reset_button.pack()

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.guess_count += 1

            if guess < self.secret_number:
                self.feedback.config(text=f"Too low! Guesses left: {self.guess_limit - self.guess_count}")
            elif guess > self.secret_number:
                self.feedback.config(text=f"Too high! Guesses left: {self.guess_limit - self.guess_count}")
            else:
                self.feedback.config(text=f"You got it in {self.guess_count} guesses!")
                self.end_game()
                return

            if self.guess_count >= self.guess_limit:
                self.feedback.config(text=f"Out of guesses! Number was {self.secret_number}")
                self.end_game()

        except ValueError:
            self.feedback.config(text="Please enter a valid number.")

        self.entry.delete(0, tk.END) # Clear the entry box

    def end_game(self):
        self.guess_button.config(state=tk.DISABLED)
        self.entry.config(state=tk.DISABLED)
        self.reset_button.config(state=tk.NORMAL)

    def reset_game(self):
        self.secret_number = random.randint(1, 100)
        self.guess_count = 0
        self.feedback.config(text="")
        self.guess_button.config(state=tk.NORMAL)
        self.entry.config(state=tk.NORMAL)
        self.entry.delete(0, tk.END)
        self.reset_button.config(state=tk.DISABLED)


if __name__ == "__main__":
    root = tk.Tk()
    game = GuessingGame(root)
    root.mainloop()
