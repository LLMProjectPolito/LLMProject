
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
])
def test_special_factorial_values(n, expected):
    """Test the special_factorial function with known correct values."""
    assert special_factorial(n) == expected

def test_special_factorial_logic():
    """Verify the logic against a manual calculation using math.factorial."""
    n = 7
    expected = 1
    for i in range(1, n + 1):
        expected *= math.factorial(i)
    assert special_factorial(n) == expected

def test_special_factorial_large_value():
    """Test with a larger value to ensure it handles growth correctly."""
    n = 10
    # 10! * 9! * ... * 1!
    # 3628800 * 362880 * 40320 * 5040 * 720 * 120 * 24 * 6 * 2 * 1
    # Result is 6658606584104736522240000000
    expected = 6658606584104736522240000000
    assert special_factorial(n) == expected

def test_special_factorial_minimum_input():
    """Test the smallest valid input according to the problem description (n > 0)."""
    assert special_factorial(1) == 1