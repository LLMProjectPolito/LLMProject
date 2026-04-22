
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

def test_special_factorial_positive_integer():
    assert special_factorial(1) == 1
    assert special_factorial(2) == 2
    assert special_factorial(3) == 12
    assert special_factorial(4) == 288
    assert special_factorial(5) == 34560
    assert special_factorial(6) == 6451200
    assert special_factorial(7) == 1612809600
    assert special_factorial(8) == 518918400000
    assert special_factorial(9) == 263588016000000
    assert special_factorial(10) == 12164510040883200000

def test_special_factorial_edge_cases():
    assert special_factorial(0) == 1
    with pytest.raises(TypeError):
        special_factorial(-1)
    with pytest.raises(TypeError):
        special_factorial(1.5)

def test_special_factorial_large_number():
    assert special_factorial(12) == 665280000000000000000
    assert special_factorial(15) == 130767436800000000000000000