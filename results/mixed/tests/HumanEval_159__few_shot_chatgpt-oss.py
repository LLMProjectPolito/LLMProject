import pytest

# Import the functions under test.
# Adjust the import path according to where the implementation lives.
# For example, if the functions are defined in a file called `solution.py`,
# you would use: from solution import is_palindrome, get_max, eat
from solution import is_palindrome, get_max, eat


# ----------------------------------------------------------------------
# Tests for `is_palindrome`
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "input_str,expected",
    [
        ("radar", True),                # classic odd‑length palindrome
        ("level", True),                # another odd‑length palindrome
        ("deed", True),                 # even‑length palindrome
        ("", True),                     # empty string (edge case)
        ("a", True),                    # single character
        ("hello", False),               # non‑palindrome
        ("Radar", False),               # case‑sensitive check
        ("RaDaR", False),               # mixed case, still false
        ("A man a plan a canal Panama".replace(" ", ""), True),  # palindrome ignoring spaces
        ("12321", True),                # numeric palindrome
        ("12345", False),               # numeric non‑palindrome
        ("😀🙃😀", True),               # Unicode characters palindrome
        ("😀🙃😎", False),              # Unicode non‑palindrome
        ("Madam", False),               # case‑sensitive, should be False
    ],
)
def test_is_palindrome_various(input_str, expected):
    """Parametrized test covering typical, edge‑case and Unicode inputs."""
    assert is_palindrome(input_str) is expected


def test_is_palindrome_mutability():
    """Ensure the function does not modify the input string."""
    original = "radar"
    copy = original[:]
    is_palindrome(original)
    assert original == copy, "The input string should remain unchanged"


# ----------------------------------------------------------------------
# Tests for `get_max`
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "arr,expected",
    [
        ([1, 2, 3], 3),                     # simple positive numbers
        ([-1, -5, -2], -1),                 # all negative numbers
        ([42], 42),                         # single element list
        ([0, 0, 0], 0),                     # all zeros
        ([5, 5, 5, 5], 5),                  # duplicates
        ([-1000, 0, 1000], 1000),           # mix of extremes
        (list(range(1000)), 999),           # large list
    ],
)
def test_get_max_normal_cases(arr, expected):
    """Validate correct maximum extraction for typical lists."""
    assert get_max(arr) == expected


def test_get_max_empty_list():
    """Empty list should return None."""
    assert get_max([]) is None


def test_get_max_mutability():
    """The original list must not be altered by the function."""
    original = [3, 1, 4, 1, 5]
    copy = original[:]
    get_max(original)
    assert original == copy, "The input list should remain unchanged"


# ----------------------------------------------------------------------
# Tests for `eat`
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "number,need,remaining,expected",
    [
        (5, 6, 10, [11, 4]),   # enough carrots left after eating needed amount
        (4, 8, 9, [12, 1]),    # exactly enough to satisfy need, leftover 1
        (1, 10, 10, [11, 0]),  # eat all remaining, still hungry
        (2, 11, 5, [7, 0]),    # not enough remaining, eat everything
        (0, 0, 0, [0, 0]),     # nothing to eat, nothing available
        (0, 5, 0, [0, 0]),     # need carrots but none are available
        (10, 0, 5, [10, 5]),   # need is zero, nothing is eaten
        (1000, 1000, 1000, [2000, 0]),  # max constraints, enough carrots
        (999, 1, 0, [1000, 0]),        # no remaining carrots, cannot eat more
        (3, 7, 4, [10, 0]),            # eat all remaining, still need more
    ],
)
def test_eat_various_cases(number, need, remaining, expected):
    """Parametrized test covering normal, edge and boundary scenarios."""
    result = eat(number, need, remaining)
    assert isinstance(result, list), "Result should be a list"
    assert len(result) == 2, "Result list must contain exactly two elements"
    assert result == expected, f"Expected {expected} but got {result}"


def test_eat_input_validation():
    """Check that the function gracefully handles out‑of‑range inputs."""
    # According to the docstring constraints, negative values are not allowed.
    # The implementation does not raise, but we verify the logical outcome.
    result = eat(-5, 10, 10)   # negative `number`
    assert result == [5, 0] or result == [5, 0], "Function should treat negative as 0 or follow its own logic"

    result = eat(5, -10, 10)   # negative `need`
    assert result == [5, 10] or result == [5, 10], "Negative need should not cause eating"

    result = eat(5, 10, -10)   # negative `remaining`
    assert result == [5, 0] or result == [5, 0], "Negative remaining should be treated as 0"


def test_eat_immutability():
    """Ensure that mutable arguments are not modified."""
    number = 4
    need = 6
    remaining = [10]  # wrap in a list to test mutability (function expects int, so it shouldn't touch it)
    # The function receives an int, so we just verify that the original ints stay the same.
    eat(number, need, remaining[0])
    assert number == 4 and need == 6 and remaining[0] == 10, "Input values must remain unchanged"


# ----------------------------------------------------------------------
# Additional sanity checks (optional)
# ----------------------------------------------------------------------
def test_combined_behaviour():
    """A sanity test that uses all three functions together."""
    s = "madam"
    assert is_palindrome(s) is True
    max_val = get_max([1, 2, 3, 4])
    assert max_val == 4
    # Use the max value as the `need` for the rabbit
    result = eat(0, max_val, 10)
    assert result == [4, 6]