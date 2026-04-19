
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

def test_special_factorial_basic():
    """Test standard positive integers including the provided example."""
    assert special_factorial(1) == 1      # 1! = 1
    assert special_factorial(2) == 2      # 2! * 1! = 2 * 1 = 2
    assert special_factorial(3) == 12     # 3! * 2! * 1! = 6 * 2 * 1 = 12
    assert special_factorial(4) == 288    # 4! * 3! * 2! * 1! = 24 * 6 * 2 * 1 = 288
    assert special_factorial(5) == 34560  # 120 * 288 = 34560

@pytest.mark.parametrize("n, expected", [
    (1, 1),
    (2, 2),
    (3, 12),
    (4, 288),
    (5, 34560),
])
def test_special_factorial_parametrized(n, expected):
    """Parametrized test to ensure consistency across multiple valid inputs."""
    assert special_factorial(n) == expected

def test_special_factorial_zero():
    """
    The docstring specifies n > 0. 
    Depending on implementation, n=0 should either raise a ValueError 
    or return a mathematically defined identity (usually 1).
    """
    # If the function is strict about n > 0:
    with pytest.raises((ValueError, AssertionError)):
        special_factorial(0)

def test_special_factorial_negative():
    """Test that negative integers are handled gracefully (should raise error)."""
    with pytest.raises((ValueError, AssertionError)):
        special_factorial(-1)
    with pytest.raises((ValueError, AssertionError)):
        special_factorial(-10)

def test_special_factorial_invalid_types():
    """Test that non-integer inputs raise a TypeError."""
    with pytest.raises(TypeError):
        special_factorial(3.5)
    with pytest.raises(TypeError):
        special_factorial("5")
    with pytest.raises(TypeError):
        special_factorial(None)

def test_special_factorial_large_value():
    """
    Test a larger value to ensure no integer overflow 
    (Python handles arbitrarily large integers, but we check for stability).
    """
    # special_factorial(10) is a very large number
    # 10! * 9! * ... * 1!
    result = special_factorial(10)
    assert isinstance(result, int)
    assert result > 0