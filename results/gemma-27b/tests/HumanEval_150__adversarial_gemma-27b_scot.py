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
    assert x_or_y(4, "world", "test") == "test"
    assert x_or_y(6, 10.0, 20.0) == 20.0
    assert x_or_y(9, False, True) == True

def test_less_than_two_returns_y():
    assert x_or_y(0, 1, 2) == 2
    assert x_or_y(1, 3, 4) == 4
    assert x_or_y(-5, "a", "b") == "b"

def test_two_returns_x():
    assert x_or_y(2, 5, 6) == 5
    assert x_or_y(2, 7.7, 8.8) == 7.7
    assert x_or_y(2, True, False) == True

def test_large_prime_returns_x():
    assert x_or_y(7919, 100, 200) == 100
    assert x_or_y(101, "large", "small") == "large"

def test_large_composite_returns_y():
    assert x_or_y(7920, 100, 200) == 200
    assert x_or_y(100, "large", "small") == "small"

def test_x_and_y_different_types():
    assert x_or_y(7, 10, "hello") == 10
    assert x_or_y(15, "world", 5) == 5
    assert x_or_y(2, 1.0, True) == 1.0
    assert x_or_y(4, False, 1) == 1