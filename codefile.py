
import random 
"""The Python random module: Your ticket to unpredictability, randomness, and delightful surprises in programming."""

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
       /    |
           ===''', '''
        +---+
        O   |
       /|\  |
       / \  |
           ===''']
    
    WORDS = 'As dusk settled over the bustling city, the neon lights flickered to life, painting the streets in a kaleidoscope of colors. Honking cars and chatter of pedestrians filled the air, creating a symphony of urban chaos. Amidst the hustle and bustle, a lone figure sat on a bench, lost in thought. The aroma of street food wafted through the air, tempting passersby with its tantalizing scent.'.split()

    def __init__(self):
        self.missed_letters = ''
        self.correct_letters = ''
        self.secret_word = self.get_random_word()
        self.game_is_done = False

    def get_random_word(self):
        return random.choice(self.WORDS)

    def display_board(self):
        print()
        print(self.HANGMAN_PICS[len(self.missed_letters)])
        print()
        print('Missed letters:', self.missed_letters)
        
        blanks = ''
        for letter in self.secret_word:
            if letter in self.correct_letters:
                blanks += letter
            else:
                blanks += '_'
        print('Word:', ' '.join(blanks))

    def get_guess(self):
        while True:
            guess = input('Please guess a letter: ').lower()
            if len(guess) != 1:
                print('Only a single letter is allowed.')
            elif guess in self.missed_letters or guess in self.correct_letters:
                print('You have already guessed that letter. Choose again.')
            elif guess not in 'abcdefghijklmnopqrstuvwxyz':
                print('Please enter a letter from the alphabet.')
            else:
                return guess

    def play_again(self):
        return input('Would you like to play again? (y)es or (n)o: ').lower().startswith('y')

    def play(self):
        print('|_H_A_N_G_M_A_N_|')

        while True:
            self.display_board()
            guess = self.get_guess()

            if guess in self.secret_word:
                self.correct_letters += guess
                if all(letter in self.correct_letters for letter in self.secret_word):
                    print('You guessed it!')
                    print('The secret word is "{}". You win!'.format(self.secret_word))
                    break
            else:
                self.missed_letters += guess
                if len(self.missed_letters) == len(self.HANGMAN_PICS) - 1:
                    self.display_board()
                    print('You have run out of guesses!')
                    print('The word was "{}".'.format(self.secret_word))
                    break

        if self.play_again():
            self.__init__()
            self.play()

if __name__ == "__main__":
    game = Hangman()
    game.play()