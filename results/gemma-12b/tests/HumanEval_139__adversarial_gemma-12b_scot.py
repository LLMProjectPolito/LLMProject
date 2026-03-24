
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
from your_module import special_factorial  # Replace your_module

def test_base_case():
    assert special_factorial(1) == 1

def test_small_values():
    assert special_factorial(2) == 2
    assert special_factorial(3) == 12
    assert special_factorial(4) == 288

def test_larger_values():
    assert special_factorial(5) == 34560
    assert special_factorial(6) == 3628800

def test_zero_input():
    with pytest.raises(ValueError):
        special_factorial(0)

def test_negative_input():
    with pytest.raises(ValueError):
        special_factorial(-1)

def test_non_integer_input():
    with pytest.raises(TypeError):
        special_factorial(1.5)