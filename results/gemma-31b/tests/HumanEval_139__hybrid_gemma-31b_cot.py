
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

def calculate_expected_special_factorial(n):
    """Helper function to compute the Brazilian factorial for test verification."""
    result = 1
    for i in range(1, n + 1):
        result *= math.factorial(i)
    return result

@pytest.mark.parametrize("n, expected", [
    (1, 1),               # 1! = 1
    (2, 2),               # 2! * 1! = 2
    (3, 12),              # 3! * 2! * 1! = 12
    (4, 288),             # 4! * 3! * 2! * 1! = 288
    (5, 34560),           # 5! * 288 = 34560
    (6, 24883200),        # 6! * 34560 = 24883200
])
def test_special_factorial_known_values(n, expected):
    """Test the function with known small Brazilian factorial values."""
    assert special_factorial(n) == expected

def test_special_factorial_large_value_verification():
    """Test a larger value using the helper function to ensure precision."""
    n = 10
    expected = calculate_expected_special_factorial(n)
    assert special_factorial(n) == expected

def test_special_factorial_mathematical_property():
    """
    Test the recursive property: special_factorial(n) = special_factorial(n-1) * n!
    This verifies consistency across a range of values.
    """
    for n in range(2, 21):
        assert special_factorial(n) == special_factorial(n - 1) * math.factorial(n)

def test_special_factorial_type_consistency():
    """Ensure the function returns an integer for valid inputs."""
    assert isinstance(special_factorial(1), int)
    assert isinstance(special_factorial(10), int)

@pytest.mark.parametrize("invalid_input", [
    0,       # Boundary case: n must be > 0
    -1,      # Negative integer
    -10,     # Large negative integer
])
def test_special_factorial_non_positive_integers(invalid_input):
    """Test that non-positive integers raise an appropriate error."""
    with pytest.raises((ValueError, AssertionError)):
        special_factorial(invalid_input)

@pytest.mark.parametrize("type_error_input", [
    "5",            # String
    5.0,            # Float
    [5],            # List
    None,           # NoneType
])
def test_special_factorial_type_errors(type_error_input):
    """Test that invalid data types raise a TypeError or ValueError."""
    with pytest.raises((TypeError, ValueError)):
        special_factorial(type_error_input)

def test_special_factorial_large_n_properties():
    """
    Test with a relatively large n to ensure Python's arbitrary precision 
    integers are handled and basic mathematical properties hold.
    """
    n = 25
    result = special_factorial(n)
    assert result > 0
    assert result % math.factorial(n) == 0