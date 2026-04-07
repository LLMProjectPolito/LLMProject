
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
    if n <= 1:
        return y
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return y
    return x

@pytest.mark.parametrize("n, x, y, expected", [
    (7, 34, 12, 34),
    (15, 8, 5, 5),
    (2, 10, 20, 10),
    (3, 5, 10, 5),
    (5, 1, 2, 1),
    (11, 100, 200, 100),
    (13, 300, 400, 300),
    (4, 1, 2, 2),
    (6, 1, 2, 2),
    (8, 1, 2, 2),
    (9, 1, 2, 2),
    (10, 1, 2, 2),
])
def test_prime_numbers(n, x, y, expected):
    assert x_or_y(n, x, y) == expected

@pytest.mark.parametrize("n, x, y, expected", [
    (1, 10, 20, 20),
    (0, 10, 20, 20),
    (-1, 10, 20, 20),
    (4, 1, 2, 2),
    (6, 1, 2, 2),
    (8, 1, 2, 2),
    (9, 1, 2, 2),
    (10, 1, 2, 2),
    (12, 1, 2, 2),
    (14, 1, 2, 2),
    (15, 1, 2, 2),
    (16, 1, 2, 2),
])
def test_non_prime_numbers(n, x, y, expected):
    assert x_or_y(n, x, y) == expected

@pytest.mark.parametrize("n, x, y, expected", [
    (1, 10, 20, 20),
    (0, 10, 20, 20),
    (-1, 10, 20, 20),
    (2, 10, 20, 10),
    (3, 10, 20, 10),
    (4, 10, 20, 20),
])
def test_edge_cases(n, x, y, expected):
    assert x_or_y(n, x, y) == expected

@pytest.mark.parametrize("n, x, y, expected", [
    (97, 100, 200, 100),  # Large prime
    (99, 100, 200, 200),  # Large non-prime
    (101, 100, 200, 100), # Large prime
    (100, 100, 200, 200), # Large non-prime
])
def test_large_numbers(n, x, y, expected):
    assert x_or_y(n, x, y) == expected