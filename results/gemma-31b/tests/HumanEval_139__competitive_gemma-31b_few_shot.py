
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
    """Test the special_factorial function with valid positive integers."""
    assert special_factorial(n) == expected

def test_special_factorial_docstring_example():
    """Verify the specific example provided in the docstring."""
    assert special_factorial(4) == 288

def test_special_factorial_large_value():
    """Test with a larger value to ensure correctness of the product sequence."""
    # 7! * 6! * 5! * 4! * 3! * 2! * 1!
    # 5040 * 720 * 120 * 24 * 6 * 2 * 1 = 125411328000
    assert special_factorial(7) == 125411328000

def test_special_factorial_mathematical_consistency():
    """Verify that special_factorial(n) == special_factorial(n-1) * math.factorial(n)."""
    n = 10
    assert special_factorial(n) == special_factorial(n - 1) * math.factorial(n)