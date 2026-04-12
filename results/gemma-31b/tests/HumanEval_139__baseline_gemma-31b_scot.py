
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
    (1, 1),          # 1! = 1
    (2, 2),          # 2! * 1! = 2 * 1 = 2
    (3, 12),         # 3! * 2! * 1! = 6 * 2 * 1 = 12
    (4, 288),        # 4! * 3! * 2! * 1! = 24 * 6 * 2 * 1 = 288
    (5, 34560),      # 5! * 288 = 120 * 288 = 34560
    (6, 24883200),   # 6! * 34560 = 720 * 34560 = 24883200
])
def test_special_factorial_valid_inputs(n, expected):
    """Test the special_factorial function with valid positive integers."""
    assert special_factorial(n) == expected

def test_special_factorial_boundary_zero():
    """
    Test behavior for n=0. 
    Depending on implementation, it might return 1 (empty product) 
    or raise an error. Given n > 0 constraint, we check for stability.
    """
    # If the function is strictly for n > 0, we check if it handles 0 
    # without crashing or returns a logical identity (1).
    try:
        result = special_factorial(0)
        # If it doesn't raise, it should ideally return 1 (the multiplicative identity)
        # or the implementation might not support it.
        assert isinstance(result, int)
    except Exception as e:
        # If it raises an exception, it's acceptable as long as it's a standard one
        assert isinstance(e, (ValueError, TypeError))

def test_special_factorial_negative():
    """Test behavior for negative integers."""
    with pytest.raises((ValueError, TypeError, Exception)):
        # The docstring specifies n > 0, so negative inputs should be handled as errors
        special_factorial(-1)

def test_special_factorial_type_safety():
    """Test that the function handles non-integer inputs gracefully."""
    with pytest.raises((TypeError, ValueError)):
        special_factorial("4")
    with pytest.raises((TypeError, ValueError)):
        special_factorial(4.5)