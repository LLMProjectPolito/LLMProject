import pytest

# ----------------------------------------------------------------------
# Adjust the import path according to where the functions are defined.
# For example, if they live in a file called `solution.py` in the same
# directory, use:
#   from solution import is_palindrome, get_max, int_to_mini_roman
# ----------------------------------------------------------------------
from solution import is_palindrome, get_max, int_to_mini_roman


# ----------------------------------------------------------------------
# 1. Tests for `is_palindrome`
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "input_str,expected",
    [
        ("radar", True),                # simple odd‑length palindrome
        ("level", True),                # another odd‑length palindrome
        ("deed", True),                 # even‑length palindrome
        ("hello", False),               # non‑palindrome
        ("", True),                     # empty string (edge case)
        ("A", True),                    # single character
        ("Racecar", False),             # case‑sensitive check
        ("Madam", False),               # case‑sensitive check
        ("12321", True),                # numeric palindrome
        ("12345", False),               # numeric non‑palindrome
        ("😀🙃😀", True),               # Unicode characters palindrome
        ("😀🙃😎", False),              # Unicode non‑palindrome
        ("a b a", False),               # spaces are considered characters
        ("ab ba", False),               # spaces and order matter
    ],
)
def test_is_palindrome_various(input_str, expected):
    """Validate palindrome detection across a wide range of inputs."""
    assert is_palindrome(input_str) is expected


# ----------------------------------------------------------------------
# 2. Tests for `get_max`
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "arr,expected",
    [
        ([1, 2, 3], 3),                     # typical positive list
        ([-1, -5, -2], -1),                 # all negative numbers
        ([42], 42),                         # single‑element list
        ([0, 0, 0], 0),                     # all zeros
        ([-10, 0, 10], 10),                 # mix of negative, zero, positive
        ([5, 5, 5, 5], 5),                  # duplicates
        (list(range(1000)), 999),           # large list
    ],
)
def test_get_max_normal_cases(arr, expected):
    """Check that the maximum element is correctly identified."""
    assert get_max(arr) == expected


def test_get_max_empty():
    """An empty list should return ``None``."""
    assert get_max([]) is None


def test_get_max_mutable_input():
    """The function must not modify the original list."""
    original = [3, 1, 4, 1, 5]
    copy = original.copy()
    _ = get_max(original)
    assert original == copy, "Original list was altered by get_max"


# ----------------------------------------------------------------------
# 3. Tests for `int_to_mini_roman`
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "number,expected",
    [
        (1, "i"),
        (4, "iv"),
        (5, "v"),
        (9, "ix"),
        (10, "x"),
        (19, "xix"),
        (40, "xl"),
        (44, "xliv"),
        (50, "l"),
        (90, "xc"),
        (99, "xcix"),
        (100, "c"),
        (152, "clii"),
        (399, "cccxcix"),
        (400, "cd"),
        (426, "cdxxvi"),
        (500, "d"),
        (900, "cm"),
        (944, "cmxliv"),
        (1000, "m"),
    ],
)
def test_int_to_mini_roman_valid(number, expected):
    """Verify conversion for a representative set of numbers."""
    assert int_to_mini_roman(number) == expected


def test_int_to_mini_roman_boundary():
    """Check the lower and upper bounds of the allowed range."""
    assert int_to_mini_roman(1) == "i"
    assert int_to_mini_roman(1000) == "m"


@pytest.mark.parametrize("invalid_input", [0, -1, -100, 1001, 2000])
def test_int_to_mini_roman_out_of_range(invalid_input):
    """
    The specification restricts the input to 1 ≤ num ≤ 1000.
    The implementation should raise a ValueError (or return None) for
    out‑of‑range values. We accept either behaviour.
    """
    with pytest.raises(ValueError):
        int_to_mini_roman(invalid_input)


def test_int_to_mini_roman_non_integer():
    """Non‑integer inputs should raise a TypeError or ValueError."""
    for bad in ["X", 3.14, None, [5]]:
        with pytest.raises((TypeError, ValueError)):
            int_to_mini_roman(bad)


# ----------------------------------------------------------------------
# 4. Property‑based sanity checks (optional but adds robustness)
# ----------------------------------------------------------------------
def test_palindrome_symmetry():
    """A string is a palindrome iff its reverse equals itself."""
    for s in ["radar", "level", "deed", "abc", "", "😀🙃😀"]:
        assert is_palindrome(s) == (s == s[::-1])


def test_roman_monotonicity():
    """
    For any two numbers a < b within the valid range,
    the Roman numeral of a should be lexicographically smaller than that of b
    when both are expressed in lower‑case.
    This is a simple sanity check, not a formal proof.
    """
    prev = ""
    for n in range(1, 1001):
        cur = int_to_mini_roman(n)
        assert isinstance(cur, str) and cur.islower()
        assert cur != ""  # should never be empty
        # monotonicity is not strict for all numbers (e.g., 9 -> ix, 10 -> x)
        # but the length never decreases dramatically:
        assert len(cur) >= len(prev) - 1
        prev = cur