from phrasehunter.phrase import Phrase
import random

class Game:
    def __init__(self):
        self.missed = 0
        self.phrases = [Phrase('A Dime a Dozen'), Phrase('Cut to the Chase'), Phrase('Put a Sock In It'), Phrase('Fish Out of Water'), Phrase('A Chip On Your Shoulder')]
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
        return random.choice(self.phrases)

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
            if len(guess) > 1 or guess.isalpha() is False:
                # using isalpha() here instead of a list of letters per Mel R's feedback
                print('That is not a valid guess! Please guess again.\n')
                self.missed += 1
                self.guesses.append(guess.lower())
                print(f'You have {5-self.missed} out of 5 tries remaining!\n')
                break
            elif guess in self.guesses:
                self.missed += 1
                self.guesses.append(guess.lower())
                print('Oops! You already guess that letter.\n')
                print(f'You have {5-self.missed} out of 5 tries remaining!\n')
                break
            elif self.active_phrase.check_letter(guess) is False:
                self.missed += 1
                self.guesses.append(guess.lower())
                print('Incorrect! That letter is not in the phrase.\n')
                print(f'You have {5-self.missed} out of 5 tries remaining!\n')
                break
            else:
                print('Good job!\n')
                self.guesses.append(guess.lower())
                break

    def game_over(self):
        if self.active_phrase.check_complete(self.guesses):
            print(f'Congratulations! You won the game! It only took you {len(self.guesses)} total guesses!\n')
        else:
            print('Game over - You ran out of incorrect guesses. Better luck next time!\n')
        while True:
            new_game = input('Would you like to play again? Y/N  >>> ')
            if new_game.lower() == 'y':
                print('\n\n\n')
                self.new_game()
                try:
                    self.start()
                except IndexError:
                    print('You have guesses all the available phrases! Good job!\n')
                    print('Thanks for playing! See you next time.')
                break
            elif new_game.lower() == 'n':
                print('\nThanks for playing! See you next time.')
                break
            else:
                print('Not a valid option...')
                continue

    def new_game(self):
        if self.active_phrase.check_complete(self.guesses):
            self.phrases.remove(self.active_phrase)
        self.missed = 0
        self.active_phrase = None
        self.guesses = []
