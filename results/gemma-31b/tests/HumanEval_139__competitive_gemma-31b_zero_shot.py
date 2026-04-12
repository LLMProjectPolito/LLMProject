
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

@pytest.mark.parametrize("n, expected", [
    (1, 1),
    (2, 2),
    (3, 12),
    (4, 288),
    (5, 34560),
    (6, 24883200),
])
def test_special_factorial_valid_inputs(n, expected):
    """Test the special factorial with valid positive integers."""
    assert special_factorial(n) == expected

def test_special_factorial_large_value():
    """Test a larger value to ensure correctness of the multiplicative chain."""
    # 7! * 6! * 5! * 4! * 3! * 2! * 1!
    # 5040 * 720 * 120 * 24 * 6 * 2 * 1 = 125411328000
    assert special_factorial(7) == 125411328000

@pytest.mark.parametrize("invalid_input", [
    (0),
    (-1),
    (-10),
])
def test_special_factorial_non_positive_integers(invalid_input):
    """Test that non-positive integers raise an appropriate error."""
    with pytest.raises((ValueError, TypeError)):
        special_factorial(invalid_input)

@pytest.mark.parametrize("invalid_type", [
    (3.14),
    ("4"),
    (None),
    ([5]),
])
def test_special_factorial_invalid_types(invalid_type):
    """Test that non-integer types raise a TypeError."""
    with pytest.raises(TypeError):
        special_factorial(invalid_type)