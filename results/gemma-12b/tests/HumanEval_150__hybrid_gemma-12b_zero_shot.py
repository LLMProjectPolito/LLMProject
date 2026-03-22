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
        assert x_or_y(6, 10, 20) == 20
        assert x_or_y(9, 30, 40) == 40
        assert x_or_y(10, 5, 10) == 10

    def test_edge_cases(self):
        assert x_or_y(1, 10, 20) == 20  # 1 is not prime
        assert x_or_y(0, 5, 10) == 10  # 0 is not prime
        assert x_or_y(-5, 15, 25) == 25 # Negative numbers are not prime
        assert x_or_y(23, None, "test") == "test"
        assert x_or_y(29, True, False) == True

    def test_large_prime(self):
        assert x_or_y(101, 1000, 2000) == 1000

    def test_large_non_prime(self):
        assert x_or_y(100, 500, 600) == 600

    def test_x_and_y_equal(self):
        assert x_or_y(7, 5, 5) == 5
        assert x_or_y(4, 10, 10) == 10

    def test_zero_input(self):
        assert x_or_y(0, 0, 0) == 0
        assert x_or_y(1, 0, 0) == 0

    def test_negative_n(self):
        assert x_or_y(-1, 1, 2) == 2
        assert x_or_y(-7, 3, 4) == 4

    def test_prime_returns_x_with_different_types(self):
        assert x_or_y(7, 34, "a") == 34
        assert x_or_y(2, 100, 1.23) == 100
        assert x_or_y(5, "a", "b") == "a"
        assert x_or_y(11, 1.23, 4.56) == 1.23
        assert x_or_y(13, [1,2], [3,4]) == [1,2]

    def test_non_prime_returns_y_with_different_types(self):
        assert x_or_y(15, "hello", "world") == "world"
        assert x_or_y(9, 7.89, 9.10) == 9.10
        assert x_or_y(10, (1,2), (3,4)) == (3,4)

    def test_type_handling(self):
        assert x_or_y(7, 34.5, 12) == 34.5
        assert x_or_y(7, 34, 12.5) == 34
        assert x_or_y(15, "string", 5) == 5
        assert x_or_y(15, 5, "string") == "string"

    def test_large_numbers(self):
        assert x_or_y(1000000007, 1, 2) == 1 # A large prime
        assert x_or_y(1000000000, 1, 2) == 2 # A large non-prime

    def test_mixed_types(self):
        assert x_or_y(7, 1, "a") == 1
        assert x_or_y(15, "a", 1) == 1
        assert x_or_y(2, 1.0, True) == 1.0
        assert x_or_y(3, True, 1.0) == True