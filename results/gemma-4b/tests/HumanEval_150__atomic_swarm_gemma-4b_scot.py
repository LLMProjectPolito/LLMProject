
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

import pytest
import math

import pytest

def test_basic():
    assert x_or_y(7, 34, 12) == 34

import pytest

def test_edge_zero():
    assert x_or_y(0, 10, 20) == 20

import pytest

def test_x_or_y_negative_n():
    assert x_or_y(-7, 34, 12) == 12