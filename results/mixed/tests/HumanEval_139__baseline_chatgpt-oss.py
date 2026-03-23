import math
import pytest

# Import the function under test.
# Adjust the import path if the implementation lives in a different module.
# The typical name used in these kata‑style exercises is `solution.py`.
from solution import special_factorial


def brute_special_factorial(n: int) -> int:
    """
    Reference implementation that follows the definition:
    product_{k=1..n} k!
    """
    if n <= 0:
        raise ValueError("n must be a positive integer")
    prod = 1
    for k in range(1, n + 1):
        prod *= math.factorial(k)
    return prod


# ----------------------------------------------------------------------
# Positive test cases – compare against the reference implementation
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "n, expected",
    [
        (1, 1),                     # 1! = 1
        (2, 2),                     # 1! * 2! = 1 * 2 = 2
        (3, 12),                    # 1! * 2! * 3! = 1 * 2 * 6 = 12
        (4, 288),                   # example from the docstring
        (5, 34560),                 # 1!*2!*3!*4!*5!
        (6, 24883200),              # 1!*…*6!
        (7, 125411328000),         # larger but still quick to compute
        (10, 131130704576000000),   # sanity‑check for a double‑digit input
    ],
)
def test_special_factorial_known_values(n, expected):
    """Check that the function returns the exact value for several known inputs."""
    assert special_factorial(n) == expected


@pytest.mark.parametrize("n", [8, 9, 11, 12])
def test_special_factorial_against_brute(n):
    """Cross‑validate against a simple reference implementation for a range of n."""
    assert special_factorial(n) == brute_special_factorial(n)


# ----------------------------------------------------------------------
# Edge‑case handling – invalid inputs
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "bad_input, exc_type",
    [
        (0, ValueError),          # n must be > 0
        (-1, ValueError),         # negative numbers are not allowed
        (-10, ValueError),        # another negative case
        (3.5, TypeError),         # non‑integer (float) should be rejected
        ("5", TypeError),         # string input
        (None, TypeError),        # NoneType
        ([], TypeError),          # list
        ({}, TypeError),          # dict
    ],
)
def test_special_factorial_invalid_inputs(bad_input, exc_type):
    """The function should raise a clear exception for unsupported arguments."""
    with pytest.raises(exc_type):
        special_factorial(bad_input)


# ----------------------------------------------------------------------
# Performance / scalability – ensure the function works for larger n
# ----------------------------------------------------------------------
def test_special_factorial_large_input():
    """
    For n = 15 the result is huge (≈ 10^27) but Python's arbitrary‑precision ints
    can handle it. The test checks that the function returns the exact value
    without raising an exception.
    """
    n = 15
    expected = brute_special_factorial(n)
    assert special_factorial(n) == expected


# ----------------------------------------------------------------------
# Idempotence – calling the function repeatedly with the same argument
# ----------------------------------------------------------------------
def test_special_factorial_idempotent_calls():
    """Repeated calls with the same argument must yield the same result."""
    n = 6
    first = special_factorial(n)
    for _ in range(5):
        assert special_factorial(n) == first