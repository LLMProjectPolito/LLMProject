
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

def test_x_or_y_boundary_one():
    # 1 is not a prime number
    assert x_or_y(1, 10, 20) == 20

def test_x_or_y_boundary_zero():
    # 0 is not a prime number
    assert x_or_y(0, 10, 20) == 20

# Focus: Logic Branches
def test_x_or_y_prime():
    # Branch: n is a prime number
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(2, 100, 200) == 100

def test_x_or_y_not_prime():
    # Branch: n is not a prime number
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(1, 100, 200) == 200
    assert x_or_y(4, 100, 200) == 200

# Focus: Type Scenarios
import pytest

def test_x_or_y_non_integer_returns():
    # Testing that x and y can be of any type (strings, lists, etc.)
    assert x_or_y(7, "prime", "not prime") == "prime"
    assert x_or_y(10, "prime", "not prime") == "not prime"
    assert x_or_y(7, [1, 2], [3, 4]) == [1, 2]
    assert x_or_y(10, [1, 2], [3, 4]) == [3, 4]

def test_x_or_y_float_n():
    # Testing n as a float to see if the function handles numeric types correctly
    assert x_or_y(7.0, 10, 20) == 10
    assert x_or_y(8.0, 10, 20) == 20

def test_x_or_y_invalid_n_type():
    # Testing n as a non-numeric type to ensure it raises a TypeError
    with pytest.raises(TypeError):
        x_or_y("7", 10, 20)