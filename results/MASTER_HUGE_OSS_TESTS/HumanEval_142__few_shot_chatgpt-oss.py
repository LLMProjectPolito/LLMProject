import pytest

# Import the functions under test.
# Adjust the module name if the implementation lives in a different file.
# The tests assume the functions are defined in a module called `solution`.
from solution import is_palindrome, get_max, sum_squares


# ----------------------------------------------------------------------
# Tests for `is_palindrome`
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "input_str,expected",
    [
        ("radar", True),          # classic odd‑length palindrome
        ("level", True),          # another odd‑length palindrome
        ("deed", True),           # even‑length palindrome
        ("hello", False),         # non‑palindrome
        ("", True),               # empty string (trivially a palindrome)
        ("A", True),              # single character
        ("Radar", False),         # case‑sensitive check
        ("Madam", False),         # case‑sensitive check
        ("12321", True),          # numeric palindrome
        ("12345", False),         # numeric non‑palindrome
        ("😀🙃😀", True),          # Unicode characters palindrome
        ("😀🙃😎", False),         # Unicode non‑palindrome
        ("a man a plan a canal panama".replace(" ", ""), True),  # palindrome ignoring spaces
    ],
)
def test_is_palindrome_various(input_str, expected):
    """Validate palindrome detection across a wide range of inputs."""
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
        ([1, 2, 3], 3),                     # typical positive numbers
        ([-1, -5, -2], -1),                 # all negative numbers
        ([42], 42),                         # single element list
        ([5, 5, 5, 5], 5),                  # all equal elements
        (list(range(1000)), 999),           # large list
        ([-100, 0, 100], 100),              # mix of negative, zero, positive
    ],
)
def test_get_max_various(arr, expected):
    """Check that the maximum element is returned correctly."""
    assert get_max(arr) == expected


def test_get_max_empty():
    """Empty list should return None."""
    assert get_max([]) is None


def test_get_max_none_input():
    """Passing None should raise a TypeError (since the function expects a list)."""
    with pytest.raises(TypeError):
        get_max(None)


# ----------------------------------------------------------------------
# Tests for `sum_squares`
# ----------------------------------------------------------------------
def _expected_sum_squares(lst):
    """
    Helper that reproduces the specification of `sum_squares`
    (used to compute expected values for the tests).
    """
    total = 0
    for idx, val in enumerate(lst):
        if idx % 3 == 0:
            total += val ** 2
        elif idx % 4 == 0:
            total += val ** 3
        else:
            total += val
    return total


@pytest.mark.parametrize(
    "input_lst,expected",
    [
        ([1, 2, 3], 6),                     # example from the docstring
        ([], 0),                            # empty list
        ([-1, -5, 2, -1, -5], -126),        # example from the docstring
        ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], None),  # will compute expected via helper
        ([10], 100),                        # index 0 → square
        ([1, 2, 3, 4], None),               # mixed indices
    ],
)
def test_sum_squares_examples(input_lst, expected):
    """
    Verify the function against documented examples and a few extra cases.
    For cases where `expected` is None we compute it with the reference helper.
    """
    if expected is None:
        expected = _expected_sum_squares(input_lst)
    assert sum_squares(input_lst) == expected


def test_sum_squares_original_list_unchanged():
    """The function must not mutate the original list."""
    original = [1, 2, 3, 4, 5, 6, 7, 8]
    copy = original.copy()
    _ = sum_squares(original)
    assert original == copy, "Original list was modified"


def test_sum_squares_large_numbers():
    """Check that the function works with large integer values without overflow."""
    large_lst = [10**6, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    expected = _expected_sum_squares(large_lst)
    assert sum_squares(large_lst) == expected


def test_sum_squares_negative_and_zero():
    """Negative numbers and zeros should be handled correctly."""
    lst = [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
    expected = _expected_sum_squares(lst)
    assert sum_squares(lst) == expected


def test_sum_squares_type_errors():
    """Non‑list inputs should raise a TypeError."""
    for bad_input in (None, 123, "string", {1, 2, 3}):
        with pytest.raises(TypeError):
            sum_squares(bad_input)