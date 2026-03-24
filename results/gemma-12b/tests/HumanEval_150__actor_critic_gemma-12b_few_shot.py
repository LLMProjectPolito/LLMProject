
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

import pytest

def is_prime(n):
    """Helper function to check if a number is prime."""
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

def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    x_or_y(7, 34, 12) == 34
    x_or_y(15, 8, 5) == 5
    x_or_y(2, 100, 200) == 100
    x_or_y(1, 10, 20) == 20
    x_or_y(0, 5, 10) == 10
    x_or_y(-5, 1, 2) == 2
    x_or_y(23, 1000, 2000) == 1000
    x_or_y(100, 1, 2) == 2
    x_or_y(3, 1, 1) == 1
    x_or_y(5, 100, 100) == 100
    """
    if is_prime(n):
        return x
    else:
        return y

@pytest.mark.parametrize(
    "n, x, y, expected",
    [
        (7, 34, 12, 34),
        (2, 100, 200, 100),
        (5, 5, 10, 5),
        (15, 8, 5, 5),
        (4, 1, 2, 2),
        (6, 10, 20, 20),
        (1, 10, 20, 20),
        (0, 5, 10, 10),
        (-5, 1, 2, 2),
        (23, 1000, 2000, 1000),
        (100, 1, 2, 2),
        (3, 1, 1, 1),
        (5, 100, 100, 100),
        (11, 10, 20, 10),
        (13, 50, 60, 50),
        (17, 70, 80, 70),
        (19, 90, 100, 90),
        (29, 110, 120, 110),
        (101, 1, 2, 1),
        (103, 3, 4, 3),
        (107, 5, 6, 5),
        (109, 7, 8, 7),
        (997, 1000, 2000, 1000),
        (1000000, 1, 2, 2),
        (999983, 100, 200, 100),
    ],
)
def test_x_or_y(n, x, y, expected):
    assert x_or_y(n, x, y) == expected

def test_is_prime_one():
    assert is_prime(1) == False

def test_is_prime_negative():
    assert is_prime(-7) == False

def test_x_or_y_large_numbers():
    assert x_or_y(2**31 - 1, 1000000, 2000000, 1000000) # Largest prime less than 2**31
    assert x_or_y(2**31 - 2, 1000000, 2000000, 2000000) # Large non-prime