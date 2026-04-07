
def special_factorial(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
    """

import pytest
import math


# Focus: Boundary Values
def test_special_factorial_boundary_zero():
    """Test special_factorial with n = 1 (boundary value)."""
    assert special_factorial(1) == 1

def test_special_factorial_boundary_two():
    """Test special_factorial with n = 2 (boundary value)."""
    assert special_factorial(2) == 2

def test_special_factorial_boundary_three():
    """Test special_factorial with n = 3 (boundary value)."""
    assert special_factorial(3) == 12

# Focus: Error Handling
def test_special_factorial_negative_input():
    """Test that a ValueError is raised when a negative integer is input."""
    import pytest
    with pytest.raises(ValueError):
        special_factorial(-1)

def test_special_factorial_zero_input():
    """Test that a ValueError is raised when zero is input."""
    import pytest
    with pytest.raises(ValueError):
        special_factorial(0)

def test_special_factorial_non_integer_input():
    """Test that a TypeError is raised when a non-integer is input."""
    import pytest
    with pytest.raises(TypeError):
        special_factorial(2.5)

# Focus: Logic Branches
def test_special_factorial_positive_n():
    assert special_factorial(4) == 288
    assert special_factorial(5) == 34560
    assert special_factorial(1) == 1
    assert special_factorial(2) == 2
    assert special_factorial(3) == 12