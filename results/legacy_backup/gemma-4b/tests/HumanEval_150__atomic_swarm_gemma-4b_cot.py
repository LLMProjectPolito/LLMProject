import pytest
import math

def test_basic():
    assert x_or_y(7, 34, 12) == 34

import pytest

def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    if n == 1:
        return y
    for i in range(2, int(n**0.5) + 1):
        if (n % i) == 0:
            return y
    return x

def test_edge_case_one():
    assert x_or_y(1, 34, 12) == 12

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

def test_x_or_y_non_prime():
    assert x_or_y(6, 34, 12) == 12