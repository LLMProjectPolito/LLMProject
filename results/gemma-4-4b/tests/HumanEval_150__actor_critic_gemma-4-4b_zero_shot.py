
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

import pytest

def x_or_y(n, x, y):
    """
    Returns x if n is a prime number, otherwise returns y.

    Args:
        n (int): The number to check for primality.
        x (int): The value to return if n is not prime.
        y (int): The value to return if n is prime.

    Returns:
        int: x if n is prime, y otherwise.
    """
    if n <= 1:
        return y
    for i in range(2, int(n**0.5) + 1):
        if (n % i) == 0:
            return y
    return x


@pytest.mark.parametrize("n, x, y, expected", [
    (7, 34, 12, 34),  # Prime number
    (15, 8, 5, 5),  # Not prime number
    (2, 10, 20, 10),  # Prime number
    (1, 5, 10, 10),  # Edge case: n = 1 (not prime)
    (0, 1, 2, 2),  # Edge case: n = 0 (not prime)
    (-1, 5, 10, 10), # Edge case: n < 0 (not prime)
    (11, 100, 200, 100), # Prime number
    (29, 1, 1000, 1), # Prime number
    (4, 1, 2, 2), # Not prime
    (17, 5, 10, 5), # Prime number
    (31, 100, 200, 100), # Prime number
    (100, 1, 2, 2), # Not prime
    (101, 1, 2, 1), # Prime number
    (103, 10, 20, 10), # Prime number
    (105, 1, 2, 2), # Not prime
    (107, 100, 200, 100) # Prime number
])
def test_x_or_y_basic(n, x, y, expected):
    assert x_or_y(n, x, y) == expected

@pytest.mark.parametrize("n, x, y, expected", [
    (2, 5, 10, 5),  # Small prime
    (3, 5, 10, 5),  # Small prime
    (5, 5, 10, 5),  # Small prime
    (13, 5, 10, 5), # Prime number
    (17, 5, 10, 5), # Prime number
    (19, 5, 10, 5), # Prime number
    (23, 5, 10, 5), # Prime number
    (29, 5, 10, 5), # Prime number
    (31, 5, 10, 5), # Prime number
])
def test_x_or_y_small_primes(n, x, y, expected):
    assert x_or_y(n, x, y) == expected

@pytest.mark.parametrize("n, x, y, expected", [
    (4, 5, 10, 10),  # Small non-prime
    (6, 5, 10, 10),  # Small non-prime
    (8, 5, 10, 10),  # Small non-prime
    (9, 5, 10, 10),  # Small non-prime
    (10, 5, 10, 10), # Small non-prime
    (12, 5, 10, 10), # Small non-prime
    (14, 5, 10, 10), # Small non-prime
    (15, 5, 10, 10), # Small non-prime
])
def test_x_or_y_small_non_primes(n, x, y, expected):
    assert x_or_y(n, x, y) == expected

@pytest.mark.parametrize("n, x, y, expected", [
    (-2, 5, 10, 10), # Negative prime
    (-1, 5, 10, 10), # Negative not prime
])
def test_x_or_y_negative_numbers(n, x, y, expected):
    assert x_or_y(n, x, y) == expected

@pytest.mark.parametrize("n, x, y, expected", [
    (5, 5, 5, 5), # x and y are equal
    (7, 34, 34, 34)
])
def test_x_or_y_equal(n, x, y, expected):
    assert x_or_y(n, x, y) == expected