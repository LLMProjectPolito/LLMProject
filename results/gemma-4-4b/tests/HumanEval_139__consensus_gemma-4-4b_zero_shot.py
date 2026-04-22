
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

def test_special_factorial_positive_number():
    assert special_factorial(1) == 1
    assert special_factorial(2) == 2
    assert special_factorial(3) == 6
    assert special_factorial(4) == 288
    assert special_factorial(5) == 34560
    assert special_factorial(6) == 6451200
    assert special_factorial(7) == 1032192000
    assert special_factorial(8) == 518918400000
    assert special_factorial(9) == 26345600000000
    assert special_factorial(10) == 36288000

def test_special_factorial_edge_cases():
    assert special_factorial(0) == 1

def test_special_factorial_negative_input():
    with pytest.raises(ValueError):
        special_factorial(-1)

def test_special_factorial_float_input():
    with pytest.raises(TypeError):
        special_factorial(2.5)