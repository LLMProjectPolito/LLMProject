
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
        assert x_or_y(5, "a", "b") == "a"
        assert x_or_y(11, 1.23, 4.56) == 1.23
        assert x_or_y(13, [1,2], [3,4]) == [1,2]

    def test_non_prime_returns_y(self):
        assert x_or_y(15, 8, 5) == 5
        assert x_or_y(4, 10, 20) == 20
        assert x_or_y(6, "hello", "world") == "world"
        assert x_or_y(9, True, False) == False
        assert x_or_y(10, None, "something") == "something"

    def test_edge_cases(self):
        assert x_or_y(1, 5, 10) == 10  # 1 is not prime
        assert x_or_y(0, 1, 2) == 2  # 0 is not prime
        assert x_or_y(-5, 3, 7) == 7 # Negative numbers are not prime
        assert x_or_y(23, 10, 20) == 10

    def test_large_prime(self):
        assert x_or_y(997, 100, 200) == 100

    def test_large_non_prime(self):
        assert x_or_y(1000, 1, 2) == 2

    def test_type_handling(self):
        assert x_or_y(7, 3.14, 2.71) == 3.14
        assert x_or_y(10, [1, 2, 3], (4, 5, 6)) == (4, 5, 6)

    def test_mixed_types(self):
        assert x_or_y(5, 10, "test") == "test"
        assert x_or_y(4, "test", 10) == 10

    def test_zero_x_y(self):
        assert x_or_y(7, 0, 0) == 0
        assert x_or_y(10, 0, 0) == 0

    def test_negative_x_y(self):
        assert x_or_y(7, -1, -2) == -1
        assert x_or_y(10, -1, -2) == -2