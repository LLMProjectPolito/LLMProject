
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

def test_x_or_y_boundary_smallest_prime():
    # 2 is the smallest prime number
    assert x_or_y(2, 10, 20) == 10

def test_x_or_y_boundary_one():
    # 1 is not a prime number
    assert x_or_y(1, 10, 20) == 20

def test_x_or_y_boundary_zero():
    # 0 is not a prime number
    assert x_or_y(0, 10, 20) == 20

# Focus: Logic Branches
def test_x_or_y_prime_branch():
    # Tests the branch where n is a prime number
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(2, 100, 200) == 100
    assert x_or_y(13, 5, 10) == 5

def test_x_or_y_non_prime_branch():
    # Tests the branch where n is not a prime number
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(1, 10, 20) == 20
    assert x_or_y(4, 50, 60) == 60

# Focus: Type Scenarios
import pytest

def test_x_or_y_non_int_xy():
    """Test that x and y can be of any type (strings, lists, etc.)"""
    assert x_or_y(7, "prime_val", "not_prime_val") == "prime_val"
    assert x_or_y(4, "prime_val", "not_prime_val") == "not_prime_val"
    assert x_or_y(7, [1, 2], {"a": 1}) == [1, 2]
    assert x_or_y(4, [1, 2], {"a": 1}) == {"a": 1}

def test_x_or_y_n_float():
    """Test that a float for n raises a TypeError as primality is for integers"""
    with pytest.raises(TypeError):
        x_or_y(7.5, 1, 2)

def test_x_or_y_n_string():
    """Test that a string for n raises a TypeError"""
    with pytest.raises(TypeError):
        x_or_y("7", 1, 2)