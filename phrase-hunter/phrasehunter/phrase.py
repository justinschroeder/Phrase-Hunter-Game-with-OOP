class Phrase():
    def __init__(self, phrase):
        self.phrase = phrase

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
        if letter in self.phrase:
            return True
        else:
            return False

    def check_complete(self, guesses):
        for letter in self.phrase:
            if letter not in guesses and letter != ' ':
                return False
        return True


if __name__ == '__main__':
    phrase = Phrase('hello world')
    letter = 'o'
    print(phrase.check_letter(letter))
    guesses = ['h','e','l','o','w','r','d']
    print(phrase.check_complete(guesses))
    phrase.display(guesses)
