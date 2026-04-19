
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

# The function special_factorial is assumed to be defined in the environment.

@pytest.mark.parametrize("n, expected", [
    (1, 1),               # 1! = 1
    (2, 2),               # 2! * 1! = 2
    (3, 12),              # 3! * 2! * 1! = 12
    (4, 288),             # 4! * 3! * 2! * 1! = 288
    (5, 34560),           # 5! * 288 = 34560
    (6, 24883200),        # 6! * 34560 = 24,883,200
])
def test_special_factorial_known_values(n, expected):
    """Test the function against a set of pre-calculated Brazilian factorials."""
    assert special_factorial(n) == expected

def test_special_factorial_recursive_property():
    """
    Verify the mathematical property: SF(n) = SF(n-1) * n!
    This ensures consistency across the sequence.
    """
    for n in range(2, 15):
        prev_sf = special_factorial(n - 1)
        current_sf = special_factorial(n)
        assert current_sf == prev_sf * math.factorial(n)

@pytest.mark.parametrize("n", [7, 8, 9, 11])
def test_special_factorial_reference_implementation(n):
    """Test the function against a reference implementation using math.factorial."""
    expected = 1
    for i in range(1, n + 1):
        expected *= math.factorial(i)
    
    assert special_factorial(n) == expected

def test_special_factorial_large_input():
    """Test a larger input to ensure integer precision and type handling."""
    n = 12
    expected = 1
    for i in range(1, n + 1):
        expected *= math.factorial(i)
    
    result = special_factorial(n)
    assert result == expected
    assert isinstance(result, int)

@pytest.mark.parametrize("invalid_n", [0, -1, -10])
def test_special_factorial_invalid_integers(invalid_n):
    """
    The domain is specified as n > 0. 
    Verify that non-positive integers raise a domain-related exception.
    """
    with pytest.raises((ValueError, AssertionError)):
        special_factorial(invalid_n)

@pytest.mark.parametrize("bad_type", [3.5, "5", [5], None])
def test_special_factorial_type_safety(bad_type):
    """Verify that non-integer inputs raise a TypeError."""
    with pytest.raises(TypeError):
        special_factorial(bad_type)