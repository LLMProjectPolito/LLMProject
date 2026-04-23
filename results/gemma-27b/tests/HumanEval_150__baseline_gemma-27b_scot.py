
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

def test_prime_number():
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(11, 100, 200) == 100
    assert x_or_y(13, 5, 6) == 5

def test_composite_number():
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(4, 1, 2) == 2
    assert x_or_y(21, 7, 8) == 8

def test_one():
    assert x_or_y(1, 10, 20) == 20

def test_two():
    assert x_or_y(2, 30, 40) == 30

def test_negative_number():
    assert x_or_y(-5, 50, 60) == 60
    assert x_or_y(-10, 1, 2) == 2

def test_zero():
    assert x_or_y(0, 7, 8) == 8