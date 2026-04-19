
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
def test_special_factorial_boundary_min():
    # Minimum valid input according to n > 0
    assert special_factorial(1) == 1

def test_special_factorial_boundary_small():
    # Smallest value that involves a product of multiple factorials
    assert special_factorial(2) == 2

def test_special_factorial_boundary_three():
    # Next boundary step to ensure sequence accumulation
    assert special_factorial(3) == 12

# Focus: Type Scenarios
import pytest

def test_special_factorial_float():
    with pytest.raises(TypeError):
        special_factorial(4.5)

def test_special_factorial_string():
    with pytest.raises(TypeError):
        special_factorial("4")

def test_special_factorial_none():
    with pytest.raises(TypeError):
        special_factorial(None)

# Focus: Logic Branches
import pytest

def test_special_factorial_boundary():
    # Test the smallest valid input (n=1)
    assert special_factorial(1) == 1

def test_special_factorial_small_branch():
    # Test the first case where the product loop runs more than once (n=2)
    # 2! * 1! = 2 * 1 = 2
    assert special_factorial(2) == 2

def test_special_factorial_general_branch():
    # Test a standard case to ensure the multiplicative logic holds for n > 2
    # 4! * 3! * 2! * 1! = 24 * 6 * 2 * 1 = 288
    assert special_factorial(4) == 288