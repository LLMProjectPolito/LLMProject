
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
        assert x_or_y(11, 100, 200) == 100
        assert x_or_y(13, 50, 60) == 50
        assert x_or_y(17, 77, 88) == 77
        assert x_or_y(19, 99, 100) == 99
        assert x_or_y(23, 1, 0) == 1
        assert x_or_y(29, -1, 0) == -1

    def test_non_prime_number(self):
        assert x_or_y(15, 8, 5) == 5
        assert x_or_y(4, 1, 2) == 2
        assert x_or_y(6, 3, 4) == 4
        assert x_or_y(8, 5, 6) == 6
        assert x_or_y(9, 7, 8) == 8
        assert x_or_y(10, 10, 11) == 11
        assert x_or_y(12, 12, 13) == 13
        assert x_or_y(14, 14, 15) == 15
        assert x_or_y(16, 16, 17) == 17
        assert x_or_y(18, 18, 19) == 19
        assert x_or_y(20, 20, 21) == 21

    def test_edge_cases(self):
        assert x_or_y(1, 10, 20) == 20
        assert x_or_y(0, 10, 20) == 20
        assert x_or_y(-1, 10, 20) == 20
        assert x_or_y(-7, 10, 20) == 20
        assert x_or_y(2, 0, 0) == 0
        assert x_or_y(4, 0, 0) == 0

    def test_large_numbers(self):
        assert x_or_y(1000000007, 1, 2) == 1  # Large prime
        assert x_or_y(1000000008, 1, 2) == 2  # Large non-prime

    def test_negative_numbers_x_y(self):
        assert x_or_y(7, -34, -12) == -34
        assert x_or_y(15, -8, -5) == -5
        assert x_or_y(2, -10, -20) == -10
        assert x_or_y(4, -1, -2) == -2