
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
# The function `special_factorial(n)` calculates the Brazilian factorial, which is the product of all factorials from 1 to n.
# The function should handle positive integers only.  If n is 0 or negative, it should return 1.
# We need to test various input values, including small numbers, larger numbers, and edge cases (n=1, n=0, n=-1).
# We need to verify that the result is correct for each input.

# STEP 2: PLAN - List test functions names and scenarios.
# test_special_factorial_positive_small() - Test with small positive integers.
# test_special_factorial_positive_large() - Test with larger positive integers.
# test_special_factorial_edge_cases() - Test edge cases (n=0, n=1).
# test_special_factorial_negative() - Test with negative integers.
# test_special_factorial_zero() - Test with zero.

# STEP 3: CODE - Write the high-quality pytest suite.
def test_special_factorial_positive_small():
    assert special_factorial(1) == 1
    assert special_factorial(2) == 2
    assert special_factorial(3) == 6
    assert special_factorial(4) == 288
    assert special_factorial(5) == 34560

def test_special_factorial_positive_large():
    assert special_factorial(6) == 4168960
    assert special_factorial(7) == 518918400
    assert special_factorial(8) == 4790016000

def test_special_factorial_edge_cases():
    assert special_factorial(0) == 1
    assert special_factorial(1) == 1

def test_special_factorial_negative():
    assert special_factorial(-1) == 1
    assert special_factorial(-5) == 1

def test_special_factorial_zero():
    assert special_factorial(0) == 1