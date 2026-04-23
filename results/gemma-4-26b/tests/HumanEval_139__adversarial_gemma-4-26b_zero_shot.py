
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

# Note: This test suite assumes special_factorial is available in the namespace.
# If testing as a separate file, use: from your_module import special_factorial

@pytest.mark.parametrize("n, expected", [
    (1, 1),           # 1! = 1
    (2, 2),           # 2! * 1! = 2 * 1 = 2
    (3, 12),          # 3! * 2! * 1! = 6 * 2 * 1 = 12
    (4, 288),         # 4! * 3! * 2! * 1! = 24 * 6 * 2 * 1 = 288
    (5, 34560),       # 5! * 4! * 3! * 2! * 1! = 120 * 288 = 34560
    (6, 24883200),    # 6! * 34560 = 720 * 34560 = 24883200
])
def test_special_factorial_correctness(n, expected):
    """Test standard valid integer inputs against known correct values."""
    assert special_factorial(n) == expected

def test_special_factorial_return_type():
    """Ensure the function returns an integer type."""
    result = special_factorial(3)
    assert isinstance(result, int), f"Expected int, got {type(result)}"

@pytest.mark.parametrize("invalid_n", [0, -1, -10, -100])
def test_special_factorial_non_positive_integers(invalid_n):
    """
    The problem states n > 0. 
    A robust implementation should raise a ValueError for n <= 0.
    """
    with pytest.raises(ValueError):
        special_factorial(invalid_n)

@pytest.mark.parametrize("bad_type", [3.5, "4", [4], None, complex(1, 2), True])
def test_special_factorial_invalid_types(bad_type):
    """
    A robust implementation should raise a TypeError for non-integer inputs.
    Note: bool is a subclass of int in Python, but logically it should be rejected.
    """
    # We check for TypeError. If the implementation allows bools, 
    # this test will fail, alerting the QA engineer to a type-safety issue.
    with pytest.raises(TypeError):
        special_factorial(bad_type)

def test_special_factorial_large_input():
    """
    Test with a larger integer to ensure the function handles large numbers 
    (Python handles arbitrary precision integers, so we check for performance/recursion limits).
    """
    # n=10 is large enough to produce a massive number without timing out.
    try:
        result = special_factorial(10)
        assert result > 0
        assert isinstance(result, int)
    except RecursionError:
        pytest.fail("special_factorial raised RecursionError; consider an iterative approach.")

def test_special_factorial_idempotency():
    """Ensure calling the function multiple times with the same input yields the same result."""
    n = 4
    assert special_factorial(n) == special_factorial(n)