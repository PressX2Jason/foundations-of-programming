import pytest
from find_longest_word_in_dictionary import find_longest_word_in_dictionary_that_subsequence_of_given_string

@pytest.mark.parametrize('S, D, correct_answer', [
    ('abppplee', ['able', 'ale', 'apple', 'bale', 'kangaroo'], 'apple'),
    ('abbbcddddde', ['abc', 'abcdddde', 'addddcbbb', 'acdddd'], 'abcdddde'),
    ('', ['ab', 'abc', 'bbab'], '')
])
def test_should_return_longest_word_in_dictionary(S, D, correct_answer):
    result = find_longest_word_in_dictionary_that_subsequence_of_given_string(S, D)
    assert result == correct_answer