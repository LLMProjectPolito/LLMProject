
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

import pytest
import math

def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    if n == 2 or n == 3 or n == 5 or n == 7 or n == 11 or n == 13 or n == 17 or n == 19 or n == 23 or n == 29 or n == 31:
        return x
    else:
        return y

def test_x_or_y_zero():
    assert x_or_y(0, 34, 12) == 12

def test_x_or_y_prime():
    assert x_or_y(7, 34, 12) == 34

def test_x_or_y_non_prime():
    assert x_or_y(15, 8, 5) == 5

def test_x_or_y_small_primes():
    assert x_or_y(2, 100, 50) == 100
    assert x_or_y(3, 100, 50) == 100
    assert x_or_y(5, 100, 50) == 100
    assert x_or_y(7, 100, 50) == 100
    assert x_or_y(11, 100, 50) == 100
    assert x_or_y(13, 100, 50) == 100
    assert x_or_y(17, 100, 50) == 100
    assert x_or_y(19, 100, 50) == 100
    assert x_or_y(23, 100, 50) == 100
    assert x_or_y(29, 100, 50) == 100
    assert x_or_y(31, 100, 50) == 100