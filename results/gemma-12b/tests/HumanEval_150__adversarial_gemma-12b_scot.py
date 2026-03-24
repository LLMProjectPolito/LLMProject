
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

import pytest

def is_prime(n):
    """Helper function to determine if a number is prime."""
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
    def test_prime_returns_x(self):
        assert x_or_y(7, 34, 12) == 34
        assert x_or_y(2, 10, 20) == 10
        assert x_or_y(5, "hello", "world") == "hello"

    def test_non_prime_returns_y(self):
        assert x_or_y(15, 8, 5) == 5
        assert x_or_y(4, 1, 2) == 2
        assert x_or_y(9, "a", "b") == "b"

    def test_n_is_zero(self):
        assert x_or_y(0, 10, 20) == 20

    def test_n_is_one(self):
        assert x_or_y(1, 5, 10) == 10

    def test_n_is_negative(self):
        assert x_or_y(-5, 1, 2) == 2

    def test_x_and_y_different_types(self):
        assert x_or_y(7, "hello", 123) == "hello"
        assert x_or_y(8, 123, "world") == "world"

    def test_large_prime(self):
        assert x_or_y(101, "big_x", "small_y") == "big_x"

    def test_large_non_prime(self):
        assert x_or_y(100, "small_x", "big_y") == "big_y"