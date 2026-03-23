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
        assert x_or_y(17, 70, 80) == 70
        assert x_or_y(19, 90, 100) == 90
        assert x_or_y(23, 110, 120) == 110
        assert x_or_y(29, 130, 140) == 130

    def test_non_prime_number(self):
        assert x_or_y(15, 8, 5) == 5
        assert x_or_y(4, 1, 2) == 2
        assert x_or_y(6, 3, 4) == 4
        assert x_or_y(8, 5, 6) == 6
        assert x_or_y(9, 7, 8) == 8
        assert x_or_y(10, 9, 10) == 10
        assert x_or_y(12, 11, 12) == 12
        assert x_or_y(14, 13, 14) == 14
        assert x_or_y(16, 15, 16) == 16
        assert x_or_y(18, 17, 18) == 18

    def test_edge_cases(self):
        assert x_or_y(1, 10, 20) == 20
        assert x_or_y(0, 10, 20) == 20
        assert x_or_y(-1, 10, 20) == 20
        assert x_or_y(2, 0, 0) == 0
        assert x_or_y(3, 0, 0) == 0
        assert x_or_y(4, 0, 0) == 0
        assert x_or_y(5, 0, 0) == 0

    def test_large_numbers(self):
        assert x_or_y(1000000007, 1, 2) == 1  # Prime
        assert x_or_y(1000000008, 1, 2) == 2  # Not prime
        assert x_or_y(999999999, 3, 4) == 4 # Not prime
        assert x_or_y(1000000009, 5, 6) == 5 # Prime

    def test_x_and_y_are_same(self):
        assert x_or_y(7, 5, 5) == 5
        assert x_or_y(15, 5, 5) == 5