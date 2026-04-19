
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
    (2468, (4, 0)),
    (1357, (0, 4)),
    (-2468, (4, 0)),
    (-1357, (0, 4)),
    (10, (1, 1)),
    (-10, (1, 1)),
    (100, (2, 1)),
    (1234567890, (5, 5)),
    (-1234567890, (5, 5)),
    (7, (0, 1)),
    (-7, (0, 1)),
    (8, (1, 0)),
    (-8, (1, 0)),
    (101010, (3, 3)),
    (-101010, (3, 3)),
    (-9, (0, 1)),
    (-4, (1, 0)),
    (101, (1, 2)),
    (2024, (4, 0)),
    (987654321, (4, 5)),
    (-987654321, (4, 5)),
])
def test_even_odd_count(num, expected):
    assert even_odd_count(num) == expected