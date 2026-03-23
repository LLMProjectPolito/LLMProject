import pytest
import math


# Focus: Boundary Values
import pytest

def test_special_factorial_boundary_zero():
    """Test the boundary value of n = 1."""
    assert special_factorial(1) == 1

def test_special_factorial_boundary_two():
    """Test the boundary value of n = 2."""
    assert special_factorial(2) == 2

def test_special_factorial_boundary_three():
    """Test the boundary value of n = 3."""
    assert special_factorial(3) == 12

# Focus: Error Handling
import pytest

def test_negative_input():
    """Test that a negative input raises a ValueError."""
    with pytest.raises(ValueError):
        special_factorial(-1)

def test_zero_input():
    """Test that a zero input raises a ValueError."""
    with pytest.raises(ValueError):
        special_factorial(0)

def test_invalid_input_type():
    """Test that a non-integer input raises a TypeError."""
    with pytest.raises(TypeError):
        special_factorial("abc")

# Focus: Logic Branches
def test_special_factorial_positive_n():
    """Test with a positive integer n."""
    assert special_factorial(4) == 288

def test_special_factorial_n_equals_1():
    """Test when n is 1."""
    assert special_factorial(1) == 1

def test_special_factorial_n_equals_2():
    """Test when n is 2."""
    assert special_factorial(2) == 2