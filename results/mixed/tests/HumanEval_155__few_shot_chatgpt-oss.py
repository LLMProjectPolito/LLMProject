import pytest

# Import the functions under test.
# Adjust the import path to match the actual location of the implementation.
# For example, if the functions are defined in `my_module.py`, replace `solution`
# with `my_module`.
from solution import is_palindrome, get_max, even_odd_count


# ----------------------------------------------------------------------
# Tests for `is_palindrome`
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "input_str,expected",
    [
        ("radar", True),                # classic odd‑length palindrome
        ("level", True),                # another odd‑length palindrome
        ("deed", True),                 # even‑length palindrome
        ("", True),                     # empty string is a palindrome
        ("a", True),                    # single character
        ("hello", False),               # non‑palindrome
        ("Radar", False),               # case‑sensitive check
        ("A man, a plan, a canal: Panama", False),  # punctuation/spaces break it
        ("あいいあ", True),              # Unicode characters
        ("12321", True),                # numeric palindrome
        ("123321", True),               # even‑length numeric palindrome
        ("12345", False),               # numeric non‑palindrome
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
        ([1, 2, 3], 3),                     # simple positive numbers
        ([-1, -5, -2], -1),                 # all negative numbers
        ([42], 42),                         # single element list
        ([5, 5, 5, 5], 5),                  # all elements equal
        ([0, -1, -2, -3], 0),               # zero is the max
        (list(range(1000)), 999),           # large list
        ([-100, 0, 100, 50], 100),          # mixed signs
        ([2**31 - 1, -2**31], 2**31 - 1),   # near‑int‑overflow values
    ],
)
def test_get_max_various(arr, expected):
    """Check that `get_max` returns the correct maximum for diverse lists."""
    assert get_max(arr) == expected


def test_get_max_empty():
    """An empty list should return `None`."""
    assert get_max([]) is None


def test_get_max_mutable_input():
    """The function must not modify the original list."""
    original = [3, 1, 4, 1, 5]
    copy = original.copy()
    _ = get_max(original)
    assert original == copy, "The input list was altered by `get_max`"


# ----------------------------------------------------------------------
# Tests for `even_odd_count`
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "num,expected",
    [
        (0, (1, 0)),          # zero is an even digit
        (5, (0, 1)),          # single odd digit
        (2, (1, 0)),          # single even digit
        (123, (1, 2)),        # mixed digits
        (-12, (1, 1)),        # negative number, same as positive counterpart
        (24680, (5, 0)),      # all even digits
        (13579, (0, 5)),      # all odd digits
        (111222333, (3, 6)),  # larger number with repeats
        (9876543210, (5, 5)), # each digit appears once
    ],
)
def test_even_odd_count_various(num, expected):
    """Validate digit counting for a variety of positive and negative integers."""
    assert even_odd_count(num) == expected


def test_even_odd_count_type_error():
    """Passing a non‑integer should raise a TypeError."""
    with pytest.raises(TypeError):
        even_odd_count(12.34)   # float
    with pytest.raises(TypeError):
        even_odd_count("123")   # string
    with pytest.raises(TypeError):
        even_odd_count([1, 2, 3])  # list


def test_even_odd_count_large_number():
    """A very large integer should still be processed correctly."""
    large_num = int("9" * 1000)  # 1000 nines → all odd digits
    expected = (0, 1000)
    assert even_odd_count(large_num) == expected