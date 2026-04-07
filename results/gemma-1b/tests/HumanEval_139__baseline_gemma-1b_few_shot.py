
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
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        result = 1
        for i in range(n, 0, -1):
            result *= i
        return result

def test_special_factorial_positive():
    assert special_factorial(4) == 288

def test_special_factorial_negative():
    assert special_factorial(-1) == 1

def test_special_factorial_zero():
    assert special_factorial(0) == 1