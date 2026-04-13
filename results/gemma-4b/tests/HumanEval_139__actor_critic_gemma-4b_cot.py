
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
    if n <= 0:
        return 1
    
    result = 1
    for i in range(1, n + 1):
        factorial = 1
        for j in range(1, i + 1):
            factorial *= j
        result *= factorial
    return result

def test_special_factorial_positive_integer():
    assert special_factorial(1) == 1
    assert special_factorial(4) == 288
    assert special_factorial(5) == 120 * 24 * 6 * 24
    assert special_factorial(6) == 720 * 720 * 720 * 24 * 6 * 24

def test_special_factorial_zero():
    assert special_factorial(0) == 1

def test_special_factorial_negative_integer():
    assert special_factorial(-1) == 1

def test_special_factorial_large_integer():
    assert special_factorial(10) == 3628800 * 3628800 * 3628800 * 3628800 * 3628800 * 3628800 * 3628800 * 3628800 * 3628800 * 3628800

def test_special_factorial_edge_case_1():
    assert special_factorial(1) == 1

def test_special_factorial_edge_case_2():
    assert special_factorial(2) == 2

def test_special_factorial_edge_case_3():
    assert special_factorial(3) == 6