
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
        assert x_or_y(3, 5, 1) == 5
        assert x_or_y(5, 100, 1) == 100
        assert x_or_y(11, 1, 2) == 1
        assert x_or_y(13, 99, 0) == 99
        assert x_or_y(17, -1, 1) == -1
        assert x_or_y(19, 0, 10) == 0

    def test_composite_number(self):
        assert x_or_y(15, 8, 5) == 5
        assert x_or_y(4, 1, 2) == 2
        assert x_or_y(6, 3, 4) == 4
        assert x_or_y(8, 5, 6) == 6
        assert x_or_y(9, 7, 8) == 8
        assert x_or_y(10, 11, 12) == 12
        assert x_or_y(12, 13, 14) == 14
        assert x_or_y(14, 15, 16) == 16

    def test_edge_cases(self):
        assert x_or_y(1, 10, 20) == 20
        assert x_or_y(0, 10, 20) == 20
        assert x_or_y(-1, 10, 20) == 20
        assert x_or_y(2, 0, 0) == 0
        assert x_or_y(1, 0, 0) == 0
        assert x_or_y(0, 0, 0) == 0

    def test_large_numbers(self):
        assert x_or_y(101, 1000, 1) == 1000  # Prime
        assert x_or_y(100, 1000, 1) == 1  # Composite
        assert x_or_y(997, 5, 10) == 5 #Prime
        assert x_or_y(999, 5, 10) == 10 #Composite

    def test_negative_numbers_x_y(self):
        assert x_or_y(7, -34, -12) == -34
        assert x_or_y(15, -8, -5) == -5
        assert x_or_y(2, -10, -20) == -10
        assert x_or_y(4, -1, -2) == -2