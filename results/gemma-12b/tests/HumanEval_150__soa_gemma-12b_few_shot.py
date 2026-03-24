
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

import pytest
from your_module import x_or_y  # Replace your_module

def is_prime(n):
    """Helper function to check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

class TestXorY:
    def test_prime_returns_x(self):
        assert x_or_y(7, 34, 12) == 34
        assert x_or_y(2, 100, 200) == 100
        assert x_or_y(5, 50, 60) == 50
        assert x_or_y(11, 111, 112) == 111
        assert x_or_y(13, 130, 131) == 130

    def test_non_prime_returns_y(self):
        assert x_or_y(15, 8, 5) == 5
        assert x_or_y(4, 1, 2) == 2
        assert x_or_y(6, 3, 4) == 4
        assert x_or_y(8, 7, 8) == 8
        assert x_or_y(9, 90, 91) == 91
        assert x_or_y(10, 100, 101) == 101

    def test_edge_cases(self):
        assert x_or_y(1, 10, 20) == 20
        assert x_or_y(0, 5, 10) == 10
        assert x_or_y(-5, 15, 25) == 25  # Negative input for n
        assert x_or_y(7, -10, 5) == -10 # Negative x
        assert x_or_y(7, 10, -5) == -5 # Negative y

    def test_large_numbers(self):
        assert x_or_y(1000000007, 1000, 2000) == 1000
        assert x_or_y(1000000008, 1000, 2000) == 2000

    def test_same_values(self):
        assert x_or_y(7, 5, 5) == 5
        assert x_or_y(8, 10, 10) == 10
        assert x_or_y(2, 2, 2) == 2