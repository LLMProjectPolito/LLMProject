
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

import pytest

def is_prime(n):
    """Helper function to check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
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

    def test_non_prime_returns_y(self):
        assert x_or_y(15, 8, 5) == 5
        assert x_or_y(4, 1, 2) == 2
        assert x_or_y(6, 10, 20) == 20

    def test_negative_input(self):
        assert x_or_y(-5, 10, 5) == 5  # Negative numbers are treated as non-prime by is_prime. Consider if this is the desired behavior.

    def test_is_prime_negative_zero_one(self):
        assert not is_prime(1)
        assert not is_prime(0)
        assert not is_prime(-1)

    def test_large_prime(self):
        assert x_or_y(101, 1000, 500) == 1000

    def test_large_non_prime(self):
        assert x_or_y(100, 1000, 500) == 500

    def test_x_equals_y(self):
        assert x_or_y(7, 5, 5) == 5

    def test_zero_input(self):
        assert x_or_y(0, 10, 5) == 5

    def test_one_input(self):
        assert x_or_y(1, 10, 5) == 5

    def test_non_integer_input(self):
        # The function doesn't explicitly handle non-integer inputs.
        # This test checks the behavior with float inputs.
        assert x_or_y(2.0, 10, 5) == 10
        assert x_or_y(2.5, 10, 5) == 5