
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

def test_special_factorial_zero():
    """Test with n = 0.  The loop should not execute, and the initial value 1 should be returned."""
    assert special_factorial(0) == 1

def test_special_factorial_zero_raises_value_error():
    """Test with n = 0. Should raise a ValueError."""
    with pytest.raises(ValueError):
        special_factorial(0)