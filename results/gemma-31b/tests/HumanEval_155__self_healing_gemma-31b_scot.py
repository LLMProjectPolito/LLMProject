
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    num_str = str(abs(num))
    even_count = 0
    odd_count = 0
    for digit in num_str:
        if int(digit) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)

import pytest

@pytest.mark.parametrize("num, expected", [
    (123, (1, 2)),
    (-12, (1, 1)),
    (0, (1, 0)),
    (2468, (4, 0)),
    (1357, (0, 4)),
    (-482, (3, 0)),
    (-135, (0, 3)),
    (101, (1, 2)),
    (2000, (4, 0)),
    (7, (0, 1)),
    (8, (1, 0)),
    (-9, (0, 1)),
    (-8, (1, 0)),
    (123456789, (4, 5)),
    (-123456789, (4, 5)),
])
def test_even_odd_count(num, expected):
    assert even_odd_count(num) == expected