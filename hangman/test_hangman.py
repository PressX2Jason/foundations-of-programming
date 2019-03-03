import pytest
from hangman import Hangman


class MockLexicon():
    def get_random_word(self):
        return 'TESTING'

def _get_game():
    return Hangman(MockLexicon())

def test_get_secret_word():
    game = _get_game()
    assert game.get_secret_word() == 'TESTING'


def test_game_over_by_out_of_guesses():
    game = _get_game()
    for _ in range(8):
        game.guess_letter('X')
    assert game.game_over() == True


def test_game_over_by_correctly_guessed():
    game = _get_game()
    game.guess_letter('T')
    game.guess_letter('E')
    game.guess_letter('S')
    game.guess_letter('I')
    game.guess_letter('N')
    game.guess_letter('G')
    assert game.game_over() == True


def test_secret_guessed():
    game = _get_game()
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
    game = _get_game()
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
    game = _get_game()
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
    game = _get_game()
    assert game.valid_guess(guess) == result
