
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
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                return -1  # n is not prime
        return x
    else:
        return y

def test_x_or_y_positive():
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(15, 8, 5) == 5

def test_x_or_y_empty():
    assert x_or_y([]) == None

def test_x_or_y_prime():
    assert x_or_y(7, 7, 7) == 7
    assert x_or_y(11, 11, 11) == 11
    assert x_or_y(13, 13, 13) == 13
    assert x_or_y(17, 17, 17) == 17
    
def test_x_or_y_one():
    assert x_or_y(1, 1, 1) == 1
    
def test_x_or_y_two():
    assert x_or_y(2, 2, 2) == 2
    
def test_x_or_y_negative():
    assert x_or_y(-1, 1, 1) == 1
    
def test_x_or_y_zero():
    assert x_or_y(0, 1, 1) == 1
    
def test_x_or_y_large_prime():
    assert x_or_y(101, 101, 101) == 101
    
def test_x_or_y_large_non_prime():
    assert x_or_y(100, 100, 101) == 101
    
def test_x_or_y_large_prime_and_non_prime():
    assert x_or_y(1000000007, 1000000007, 1000000007) == 1000000007