import pytest

# Import the functions to be tested.
# Adjust the import path if the implementation lives in a different module.
# For example, if the functions are defined in `solution.py`, use:
# from solution import is_palindrome, get_max, sorted_list_sum
from solution import is_palindrome, get_max, sorted_list_sum


# ----------------------------------------------------------------------
# Tests for `is_palindrome`
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "input_str,expected",
    [
        ("radar", True),          # classic odd‑length palindrome
        ("level", True),
        ("deified", True),
        ("hello", False),         # simple non‑palindrome
        ("world", False),
        ("", True),               # empty string is a palindrome by definition
        ("a", True),              # single character
        ("Radar", False),         # case‑sensitive check
        ("Madam", False),
        ("12321", True),          # numeric characters are treated as normal chars
        ("12345", False),
        ("A man a plan a canal Panama".replace(" ", ""), False),  # spaces removed, still case‑sensitive
    ],
)
def test_is_palindrome_various(input_str, expected):
    """Parametrized test covering typical, edge‑case and case‑sensitive inputs."""
    assert is_palindrome(input_str) is expected


def test_is_palindrome_mutability():
    """Ensure the function does not modify the original string (strings are immutable, but we check anyway)."""
    original = "radar"
    copy = original[:]
    assert is_palindrome(original) is True
    # The original should stay unchanged
    assert original == copy


# ----------------------------------------------------------------------
# Tests for `get_max`
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "arr,expected",
    [
        ([1, 2, 3], 3),                     # positive numbers
        ([-1, -5, -2], -1),                 # all negative numbers
        ([0, -1, 5, 3], 5),                 # mix of zero, negative and positive
        ([42], 42),                         # single element list
        ([-100, -100, -100], -100),         # duplicates of the same negative value
        ([5, 5, 5, 5], 5),                  # duplicates of the same positive value
    ],
)
def test_get_max_normal_cases(arr, expected):
    """Test typical non‑empty lists."""
    assert get_max(arr) == expected


def test_get_max_empty_list():
    """The function should return `None` for an empty list."""
    assert get_max([]) is None


def test_get_max_mutability():
    """The original list must stay unchanged after the call."""
    original = [3, 1, 4, 1, 5]
    copy = original[:]
    _ = get_max(original)
    assert original == copy


# ----------------------------------------------------------------------
# Tests for `sorted_list_sum`
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "input_lst,expected",
    [
        # Basic examples from the docstring
        (["aa", "a", "aaa"], ["aa"]),
        (["ab", "a", "aaa", "cd"], ["ab", "cd"]),
        # All even‑length strings, already sorted
        (["aa", "bb", "cc"], ["aa", "bb", "cc"]),
        # All even‑length strings, unsorted – should be sorted by length then alphabetically
        (["bbbb", "aa", "ccc", "dd"], ["aa", "dd", "ccc", "bbbb"]),
        # Duplicates should be preserved
        (["aa", "bb", "aa", "c"], ["aa", "aa", "bb"]),
        # Mixed case – sorting is case‑sensitive (ASCII order)
        (["Ab", "aB", "ab", "AB"], ["AB", "Ab", "aB", "ab"]),
        # Empty input list
        ([], []),
        # No even‑length strings – result should be empty
        (["a", "bbb", "cde"], []),
        # Strings with same length but different alphabetical order
        (["dog", "cat", "bat"], ["bat", "cat", "dog"]),
        # Long strings
        (["longword", "short", "tiny", "medium"], ["medium", "longword"]),
    ],
)
def test_sorted_list_sum_various(input_lst, expected):
    """
    Verify that:
    * odd‑length strings are removed,
    * the remaining strings are sorted by length (ascending),
    * ties are broken alphabetically,
    * duplicates are kept,
    * the original list is not mutated.
    """
    original_copy = input_lst[:]
    result = sorted_list_sum(input_lst)
    assert result == expected
    # Ensure the function does not modify the original list
    assert input_lst == original_copy


def test_sorted_list_sum_all_even_lengths():
    """When all strings have even length, only sorting should happen."""
    lst = ["zzzz", "aa", "bbbb", "c"]
    # After removing odd length ("c"), we expect sorting by length then alphabetically
    expected = ["aa", "bbbb", "zzzz"]
    assert sorted_list_sum(lst) == expected


def test_sorted_list_sum_all_odd_lengths():
    """When every string has odd length, the result must be an empty list."""
    lst = ["a", "bbb", "ccccc"]
    assert sorted_list_sum(lst) == []


def test_sorted_list_sum_mutability():
    """The function should return a new list and leave the input untouched."""
    lst = ["ab", "c", "de", "fgh"]
    copy = lst[:]
    result = sorted_list_sum(lst)
    # Result is a new list (different object)
    assert result is not lst
    # Original list unchanged
    assert lst == copy