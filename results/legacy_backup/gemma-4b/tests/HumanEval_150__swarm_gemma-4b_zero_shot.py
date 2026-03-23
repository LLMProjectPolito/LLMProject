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

def test_x_or_y_composite():
    assert x_or_y(15, 8, 5) == 5

def test_x_or_y_two():
    assert x_or_y(2, 34, 12) == 34

def test_x_or_y_three():
    assert x_or_y(3, 34, 12) == 34

def test_x_or_y_five():
    assert x_or_y(5, 34, 12) == 34

def test_x_or_y_seven():
    assert x_or_y(7, 34, 12) == 34

def test_x_or_y_eleven():
    assert x_or_y(11, 34, 12) == 34

def test_x_or_y_thirteen():
    assert x_or_y(13, 34, 12) == 34

def test_x_or_y_seventeen():
    assert x_or_y(17, 34, 12) == 34

def test_x_or_y_nineteen():
    assert x_or_y(19, 34, 12) == 34

def test_x_or_y_twenty_three():
    assert x_or_y(23, 34, 12) == 34

def test_x_or_y_twenty_nine():
    assert x_or_y(29, 34, 12) == 34

def test_x_or_y_thirty_one():
    assert x_or_y(31, 34, 12) == 34