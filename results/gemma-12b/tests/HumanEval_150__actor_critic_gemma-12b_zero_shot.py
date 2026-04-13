
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
    Negative numbers are treated as non-prime.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    """
    if n <= 1:
        return y
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return y
    return x

@pytest.mark.parametrize("n, x, y, expected", [
    (7, 34, 12, 34),
    (2, 100, 200, 100),
    (5, 50, 60, 50),
    (11, 70, 80, 70),
    (13, 1, 2, 1),
    (17, 1000, 2000, 1000),  # Larger prime
])
def test_prime_number(n, x, y, expected):
    assert x_or_y(n, x, y) == expected

@pytest.mark.parametrize("n, x, y, expected", [
    (15, 8, 5, 5),
    (4, 20, 30, 30),
    (6, 10, 15, 15),
    (8, 40, 50, 50),
    (9, 1000, 2000, 2000),
    (10, 5, 10, 10), # Added a different non-prime
])
def test_non_prime_number(n, x, y, expected):
    assert x_or_y(n, x, y) == expected

def test_negative_input():
    assert x_or_y(-1, 5, 6) == 6
    assert x_or_y(-2, 10, 20) == 20

def test_large_non_prime():
    assert x_or_y(999999996, 100, 200) == 200

def test_edge_case_two():
    assert x_or_y(2, 5, 10) == 5