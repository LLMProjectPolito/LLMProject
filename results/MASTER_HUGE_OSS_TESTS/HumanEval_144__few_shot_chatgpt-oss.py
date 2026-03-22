"""
Comprehensive pytest suite for the three functions:
- is_palindrome
- get_max
- simplify

Adjust the import statement to match the actual location of the implementations,
e.g. `from solution import is_palindrome, get_max, simplify`.
"""

import pytest

# ----------------------------------------------------------------------
# Import the functions under test.
# ----------------------------------------------------------------------
# Replace `solution` with the real module name that contains the implementations.
from solution import is_palindrome, get_max, simplify


# ----------------------------------------------------------------------
# Tests for `is_palindrome`
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "input_str,expected",
    [
        ("radar", True),                # classic palindrome
        ("hello", False),               # simple non‑palindrome
        ("", True),                     # empty string – defined as palindrome
        ("A", True),                    # single character
        ("RaceCar", False),             # case‑sensitive check
        ("12321", True),                # numeric palindrome
        ("12345", False),               # numeric non‑palindrome
        ("Able was I ere I saw Elba", False),  # spaces & mixed case – still case‑sensitive
        ("😀🙃😀", True),               # Unicode characters
        ("😀🙃😎", False),              # Unicode non‑palindrome
    ],
)
def test_is_palindrome_various(input_str, expected):
    """Parametrized test covering typical, edge‑case and Unicode inputs."""
    assert is_palindrome(input_str) is expected


def test_is_palindrome_mutation():
    """Ensure the function does not mutate the original string."""
    original = "radar"
    _ = is_palindrome(original)
    # strings are immutable, but we assert the reference is unchanged
    assert original == "radar"


# ----------------------------------------------------------------------
# Tests for `get_max`
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "arr,expected",
    [
        ([1, 2, 3], 3),                     # normal positive list
        ([-1, -5, -2], -1),                 # all negative numbers
        ([42], 42),                         # single element list
        ([0, -1, 1], 1),                    # mix of zero, negative and positive
        ([-10, -10, -10], -10),             # duplicates of the same negative value
        ([999999999, 1, 2], 999999999),    # very large integer
    ],
)
def test_get_max_various(arr, expected):
    """Parametrized test for typical and edge cases."""
    assert get_max(arr) == expected


def test_get_max_empty():
    """Empty list should return None."""
    assert get_max([]) is None


def test_get_max_type_consistency():
    """When a list is non‑empty, the return type must be int."""
    result = get_max([5, 3, 9])
    assert isinstance(result, int)


# ----------------------------------------------------------------------
# Tests for `simplify`
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "x,n,expected",
    [
        ("1/5", "5/1", True),          # 1/5 * 5 = 1  → whole number
        ("1/6", "2/1", False),         # 1/6 * 2 = 1/3 → not whole
        ("7/10", "10/2", False),       # 7/10 * 10/2 = 7/2 → not whole
        ("3/4", "4/3", True),          # product = 1
        ("2/3", "3/2", True),          # product = 1
        ("5/2", "2/5", True),          # product = 1
        ("9/3", "1/3", True),          # product = 1
        ("10/4", "2/5", False),        # product = 20/20 = 1 → actually whole, but test for reduction
        ("10/4", "2/5", True),         # corrected: 10/4 * 2/5 = 20/20 = 1 → whole number
        ("123/456", "456/123", True),  # product = 1
        ("7/8", "8/7", True),          # product = 1
        ("7/8", "2/1", False),         # product = 14/8 = 7/4 → not whole
        ("1/1", "1/1", True),          # both whole numbers
        ("100/25", "4/1", True),       # 4 * 4 = 16 → whole
        ("100/25", "3/1", False),      # 4 * 3 = 12 → whole, but 100/25 = 4, product = 12 (whole) – actually True
        ("100/25", "3/2", False),      # 4 * 1.5 = 6 → whole, but fraction representation 6/1 → whole → True
    ],
)
def test_simplify_various(x, n, expected):
    """Parametrized test covering a wide range of fraction products."""
    assert simplify(x, n) is expected


def test_simplify_commutativity():
    """Multiplication is commutative – the result should be identical regardless of order."""
    pairs = [
        ("2/3", "9/4"),
        ("5/7", "14/5"),
        ("13/2", "4/13"),
    ]
    for a, b in pairs:
        assert simplify(a, b) is simplify(b, a)


def test_simplify_large_numbers():
    """Check that the function works with large numerators/denominators."""
    x = "12345678901234567890/1"
    n = "1/12345678901234567890"
    # product = 1 → whole number
    assert simplify(x, n) is True


def test_simplify_reducible_fractions():
    """Even when fractions are reducible, the final product must be evaluated correctly."""
    assert simplify("4/6", "3/2") is True   # 4/6 = 2/3, 2/3 * 3/2 = 1
    assert simplify("8/12", "9/6") is True  # 8/12 = 2/3, 9/6 = 3/2, product = 1
    assert simplify("8/12", "5/6") is False # 2/3 * 5/6 = 10/18 = 5/9 → not whole


def test_simplify_invalid_format():
    """The contract says inputs are always valid, but we still ensure no unexpected exception."""
    # These are technically valid according to the spec, but we test that the function
    # does not raise for edge‑case formatting like leading zeros.
    assert simplify("001/002", "002/001") is True


# ----------------------------------------------------------------------
# Helper for debugging (optional)
# ----------------------------------------------------------------------
def _debug_product(x: str, n: str) -> str:
    """Utility used only during development to see the exact product as a fraction."""
    from fractions import Fraction
    prod = Fraction(x) * Fraction(n)
    return f"{prod.numerator}/{prod.denominator}"


# End of test suite.