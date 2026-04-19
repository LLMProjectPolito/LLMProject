
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

import pytest
import math

def test_x_or_y_with_one():
    # 1 is not a prime number, so it should return y
    assert x_or_y(1, 100, 200) == 200

def test_x_or_y_edge_case_one():
    assert x_or_y(1, "prime", "not prime") == "not prime"