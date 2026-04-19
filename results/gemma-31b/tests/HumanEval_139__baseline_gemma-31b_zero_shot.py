
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
from solution import special_factorial

@pytest.mark.parametrize("n, expected", [
    (1, 1),            # 1! = 1
    (2, 2),            # 2! * 1! = 2 * 1 = 2
    (3, 12),           # 3! * 2! * 1! = 6 * 2 * 1 = 12
    (4, 288),          # 4! * 3! * 2! * 1! = 24 * 6 * 2 * 1 = 288
    (5, 34560),        # 5! * 4! * 3! * 2! * 1! = 120 * 288 = 34560
    (6, 24883200),     # 6! * 34560 = 720 * 34560 = 24883200
])
def test_special_factorial_valid_inputs(n, expected):
    """Test the special_factorial function with valid positive integers."""
    assert special_factorial(n) == expected

def test_special_factorial_large_value():
    """Test with a larger value to ensure it handles growth correctly."""
    # 7! = 5040. 24883200 * 5040 = 125411328000
    assert special_factorial(7) == 125411328000

def test_special_factorial_type_error():
    """Test that the function handles non-integer inputs if applicable."""
    with pytest.raises(TypeError):
        special_factorial("4")
    with pytest.raises(TypeError):
        special_factorial(4.5)

def test_special_factorial_domain_error():
    """Test that the function handles inputs outside the defined domain (n > 0)."""
    # Depending on implementation, this might raise ValueError or return 0/1.
    # Assuming the constraint n > 0 is strictly enforced.
    with pytest.raises((ValueError, AssertionError)):
        special_factorial(0)
    with pytest.raises((ValueError, AssertionError)):
        special_factorial(-1)