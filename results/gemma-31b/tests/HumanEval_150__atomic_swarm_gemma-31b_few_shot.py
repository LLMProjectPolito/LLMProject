
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

import pytest
import math

def test_x_or_y():
    assert x_or_y(7, 34, 12) == 34

def test_x_or_y_non_prime_edge():
    assert x_or_y(1, 10, 20) == 20

def test_x_or_y_boundary_one():
    assert x_or_y(1, 10, 20) == 20