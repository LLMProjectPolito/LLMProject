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
        assert x_or_y(3, 5, 6) == 5
        assert x_or_y(5, 1, 2) == 1
        assert x_or_y(11, 100, 200) == 100
        assert x_or_y(13, 7, 8) == 7

    def test_composite_number(self):
        assert x_or_y(15, 8, 5) == 5
        assert x_or_y(4, 1, 2) == 2
        assert x_or_y(6, 3, 4) == 4
        assert x_or_y(8, 9, 10) == 10
        assert x_or_y(9, 11, 12) == 12
        assert x_or_y(10, 13, 14) == 14

    def test_edge_cases(self):
        assert x_or_y(1, 1, 2) == 2  # 1 is not prime
        assert x_or_y(0, 3, 4) == 4  # 0 is not prime
        assert x_or_y(-1, 5, 6) == 6 # Negative numbers are not prime
        assert x_or_y(2, 0, 0) == 0
        assert x_or_y(1, 0, 0) == 0

    def test_large_prime(self):
        assert x_or_y(7919, 100, 200) == 100

    def test_large_composite(self):
        assert x_or_y(7920, 300, 400) == 400

    def test_x_and_y_are_same(self):
        assert x_or_y(7, 5, 5) == 5
        assert x_or_y(15, 5, 5) == 5

    def test_is_prime_function(self):
        assert is_prime(2) == True
        assert is_prime(3) == True
        assert is_prime(5) == True
        assert is_prime(7) == True
        assert is_prime(11) == True
        assert is_prime(1) == False
        assert is_prime(4) == False
        assert is_prime(6) == False
        assert is_prime(8) == False
        assert is_prime(9) == False
        assert is_prime(10) == False