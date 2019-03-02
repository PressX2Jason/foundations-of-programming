from hangman_lexicon import HangmanLexicon
from random import randrange


class Hangman():
    def __init__(self, lexicon=HangmanLexicon()):
        self._secret_word = lexicon.get_word(
            randrange(lexicon.get_word_count()))
        self._guessed_word = ['-' for i in range(len(self._secret_word))]
        self._guess_count = 0
        self._max_guess = 8

    def get_remaining_guesses(self):
        return self._max_guess - self._guess_count

    def get_current_guess(self):
        return ''.join(self._guessed_word)

    def get_secret_word(self):
        return self._secret_word

    def _update_guessed_word(self, letter):
        for i, c in enumerate(self._secret_word):
            if c == letter:
                self._guessed_word[i] = c

    def guess_letter(self, letter):
        letter = letter.upper()
        if letter in self._secret_word:
            self._update_guessed_word(letter)
            return True
        else:
            self._guess_count += 1
            return False

    def secret_guessed(self):
        return '-' not in self._guessed_word

    def out_of_guesses(self):
        return self.get_remaining_guesses() == 0

    def game_over(self):
        return self.out_of_guesses() or self.secret_guessed()

    def valid_guess(self, guess):
        guess = guess.strip()
        return len(guess) == 1 and guess.isalpha()
