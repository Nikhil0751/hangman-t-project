import tkinter as tk
from tkinter import messagebox
import random

class HangmanGUI:
    def _init_(self, master):
        self.master = master
        self.master.title("Hangman Game")
        self.word_to_guess = random.choice(self.get_words()).lower()
        self.guesses = []
        self.MAX_TRIES = 6
        self.create_widgets()
        self.draw_board()

    def create_widgets(self):
        self.canvas = tk.Canvas(self.master, width=400, height=400)
        self.canvas.grid(row=0, column=0, columnspan=3)

        self.word_label = tk.Label(self.master, text="Word: ")
        self.word_label.grid(row=1, column=0, sticky='e')

        self.guess_entry = tk.Entry(self.master, width=5)
        self.guess_entry.grid(row=1, column=1)

        self.guess_button = tk.Button(self.master, text="Guess", command=self.make_guess)
        self.guess_button.grid(row=1, column=2)

        self.restart_button = tk.Button(self.master, text="Restart", command=self.restart_game)
        self.restart_button.grid(row=2, column=1, columnspan=2)

    def get_words(self):
        return ['hangman', 'computer', 'python', 'keyboard', 'mouse', 'apple', 'banana', 'orange']

    def draw_board(self):
        self.canvas.delete("hangman")
        if len(self.guesses) > 0:
            for idx, pic in enumerate(Hangman.HANGMAN_PICS[:len(self.guesses)]):
                self.canvas.create_text(200, 50 + 50 * idx, text=pic, font=("Courier", 24), tag="hangman")
        else:
            self.canvas.create_text(200, 200, text=Hangman.HANGMAN_PICS[0], font=("Courier", 24), tag="hangman")

    def make_guess(self):
        guess = self.guess_entry.get().lower()
        if guess not in self.guesses:
            self.guesses.append(guess)
            if guess in self.word_to_guess:
                self.update_word_label()
                if self.check_win():
                    messagebox.showinfo("Hangman", "You win!")
            else:
                self.draw_board()
                if len(self.guesses) >= self.MAX_TRIES:
                    messagebox.showinfo("Hangman", f"Game over! The word was {self.word_to_guess}.")
        self.guess_entry.delete(0, 'end')

    def update_word_label(self):
        guessed_word = ''.join([letter if letter in self.guesses else '_' for letter in self.word_to_guess])
        self.word_label.config(text="Word: " + guessed_word)

    def check_win(self):
        return all(letter in self.guesses for letter in self.word_to_guess)

    def restart_game(self):
        self.word_to_guess = random.choice(self.get_words()).lower()
        self.guesses = []
        self.draw_board()
        self.update_word_label()

class Hangman:
    HANGMAN_PICS = ['''+---+
    |
    |
    |
   ===''', '''+---+
O   |
    |
    |
   ===''', '''
+---+
O   |
|   |
    |
   ===''', '''
+---+
O   |
/|   |
    |
   ===''', '''
+---+
O   |
/|\  |
    |
   ===''', '''
+---+
O   |
/|\  |
/   |
   ===''', '''
+---+
O   |
/|\  |
/ \  |
   ===''']

def main():
    root = tk.Tk()
    hangman_game = HangmanGUI(root)
    root.mainloop()

if _name_ == "_main_":
    main()