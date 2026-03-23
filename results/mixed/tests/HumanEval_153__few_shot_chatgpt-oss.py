import pytest

# Import the functions that are defined in the solution file.
# Adjust the import path if the implementation lives in a different module.
from solution import is_palindrome, get_max, Strongest_Extension


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
        ("Able was I ere I saw ElbA", False),  # mixed case, spaces not ignored
        ("madamimadam", True),    # even length palindrome
        ("😀🙃😀", True),          # Unicode characters
    ],
)
def test_is_palindrome(input_str, expected):
    assert is_palindrome(input_str) is expected


# ----------------------------------------------------------------------
# Tests for `get_max`
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "arr,expected",
    [
        ([1, 2, 3], 3),                     # all positive
        ([-1, -5, -2], -1),                 # all negative
        ([-10, 0, 10], 10),                 # mixed signs
        ([42], 42),                         # single element
        ([], None),                         # empty list returns None
    ],
)
def test_get_max(arr, expected):
    assert get_max(arr) == expected


# ----------------------------------------------------------------------
# Tests for `Strongest_Extension`
# ----------------------------------------------------------------------
def test_strongest_extension_basic():
    # Example from the docstring
    result = Strongest_Extension(
        "Slices",
        ["SErviNGSliCes", "Cheese", "StuFfed"]
    )
    assert result == "Slices.SErviNGSliCes"


def test_strongest_extension_tie():
    # Two extensions with identical strength; the first one should win.
    result = Strongest_Extension(
        "my_class",
        ["Aa", "Bb"]          # both have CAP=1, SM=1 → strength 0
    )
    assert result == "my_class.Aa"


def test_strongest_extension_all_upper():
    # Upper‑case letters increase strength.
    result = Strongest_Extension(
        "Demo",
        ["XYZ", "AB"]
    )
    # XYZ: CAP=3, SM=0 → strength 3 ; AB: strength 2
    assert result == "Demo.XYZ"


def test_strongest_extension_all_lower():
    # All lower‑case letters give negative strength.
    result = Strongest_Extension(
        "Demo",
        ["abc", "de"]
    )
    # abc: CAP=0, SM=3 → -3 ; de: -2 → de is stronger (less negative)
    assert result == "Demo.de"


def test_strongest_extension_mixed_complex():
    # More elaborate mix of cases.
    extensions = [
        "aBcDeF",   # CAP=3, SM=3 → 0
        "GHIj",     # CAP=3, SM=1 → 2
        "klMN",     # CAP=2, SM=2 → 0
        "opqr",     # CAP=0, SM=4 → -4
    ]
    result = Strongest_Extension("Complex", extensions)
    assert result == "Complex.GHIj"


def test_strongest_extension_empty_list():
    # The function is not defined for an empty list; we expect a clear error.
    with pytest.raises(ValueError):
        Strongest_Extension("Empty", [])


def test_strongest_extension_non_string_items():
    # Non‑string items should raise a TypeError (implementation dependent).
    with pytest.raises(TypeError):
        Strongest_Extension("Bad", [123, None])