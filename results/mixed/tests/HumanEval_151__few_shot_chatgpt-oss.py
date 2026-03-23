# test_suite.py
import pytest

# ----------------------------------------------------------------------
# Adjust the import below to match the actual location of the functions.
# For example, if the functions are defined in a file named `solution.py`,
# use:  from solution import is_palindrome, get_max, double_the_difference
# ----------------------------------------------------------------------
from __main__ import (          # type: ignore
    is_palindrome,
    get_max,
    double_the_difference,
)

# ----------------------------------------------------------------------
# is_palindrome tests
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "input_str,expected",
    [
        ("radar", True),          # simple palindrome
        ("hello", False),         # simple non‑palindrome
        ("", True),               # empty string (edge case)
        ("Radar", False),         # case‑sensitive check
        ("A", True),              # single character
        ("aa", True),             # even length palindrome
        ("ab", False),            # even length non‑palindrome
        ("12321", True),          # numeric palindrome
        ("12345", False),         # numeric non‑palindrome
        ("Madam", False),         # mixed case, not palindrome
    ],
)
def test_is_palindrome_various(input_str, expected):
    """Validate palindrome detection across a range of inputs."""
    assert is_palindrome(input_str) is expected


# ----------------------------------------------------------------------
# get_max tests
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "arr,expected",
    [
        ([1, 2, 3], 3),                     # typical positive list
        ([-1, -5, -2], -1),                 # all negative numbers
        ([0], 0),                           # single zero element
        ([5, 5, 5], 5),                     # all equal elements
        ([-10, 0, 10], 10),                 # mixed sign list
        (list(range(1000)), 999),           # large list
        ([-1000, -500, -1], -1),            # large negative values
    ],
)
def test_get_max_normal_cases(arr, expected):
    """Check that get_max returns the correct maximum for non‑empty lists."""
    assert get_max(arr) == expected


def test_get_max_empty():
    """Empty list should return None."""
    assert get_max([]) is None


def test_get_max_single_element():
    """Single‑element list should return that element."""
    assert get_max([42]) == 42


def test_get_max_non_list_input():
    """Passing a non‑list should raise a TypeError (the function expects a list)."""
    with pytest.raises(TypeError):
        get_max(None)          # type: ignore[arg-type]
    with pytest.raises(TypeError):
        get_max("not a list")  # type: ignore[arg-type]


# ----------------------------------------------------------------------
# double_the_difference tests
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "lst,expected",
    [
        ([1, 3, 2, 0], 10),          # example from docstring
        ([-1, -2, 0], 0),            # all negative or zero
        ([9, -2], 81),               # single odd positive
        ([0], 0),                    # single zero
        ([], 0),                     # empty list
        ([1, 2, 3, 4, 5], 1 + 9 + 25),  # mixed odds and evens
        ([7, 7, 7], 49 + 49 + 49),   # repeated odds
        ([2, 4, 6], 0),              # only evens
        ([-3, -5, -7], 0),           # only negative odds (ignored)
        ([1.5, 3, "5", 5], 9 + 25), # non‑int types ignored
        ([True, False, 1, 3], 1 + 9), # bool is subclass of int but should be ignored
    ],
)
def test_double_the_difference_various(lst, expected):
    """Validate the sum of squares of odd, non‑negative integers."""
    assert double_the_difference(lst) == expected


def test_double_the_difference_mutability():
    """Ensure the original list is not modified."""
    original = [1, 2, 3]
    copy = original.copy()
    _ = double_the_difference(original)
    assert original == copy, "Function should not mutate its input"


def test_double_the_difference_large_numbers():
    """Stress test with large integers to verify no overflow issues."""
    large_odds = [10_001, 20_003, 30_005]
    expected = sum(x * x for x in large_odds)
    assert double_the_difference(large_odds) == expected


def test_double_the_difference_invalid_input():
    """Passing a non‑iterable should raise a TypeError."""
    with pytest.raises(TypeError):
        double_the_difference(None)          # type: ignore[arg-type]
    with pytest.raises(TypeError):
        double_the_difference(123)           # type: ignore[arg-type]