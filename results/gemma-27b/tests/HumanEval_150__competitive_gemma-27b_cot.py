
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

import pytest

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

@pytest.mark.parametrize("n, x, y, expected", [
    (7, 34, 12, 34),
    (15, 8, 5, 5),
    (2, 10, 20, 10),
    (3, 5, 10, 5),
    (4, 1, 2, 2),
    (5, 100, 200, 100),
    (6, 1, 2, 2),
    (1, 5, 10, 10),
    (0, 1, 2, 2),
    (-1, 1, 2, 2),
    (101, 1, 2, 1),
    (97, 3, 5, 3),
    (100, 7, 9, 9),
    (29, 10, 11, 10),
    (31, 12, 13, 12),
])
def test_x_or_y(n, x, y, expected):
    assert x_or_y(n, x, y) == expected