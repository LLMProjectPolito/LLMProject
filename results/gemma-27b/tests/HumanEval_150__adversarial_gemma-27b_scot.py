
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
    if n < 2:
        return y
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return y
    return x

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def test_prime_returns_x():
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(3, "hello", 10) == "hello"
    assert x_or_y(5, 1.5, 2.5) == 1.5
    assert x_or_y(11, True, False) == True

def test_composite_returns_y():
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(4, "world", "!") == "!"
    assert x_or_y(6, 3.14, 2.71) == 2.71
    assert x_or_y(9, 1, 0) == 0

def test_less_than_two_returns_y():
    assert x_or_y(0, 10, 20) == 20
    assert x_or_y(1, "a", "b") == "b"
    assert x_or_y(-5, 5.0, 6.0) == 6.0

def test_two_returns_x():
    assert x_or_y(2, 100, 200) == 100
    assert x_or_y(2, "x", "y") == "x"
    assert x_or_y(2, 1, 2) == 1

def test_large_prime_returns_x():
    assert x_or_y(7919, "large_x", "large_y") == "large_x"

def test_large_composite_returns_y():
    assert x_or_y(7920, "large_x", "large_y") == "large_y"

def test_x_and_y_different_types():
    assert x_or_y(13, 10, "string") == 10
    assert x_or_y(16, 5, [1, 2, 3]) == [1, 2, 3]