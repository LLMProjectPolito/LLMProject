
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

def special_factorial(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    if n <= 0:
        raise ValueError("Input must be an integer greater than 0.")
    
    result = 1
    for i in range(1, n + 1):
        result *= math.factorial(i)
    return result

@pytest.mark.parametrize("n, expected", [
    (1, 1),             # 1! = 1
    (2, 2),             # 2! * 1! = 2 * 1 = 2
    (3, 12),            # 3! * 2! * 1! = 6 * 2 * 1 = 12
    (4, 288),           # 4! * 3! * 2! * 1! = 24 * 6 * 2 * 1 = 288
    (5, 34560),         # 5! * 288 = 120 * 288 = 34560
])
def test_special_factorial_standard_values(n, expected):
    """Test standard positive integers based on the definition."""
    assert special_factorial(n) == expected

def test_special_factorial_large_value():
    """Test a larger value using a pre-calculated constant to avoid tautological logic."""
    # Pre-calculated value for n=10: 1! * 2! * ... * 10!
    expected = 665860658410473600000
    assert special_factorial(10) == expected

def test_special_factorial_zero():
    """Test that n=0 raises a ValueError as per the constraint n > 0."""
    with pytest.raises(ValueError, match="Input must be an integer greater than 0"):
        special_factorial(0)

def test_special_factorial_negative():
    """Test that negative integers raise a ValueError."""
    with pytest.raises(ValueError, match="Input must be an integer greater than 0"):
        special_factorial(-5)

def test_special_factorial_float():
    """Test that non-integer numeric types raise a TypeError."""
    with pytest.raises(TypeError, match="Input must be an integer"):
        special_factorial(4.5)

def test_special_factorial_string():
    """Test that non-numeric types raise a TypeError."""
    with pytest.raises(TypeError, match="Input must be an integer"):
        special_factorial("4")

def test_special_factorial_none():
    """Test that None input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be an integer"):
        special_factorial(None)