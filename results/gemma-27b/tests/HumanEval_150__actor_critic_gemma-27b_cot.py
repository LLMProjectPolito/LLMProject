
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

import pytest

def is_prime(n):
    """Helper function to determine if a number is prime."""
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
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    if is_prime(n):
        return x
    else:
        return y

@pytest.mark.parametrize(
    "n, x, y, expected",
    [
        (7, 34, 12, 34),
        (2, 10, 20, 10),
        (3, 5, 1, 5),
        (5, 100, 200, 100),
        (11, 1, 2, 1),
        (13, -5, 10, -5),
        (17, 0, 1, 0),
        (19, 10, -10, 10),
        (15, 8, 5, 5),
        (4, 1, 2, 2),
        (6, 10, 5, 5),
        (8, 20, 10, 10),
        (9, 5, 1, 1),
        (10, -1, -2, -2),
        (12, 0, 1, 1),
        (14, 10, -10, -10),
    ],
)
def test_x_or_y(n, x, y, expected):
    """Tests the x_or_y function with various prime and non-prime inputs."""
    assert x_or_y(n, x, y) == expected

def test_x_or_y_prime_not_prime():
    """Tests x_or_y with prime and non-prime n values."""
    assert x_or_y(7, 10, 20) == 10  # n is prime, return x
    assert x_or_y(8, 10, 20) == 20  # n is not prime, return y

def test_x_or_y_edge_cases():
    """Tests x_or_y with edge cases like 0, 1, and negative numbers."""
    assert x_or_y(1, 10, 20) == 20  # 1 is not prime
    assert x_or_y(2, 10, 20) == 10  # 2 is prime
    assert x_or_y(0, 10, 20) == 20  # 0 is not prime
    assert x_or_y(-1, 10, 20) == 20 # negative number is not prime
    assert x_or_y(100, 10, 20) == 20
    assert x_or_y(101, 10, 20) == 10 # 101 is prime

def test_x_or_y_large_numbers():
    """Tests x_or_y with large numbers to ensure it handles them correctly."""
    assert x_or_y(997, 100, 200) == 100 # 997 is prime
    assert x_or_y(999, 100, 200) == 200 # 999 is not prime