
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

    def test_non_prime_returns_y(self):
        assert x_or_y(15, 8, 5) == 5
        assert x_or_y(4, 1, 2) == 2
        assert x_or_y(6, 3, 4) == 4
        assert x_or_y(9, 7, 8) == 8
        assert x_or_y(10, 9, 10) == 10

    def test_edge_cases(self):
        assert x_or_y(1, 10, 20) == 20  # 1 is not prime
        assert x_or_y(0, 5, 10) == 10  # 0 is not prime
        assert x_or_y(-5, 15, 25) == 25 # Negative numbers are not prime

    def test_large_prime(self):
        assert x_or_y(101, 200, 300) == 200

    def test_large_non_prime(self):
        assert x_or_y(100, 400, 500) == 500

    def test_x_and_y_equal(self):
        assert x_or_y(7, 5, 5) == 5
        assert x_or_y(4, 10, 10) == 10

    def test_n_is_prime_x_is_negative(self):
        assert x_or_y(7, -34, 12) == -34

    def test_n_is_not_prime_y_is_negative(self):
        assert x_or_y(15, 8, -5) == -5