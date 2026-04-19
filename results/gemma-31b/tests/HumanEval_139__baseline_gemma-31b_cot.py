
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
def test_special_factorial_basic(n, expected):
    """Test basic cases for the Brazilian factorial."""
    assert special_factorial(n) == expected

def test_special_factorial_large():
    """Test a larger value of n to ensure correctness and handle large integers."""
    n = 10
    expected = 1
    for i in range(1, n + 1):
        expected *= math.factorial(i)
    assert special_factorial(n) == expected

def test_special_factorial_consistency():
    """Test that special_factorial(n) == special_factorial(n-1) * n!"""
    n = 7
    # special_factorial(7) should be special_factorial(6) * 7!
    val_6 = special_factorial(6)
    val_7 = special_factorial(7)
    assert val_7 == val_6 * math.factorial(7)

@pytest.mark.parametrize("n", [0, -1, -10])
def test_special_factorial_invalid_input(n):
    """
    The problem states n > 0. Depending on implementation, 
    this might raise an error or return a specific value.
    Since the behavior for n <= 0 isn't defined, we check if it 
    handles it gracefully or as per standard factorial logic (if applicable).
    """
    # This test is a placeholder for boundary behavior. 
    # If the function is strictly for n > 0, we assume it might raise an exception 
    # or return 1/0. Given the prompt, we focus on the defined domain.
    pass