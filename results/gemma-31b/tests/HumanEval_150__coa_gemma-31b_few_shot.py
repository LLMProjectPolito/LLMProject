
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
def test_x_or_y_boundary_smallest_prime():
    # 2 is the smallest prime number
    assert x_or_y(2, 10, 20) == 10

def test_x_or_y_boundary_below_prime():
    # 1 is not a prime number
    assert x_or_y(1, 10, 20) == 20

def test_x_or_y_boundary_zero_negative():
    # 0 and negative numbers are not prime
    assert x_or_y(0, 10, 20) == 20
    assert x_or_y(-7, 10, 20) == 20

# Focus: Logic Branches
def test_x_or_y_prime_branch():
    # Test branch where n is a prime number
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(2, 100, 200) == 100
    assert x_or_y(13, 50, 60) == 50

def test_x_or_y_non_prime_branch():
    # Test branch where n is not a prime number
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(1, 10, 20) == 20
    assert x_or_y(4, 100, 200) == 200

# Focus: Type Scenarios
def test_x_or_y_string_types():
    assert x_or_y(7, "prime_val", "not_prime_val") == "prime_val"
    assert x_or_y(8, "prime_val", "not_prime_val") == "not_prime_val"

def test_x_or_y_float_types():
    assert x_or_y(11, 1.1, 2.2) == 1.1
    assert x_or_y(12, 1.1, 2.2) == 2.2

def test_x_or_y_collection_types():
    assert x_or_y(13, [1, 2], {"key": "val"}) == [1, 2]
    assert x_or_y(14, [1, 2], {"key": "val"}) == {"key": "val"}