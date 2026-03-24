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
    def test_prime_n(self):
        assert x_or_y(7, 34, 12) == 34
        assert x_or_y(2, 100, 200) == 100
        assert x_or_y(11, 5, 10) == 5
        assert x_or_y(13, "a", "b") == "a"

    def test_non_prime_n(self):
        assert x_or_y(15, 8, 5) == 5
        assert x_or_y(4, 1, 2) == 2
        assert x_or_y(9, "x", "y") == "y"
        assert x_or_y(1, 10, 20) == 20
        assert x_or_y(0, 5, 10) == 10

    def test_negative_n(self):
        assert x_or_y(-5, 1, 2) == 2
        assert x_or_y(-7, 3, 4) == 4

    def test_zero_x_y(self):
        assert x_or_y(5, 0, 0) == 0
        assert x_or_y(4, 0, 0) == 0

    def test_mixed_types(self):
        assert x_or_y(7, 1, "hello") == 1
        assert x_or_y(8, "world", 2) == 2