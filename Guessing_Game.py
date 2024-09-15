import tkinter as tk
from tkinter import messagebox
import random

# Function to start a new game
def new_game():
    global random_number, guess_count
    random_number = random.randint(1, 100)
    guess_count = 0
    guess_button.config(state="normal")
    result_label.config(text="I've picked a number between 1 and 100. Can you guess it?")
    entry_box.delete(0, 'end')
    progress_bar.set(0)  # Fixed this line to use 'set()' instead of 'config()'
    hint_label.config(text="")
    score_label.config(text=f"Guesses: {guess_count}")

# Function to give hints based on the number of guesses
def provide_hint(guess):
    if guess_count == 5:
        hint_label.config(text=f"Hint: The number is {'even' if random_number % 2 == 0 else 'odd'}.")
    elif guess_count == 8:
        if random_number <= 50:
            hint_label.config(text="Hint: The number is 50 or lower.")
        else:
            hint_label.config(text="Hint: The number is greater than 50.")

# Function to handle the user's guess
def check_guess():
    global guess_count
    try:
        guess = int(entry_box.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")
        return

    if guess < 1 or guess > 100:
        result_label.config(text="Please guess a number between 1 and 100.")
    else:
        guess_count += 1
        score_label.config(text=f"Guesses: {guess_count}")
        
        # Calculate the closeness for the progress bar
        closeness = 100 - abs(random_number - guess)
        progress_bar.set(closeness)  # Fixed this line to use 'set()' instead of 'config()'

        if guess < random_number:
            result_label.config(text="Too low! Try again.")
        elif guess > random_number:
            result_label.config(text="Too high! Try again.")
        else:
            result_label.config(text=f"Congratulations! {guess} is correct.")
            guess_button.config(state="disabled")

        provide_hint(guess)

# Creating the main window
window = tk.Tk()
window.title("Unique Guessing Game")

# Set window background color
window.configure(bg='#f0f4f5')

# Styling options
label_font = ("Helvetica", 14)
button_font = ("Helvetica", 12)
bg_color = '#f0f4f5'

# Instructions
instructions_label = tk.Label(window, text="Welcome to the Unique Guessing Game!", font=("Helvetica", 16), bg=bg_color)
instructions_label.pack(pady=10)

# Entry for guess
entry_label = tk.Label(window, text="Enter your guess:", font=label_font, bg=bg_color)
entry_label.pack()

entry_box = tk.Entry(window, font=("Helvetica", 14), width=10)
entry_box.pack(pady=10)

# Guess button
guess_button = tk.Button(window, text="Guess", font=button_font, command=check_guess, bg='#00bcd4', fg='white')
guess_button.pack(pady=10)

# Result label
result_label = tk.Label(window, text="", font=label_font, bg=bg_color)
result_label.pack(pady=10)

# Progress bar to indicate closeness
progress_bar = tk.Scale(window, from_=0, to=100, orient='horizontal', length=300, bg=bg_color, fg='#00bcd4', sliderlength=20, state="normal")
progress_bar.pack(pady=10)

# Hint label
hint_label = tk.Label(window, text="", font=label_font, bg=bg_color)
hint_label.pack(pady=10)

# Score display
score_label = tk.Label(window, text="Guesses: 0", font=label_font, bg=bg_color)
score_label.pack(pady=10)

# New game button
new_game_button = tk.Button(window, text="New Game", font=button_font, command=new_game, bg='#00796b', fg='white')
new_game_button.pack(pady=20)

# Start a new game on load
new_game()

# Start the Tkinter event loop
window.mainloop()
