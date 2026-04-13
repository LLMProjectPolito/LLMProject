
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
    """Test with n = 0.  Should raise a ValueError because the factorial is not defined for 0."""
    with pytest.raises(ValueError):
        from your_module import special_factorial  # Replace your_module
        special_factorial(0)