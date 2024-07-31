import tkinter as tk
from tkinter import messagebox
import random

class GuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Guessing Game")
        self.master.geometry("300x150")
        
        self.random_number = random.randint(1, 100)
        self.attempts = 0
        
        self.label = tk.Label(master, text="Guess a number between 1 and 100:")
        self.label.pack(pady=10)
        
        self.entry = tk.Entry(master)
        self.entry.pack(pady=5)
        
        self.guess_button = tk.Button(master, text="Guess", command=self.check_guess)
        self.guess_button.pack(pady=5)
        
        self.reset_button = tk.Button(master, text="Reset", command=self.reset_game)
        self.reset_button.pack(pady=5)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1

            if guess < self.random_number:
                messagebox.showinfo("Result", "Too low! Try again.")
            elif guess > self.random_number:
                messagebox.showinfo("Result", "Too high! Try again.")
            else:
                messagebox.showinfo("Result", f"Congratulations! You've guessed it in {self.attempts} attempts.")
                self.reset_game()

        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid number.")

    def reset_game(self):
        self.random_number = random.randint(1, 100)
        self.attempts = 0
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    game = GuessingGame(root)
    root.mainloop()
