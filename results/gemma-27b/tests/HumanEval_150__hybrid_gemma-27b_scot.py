
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

def test_negative_input():
    assert x_or_y(-5, 10, 20) == 20

def test_zero_input():
    assert x_or_y(0, 10, 20) == 20

def test_one_input():
    assert x_or_y(1, 10, 20) == 20

def test_two_input():
    assert x_or_y(2, 10, 20) == 10

def test_small_prime():
    assert x_or_y(7, 34, 12) == 34

def test_small_composite():
    assert x_or_y(4, 8, 5) == 5

def test_larger_prime():
    assert x_or_y(29, 100, 50) == 100

def test_larger_composite():
    assert x_or_y(30, 100, 50) == 50