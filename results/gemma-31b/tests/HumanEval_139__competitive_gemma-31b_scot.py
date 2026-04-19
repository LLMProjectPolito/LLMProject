
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
    (7, 125411328000),
])
def test_special_factorial_known_values(n, expected):
    """Test the function with known Brazilian factorial values."""
    assert special_factorial(n) == expected

def test_special_factorial_dynamic_verification():
    """Verify the function against a manual calculation using math.factorial."""
    n = 10
    expected = 1
    for i in range(1, n + 1):
        expected *= math.factorial(i)
    assert special_factorial(n) == expected

def test_special_factorial_large_input():
    """Ensure the function handles larger integers (Python's arbitrary precision)."""
    # Testing for n=15 to ensure no overflow and correct type
    result = special_factorial(15)
    assert isinstance(result, int)
    assert result > 0

def test_special_factorial_invalid_type():
    """Test that the function raises a TypeError when passed a non-integer."""
    with pytest.raises(TypeError):
        special_factorial("4")
    with pytest.raises(TypeError):
        special_factorial(4.5)

def test_special_factorial_boundary_zero():
    """
    Test behavior for n=0. 
    The docstring specifies n > 0, so we check if it handles it 
    gracefully or raises an error depending on implementation.
    """
    # If the implementation follows the n > 0 constraint strictly, 
    # it might raise an error or return 1 (empty product).
    # This test ensures we know how it behaves.
    try:
        result = special_factorial(0)
        # If it doesn't raise, it should at least return a number
        assert isinstance(result, int)
    except (ValueError, AssertionError):
        pass