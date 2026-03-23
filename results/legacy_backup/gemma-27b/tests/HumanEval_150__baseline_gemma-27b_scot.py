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
    assert x_or_y(5, 1, 0) == 1

def test_not_prime_number():
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(4, 1, 2) == 2
    assert x_or_y(9, 3, 4) == 4

def test_one():
    assert x_or_y(1, 10, 20) == 20

def test_two():
    assert x_or_y(2, 5, 6) == 5

def test_negative_number():
    assert x_or_y(-5, 7, 8) == 8
    assert x_or_y(-1, 1, 2) == 2

def test_zero():
    assert x_or_y(0, 1, 2) == 2

def test_large_prime():
    assert x_or_y(7919, 1000, 2000) == 1000

def test_large_not_prime():
    assert x_or_y(7920, 1000, 2000) == 2000