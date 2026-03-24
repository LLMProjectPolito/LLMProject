
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

import pytest

def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    if n <= 1:
        return y
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return y
    return x

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

class TestXorY:
    def test_prime_number(self):
        assert x_or_y(7, 34, 12) == 34
        assert x_or_y(2, 10, 20) == 10
        assert x_or_y(3, 5, 8) == 5
        assert x_or_y(5, 1, 2) == 1
        assert x_or_y(11, 99, 1) == 99
        assert x_or_y(13, 100, 0) == 100
        assert x_or_y(17, 50, 25) == 50
        assert x_or_y(19, 7, 3) == 7

    def test_non_prime_number(self):
        assert x_or_y(15, 8, 5) == 5
        assert x_or_y(4, 1, 2) == 2
        assert x_or_y(6, 10, 5) == 5
        assert x_or_y(8, 20, 10) == 10
        assert x_or_y(9, 30, 15) == 15
        assert x_or_y(10, 40, 20) == 20
        assert x_or_y(12, 60, 30) == 30
        assert x_or_y(14, 70, 35) == 35
        assert x_or_y(16, 80, 40) == 40

    def test_edge_cases(self):
        assert x_or_y(1, 10, 20) == 20  # 1 is not prime
        assert x_or_y(0, 10, 20) == 20  # 0 is not prime
        assert x_or_y(-1, 10, 20) == 20 # Negative numbers are not prime
        assert x_or_y(2, 0, 0) == 0
        assert x_or_y(3, 0, 0) == 0
        assert x_or_y(4, 0, 0) == 0

    def test_large_prime(self):
        assert x_or_y(7919, 1000, 1) == 1000

    def test_large_non_prime(self):
        assert x_or_y(7920, 1000, 1) == 1

    def test_x_and_y_are_same(self):
        assert x_or_y(7, 5, 5) == 5
        assert x_or_y(15, 5, 5) == 5