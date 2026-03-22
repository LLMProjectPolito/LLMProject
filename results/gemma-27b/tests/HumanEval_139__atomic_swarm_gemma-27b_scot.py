import pytest
import math

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
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)

    result = 1
    for i in range(1, n + 1):
        result *= factorial(i)
    return result

def test_basic():
    assert special_factorial(4) == 288

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

def test_edge_zero():
    assert special_factorial(0) == 1

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
        raise ValueError("Input must be a positive integer.")

    def factorial(num):
        if num == 0:
            return 1
        else:
            return num * factorial(num-1)

    result = 1
    for i in range(1, n + 1):
        result *= factorial(i)
    return result

def test_negative_input():
    """Test with a negative input to check for ValueError."""
    with pytest.raises(ValueError) as excinfo:
        special_factorial(-1)
    assert str(excinfo.value) == "Input must be a positive integer."