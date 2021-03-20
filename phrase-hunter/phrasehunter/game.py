from phrasehunter.phrase import Phrase
import random

class Game:
    def __init__(self):
        self.missed = 0
        self.phrases = ['a dime a dozen', 'cut to the chase', 'put a sock in it', 'fish out of water', 'a chip on your shoulder']
        self.active_phrase = None
        self.guesses = []

    def start(self):
        self.welcome()
        self.active_phrase = self.get_random_phrase()
        while self.active_phrase.check_complete(self.guesses) is False and self.missed < 5:
            self.active_phrase.display(self.guesses)
            print('\n')
            self.get_guess()
        self.active_phrase.display(self.guesses)
        self.game_over()

    def get_random_phrase(self):
        return Phrase(random.choice(self.phrases).lower())

    def welcome(self):
        welcome = 'WELCOME TO THE PHRASE GUESSING GAME'
        print('-'*len(welcome))
        print(welcome)
        print('-'*len(welcome))
        instructions = """Instructions:
- A secret phrase will be selected at random.
- You will guess one letter at a time to reveal parts of the phrase.
- If your guess is correct, that letter in the phrase will be revealed.
- You have won the game once all the letters in the phrase are revealed.
- But be careful! You can only guess incorrectly 5 times before you lose the game.
- Good luck!!"""
        print('\n'+instructions+'\n')

    def get_guess(self):
        while True:
            guess = input('Guess a Letter:    ')
            print('\n')
            valid_guesses = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
            if len(guess) > 1 or guess not in valid_guesses:
                print('That is not a valid guess! Please guess again.\n')
                self.missed += 1
                print(f'You have {5-self.missed} out of 5 tries remaining!\n')
                continue
            elif guess in self.guesses:
                self.missed += 1
                self.guesses.append(guess)
                print('Oops! You already guess that letter.\n')
                print(f'You have {5-self.missed} out of 5 tries remaining!\n')
                break
            elif guess not in self.active_phrase.phrase:
                self.missed += 1
                self.guesses.append(guess)
                print('Incorrect! That letter is not in the phrase.\n')
                print(f'You have {5-self.missed} out of 5 tries remaining!\n')
                break
            else:
                print('Good job!\n')
                self.guesses.append(guess)
                break

    def game_over(self):
        if self.active_phrase.check_complete(self.guesses):
            print(f'Congratulations! You won the game! It only took you {len(self.guesses)} total guesses!\n')
        else:
            print('Game over - You ran out of incorrect guesses. Better luck next time!\n')
        new_game = input('Would you like to play again? Y/N  >>> ')
        if new_game.lower() == 'y':
            print('\n\n\n')
            self.new_game()
            try:
                self.start()
            except IndexError:
                print('You have guesses all the available phrases! Good job!\n')
                print('Thanks for playing! See you next time.')
        else:
            print('\nThanks for playing! See you next time.')

    def new_game(self):
        if self.active_phrase.check_complete(self.guesses):
            self.phrases.remove(self.active_phrase.phrase)
        self.missed = 0
        self.active_phrase = None
        self.guesses = []
