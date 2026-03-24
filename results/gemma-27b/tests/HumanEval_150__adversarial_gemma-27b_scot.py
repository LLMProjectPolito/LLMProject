
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

def test_non_prime_number():
    assert x_or_y(15, 8, 5) == 5

def test_n_is_one():
    assert x_or_y(1, 10, 20) == 20

def test_n_is_zero():
    assert x_or_y(0, 30, 40) == 40

def test_n_is_negative():
    assert x_or_y(-5, 50, 60) == 60

def test_small_prime():
    assert x_or_y(2, 1, 2) == 1

def test_small_non_prime():
    assert x_or_y(4, 1, 2) == 2

def test_larger_prime():
    assert x_or_y(29, 100, 200) == 100

def test_larger_non_prime():
    assert x_or_y(30, 100, 200) == 200

def test_examples():
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(15, 8, 5) == 5