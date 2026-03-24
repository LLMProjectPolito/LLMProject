
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

class TestXorY:

    def test_prime_number(self):
        assert x_or_y(7, 34, 12) == 34
        assert x_or_y(2, 100, 200) == 100
        assert x_or_y(5, 5, 10) == 5
        assert x_or_y(11, 111, 222) == 111

    def test_non_prime_number(self):
        assert x_or_y(15, 8, 5) == 5
        assert x_or_y(4, 1, 2) == 2
        assert x_or_y(9, 10, 20) == 20
        assert x_or_y(6, 30, 40) == 40

    def test_edge_cases(self):
        assert x_or_y(0, 1, 2) == 2  # 0 is not prime
        assert x_or_y(1, 1, 2) == 2  # 1 is not prime
        assert x_or_y(2, 2, 2) == 2 # 2 is prime
        assert x_or_y(-5, 10, 20) == 20 # Negative numbers are not prime

    def test_same_values(self):
        assert x_or_y(7, 7, 7) == 7
        assert x_or_y(4, 4, 4) == 4

    def test_large_prime(self):
        assert x_or_y(101, 1010, 2020) == 1010

    def test_large_non_prime(self):
        assert x_or_y(100, 1000, 2000) == 2000