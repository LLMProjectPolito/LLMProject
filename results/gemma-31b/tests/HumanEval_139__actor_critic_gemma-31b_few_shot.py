
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
def test_special_factorial_parametrized(n, expected):
    """Parametrized test for multiple known values to ensure correctness and growth."""
    assert special_factorial(n) == expected

def test_special_factorial_invalid_value():
    """Test that non-positive integers raise a ValueError."""
    with pytest.raises(ValueError):
        special_factorial(0)
    with pytest.raises(ValueError):
        special_factorial(-1)
    with pytest.raises(ValueError):
        special_factorial(-100)  # Testing a larger negative number

def test_special_factorial_invalid_type():
    """Test that non-integer inputs raise a TypeError."""
    with pytest.raises(TypeError):
        special_factorial("5")
    with pytest.raises(TypeError):
        special_factorial(5.5)
    with pytest.raises(TypeError):
        special_factorial(None)