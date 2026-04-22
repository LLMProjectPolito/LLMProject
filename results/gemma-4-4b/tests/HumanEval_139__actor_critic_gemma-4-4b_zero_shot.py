
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
    where n >= 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.  For non-positive inputs, the function returns 1.
    """
    if n <= 0:
        return 1
    
    result = 1
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
        result *= factorial
    return result


@pytest.mark.parametrize("n, expected", [
    (1, 1),
    (2, 2),
    (3, 12),
    (4, 288),
    (5, 34560),
    (6, 518400),
    (7, 8640000),
    (8, 138240000),
    (9, 2073600000),
    (10, 36288000000),
])
def test_special_factorial_positive(n, expected):
    assert special_factorial(n) == expected

@pytest.mark.parametrize("n, expected", [
    (0, 1),  # Edge case: 0! = 1
    (-1, 1), #Edge case: negative input
    (-2, 1),
])
def test_special_factorial_negative(n, expected):
    assert special_factorial(n) == expected

@pytest.mark.parametrize("n, expected", [
    (11, 3991680000000),
])
def test_special_factorial_large(n, expected):
    assert special_factorial(n) == expected