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


@pytest.mark.parametrize('guess, current_guess', [
    ('', '-------'),
    ('T', 'T--T---'),
    ('E', '-E-----'),
    ('S', '--S----'),
    ('I', '----I--'),
    ('N', '-----N-'),
    ('G', '------G'),    
])
def test_get_current_guess(guess, current_guess):
    game = Hangman(MockLexicon())
    game.guess_letter(guess)
    assert game.get_current_guess() == current_guess

def test_get_secret_word():
    game = Hangman(MockLexicon())
    assert game.get_secret_word() == 'TESTING'