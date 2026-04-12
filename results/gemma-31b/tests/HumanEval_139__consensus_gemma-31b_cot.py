
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
def test_special_factorial_known_values(n, expected):
    """Test the special_factorial with known valid positive integers."""
    assert special_factorial(n) == expected

def test_special_factorial_large_value():
    """Test with a larger value to ensure correctness and handle large integers."""
    n = 10
    expected = 1
    for i in range(1, n + 1):
        expected *= math.factorial(i)
    assert special_factorial(n) == expected

def test_special_factorial_mathematical_property():
    """Verify the property: special_factorial(n) = n! * special_factorial(n-1)"""
    for n in range(2, 11):
        assert special_factorial(n) == math.factorial(n) * special_factorial(n - 1)

def test_special_factorial_type_error():
    """Test that non-integer inputs raise appropriate errors."""
    with pytest.raises(TypeError):
        special_factorial("4")
    with pytest.raises(TypeError):
        special_factorial(4.5)

def test_special_factorial_invalid_range():
    """Test behavior for n <= 0 as the specification requires n > 0."""
    with pytest.raises((ValueError, AssertionError, IndexError)):
        special_factorial(0)
    with pytest.raises((ValueError, AssertionError, IndexError)):
        special_factorial(-1)