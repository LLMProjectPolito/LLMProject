
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
    for i in range(2, int(n**0.5) + 1):
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
    def test_prime_n(self):
        assert x_or_y(7, 34, 12) == 34
        assert x_or_y(2, 100, 200) == 100
        assert x_or_y(11, 5, 10) == 5
        assert x_or_y(23, 1, 2) == 1

    def test_non_prime_n(self):
        assert x_or_y(15, 8, 5) == 5
        assert x_or_y(4, 20, 30) == 30
        assert x_or_y(9, 10, 20) == 20
        assert x_or_y(1, 50, 60) == 60

    def test_edge_cases(self):
        assert x_or_y(0, 1, 2) == 2
        assert x_or_y(-5, 3, 4) == 4
        assert x_or_y(2, 0, 0) == 0
        assert x_or_y(3, 0, 0) == 0

    def test_large_numbers(self):
        assert x_or_y(101, 1000, 2000) == 1000
        assert x_or_y(1000, 1000, 2000) == 2000

    def test_negative_x_y(self):
        assert x_or_y(7, -34, -12) == -34
        assert x_or_y(15, -8, -5) == -5