
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
from solution import special_factorial

@pytest.mark.parametrize("n, expected", [
    (1, 1),
    (2, 2),
    (3, 12),
    (4, 288),
    (5, 34560),
    (6, 24883200),
])
def test_special_factorial_positive_integers(n, expected):
    """Test the special factorial with various positive integers."""
    assert special_factorial(n) == expected

def test_special_factorial_large_value():
    """Test with a slightly larger value to ensure correctness of the product chain."""
    # 7! = 5040
    # special_factorial(7) = 5040 * special_factorial(6)
    # 5040 * 24883200 = 125411328000
    assert special_factorial(7) == 125411328000

def test_special_factorial_type_consistency():
    """Ensure the return type is an integer."""
    result = special_factorial(3)
    assert isinstance(result, int)