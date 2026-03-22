import pytest

# Import the function under test.
# Adjust the module name (`solution`) to match the file that contains `x_or_y`.
from solution import x_or_y


# ----------------------------------------------------------------------
# Helper – a tiny deterministic prime checker used only for test validation.
# ----------------------------------------------------------------------
def _is_prime(num: int) -> bool:
    """Return True if *num* is a prime number (simple deterministic check)."""
    if num < 2:
        return False
    if num in (2, 3):
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


# ----------------------------------------------------------------------
# Parametrized tests covering normal, edge‑case and type‑variant inputs.
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "n, x, y, expected",
    [
        # Basic examples from the docstring
        (7, 34, 12, 34),   # 7 is prime
        (15, 8, 5, 5),     # 15 is not prime

        # Small numbers
        (2, "prime", "not", "prime"),   # smallest prime
        (1, "prime", "not", "not"),     # 1 is NOT prime
        (0, "prime", "not", "not"),     # 0 is NOT prime
        (-3, "prime", "not", "not"),    # negative numbers are NOT prime

        # Larger primes and composites
        (101, 1.23, 4.56, 1.23),        # 101 is prime
        (100, 1.23, 4.56, 4.56),        # 100 is composite
        (9973, "yes", "no", "yes"),     # larger prime
        (9974, "yes", "no", "no"),      # just after a prime

        # Same value for x and y – result should be that value regardless
        (13, "same", "same", "same"),
        (14, "same", "same", "same"),
    ],
)
def test_x_or_y_various_inputs(n, x, y, expected):
    """Validate that `x_or_y` returns the correct branch for a wide range of inputs."""
    assert x_or_y(n, x, y) == expected


# ----------------------------------------------------------------------
# Property‑based style test – compare against a known‑good prime checker.
# ----------------------------------------------------------------------
@pytest.mark.parametrize("n", list(range(-10, 200)))  # a reasonable range for quick checks
def test_x_or_y_against_reference_prime_checker(n):
    """For every integer in the range, the function must behave like the reference prime checker."""
    x_val = object()   # unique sentinel objects to ensure we can tell which one is returned
    y_val = object()
    expected = x_val if _is_prime(n) else y_val
    assert x_or_y(n, x_val, y_val) is expected


# ----------------------------------------------------------------------
# Immutability test – ensure the function does not alter mutable arguments.
# ----------------------------------------------------------------------
def test_x_or_y_does_not_mutate_inputs():
    """`x_or_y` should not modify mutable arguments passed as `x` or `y`."""
    n = 11  # prime
    x = {"key": "value"}
    y = [1, 2, 3]

    # Keep copies for later comparison
    x_copy = x.copy()
    y_copy = y[:]

    result = x_or_y(n, x, y)

    # Result must be the original `x` object (since n is prime)
    assert result is x
    # Original objects must stay unchanged
    assert x == x_copy
    assert y == y_copy


# ----------------------------------------------------------------------
# Type‑error handling – the function is expected to work only with integers for `n`.
# ----------------------------------------------------------------------
@pytest.mark.parametrize("bad_n", ["7", 7.0, None, [7], (7,)])
def test_x_or_y_invalid_n_type_raises(bad_n):
    """Passing a non‑int as `n` should raise a TypeError (or a ValueError depending on implementation)."""
    with pytest.raises((TypeError, ValueError)):
        x_or_y(bad_n, "x", "y")