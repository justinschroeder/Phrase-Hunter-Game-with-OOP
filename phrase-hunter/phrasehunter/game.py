from phrase import Phrase
import random

class Game:
    def __init__(self):
        self.missed = 0
        self.phrases = ['A Dime a Dozen', 'Cut to the Chase', 'Put a Sock In It', 'Fish Out of Water', 'A Chip on Your Shoulder']
        self.active_phrase = None
        self.guesses = []

    def start(self):
        pass

    def get_random_phrase(self):
        self.active_phrase = random.choice(self.phrases)
        return

    def welcome(self):
        pass

    def get_guess(self):
        pass

    def game_over(self):
        pass


if __name__ == '__main__':
    game = Game()
    game.get_random_phrase()
    print(game.active_phrase)
