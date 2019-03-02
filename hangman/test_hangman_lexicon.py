import pytest
from hangman_lexicon import HangmanLexicon

lexicon = HangmanLexicon()

@pytest.mark.parametrize('index, word', [
    (0 , 'BUOY'),
    (1 , 'COMPUTER'),
    (2 , 'CONNOISSEUR'),
    (3 , 'DEHYDRATE'),
    (4 , 'FUZZY'),
    (5 , 'HUBBUB'),
    (6 , 'KEYHOLE'),
    (7 , 'QUAGMIRE'),
    (8 , 'SLITHER'),
    (9 , 'ZIRCON'),
])
def test_lexicon_get_word(index, word):
    assert lexicon.get_word(index) == word

def test_lexicon_get_word_count():
    assert lexicon.get_word_count() == 10