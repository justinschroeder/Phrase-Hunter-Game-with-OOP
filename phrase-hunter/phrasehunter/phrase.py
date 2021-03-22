class Phrase():
    def __init__(self, phrase):
        self.phrase = phrase.lower()

    def display(self, guesses):
        for letter in self.phrase:
            if letter in guesses:
                print(letter, end=' ')
            elif letter == ' ':
                print(letter, end=' ')
            else:
                print('_', end=' ')
        print('\n')

    def check_letter(self, letter):
        if letter.lower() in self.phrase:
            return True
        else:
            return False

    def check_complete(self, guesses):
        for letter in self.phrase:
            if letter not in guesses and letter != ' ':
                return False
        return True
