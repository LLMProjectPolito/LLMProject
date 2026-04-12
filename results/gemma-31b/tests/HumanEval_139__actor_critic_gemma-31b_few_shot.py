
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

@pytest.mark.parametrize("n, expected", [
    (1, 1),
    (2, 2),
    (3, 12),
    (4, 288),
    (5, 34560),
])
def test_special_factorial_valid(n, expected):
    """Parametrized test for multiple known valid values."""
    assert special_factorial(n) == expected

def test_special_factorial_large_n():
    """
    Test with a larger value to ensure the implementation is iterative 
    or handles recursion limits correctly, avoiding RecursionError.
    """
    # We don't necessarily need to check the exact value of 100!! 
    # as it is massive, but we ensure it completes and returns an int.
    result = special_factorial(100)
    assert isinstance(result, int)

@pytest.mark.parametrize("n", [0, -1, -10])
def test_special_factorial_value_error(n):
    """Test that values violating the n > 0 constraint raise a ValueError."""
    with pytest.raises(ValueError):
        special_factorial(n)

@pytest.mark.parametrize("n", [
    "4",       # String
    4.5,       # Float
    4.0,       # Float-integer (should be rejected for strict type checking)
    None,      # NoneType
    [5],       # List
    True,      # Boolean (subclass of int)
    False,     # Boolean (subclass of int)
])
def test_special_factorial_type_error(n):
    """Test that non-integer inputs (including booleans and float-integers) raise a TypeError."""
    with pytest.raises(TypeError):
        special_factorial(n)