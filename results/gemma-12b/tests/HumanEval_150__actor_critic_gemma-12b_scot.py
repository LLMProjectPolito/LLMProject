
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

import pytest

def is_prime(n):
    """Helper function to check if a number is prime.
    Returns False for negative numbers.
    """
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
        assert x_or_y(2, 10, 5) == 10
        assert x_or_y(3, 100, 20) == 100
        assert x_or_y(5, -5, 0) == -5

    def test_non_prime_returns_y(self):
        assert x_or_y(15, 8, 5) == 5
        assert x_or_y(4, 1, 2) == 2
        assert x_or_y(6, 10, 20) == 20
        assert x_or_y(8, 100, 200) == 200
        assert x_or_y(9, 5, 10) == 10

    def test_n_is_zero(self):
        assert x_or_y(0, 1, 2) == 2

    def test_n_is_one(self):
        assert x_or_y(1, 5, 10) == 10

    def test_n_is_negative(self):
        assert x_or_y(-5, 1, 2) == 2

    def test_x_is_negative(self):
        assert x_or_y(7, -34, 12) == -34

    def test_y_is_negative(self):
        assert x_or_y(15, 8, -5) == -5

    def test_x_is_zero(self):
        assert x_or_y(7, 0, 12) == 0

    def test_y_is_zero(self):
        assert x_or_y(15, 8, 0) == 0

    def test_x_and_y_are_zero(self):
        assert x_or_y(7, 0, 0) == 0
        assert x_or_y(8, 0, 0) == 0

    def test_large_prime(self):
        assert x_or_y(101, 1000, 2000) == 1000

    def test_large_non_prime(self):
        assert x_or_y(100, 1000, 2000) == 2000

    def test_identical_x_and_y(self):
        assert x_or_y(7, 5, 5) == 5
        assert x_or_y(8, 5, 5) == 5

    def test_both_negative(self):
        assert x_or_y(7, -5, -10) == -5
        assert x_or_y(8, -5, -10) == -10

    def test_max_int_prime(self):
        assert x_or_y(2147483647, 1, 2) == 1

    def test_max_int_non_prime(self):
        assert x_or_y(2147483646, 1, 2) == 2