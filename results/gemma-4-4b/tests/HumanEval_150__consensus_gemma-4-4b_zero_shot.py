
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
    if n > 1:
        for i in range(2, int(n**0.5) + 1):
            if (n % i) == 0:
                return y
        return x
    else:
        return y

class TestXOrY:
    def test_prime_number(self):
        assert x_or_y(7, 34, 12) == 34
        assert x_or_y(13, 5, 2) == 5
        assert x_or_y(2, 10, 5) == 10
        assert x_or_y(3, 10, 5) == 10
        assert x_or_y(5, 20, 10) == 20
        assert x_or_y(17, 1, 100) == 1

    def test_not_prime_number(self):
        assert x_or_y(4, 34, 12) == 12
        assert x_or_y(15, 8, 5) == 5
        assert x_or_y(6, 10, 5) == 5
        assert x_or_y(8, 20, 10) == 10
        assert x_or_y(9, 1, 100) == 100
        assert x_or_y(10, 10, 5) == 5
        assert x_or_y(12, 1, 100) == 100

    def test_edge_cases(self):
        assert x_or_y(1, 10, 5) == 5
        assert x_or_y(0, 10, 5) == 5
        assert x_or_y(2, 10, 5) == 10
        assert x_or_y(3, 10, 5) == 10
        assert x_or_y(5, 10, 5) == 10
        assert x_or_y(11, 10, 5) == 10
        assert x_or_y(1, 1, 1) == 1
        assert x_or_y(2, 1, 1) == 1
        assert x_or_y(3, 1, 1) == 1
        assert x_or_y(4, 1, 1) == 1
        assert x_or_y(5, 1, 1) == 1
        assert x_or_y(6, 1, 1) == 1
    
    def test_large_numbers(self):
        assert x_or_y(7919, 1000, 500) == 1000
        assert x_or_y(1000000007, 1, 0) == 1
        assert x_or_y(1000000000, 1, 0) == 0