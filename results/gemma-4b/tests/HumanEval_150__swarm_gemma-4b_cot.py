import pytest
import math

def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    if n == 1:
        return y
    for i in range(2, int(n**0.5) + 1):
        if (n % i) == 0:
            return y
    return x

def test_x_or_y_one():
    assert x_or_y(1, 34, 12) == 12

def test_x_or_y_prime():
    assert x_or_y(7, 34, 12) == 34

def test_x_or_y_composite():
    assert x_or_y(15, 8, 5) == 5

def test_x_or_y_n_equals_2():
    assert x_or_y(2, 34, 12) == 34

def test_x_or_y_n_equals_3():
    assert x_or_y(3, 34, 12) == 34

def test_x_or_y_n_equals_4():
    assert x_or_y(4, 34, 12) == 12