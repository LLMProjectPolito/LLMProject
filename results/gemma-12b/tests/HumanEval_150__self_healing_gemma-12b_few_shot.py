
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
        assert x_or_y(11, 50, 100) == 50
        assert x_or_y(13, "a", "b") == "a"
        assert x_or_y(17, 1, 0) == 1

    def test_non_prime_returns_y(self):
        assert x_or_y(15, 8, 5) == 5
        assert x_or_y(4, 10, 20) == 20
        assert x_or_y(9, "a", "b") == "b"
        assert x_or_y(1, 10, 20) == 20
        assert x_or_y(6, 0, 1) == 1

    def test_edge_cases(self):
        assert x_or_y(0, 10, 20) == 20
        assert x_or_y(1, 10, 20) == 20
        assert x_or_y(2, 10, 20) == 10
        assert x_or_y(-1, 10, 20) == 20
        assert x_or_y(-2, 10, 20) == 20

    def test_mixed_types(self):
        assert x_or_y(7, "hello", 12) == "hello"
        assert x_or_y(15, 8, "world") == "world"
        assert x_or_y(5, 1.5, 2.5) == 2.5
        assert x_or_y(5, True, False) == False
        assert x_or_y(5, [1,2], (3,4)) == (3,4)