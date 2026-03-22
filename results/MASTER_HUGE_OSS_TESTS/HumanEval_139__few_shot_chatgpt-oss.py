import pytest

# ----------------------------------------------------------------------
# Import the functions under test.
# If the functions live in a different module, replace the import line
# with the appropriate module name, e.g.:
#   from my_module import is_palindrome, get_max, special_factorial
# ----------------------------------------------------------------------
from . import is_palindrome, get_max, special_factorial


# ----------------------------------------------------------------------
# is_palindrome tests
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "input_str,expected",
    [
        ("radar", True),          # simple palindrome
        ("hello", False),         # simple non‑palindrome
        ("", True),               # empty string
        ("Radar", False),         # case‑sensitive check
        ("A", True),              # single character
        ("Able was I ere I saw Elba", False),  # mixed case, spaces not ignored
        ("あいいあ", True),        # Unicode palindrome
        ("12321", True),          # numeric characters
        ("12345", False),         # numeric non‑palindrome
        ("!@#@@#@!", True),       # punctuation palindrome
    ],
)
def test_is_palindrome_various(input_str, expected):
    """Run a battery of palindrome checks."""
    assert is_palindrome(input_str) is expected


# ----------------------------------------------------------------------
# get_max tests
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "arr,expected",
    [
        ([1, 2, 3], 3),                     # positive numbers
        ([-1, -5, -2], -1),                 # all negative
        ([42], 42),                         # single element
        ([], None),                         # empty list
        ([5, 5, 5, 5], 5),                  # all equal
        (list(range(1000)), 999),           # large list
        ([-100, 0, 100], 100),              # mixed sign
        ([2**31, -2**31, 0], 2**31),        # very large integers
    ],
)
def test_get_max_various(arr, expected):
    """Validate get_max on a variety of inputs."""
    assert get_max(arr) == expected


# ----------------------------------------------------------------------
# special_factorial tests
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "n,expected",
    [
        (1, 1),          # 1! = 1
        (2, 2),          # 2! * 1! = 2 * 1
        (3, 12),         # 3! * 2! * 1! = 6 * 2 * 1
        (4, 288),        # example from the docstring
        (5, 34_560),     # 5! * 4! * 3! * 2! * 1!
        (6, 2_985_984),  # 6! * 5! * ... * 1!
    ],
)
def test_special_factorial_correctness(n, expected):
    """Check that the special factorial matches the mathematically expected value."""
    assert special_factorial(n) == expected


def test_special_factorial_invalid_input():
    """The function is defined only for n > 0. Verify that invalid inputs raise."""
    with pytest.raises(ValueError):
        special_factorial(0)

    with pytest.raises(ValueError):
        special_factorial(-3)

    # Non‑integer types should also be rejected (TypeError is a reasonable choice)
    with pytest.raises(TypeError):
        special_factorial(3.5)

    with pytest.raises(TypeError):
        special_factorial("4")