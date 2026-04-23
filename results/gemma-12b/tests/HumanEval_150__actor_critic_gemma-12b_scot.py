
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
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
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

class TestXorY:
    def test_prime_returns_x(self):
        assert x_or_y(7, 34, 12) == 34
        assert x_or_y(2, 10, 5) == 10
        assert x_or_y(3, 100, 20) == 100

    def test_non_prime_returns_y(self):
        assert x_or_y(15, 8, 5) == 5
        assert x_or_y(4, 1, 2) == 2
        assert x_or_y(6, 10, 20) == 20

    def test_edge_cases_n(self):
        assert x_or_y(0, 10, 5) == 5  # n = 0, non-prime
        assert x_or_y(1, 10, 5) == 5  # n = 1, non-prime
        assert x_or_y(-5, 10, 5) == 5 # n = -5, non-prime

    def test_negative_x_and_y(self):
        assert x_or_y(7, -34, -12) == -34
        assert x_or_y(15, -8, -5) == -5

    def test_zero_x_and_y(self):
        assert x_or_y(7, 0, 12) == 0
        assert x_or_y(15, 8, 0) == 0

    def test_x_equals_y(self):
        assert x_or_y(7, 10, 10) == 10
        assert x_or_y(15, 10, 10) == 10

    def test_large_prime(self):
        assert x_or_y(101, 1000, 500) == 1000

    def test_large_non_prime(self):
        assert x_or_y(100, 1000, 500) == 500