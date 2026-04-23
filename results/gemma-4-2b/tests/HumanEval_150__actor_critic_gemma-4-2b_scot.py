
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

def test_prime_number():
    assert x_or_y(2, 34, 12) == 34
    assert x_or_y(3, 34, 12) == 34
    assert x_or_y(5, 34, 12) == 34
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(11, 34, 12) == 34
    assert x_or_y(13, 34, 12) == 34

def test_non_prime_number():
    assert x_or_y(4, 34, 12) == 12
    assert x_or_y(6, 34, 12) == 12
    assert x_or_y(8, 34, 12) == 12
    assert x_or_y(9, 34, 12) == 12
    assert x_or_y(10, 34, 12) == 12
    assert x_or_y(12, 34, 12) == 12

def test_edge_cases():
    assert x_or_y(1, 34, 12) == 12
    assert x_or_y(2, 34, 12) == 34
    assert x_or_y(3, 34, 12) == 34
    assert x_or_y(4, 34, 12) == 12
    assert x_or_y(5, 34, 12) == 34

def test_equal_x_and_y():
    assert x_or_y(5, 34, 34) == 34
    assert x_or_y(11, 34, 34) == 34
    assert x_or_y(13, 34, 34) == 34

def test_different_x_and_y():
    assert x_or_y(5, 12, 34) == 34
    assert x_or_y(11, 12, 34) == 34
    assert x_or_y(13, 12, 34) == 34

def test_large_prime():
    assert x_or_y(1009, 34, 12) == 34

def test_large_non_prime():
    assert x_or_y(1000, 34, 12) == 12

def test_zero():
    assert x_or_y(0, 34, 12) == 12