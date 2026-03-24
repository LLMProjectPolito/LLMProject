
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
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def test_special_factorial_4():
    assert special_factorial(4) == 288

def test_special_factorial_0():
    assert special_factorial(0) == 1

def test_special_factorial_1():
    assert special_factorial(1) == 1

def test_special_factorial_2():
    assert special_factorial(2) == 2

def test_special_factorial_3():
    assert special_factorial(3) == 6

def test_special_factorial_5():
    assert special_factorial(5) == 120

def test_special_factorial_6():
    assert special_factorial(6) == 720