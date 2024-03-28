import tkinter as tk
from tkinter import messagebox
import random

class HangmanMultiplayerGUI:
    def _init_(self, master):
        self.master = master
        self.master.title("Hangman Multiplayer Game")
        self.player1_word = ""
        self.player2_word = ""
        self.guesses = []
        self.MAX_TRIES = 6
        self.create_widgets()
        self.start_game()

    def create_widgets(self):
        self.canvas = tk.Canvas(self.master, width=400, height=400)
        self.canvas.grid(row=0, column=0, columnspan=3)

        self.player1_label = tk.Label(self.master, text="Player 1 Word: ")
        self.player1_label.grid(row=1, column=0, sticky='e')

        self.player1_entry = tk.Entry(self.master, width=20)
        self.player1_entry.grid(row=1, column=1)

        self.player2_label = tk.Label(self.master, text="Player 2 Word: ")
        self.player2_label.grid(row=2, column=0, sticky='e')

        self.player2_entry = tk.Entry(self.master, width=20)
        self.player2_entry.grid(row=2, column=1)

        self.start_button = tk.Button(self.master, text="Start Game", command=self.start_game)
        self.start_button.grid(row=3, column=0, columnspan=2)

        self.guess_label = tk.Label(self.master, text="Guess a letter: ")
        self.guess_label.grid(row=4, column=0, sticky='e')

        self.guess_entry = tk.Entry(self.master, width=5)
        self.guess_entry.grid(row=4, column=1)

        self.guess_button = tk.Button(self.master, text="Guess", command=self.make_guess)
        self.guess_button.grid(row=5, column=0, columnspan=2)

        self.restart_button = tk.Button(self.master, text="Restart", command=self.restart_game)
        self.restart_button.grid(row=6, column=0, columnspan=2)

    def start_game(self):
        self.player1_word = self.player1_entry.get().lower()
        self.player2_word = self.player2_entry.get().lower()
        self.guesses = []
        self.draw_board()

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
            if guess in self.player1_word:
                self.update_word_label(self.player1_word)
                if self.check_win(self.player1_word):
                    messagebox.showinfo("Hangman", "Player 1 wins! The word was '{}'.".format(self.player1_word))
            elif guess in self.player2_word:
                self.update_word_label(self.player2_word)
                if self.check_win(self.player2_word):
                    messagebox.showinfo("Hangman", "Player 2 wins! The word was '{}'.".format(self.player2_word))
            else:
                self.draw_board()
                if len(self.guesses) >= self.MAX_TRIES:
                    messagebox.showinfo("Hangman", "Game over! No one guessed the word.")
        self.guess_entry.delete(0, 'end')

    def update_word_label(self, word):
        guessed_word = ''.join([letter if letter in self.guesses else '_' for letter in word])
        self.guess_label.config(text="Word: " + guessed_word)

    def check_win(self, word):
        return all(letter in self.guesses for letter in word)

    def restart_game(self):
        self.player1_entry.delete(0, 'end')
        self.player2_entry.delete(0, 'end')
        self.start_game()

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
    hangman_game = HangmanMultiplayerGUI(root)
    root.mainloop()

if _name_ == "_main_":
    main()