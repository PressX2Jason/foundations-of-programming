import pytest
from hangman import Hangman


class MockLexicon():
    def __init__(self):
        self.words = {
            0: 'TESTING',
        }
        self.wordCount = len(self.words)

    def get_word_count(self):
        return self.wordCount

    def get_random_word(self):
        return self.get_word(0)

    def get_word(self, index):
        if index not in self.words:
            raise IndexError('getWord: Illegal index')
        return self.words[index]


def test_get_secret_word():
    game = Hangman(MockLexicon())
    assert game.get_secret_word() == 'TESTING'

def test_game_over_by_out_of_guesses():
    game = Hangman(MockLexicon())
    for _ in range(8):
        game.guess_letter('X')
    assert game.game_over() == True

def test_game_over_by_correctly_guessed():
    game = Hangman(MockLexicon())
    game.guess_letter('T')
    game.guess_letter('E')
    game.guess_letter('S')
    game.guess_letter('I')
    game.guess_letter('N')
    game.guess_letter('G')
    assert game.game_over() == True


def test_secret_guessed():
    game = Hangman(MockLexicon())
    game.guess_letter('T')
    assert game.secret_guessed() == False
    game.guess_letter('E')
    assert game.secret_guessed() == False
    game.guess_letter('S')
    assert game.secret_guessed() == False
    game.guess_letter('I')
    assert game.secret_guessed() == False
    game.guess_letter('N')
    assert game.secret_guessed() == False
    game.guess_letter('G')
    assert game.secret_guessed() == True


def test_out_of_guesses():
    game = Hangman(MockLexicon())
    for i in range(8):
        game.guess_letter('X')
        if i == 7:
            assert game.out_of_guesses() == True
        else:
            assert game.out_of_guesses() == False


@pytest.mark.parametrize('guess, current_guess', [
    ('', '-------'),
    ('T', 'T--T---'),
    ('E', '-E-----'),
    ('S', '--S----'),
    ('I', '----I--'),
    ('N', '-----N-'),
    ('G', '------G'),
    ('X', '-------')
])
def test_get_current_guess(guess, current_guess):
    game = Hangman(MockLexicon())
    game.guess_letter(guess)
    assert game.get_current_guess() == current_guess


@pytest.mark.parametrize('guess, result', [
    ('', False),
    ('tt', False),
    (' ', False),
    ('t', True),
    ('T', True),
    (' t', True),
    ('t ', True),
    (' t ', True)
])
def test_valid_guess(guess, result):
    game = Hangman(MockLexicon())
    assert game.valid_guess(guess) == result
