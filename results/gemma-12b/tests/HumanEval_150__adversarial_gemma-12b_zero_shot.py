
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
        assert x_or_y(2, 100, 200) == 100
        assert x_or_y(5, 50, 60) == 50
        assert x_or_y(11, 1, 2) == 1

    def test_non_prime_number(self):
        assert x_or_y(15, 8, 5) == 5
        assert x_or_y(4, 20, 30) == 30
        assert x_or_y(6, 10, 20) == 20
        assert x_or_y(9, 5, 10) == 10
        assert x_or_y(1, 10, 20) == 20

    def test_edge_cases(self):
        assert x_or_y(0, 1, 2) == 2
        assert x_or_y(-1, 5, 10) == 10
        assert x_or_y(2.5, 1, 2) == 2 #handles non-integer input
        assert x_or_y(3.0, 1, 2) == 1 #handles float input that is prime
        assert x_or_y(4.0, 1, 2) == 2 #handles float input that is not prime

    def test_negative_numbers(self):
        assert x_or_y(-7, 1, 2) == 2
        assert x_or_y(-2, 1, 2) == 2
        assert x_or_y(-5, 1, 2) == 2

    def test_large_numbers(self):
        assert x_or_y(997, 100, 200) == 100
        assert x_or_y(1000, 100, 200) == 200