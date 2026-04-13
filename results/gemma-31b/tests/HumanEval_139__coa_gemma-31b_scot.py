
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
    assert special_factorial(1) == 1

def test_special_factorial_boundary_small():
    assert special_factorial(2) == 2

# Focus: Type Scenarios
import pytest

def test_special_factorial_float():
    with pytest.raises(TypeError):
        special_factorial(3.5)

def test_special_factorial_string():
    with pytest.raises(TypeError):
        special_factorial("5")

def test_special_factorial_none():
    with pytest.raises(TypeError):
        special_factorial(None)

# Focus: Logic Branches
import pytest

def test_special_factorial_base_case():
    # Tests the smallest valid input branch (n=1)
    assert special_factorial(1) == 1

def test_special_factorial_small_branch():
    # Tests the logic for a small integer where the product loop runs minimally
    assert special_factorial(2) == 2  # 2! * 1! = 2 * 1

def test_special_factorial_general_branch():
    # Tests the general logic branch for larger integers
    assert special_factorial(4) == 288  # 4! * 3! * 2! * 1! = 24 * 6 * 2 * 1