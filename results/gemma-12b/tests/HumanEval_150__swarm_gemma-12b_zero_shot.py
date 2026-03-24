
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

import pytest
import math

def test_x_or_y_edge_case_n_equals_one():
    """Test when n is 1, which is not a prime number."""
    assert x_or_y(1, 34, 12) == 12

def test_x_or_y_n_is_one():
    assert x_or_y(1, 5, 10) == 10