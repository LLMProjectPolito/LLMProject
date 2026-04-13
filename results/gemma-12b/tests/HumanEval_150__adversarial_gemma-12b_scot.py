
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
    def test_prime_number(self):
        assert x_or_y(7, 34, 12) == 34

    def test_non_prime_number(self):
        assert x_or_y(15, 8, 5) == 5

    def test_n_is_zero(self):
        assert x_or_y(0, 10, 20) == 20

    def test_n_is_one(self):
        assert x_or_y(1, 10, 20) == 20

    def test_n_is_negative(self):
        assert x_or_y(-5, 10, 20) == 20

    def test_x_is_string(self):
        assert x_or_y(7, "hello", 12) == "hello"

    def test_y_is_string(self):
        assert x_or_y(15, 8, "world") == "world"

    def test_x_and_y_are_strings(self):
        assert x_or_y(7, "hello", "world") == "hello"

    def test_small_prime(self):
        assert x_or_y(2, 1, 2) == 1

    def test_small_non_prime(self):
        assert x_or_y(4, 1, 2) == 2

    def test_larger_prime(self):
        assert x_or_y(11, 100, 200) == 100

    def test_larger_non_prime(self):
        assert x_or_y(12, 100, 200) == 200