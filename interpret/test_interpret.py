import pytest
from interpret import interpret


@pytest.mark.parametrize('value, cmd, args, res', [
    (1, ['+'], [1], 2),
    (4, ['-'], [2], 2),
    (1, ['+', '*'], [1, 3], 6),
    (3, ['*'], [4], 12),
    (0, ['?'], [4], -1),
    (1, ['+', '*', '-'], [1, 3, 2], 4)
])
def test_interpret(value, cmd, args, res):
    assert interpret(value, cmd, args) == res
