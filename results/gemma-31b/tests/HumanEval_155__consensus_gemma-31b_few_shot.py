
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
    (3, (0, 1)),
    (-2, (1, 0)),
    (-3, (0, 1)),
    (2468, (4, 0)),
    (1357, (0, 4)),
    (-1357, (0, 4)),
    (102, (2, 1)),
    (-102, (2, 1)),
    (100, (2, 1)),
    (-101, (1, 2)),
    (-468, (3, 0)),
    (1000, (3, 1)),
    (1111, (0, 4)),
    (2222, (4, 0)),
    (123456789, (4, 5)),
    (-123456789, (4, 5)),
    (2046813579, (5, 5)),
    (-2046813579, (5, 5)),
    (24680, (5, 0)),
    (13579, (0, 5)),
    (1234567890, (5, 5)),
    (-1234567890, (5, 5)),
])
def test_even_odd_count(num, expected):
    assert even_odd_count(num) == expected