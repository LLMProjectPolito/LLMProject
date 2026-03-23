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
    def test_prime_n_returns_x(self):
        assert x_or_y(7, 34, 12) == 34
        assert x_or_y(2, 100, 200) == 100
        assert x_or_y(5, 5, 10) == 5
        assert x_or_y(11, "a", "b") == "a"

    def test_non_prime_n_returns_y(self):
        assert x_or_y(15, 8, 5) == 5
        assert x_or_y(4, 1, 2) == 2
        assert x_or_y(6, "x", "y") == "y"
        assert x_or_y(9, 10, 20) == 20

    def test_n_is_1_returns_y(self):
        assert x_or_y(1, 5, 10) == 10

    def test_n_is_0_returns_y(self):
        assert x_or_y(0, 1, 2) == 2

    def test_n_is_negative_returns_y(self):
        assert x_or_y(-5, 1, 2) == 2

    def test_x_and_y_are_same(self):
        assert x_or_y(7, 5, 5) == 5
        assert x_or_y(10, 5, 5) == 5

    def test_mixed_data_types(self):
        assert x_or_y(3, 10, "hello") == 10
        assert x_or_y(4, "world", 20) == 20