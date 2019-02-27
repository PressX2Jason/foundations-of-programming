import pytest
from find_longest_word_in_dictionary import find_longest_word_in_dictionary_that_subsequence_of_given_string

@pytest.mark.parametrize('S,D', [
    ('abppplee', ['able', 'ale', 'apple', 'bale', 'kangaroo'])
])
def test_should_return_longest_word_in_dictionary(S, D):
    result = find_longest_word_in_dictionary_that_subsequence_of_given_string(S, D)
    assert result == 'apple'
    assert result != 'bale'
    assert result != 'kangaroo'
