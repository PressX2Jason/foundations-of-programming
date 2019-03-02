from hangman import Hangman


class HangmanDriver():
    def __init__(self):
        self.game = Hangman()

    def run(self):
        print('Welcome to Hangman!')

        while not self.game.game_over():
            print(
                f'The word now looks like this: {self.game.get_current_guess()}')

            if self.game.get_remaining_guesses() > 1:
                print(
                    f'You have {self.game.get_remaining_guesses()} guesses left')
            else:
                print('You only have one guess left.')

            guess = ''
            while not self.game.valid_guess(guess):
                guess = input('Your guess: ')

            if self.game.guess_letter(guess):
                print('That guess is correct.')
            else:
                print(f'There are no {guess}\'s in the word.')

        if self.game.out_of_guesses():
            print('You\'re complete hung')
            print(f'The word was: {self.game.get_secret_word()}')
            print('You lose.')

        if self.game.secret_guessed():
            print(f'You guessed the word: {self.game.get_secret_word()}')
            print('You win.')


driver = HangmanDriver()
driver.run()
