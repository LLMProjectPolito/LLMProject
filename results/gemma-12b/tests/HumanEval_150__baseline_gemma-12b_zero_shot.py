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
        assert x_or_y(5, 100, 50) == 100
        assert x_or_y(11, 5, 10) == 5

    def test_non_prime_returns_y(self):
        assert x_or_y(15, 8, 5) == 5
        assert x_or_y(4, 1, 2) == 2
        assert x_or_y(6, 10, 20) == 20
        assert x_or_y(9, 5, 10) == 10
        assert x_or_y(10, 1, 2) == 2

    def test_edge_cases(self):
        assert x_or_y(1, 5, 10) == 10  # 1 is not prime
        assert x_or_y(0, 5, 10) == 10  # 0 is not prime
        assert x_or_y(-5, 5, 10) == 10 # Negative numbers are not prime
        assert x_or_y(2, 5, 5) == 5 # Prime, x and y are the same
        assert x_or_y(3, 5, 5) == 5 # Prime, x and y are the same

    def test_large_prime(self):
        assert x_or_y(101, 1000, 1) == 1000

    def test_large_non_prime(self):
        assert x_or_y(100, 1, 1000) == 1000

    def test_x_and_y_same(self):
        assert x_or_y(7, 5, 5) == 5
        assert x_or_y(4, 5, 5) == 5