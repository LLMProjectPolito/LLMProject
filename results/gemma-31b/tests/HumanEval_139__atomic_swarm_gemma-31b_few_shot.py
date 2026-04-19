
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

def test_special_factorial():
    assert special_factorial(4) == 288

def test_special_factorial_one():
    assert special_factorial(1) == 1

import pytest

def test_special_factorial_invalid_boundary():
    with pytest.raises(ValueError):
        special_factorial(0)