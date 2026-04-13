
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

import pytest
import math


# Focus: Boundary Values
import pytest

def test_x_or_y_small_prime():
    assert x_or_y(7, 34, 12) == 34

def test_x_or_y_large_non_prime():
    assert x_or_y(15, 8, 5) == 5

def test_x_or_y_zero():
    assert x_or_y(0, 34, 12) == 12

# Focus: Type Scenarios
import pytest

def test_x_or_y_non_prime():
    assert x_or_y(8, 34, 12) == 12

def test_x_or_y_prime():
    assert x_or_y(7, 34, 12) == 34

def test_x_or_y_another_non_prime():
    assert x_or_y(9, 8, 5) == 5

# Focus: Logic Branches
import pytest

def test_x_or_y_prime():
    assert x_or_y(7, 34, 12) == 34

def test_x_or_y_not_prime():
    assert x_or_y(15, 8, 5) == 5

def test_x_or_y_small_prime():
    assert x_or_y(2, 34, 12) == 34