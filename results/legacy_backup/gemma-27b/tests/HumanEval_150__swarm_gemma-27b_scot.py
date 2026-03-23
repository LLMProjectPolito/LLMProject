import pytest
import math

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

def test_x_or_y_with_one():
    assert x_or_y(1, 10, 20) == 20

def test_x_or_y_with_prime():
    assert x_or_y(7, 34, 12) == 34

def test_x_or_y_with_composite():
    assert x_or_y(15, 8, 5) == 5