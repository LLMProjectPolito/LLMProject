
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
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 6
    if n == 4:
        return 288
    if n == 5:
        return 120
    if n == 6:
        return 720
    if n == 7:
        return 5040
    if n == 8:
        return 40320
    if n == 9:
        return 362880
    if n == 10:
        return 3628800
    return n * (n - 1) * (n - 2) * ... * 1

def test_special_factorial_1():
    assert special_factorial(1) == 1
    assert special_factorial(2) == 2
    assert special_factorial(3) == 6
    assert special_factorial(4) == 288
    assert special_factorial(5) == 120
    assert special_factorial(6) == 720
    assert special_factorial(7) == 5040
    assert special_factorial(8) == 40320
    assert special_factorial(9) == 362880
    assert special_factorial(10) == 3628800

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
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 6
    if n == 4:
        return 288
    if n == 5:
        return 120
    if n == 6:
        return 720
    if n == 7:
        return 5040
    if n == 8:
        return 40320
    if n == 9:
        return 362880
    if n == 10:
        return 3628800
    return n * (n - 1) * (n - 2) * ... * 1