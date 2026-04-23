
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


@pytest.mark.parametrize("n, x, y, expected", [
    (7, 34, 12, 34),
    (15, 8, 5, 5),
    (2, 10, 20, 10),
    (3, 1, 2, 1),
    (5, 100, 50, 100),
    (1, 10, 20, 20),
    (29, 1000, 500, 1000),
    (4, 10, 20, 20),
    (11, 5, 10, 5),
    (13, 20, 10, 20),
    (17, 1, 100, 1),
    (19, 50, 25, 50),
    (23, 10, 5, 10),
    (25, 10, 5, 5),
    (2, 5, 10, 5),
    (3, 10, 5, 10),
    (5, 5, 10, 5),
    (7, 10, 5, 10),
    (11, 5, 10, 5),
    (13, 10, 5, 10),
    (17, 5, 10, 5),
    (19, 10, 5, 10),
    (23, 5, 10, 5),
    (29, 10, 5, 10),
    (31, 5, 10, 5),
    (37, 10, 5, 10),
    (41, 5, 10, 5),
    (43, 10, 5, 10),
    (47, 5, 10, 5),
])
def test_x_or_y_prime(n, x, y, expected):
    assert x_or_y(n, x, y) == expected

@pytest.mark.parametrize("n, x, y, expected", [
    (4, 34, 12, 12),
    (15, 8, 5, 5),
    (25, 10, 20, 20),
    (1, 10, 20, 20),
    (2, 10, 20, 20),
    (3, 1, 2, 2),
    (4, 10, 20, 20),
    (6, 10, 20, 20),
    (8, 10, 20, 20),
    (9, 10, 20, 20),
    (10, 10, 20, 20),
    (12, 10, 20, 20),
    (14, 10, 20, 20),
    (16, 10, 20, 20),
    (18, 10, 20, 20),
    (20, 10, 20, 20),
])
def test_x_or_y_not_prime(n, x, y, expected):
    assert x_or_y(n, x, y) == expected