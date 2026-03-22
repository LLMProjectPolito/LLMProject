import pytest
from math import factorial

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
    result = 1
    for i in range(1, n + 1):
        result *= factorial(i)
    return result

def test_special_factorial_positive_integer():
    assert special_factorial(1) == 1
    assert special_factorial(2) == 2
    assert special_factorial(3) == 6
    assert special_factorial(4) == 288
    assert special_factorial(5) == 34560
    assert special_factorial(6) == 41779288
    assert special_factorial(7) == 57609332880

def test_special_factorial_zero():
    with pytest.raises(ValueError):
        special_factorial(0)

def test_special_factorial_negative_integer():
    with pytest.raises(ValueError):
        special_factorial(-1)

def test_special_factorial_large_integer():
    assert special_factorial(10) == 3628800 * 3628800 * 3628800 * 3628800 * 3628800 * 3628800 * 3628800 * 3628800 * 3628800 * 3628800
    assert special_factorial(15)