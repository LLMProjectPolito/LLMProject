
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

import pytest

def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    >>> x_or_y(7, 34, 12)
    34
    >>> x_or_y(15, 8, 5)
    5
    
    """
    if n <= 1:
        return y
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return y
    return x

@pytest.mark.parametrize("n, x, y, expected", [
    (7, 34, 12, 34),
    (2, 10, 20, 10),
    (3, 5, 1, 5),
    (5, 100, 0, 100),
    (11, 1, 2, 1),
    (13, -1, 0, -1),
    (17, 10, -10, 10),
    (19, 0, 1, 0),
    (15, 8, 5, 5),
    (4, 1, 2, 2),
    (6, 5, 10, 10),
    (8, 2, 4, 4),
    (9, 3, 6, 6),
    (10, 7, 8, 8),
    (12, 9, 1, 1),
    (14, 0, -1, -1),
    (16, -2, 2, 2),
])
def test_x_or_y_when_n_is_prime_or_not(n, x, y, expected):
    assert x_or_y(n, x, y) == expected

@pytest.mark.parametrize("n, x, y, expected", [
    (1, 10, 20, 20),
    (0, 5, 1, 1),
    (2, 0, 0, 0),
    (-1, 1, 2, 2),
    (-2, 3, 4, 4),
])
def test_x_or_y_with_edge_cases(n, x, y, expected):
    assert x_or_y(n, x, y) == expected

def test_x_or_y_with_large_non_prime():
    assert x_or_y(1000, 1, 2) == 2

def test_x_or_y_with_negative_input():
    assert x_or_y(-5, 10, 20) == 20

def test_x_or_y_with_large_prime():
    assert x_or_y(7919, 1, 2) == 1