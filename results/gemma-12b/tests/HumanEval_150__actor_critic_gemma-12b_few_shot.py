
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
    # Optimization: Start from 2 and only check odd numbers after 2
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    x_or_y(7, 34, 12) == 34  # Demonstrates the prime case
    x_or_y(15, 8, 5) == 5   # Demonstrates the non-prime case
    
    """
    if is_prime(n):
        return x
    else:
        return y

@pytest.mark.parametrize(
    "n, x, y, expected",
    [
        (7, 34, 12, 34),  # Prime number
        (2, 100, 200, 100), # Prime number - Explicit test for 2
        (3, 1, 2, 1),  # Prime number - Smallest odd prime after 2
        (5, 5, 10, 5), # Prime number
        (4, 1, 2, 2),  # Not prime - Explicit test for 4
        (9, 1, 2, 2),  # Not prime - Perfect square
        (15, 8, 5, 5),  # Not prime
        (4, 10, 20, 20), # Not prime
        (6, 10, 20, 20), # Not prime
        (1, 10, 20, 20),  # Edge case: 1 is not prime
        (0, 5, 10, 10),  # Edge case: 0 is not prime
        (-5, 1, 2, 2), # Edge case: Negative number
        (23, 1000, 2000, 1000), # Larger prime number
        (100, 1, 2, 2), # Larger non-prime number
        (101, 1, 2, 1), # Larger prime number
        (103, 1, 2, 1), # Another larger prime number
        (107, 1, 2, 1), # Yet another larger prime number
        (7919, 1, 2, 1), # A larger prime number
        # Large prime number test (optional - may impact performance)
        # (7919, 100, 200, 100), # A larger prime number
    ],
)
def test_x_or_y(n, x, y, expected):
    assert x_or_y(n, x, y) == expected