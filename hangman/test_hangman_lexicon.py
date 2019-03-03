import pytest
from hangman_lexicon import HangmanLexicon

lexicon = HangmanLexicon()

seedWords = [
    'BUOY',
    'COMPUTER',
    'CONNOISSEUR',
    'DEHYDRATE',
    'FUZZY',
    'HUBBUB',
    'KEYHOLE',
    'QUAGMIRE',
    'SLITHER',
    'ZIRCON'
]


@pytest.mark.parametrize('index, word',
                         [(index, word)
                          for index, word in enumerate(seedWords)]
                         )
def test_lexicon_get_word(index, word):
    assert lexicon._get_word(index) == word


def test_lexicon_get_word_count():
    assert lexicon._get_word_count() == len(seedWords)


def test_get_random_word():
    word = lexicon.get_random_word()
    assert word in seedWords


def test_get_word_out_of_bounds():
    with pytest.raises(IndexError):
        lexicon._get_word(99)
