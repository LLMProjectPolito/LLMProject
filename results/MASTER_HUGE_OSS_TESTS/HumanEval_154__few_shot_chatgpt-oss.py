import pytest

# Import the functions under test.
# Adjust the import path according to where the implementation lives.
# For example, if the functions are defined in a file named `solution.py`,
# the import would be: from solution import is_palindrome, get_max, cycpattern_check
from solution import is_palindrome, get_max, cycpattern_check


# ----------------------------------------------------------------------
# Tests for `is_palindrome`
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "input_str,expected",
    [
        ("radar", True),                     # classic odd‑length palindrome
        ("level", True),                     # another odd‑length palindrome
        ("deed", True),                      # even‑length palindrome
        ("", True),                          # empty string (vacuously a palindrome)
        ("a", True),                         # single character
        ("hello", False),                    # non‑palindrome
        ("Radar", False),                    # case‑sensitive check
        ("RaDaR", False),                    # mixed case, still false
        ("12321", True),                     # numeric palindrome
        ("12345", False),                    # numeric non‑palindrome
        ("A man, a plan, a canal: Panama", False),  # punctuation/spaces – false because function is literal
        ("😀🙃😀", True),                     # Unicode characters
        ("😀🙃😎", False),                    # Unicode non‑palindrome
        ("   ", True),                       # spaces only – palindrome
        ("abccba", True),                    # even length palindrome
        ("abcba", True),                     # odd length palindrome
        ("abca", False),                     # near‑palindrome
    ],
)
def test_is_palindrome_various(input_str, expected):
    """Parametrized test covering typical, edge‑case and Unicode inputs."""
    assert is_palindrome(input_str) is expected


def test_is_palindrome_long_string():
    """A long palindrome should still be detected correctly."""
    long_pal = "a" * 1000 + "b" + "a" * 1000
    assert is_palindrome(long_pal) is True

    long_non_pal = "a" * 2000 + "b"
    assert is_palindrome(long_non_pal) is False


# ----------------------------------------------------------------------
# Tests for `get_max`
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "arr,expected",
    [
        ([1, 2, 3], 3),                      # simple positive numbers
        ([-1, -5, -2], -1),                  # all negative numbers
        ([], None),                         # empty list returns None
        ([42], 42),                          # single element list
        ([5, 5, 5, 5], 5),                   # all equal elements
        ([-10, 0, 10, 20, -20], 20),         # mixed signs
        (list(range(1000)), 999),           # large list
        ([-1000, -500, -1, -999], -1),       # large negative numbers
    ],
)
def test_get_max_various(arr, expected):
    """Parametrized test for typical, edge‑case and large inputs."""
    assert get_max(arr) == expected


def test_get_max_mutability():
    """Ensure the original list is not altered by `get_max`."""
    original = [3, 1, 4, 1, 5, 9]
    copy = original.copy()
    _ = get_max(original)
    assert original == copy, "The input list should remain unchanged"


# ----------------------------------------------------------------------
# Tests for `cycpattern_check`
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "a,b,expected",
    [
        ("abcd", "abd", False),          # no rotation matches
        ("hello", "ell", True),          # substring without rotation
        ("whassup", "psus", False),      # rotation exists but not a substring
        ("abab", "baa", True),           # rotation "aab" is a substring of "abab"
        ("efef", "eeff", False),         # rotation exists but not a substring
        ("himenss", "simen", True),      # rotation "mensi" appears in "himenss"
        ("abcde", "cdeab", True),        # full rotation matches whole string
        ("abcde", "deabc", True),        # another full rotation
        ("abcde", "eabcd", True),        # rotation at the end
        ("abcde", "abcdf", False),       # same length but different char
        ("", "", True),                  # both empty strings – vacuously true
        ("", "a", False),                # empty first string cannot contain anything
        ("a", "", True),                 # empty pattern is always a substring
        ("a", "a", True),                # single‑character match
        ("a", "b", False),               # single‑character mismatch
        ("aaaaa", "aa", True),           # repeated characters, many possible rotations
        ("abcabcabc", "cab", True),      # rotation appears multiple times
        ("xyz", "zyx", True),            # reverse is a rotation of length‑3 string
        ("xyz", "zxy", True),            # rotation that is not the original order
        ("xyz", "yxz", False),           # not a rotation
        ("😀🙃😀", "🙃😀😀", True),        # Unicode rotation match
        ("😀🙃😀", "😀😀🙃", False),       # Unicode rotation not present
    ],
)
def test_cycpattern_check_various(a, b, expected):
    """Parametrized test covering the examples and many edge cases."""
    assert cycpattern_check(a, b) is expected


def test_cycpattern_check_long_strings():
    """Stress test with long strings and many possible rotations."""
    base = "abcd" * 250   # 1000 characters
    pattern = "cdab"
    # pattern is a rotation of base and appears many times
    assert cycpattern_check(base, pattern) is True

    # a pattern that is a rotation but does NOT appear as a substring
    pattern_not_present = "dabc"
    # In this particular construction, "dabc" also appears, so we modify:
    base2 = "ab" * 500 + "cd" * 500
    assert cycpattern_check(base2, "dcab") is False


def test_cycpattern_check_no_side_effects():
    """Ensure the function does not mutate its inputs."""
    a = "original"
    b = "rigi"
    a_copy = a[:]
    b_copy = b[:]
    _ = cycpattern_check(a, b)
    assert a == a_copy and b == b_copy, "Inputs should remain unchanged"