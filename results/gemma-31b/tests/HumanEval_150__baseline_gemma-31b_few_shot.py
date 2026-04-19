
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

import pytest

def test_x_or_y_prime():
    """Test that x is returned when n is a prime number."""
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(2, 10, 20) == 10
    assert x_or_y(3, 100, 200) == 100
    assert x_or_y(13, "prime", "not prime") == "prime"
    assert x_or_y(101, True, False) == True

def test_x_or_y_not_prime():
    """Test that y is returned when n is a composite number."""
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(4, 10, 20) == 20
    assert x_or_y(9, 100, 200) == 200
    assert x_or_y(100, "prime", "not prime") == "not prime"

def test_x_or_y_boundary_cases():
    """Test boundary cases for primality (n < 2)."""
    # 1 is not prime
    assert x_or_y(1, "x", "y") == "y"
    # 0 is not prime
    assert x_or_y(0, "x", "y") == "y"
    # Negative numbers are not prime
    assert x_or_y(-7, "x", "y") == "y"
    assert x_or_y(-2, "x", "y") == "y"

def test_x_or_y_return_types():
    """Test that the function returns the exact object passed as x or y regardless of type."""
    complex_obj = {"key": "value"}
    list_obj = [1, 2, 3]
    
    # n is prime, return x (complex_obj)
    assert x_or_y(11, complex_obj, list_obj) is complex_obj
    # n is not prime, return y (list_obj)
    assert x_or_y(12, complex_obj, list_obj) is list_obj