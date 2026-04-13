
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
    """Test basic cases provided in the description and small integers."""
    assert special_factorial(1) == 1  # 1! = 1
    assert special_factorial(2) == 2  # 2! * 1! = 2 * 1 = 2
    assert special_factorial(3) == 12 # 3! * 2! * 1! = 6 * 2 * 1 = 12
    assert special_factorial(4) == 288 # 4! * 3! * 2! * 1! = 24 * 6 * 2 * 1 = 288

def test_special_factorial_larger():
    """Test a slightly larger integer to ensure multiplicative growth is correct."""
    # 5! * 4! * 3! * 2! * 1! = 120 * 288 = 34560
    assert special_factorial(5) == 34560

def test_special_factorial_boundary():
    """Test the minimum valid input according to the definition (n > 0)."""
    assert special_factorial(1) == 1

@pytest.mark.parametrize("n, expected", [
    (1, 1),
    (2, 2),
    (3, 12),
    (4, 288),
    (5, 34560),
])
def test_special_factorial_parametrized(n, expected):
    """Parametrized test for multiple values to ensure consistency."""
    assert special_factorial(n) == expected