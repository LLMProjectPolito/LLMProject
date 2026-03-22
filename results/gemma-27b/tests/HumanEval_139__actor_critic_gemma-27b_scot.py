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
    if n <= 0:
        raise ValueError("Input must be a positive integer.")
    result = 1
    for i in range(1, n + 1):
        result *= factorial(i)
    return result

def test_special_factorial_typical():
    assert special_factorial(4) == 288

def test_special_factorial_one():
    assert special_factorial(1) == 1

def test_special_factorial_five():
    assert special_factorial(5) == 34560

def test_special_factorial_six():
    assert special_factorial(6) == 24883200

def test_special_factorial_invalid_zero():
    with pytest.raises(ValueError):
        special_factorial(0)

def test_special_factorial_invalid_negative():
    with pytest.raises(ValueError):
        special_factorial(-1)

def test_special_factorial_overflow():
    with pytest.raises(OverflowError):
        special_factorial(8)

def test_special_factorial_large():
    assert special_factorial(10) == 1307674368000