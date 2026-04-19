
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

# The function to be tested
def special_factorial(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    if n <= 0:
        raise ValueError("Input must be a positive integer greater than 0.")
    
    result = 1
    for i in range(1, n + 1):
        result *= math.factorial(i)
    return result

# --- Pytest Suite ---

@pytest.mark.parametrize("n, expected", [
    (1, 1),             # 1! = 1
    (2, 2),             # 2! * 1! = 2 * 1 = 2
    (3, 12),            # 3! * 2! * 1! = 6 * 2 * 1 = 12
    (4, 288),           # 4! * 3! * 2! * 1! = 24 * 6 * 2 * 1 = 288
    (5, 34560),         # 5! * 288 = 120 * 288 = 34560
])
def test_special_factorial_correctness(n, expected):
    """Test the function with known correct values for small positive integers."""
    assert special_factorial(n) == expected

def test_special_factorial_large_value():
    """Test with a larger value to ensure it handles growth correctly."""
    # 6! * 5! * 4! * 3! * 2! * 1! = 720 * 34560 = 24883200
    assert special_factorial(6) == 24883200

@pytest.mark.parametrize("invalid_input", [0, -1, -100])
def test_special_factorial_non_positive_integers(invalid_input):
    """Test that values <= 0 raise a ValueError as per the constraint n > 0."""
    with pytest.raises(ValueError):
        special_factorial(invalid_input)

@pytest.mark.parametrize("wrong_type", [3.5, "4", [5], None])
def test_special_factorial_invalid_types(wrong_type):
    """Test that non-integer inputs raise a TypeError."""
    with pytest.raises(TypeError):
        special_factorial(wrong_type)

def test_special_factorial_performance_and_stability():
    """Test a moderately large n to ensure no crash and correct mathematical growth."""
    # We don't need to calculate the exact value for very large n, 
    # but we check if it returns an integer and is greater than the previous result.
    res_10 = special_factorial(10)
    res_11 = special_factorial(11)
    assert isinstance(res_10, int)
    assert res_11 > res_10
    # Mathematical check: sf(11) should be sf(10) * 11!
    assert res_11 == res_10 * math.factorial(11)