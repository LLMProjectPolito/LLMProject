
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

# Note: The function special_factorial(n) is assumed to be defined in the environment.

@pytest.mark.parametrize("n, expected", [
    (1, 1),          # 1! = 1
    (2, 2),          # 2! * 1! = 2 * 1 = 2
    (3, 12),         # 3! * 2! * 1! = 6 * 2 * 1 = 12
    (4, 288),        # 4! * 3! * 2! * 1! = 24 * 6 * 2 * 1 = 288
    (5, 34560),      # 5! * 4! * 3! * 2! * 1! = 120 * 288 = 34560
])
def test_special_factorial_correctness(n, expected):
    """Verify the function returns correct mathematical values for valid positive integers."""
    assert special_factorial(n) == expected

def test_special_factorial_large_input():
    """Verify the function handles moderately large inputs without logic errors."""
    # n=10 is large enough to check cumulative product but small enough for quick execution
    # 10! * 9! * ... * 1! is a very large number
    result = special_factorial(10)
    assert isinstance(result, int)
    assert result > 0

@pytest.mark.parametrize("invalid_n", [0, -1, -10, -100])
def test_special_factorial_invalid_domain(invalid_n):
    """Verify that n <= 0 raises a ValueError as per the mathematical constraint n > 0."""
    with pytest.raises(ValueError):
        special_factorial(invalid_n)

@pytest.mark.parametrize("bad_type", [4.5, "4", None, [4], {"n": 4}])
def test_special_factorial_invalid_types(bad_type):
    """Verify that non-integer inputs raise a TypeError."""
    with pytest.raises(TypeError):
        special_factorial(bad_type)

def test_special_factorial_return_type():
    """Ensure the output is always an integer, even for larger values."""
    result = special_factorial(5)
    assert isinstance(result, int), f"Expected int, got {type(result)}"

def test_special_factorial_idempotency():
    """Verify that calling the function multiple times with the same input yields the same result."""
    n = 6
    first_call = special_factorial(n)
    second_call = special_factorial(n)
    assert first_call == second_call