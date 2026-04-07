
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
    assert x_or_y(11, 5, 8) == 5
    assert x_or_y(2, 10, 20) == 10

def test_composite_number():
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(4, 1, 2) == 2
    assert x_or_y(9, 100, 200) == 200

def test_number_one():
    assert x_or_y(1, 5, 10) == 10

def test_number_two():
    assert x_or_y(2, 10, 20) == 10

def test_different_x_y():
    assert x_or_y(13, "hello", "world") == "hello"
    assert x_or_y(6, True, False) == False

def test_large_prime():
    assert x_or_y(7919, 1, 0) == 1

def test_large_composite():
    assert x_or_y(10000, 1, 0) == 0