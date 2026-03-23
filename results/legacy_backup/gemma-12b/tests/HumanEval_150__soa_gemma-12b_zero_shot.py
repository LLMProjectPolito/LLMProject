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
        assert x_or_y(13, 1, 2) == 1

    def test_non_prime_returns_y(self):
        assert x_or_y(15, 8, 5) == 5
        assert x_or_y(4, 10, 20) == 20
        assert x_or_y(6, 50, 100) == 100
        assert x_or_y(9, 2, 4) == 4
        assert x_or_y(10, 100, 50) == 50

    def test_edge_cases(self):
        assert x_or_y(1, 5, 10) == 10  # 1 is not prime
        assert x_or_y(0, 10, 20) == 20  # 0 is not prime
        assert x_or_y(-5, 1, 2) == 2 # Negative numbers are not prime
        assert x_or_y(23, 100, 200) == 100
        assert x_or_y(29, 500, 1000) == 500

    def test_large_prime(self):
        assert x_or_y(101, 10, 20) == 10

    def test_large_non_prime(self):
        assert x_or_y(1000, 1, 2) == 2

    def test_x_and_y_equal(self):
        assert x_or_y(7, 5, 5) == 5
        assert x_or_y(10, 5, 5) == 5

    def test_zero_input(self):
        assert x_or_y(0, 0, 0) == 0
        assert x_or_y(1, 0, 0) == 0
        assert x_or_y(2, 0, 0) == 0