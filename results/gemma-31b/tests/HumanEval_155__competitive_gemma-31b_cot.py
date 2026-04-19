
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

import pytest

@pytest.mark.parametrize("num, expected", [
    (0, (1, 0)),
    (1, (0, 1)),
    (2, (1, 0)),
    (123, (1, 2)),
    (-12, (1, 1)),
    (2468, (4, 0)),
    (1357, (0, 4)),
    (-2468, (4, 0)),
    (-1357, (0, 4)),
    (100, (2, 1)),
    (101, (1, 2)),
    (123456, (3, 3)),
    (-123456, (3, 3)),
    (999, (0, 3)),
    (888, (3, 0)),
])
def test_even_odd_count(num, expected):
    assert even_odd_count(num) == expected