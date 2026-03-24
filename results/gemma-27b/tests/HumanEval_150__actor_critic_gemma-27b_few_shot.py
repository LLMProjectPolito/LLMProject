
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

def test_x_or_y():
    # Consolidated tests for prime and non-prime numbers
    assert x_or_y(7, 34, 12) == 34  # Test case for a prime number
    assert x_or_y(15, 8, 5) == 5  # Test case for a non-prime number
    assert x_or_y(2, 10, 20) == 10  # Test case for the prime number 2
    assert x_or_y(3, 5, 1) == 5  # Test case for a small prime
    assert x_or_y(5, 100, 1) == 100  # Another prime test
    assert x_or_y(4, 1, 2) == 2  # Test case for a non-prime number
    assert x_or_y(6, 3, 4) == 4  # Another non-prime test
    assert x_or_y(8, 7, 6) == 6  # Test with an even non-prime
    assert x_or_y(9, 10, 11) == 11  # Test with an odd non-prime
    assert x_or_y(10, 12, 13) == 13  # Another non-prime test
    assert x_or_y(11, 1, 2) == 1  # Test with a larger prime
    assert x_or_y(13, 99, 0) == 99  # Another prime test
    assert x_or_y(97, 1, 2) == 1  # Test with a larger prime

    # Edge case tests
    assert x_or_y(1, 1, 2) == 2  # Test case for n = 1, which is not prime
    assert x_or_y(0, 1, 2) == 2  # Test case for n = 0, which is not prime
    assert x_or_y(-1, 1, 2) == 2  # Test case for n = -1, which is not prime.  Explicitly testing negative input.
    assert x_or_y(2, 0, 0) == 0  # Test case where x and y are zero and n is prime
    assert x_or_y(100, 0, 0) == 0  # Test case where x and y are zero and n is not prime
    assert x_or_y(17, -1, 1) == -1  # Test case with negative y and prime n
    assert x_or_y(4, -1, 1) == 1  # Test case with negative y and non-prime n

    # Test with larger numbers
    assert x_or_y(101, 5, 6) == 5  # Test with a larger prime
    assert x_or_y(102, 5, 6) == 6  # Test with a larger non-prime
    assert x_or_y(1000, 10, 11) == 11 # Test with a larger non-prime
    assert x_or_y(1009, 10, 11) == 10 # Test with a larger prime