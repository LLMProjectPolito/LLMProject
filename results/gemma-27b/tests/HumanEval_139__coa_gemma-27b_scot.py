
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


# Focus: Boundary Values
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
    
    result = 1
    for i in range(1, n + 1):
        factorial = 1
        for j in range(1, i + 1):
            factorial *= j
        result *= factorial
    return result

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def test_special_factorial_boundary_1():
    assert special_factorial(1) == 1

def test_special_factorial_boundary_2():
    assert special_factorial(2) == 2

def test_special_factorial_boundary_3():
    assert special_factorial(3) == 12

# Focus: Large Inputs
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

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

@pytest.mark.parametrize("n", [10, 12, 15])
def test_special_factorial_large_input(n):
    expected = 1
    for i in range(1, n + 1):
        expected *= factorial(i)
    assert special_factorial(n) == expected

@pytest.mark.parametrize("n", [8, 11, 14])
def test_special_factorial_large_input_2(n):
    expected = 1
    for i in range(1, n + 1):
        expected *= factorial(i)
    assert special_factorial(n) == expected

# Focus: Error Handling/Invalid Input
import pytest

def test_special_factorial_negative_input():
    with pytest.raises(ValueError) as excinfo:
        special_factorial(-1)
    assert "Input must be a positive integer." == str(excinfo.value)

def test_special_factorial_zero_input():
    with pytest.raises(ValueError) as excinfo:
        special_factorial(0)
    assert "Input must be a positive integer." == str(excinfo.value)

def test_special_factorial_non_integer_input():
    with pytest.raises(TypeError) as excinfo:
        special_factorial(1.5)
    assert "Input must be an integer." == str(excinfo.value)