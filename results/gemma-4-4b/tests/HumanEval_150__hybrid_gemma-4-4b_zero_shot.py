
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
    (2, 10, 5, 10),  # n is prime
    (3, 10, 5, 10),  # n is prime
    (5, 10, 5, 10),  # n is prime
    (7, 10, 5, 10),  # n is prime
    (11, 10, 5, 10), # n is prime
    (13, 10, 5, 10), # n is prime
    (17, 10, 5, 10), # n is prime
    (19, 10, 5, 10), # n is prime
    (23, 10, 5, 10), # n is prime
    (29, 10, 5, 10), # n is prime
    (4, 10, 5, 5),   # n is not prime
    (6, 10, 5, 5),   # n is not prime
    (8, 10, 5, 5),   # n is not prime
    (9, 10, 5, 5),   # n is not prime
    (10, 10, 5, 5),  # n is not prime
    (12, 10, 5, 5),  # n is not prime
    (14, 10, 5, 5),  # n is not prime
    (15, 10, 5, 5),  # n is not prime
    (16, 10, 5, 5),  # n is not prime
    (18, 10, 5, 5),  # n is not prime
    (20, 10, 5, 5),  # n is not prime
    (1, 10, 5, 5),   # n is not prime
    (0, 10, 5, 5),   # n is not prime
    (-1, 10, 5, 5),  # n is not prime
    (49, 10, 5, 5), # n is not prime
    (100, 10, 5, 5), # n is not prime
    (101, 10, 5, 10), # n is prime
    (103, 10, 5, 10), # n is prime
    (107, 10, 5, 10)  # n is prime
])
def test_x_or_y_prime(n, x, y, expected):
    assert x_or_y(n, x, y) == expected

@pytest.mark.parametrize("n, x, y, expected", [
    (4, 10, 5, 5),  # n is not prime
    (6, 10, 5, 5),  # n is not prime
    (8, 10, 5, 5),  # n is not prime
    (9, 10, 5, 5),  # n is not prime
    (10, 10, 5, 5),  # n is not prime
    (12, 10, 5, 5),  # n is not prime
    (14, 10, 5, 5),  # n is not prime
    (15, 10, 5, 5),  # n is not prime
    (16, 10, 5, 5),  # n is not prime
    (18, 10, 5, 5),  # n is not prime
    (20, 10, 5, 5),  # n is not prime
    (1, 10, 5, 5),   # n is not prime
    (0, 10, 5, 5),   # n is not prime
    (-1, 10, 5, 5),  # n is not prime
    (49, 10, 5, 5), # n is not prime
    (100, 10, 5, 5)  # n is not prime
])
def test_x_or_y_not_prime(n, x, y, expected):
    assert x_or_y(n, x, y) == expected

@pytest.mark.parametrize("n", [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 1, 0, -1, 49, 100, 101, 103, 107])
def test_is_prime_basic(n):
    assert is_prime(n) == (n > 1 and all(n % i for i in range(2, int(n**0.5) + 1))) or n in (2,3)