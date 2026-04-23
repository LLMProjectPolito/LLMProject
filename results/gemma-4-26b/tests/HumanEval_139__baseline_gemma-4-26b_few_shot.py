
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
def test_special_factorial_valid_inputs(n, expected):
    """Tests the Brazilian factorial with valid positive integers."""
    assert special_factorial(n) == expected

def test_special_factorial_large_value():
    """Tests the function with a larger integer to ensure mathematical accuracy."""
    # 6! * 5! * 4! * 3! * 2! * 1! = 720 * 34560 = 24883200
    assert special_factorial(6) == 24883200

def test_special_factorial_zero_input():
    """Tests that n=0 raises a ValueError as the definition requires n > 0."""
    with pytest.raises(ValueError):
        special_factorial(0)

def test_special_factorial_negative_input():
    """Tests that negative integers raise a ValueError."""
    with pytest.raises(ValueError):
        special_factorial(-5)

def test_special_factorial_type_error():
    """Tests that non-integer inputs raise a TypeError."""
    with pytest.raises(TypeError):
        special_factorial("4")
    with pytest.raises(TypeError):
        special_factorial(4.5)