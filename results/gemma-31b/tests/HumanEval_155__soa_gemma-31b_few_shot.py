
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
    (-2468, (4, 0)),
    (-1357, (0, 4)),
    (100, (2, 1)),
    (-100, (2, 1)),
    (10203, (3, 2)),
    (99999, (0, 5)),
    (88888, (5, 0)),
    (123456789, (4, 5)),
    (-123456789, (4, 5)),
])
def test_even_odd_count(num, expected):
    assert even_odd_count(num) == expected