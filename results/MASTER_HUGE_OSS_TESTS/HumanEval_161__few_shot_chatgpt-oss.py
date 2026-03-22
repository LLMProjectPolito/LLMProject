# tests/test_solution.py
import pytest

# Import the functions to be tested.
# Adjust the import path if the implementation resides in a different module.
from solution import is_palindrome, get_max, solve


# ----------------------------------------------------------------------
# Tests for `is_palindrome`
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "input_str,expected",
    [
        ("radar", True),          # classic palindrome
        ("hello", False),         # non‑palindrome
        ("", True),               # empty string is a palindrome
        ("Radar", False),         # case‑sensitive check
        ("A", True),              # single character
        ("aa", True),             # two identical chars
        ("ab", False),            # two different chars
        ("Able was I ere I saw ElbA", False),  # spaces & mixed case → not palindrome
        ("madamimadam", True),    # even length palindrome
        ("😀🙃😀", True),          # Unicode characters
        ("12321", True),          # numeric palindrome
        ("12345", False),         # numeric non‑palindrome
    ],
)
def test_is_palindrome_various(input_str, expected):
    """Parametrized test covering typical, edge‑case and Unicode inputs."""
    assert is_palindrome(input_str) is expected


def test_is_palindrome_mutability():
    """Ensure the function does not modify the original string."""
    original = "radar"
    _ = is_palindrome(original)
    assert original == "radar"


# ----------------------------------------------------------------------
# Tests for `get_max`
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "arr,expected",
    [
        ([1, 2, 3], 3),                     # simple positive numbers
        ([-1, -5, -2], -1),                 # all negative numbers
        ([42], 42),                         # single element list
        ([0, 0, 0], 0),                     # all equal elements
        ([-10, 0, 10, 5], 10),              # mixed sign numbers
        (list(range(1000)), 999),           # large list
        ([2**31 - 1, -2**31], 2**31 - 1),   # boundary 32‑bit ints
    ],
)
def test_get_max_various(arr, expected):
    """Parametrized test for typical and boundary integer lists."""
    assert get_max(arr) == expected


def test_get_max_empty():
    """Empty list should return None."""
    assert get_max([]) is None


def test_get_max_none_input():
    """Passing None should raise a TypeError (function expects a list)."""
    with pytest.raises(TypeError):
        get_max(None)   # type: ignore[arg-type]


# ----------------------------------------------------------------------
# Tests for `solve`
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "s,expected",
    [
        ("1234", "4321"),               # only digits → reversed
        ("ab", "AB"),                   # only letters → case flipped
        ("AB", "ab"),                   # only uppercase letters
        ("#a@C", "#A@c"),               # mixed letters & symbols
        ("!@#$", "$#@!"),               # no letters → reversed
        ("", ""),                       # empty string → empty
        ("a", "A"),                     # single lower‑case letter
        ("Z", "z"),                     # single upper‑case letter
        ("Hello, World!", "hELLO, wORLD!"),  # sentence with punctuation
        ("123abcXYZ!", "123ABCxyz!"),   # digits + mixed case letters
        ("   ", "   "),                 # spaces only (no letters) → reversed (same)
        ("ß", "SS"),                    # German sharp s – Python's upper() yields "SS"
        ("ǅ", "ǆ"),                     # Latin digraph – case flip works
    ],
)
def test_solve_various(s, expected):
    """Parametrized test covering all branches of `solve`."""
    assert solve(s) == expected


def test_solve_no_letter_reverse():
    """String without any alphabetic characters must be reversed unchanged."""
    s = "123!@#"
    assert solve(s) == s[::-1]


def test_solve_all_letters_case_flip():
    """When the string consists solely of letters, each character's case must be flipped."""
    s = "PythonTesting"
    expected = "pYTHONtESTING"
    assert solve(s) == expected


def test_solve_immutability():
    """`solve` should not modify the original string object."""
    original = "AbC123"
    _ = solve(original)
    assert original == "AbC123"


def test_solve_type_error():
    """Passing a non‑string argument should raise a TypeError."""
    with pytest.raises(TypeError):
        solve(123)   # type: ignore[arg-type]