
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

    For non-positive integers (n <= 0), the function returns y.

    Examples:
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(15, 8, 5) == 5
    
    """
    if n <= 1:
        return y
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return y
    return x

def test_prime():
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(11, 100, 200) == 100
    assert x_or_y(5, 1, 0) == 1
    assert x_or_y(7919, 1000, 2000) == 1000

def test_composite():
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(4, 1, 2) == 2
    assert x_or_y(9, 10, 20) == 20
    assert x_or_y(7920, 1000, 2000) == 2000

def test_zero():
    assert x_or_y(0, 1, 2) == 2

def test_one():
    assert x_or_y(1, 1, 2) == 2

def test_two():
    assert x_or_y(2, 1, 2) == 1

def test_negative():
    assert x_or_y(-5, 1, 2) == 2
    assert x_or_y(-1, 3, 4) == 4
    assert x_or_y(-7, 5, 6) == 6
    assert x_or_y(-11, 7, 8) == 8

def test_equal_values():
    assert x_or_y(7, 5, 5) == 5
    assert x_or_y(12, 5, 5) == 5
    assert x_or_y(7, 5, 5.0) == 5.0
    assert x_or_y(12, 5.0, 5) == 5.0

def test_large_composite():
    assert x_or_y(1000000, 1, 2) == 2

def test_large_prime():
    assert x_or_y(7919, 1000, 2000) == 1000