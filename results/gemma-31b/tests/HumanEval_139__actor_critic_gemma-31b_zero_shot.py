
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
    (1, 1),            # 1! = 1
    (2, 2),            # 2! * 1! = 2 * 1 = 2
    (3, 12),           # 3! * 2! * 1! = 6 * 2 * 1 = 12
    (4, 288),          # 4! * 3! * 2! * 1! = 24 * 6 * 2 * 1 = 288
    (5, 34560),        # 5! * 288 = 120 * 288 = 34560
])
def test_special_factorial_valid_inputs(n, expected):
    """Test the function with standard valid positive integers."""
    assert special_factorial(n) == expected

def test_special_factorial_large_value():
    """Test with a larger value to ensure it handles large integer growth."""
    # 6! * 5! * 4! * 3! * 2! * 1! = 720 * 34560 = 24883200
    assert special_factorial(6) == 24883200

def test_special_factorial_zero():
    """Test that n=0 raises a ValueError as per the constraint n > 0."""
    with pytest.raises(ValueError, match="Input must be an integer greater than 0."):
        special_factorial(0)

def test_special_factorial_negative():
    """Test that negative integers raise a ValueError."""
    with pytest.raises(ValueError, match="Input must be an integer greater than 0."):
        special_factorial(-1)
    with pytest.raises(ValueError, match="Input must be an integer greater than 0."):
        special_factorial(-10)

def test_special_factorial_invalid_types():
    """Test that non-integer inputs raise a TypeError."""
    with pytest.raises(TypeError, match="Input must be an integer."):
        special_factorial(4.5)
    with pytest.raises(TypeError, match="Input must be an integer."):
        special_factorial("4")
    with pytest.raises(TypeError, match="Input must be an integer."):
        special_factorial(None)