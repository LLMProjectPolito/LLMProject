
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

### SCoT Steps:

# STEP 1: REASONING - Analyze functional goals and constraints.
# The function calculates the Brazilian factorial, which is the product of all factorials from 1 to n.
# The input 'n' must be a positive integer.
# Edge cases: n = 0, n = 1, n = 2, n = 3, n = 4, n = 5.
# The function should handle large factorials without overflow (within reasonable limits).

# STEP 2: PLAN - List test functions names and scenarios.
# test_special_factorial_positive_numbers
# test_special_factorial_zero
# test_special_factorial_one
# test_special_factorial_small_numbers
# test_special_factorial_larger_numbers

# STEP 3: CODE - Write the high-quality pytest suite.
def test_special_factorial_positive_numbers():
    assert special_factorial(1) == 1
    assert special_factorial(2) == 2
    assert special_factorial(3) == 6
    assert special_factorial(4) == 288
    assert special_factorial(5) == 34560
    assert special_factorial(6) == 4177926400

def test_special_factorial_zero():
    assert special_factorial(0) == 1

def test_special_factorial_one():
    assert special_factorial(1) == 1

def test_special_factorial_small_numbers():
    assert special_factorial(2) == 2
    assert special_factorial(3) == 6

def test_special_factorial_larger_numbers():
    assert special_factorial(4) == 288
    assert special_factorial(5) == 34560
    assert special_factorial(6) == 4177926400