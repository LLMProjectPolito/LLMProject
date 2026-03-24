
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

def test_positive_integer():
    assert special_factorial(5) == 34560
    assert special_factorial(6) == 4665600

def test_n_equals_1():
    assert special_factorial(1) == 1

def test_n_equals_2():
    assert special_factorial(2) == 2

def test_n_equals_3():
    assert special_factorial(3) == 12

def test_n_equals_4():
    assert special_factorial(4) == 288

def test_zero():
    with pytest.raises(ValueError):
        special_factorial(0)

def test_negative():
    with pytest.raises(ValueError):
        special_factorial(-1)