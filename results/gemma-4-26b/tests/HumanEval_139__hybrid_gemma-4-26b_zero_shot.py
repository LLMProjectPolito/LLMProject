
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

# Assuming special_factorial is imported from the module under test
# from your_module import special_factorial

@pytest.mark.parametrize("n, expected", [
    (1, 1),
    (2, 2),
    (3, 12),
    (4, 288),
    (5, 34560),
    (6, 24883200),
])
def test_special_factorial_known_values(n, expected):
    """Test the function against known correct outputs and docstring examples."""
    assert special_factorial(n) == expected

@pytest.mark.parametrize("n", range(2, 16))
def test_special_factorial_recurrence_relation(n):
    """
    Test the mathematical property: SF(n) = n! * SF(n-1).
    This ensures the cumulative product logic is consistent across a range.
    """
    assert special_factorial(n) == math.factorial(n) * special_factorial(n - 1)

def test_special_factorial_monotonicity():
    """Verify that the sequence is strictly increasing for n > 1."""
    values = [special_factorial(n) for n in range(1, 10)]
    for i in range(len(values) - 1):
        assert values[i+1] > values[i]

def test_special_factorial_large_integer_integrity():
    """
    Ensure the function handles large integers correctly, maintains 
    arbitrary precision, and returns the correct type.
    """
    n = 12
    result = special_factorial(n)
    assert isinstance(result, int)
    # Verify against recurrence to ensure precision wasn't lost
    assert result == math.factorial(n) * special_factorial(n - 1)

@pytest.mark.parametrize("invalid_n", [0, -1, -5])
def test_special_factorial_invalid_domain(invalid_n):
    """
    Test that the function handles inputs outside the defined domain (n > 0).
    Supports both ValueError and AssertionError depending on implementation.
    """
    with pytest.raises((ValueError, AssertionError)):
        special_factorial(invalid_n)

@pytest.mark.parametrize("bad_type", [3.5, "4", [5], None])
def test_special_factorial_type_safety(bad_type):
    """Test that non-integer inputs raise a TypeError."""
    with pytest.raises(TypeError):
        special_factorial(bad_type)