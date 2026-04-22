
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
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    if is_prime(n):
        return x
    else:
        return y

def is_prime(n):
    """Helper function to check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


@pytest.mark.parametrize(
    "n, x, y, expected",
    [
        (7, 34, 12, 34),  # Prime n
        (15, 8, 5, 5),  # Not prime n
        (2, 10, 20, 10),  # Prime n
        (1, 10, 20, 20),  # Not prime n
        (3, 5, 10, 5),  # Prime n
        (4, 5, 10, 10),  # Not prime n
        (5, 5, 10, 5),  # Prime n
        (6, 5, 10, 10),  # Not prime n
        (11, 1, 2, 1), # Prime n
        (12, 1, 2, 2), # Not prime n
        (29, 100, 200, 100), #Prime n
        (100, 100, 200, 200), #Not prime n
        (17, 1, 2, 1), #Prime n
        (25, 1, 2, 2), #Not prime n
    ],
)
def test_x_or_y_valid_inputs(n, x, y, expected):
    assert x_or_y(n, x, y) == expected


@pytest.mark.parametrize(
    "n, x, y, expected",
    [
        (0, 10, 20, 20),  # n = 0
        (-1, 10, 20, 20),  # n = -1
        (-7, 34, 12, 12), #Negative prime
        (-15, 8, 5, 5), #Negative non prime
    ],
)
def test_x_or_y_negative_inputs(n, x, y, expected):
    assert x_or_y(n, x, y) == expected

@pytest.mark.parametrize(
    "n, x, y, expected",
    [
        (1000000007, 1, 2, 1), #Large prime
        (1000000008, 1, 2, 2), #Large non prime
    ],
)
def test_x_or_y_large_inputs(n, x, y, expected):
    assert x_or_y(n, x, y) == expected