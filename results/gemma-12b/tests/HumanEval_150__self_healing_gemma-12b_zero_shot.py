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
        assert x_or_y(2, 5, 10) == 5 # 2 is prime
        assert x_or_y(3, 5, 10) == 5 # 3 is prime

    def test_large_numbers(self):
        assert x_or_y(101, 1000, 2000) == 1000
        assert x_or_y(1000, 1000, 2000) == 2000

    def test_same_values(self):
        assert x_or_y(7, 5, 5) == 5
        assert x_or_y(4, 5, 5) == 5
        assert x_or_y(2, 5, 5) == 5