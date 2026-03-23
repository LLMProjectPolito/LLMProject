import pytest

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

def test_prime_x():
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(11, 5, 2) == 5
    assert x_or_y(13, 100, 50) == 100

def test_non_prime_y():
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(20, 10, 200) == 200
    assert x_or_y(9, 7, 3) == 3

def test_n_equals_1():
    assert x_or_y(1, 34, 12) == 12

def test_n_equals_2():
    assert x_or_y(2, 34, 12) == 34

def test_x_equals_y():
    assert x_or_y(4, 10, 10) == 10
    assert x_or_y(9, 5, 5) == 5

def test_large_prime():
    assert x_or_y(997, 1000, 500) == 1000

def test_large_non_prime():
    assert x_or_y(998, 1000, 500) == 500