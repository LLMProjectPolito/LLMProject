
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
        assert x_or_y(2, 10, 20) == 10
        assert x_or_y(5, 100, 200) == 100
        assert x_or_y(11, 5, 15) == 5
        assert x_or_y(13, 100, 200) == 100
        assert x_or_y(1000000007, 1, 2) == 1 #large prime

    def test_non_prime_returns_y(self):
        assert x_or_y(15, 8, 5) == 5
        assert x_or_y(4, 1, 2) == 2
        assert x_or_y(6, 10, 20) == 20
        assert x_or_y(9, 25, 30) == 30
        assert x_or_y(10, 1000, 2000) == 2000
        assert x_or_y(1000000000, 1, 2) == 2 #large non-prime

    def test_edge_cases(self):
        assert x_or_y(1, 5, 10) == 10  # 1 is not prime
        assert x_or_y(0, 1, 2) == 2  # 0 is not prime
        assert x_or_y(-5, 3, 7) == 7 # Negative numbers are not prime
        assert x_or_y(2, 0, 0) == 0 # Prime number, x = 0
        assert x_or_y(4, 0, 0) == 0 # Non-prime, y = 0

    def test_type_handling(self):
        assert x_or_y(7, "hello", 12) == "hello"
        assert x_or_y(7, 34, "world") == "world"
        assert x_or_y(7.0, 34, 12) == 34 # float input for n
        assert x_or_y(7, 34.5, 12) == 12 # float input for x or y
        assert x_or_y(7, 34, 12.5) == 12.5
        assert x_or_y(7, 34, 12.0) == 12.0

    def test_large_numbers(self):
        assert x_or_y(997, 1000, 2000) == 1000
        assert x_or_y(1000, 1000, 2000) == 2000
        assert x_or_y(9999991, 1000000, 2000000) == 1000000

    def test_same_values(self):
        assert x_or_y(7, 5, 5) == 5
        assert x_or_y(4, 10, 10) == 10