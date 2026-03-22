import pytest

def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    if n < 2:
        return y
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return y
    return x

def is_prime(n):
    if n < 2:
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
        assert x_or_y(13, 50, 75) == 50
        assert x_or_y(17, 10, 5) == 10
        assert x_or_y(19, 2, 4) == 2

    def test_composite_number(self):
        assert x_or_y(15, 8, 5) == 5
        assert x_or_y(4, 1, 2) == 2
        assert x_or_y(6, 10, 5) == 5
        assert x_or_y(8, 20, 10) == 10
        assert x_or_y(9, 30, 15) == 15
        assert x_or_y(10, 5, 10) == 10
        assert x_or_y(12, 100, 50) == 50
        assert x_or_y(14, 25, 12) == 12
        assert x_or_y(16, 1, 3) == 3

    def test_edge_cases(self):
        assert x_or_y(1, 10, 20) == 20
        assert x_or_y(0, 5, 10) == 10
        assert x_or_y(-1, 1, 2) == 2
        assert x_or_y(2, 0, 1) == 0
        assert x_or_y(3, 0, 1) == 0
        assert x_or_y(4, 0, 1) == 1

    def test_large_numbers(self):
        assert x_or_y(101, 1000, 500) == 1000
        assert x_or_y(100, 200, 100) == 100
        assert x_or_y(97, 10, 5) == 10
        assert x_or_y(99, 1, 2) == 2
        assert x_or_y(1000, 100, 50) == 50
        assert x_or_y(1001, 200, 100) == 200