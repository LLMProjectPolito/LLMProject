
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

import pytest

@pytest.mark.parametrize("num, expected", [
    (123, (1, 2)),
    (-12, (1, 1)),
    (0, (1, 0)),
    (1, (0, 1)),
    (2, (1, 0)),
    (2468, (4, 0)),
    (1357, (0, 4)),
    (102345, (3, 3)),
    (-246, (3, 0)),
    (-135, (0, 3)),
    (100, (2, 1)),
    (-100, (2, 1)),
    (1234567890, (5, 5)),
    (-1234567890, (5, 5)),
])
def test_even_odd_count(num, expected):
    assert even_odd_count(num) == expected