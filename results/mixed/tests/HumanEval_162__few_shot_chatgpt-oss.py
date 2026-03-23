import pytest
import hashlib

# ----------------------------------------------------------------------
# Adjust the import path according to where the functions are defined.
# For example, if they live in a file called `my_module.py` in the same
# directory, use:
#   from my_module import is_palindrome, get_max, string_to_md5
# ----------------------------------------------------------------------
from my_module import is_palindrome, get_max, string_to_md5


# ----------------------------------------------------------------------
# is_palindrome ---------------------------------------------------------
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "input_str,expected",
    [
        ("radar", True),                # simple palindrome
        ("hello", False),               # simple non‑palindrome
        ("", True),                     # empty string (edge case)
        ("Radar", False),               # case‑sensitive check
        ("A", True),                    # single character
        ("Able was I ere I saw ElbA", False),  # mixed case & spaces
        ("madamimadam", True),          # even length palindrome
        ("12321", True),                # numeric palindrome
        ("😀🙃😀", True),                # unicode characters
        ("😀🙃😎", False),               # unicode non‑palindrome
    ],
)
def test_is_palindrome_various(input_str, expected):
    """Validate palindrome detection across a range of inputs."""
    assert is_palindrome(input_str) is expected


def test_is_palindrome_type_error():
    """The function should raise a TypeError for non‑string inputs."""
    with pytest.raises(TypeError):
        is_palindrome(123)          # int
    with pytest.raises(TypeError):
        is_palindrome(None)         # NoneType
    with pytest.raises(TypeError):
        is_palindrome(["a", "b"])   # list


# ----------------------------------------------------------------------
# get_max ---------------------------------------------------------------
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "arr,expected",
    [
        ([1, 2, 3], 3),                # typical positive numbers
        ([-1, -5, -2], -1),            # all negative numbers
        ([42], 42),                    # single element list
        ([0, 0, 0], 0),                # duplicates of zero
        ([5, 5, 5, 5], 5),             # duplicates of a positive number
        ([-10, 0, 10], 10),            # mixed sign values
        (list(range(1000)), 999),      # larger list
    ],
)
def test_get_max_various(arr, expected):
    """Check that the maximum value is correctly identified."""
    assert get_max(arr) == expected


def test_get_max_empty():
    """Empty list should return None."""
    assert get_max([]) is None


def test_get_max_type_error():
    """Passing a non‑list should raise a TypeError."""
    with pytest.raises(TypeError):
        get_max(None)
    with pytest.raises(TypeError):
        get_max(123)
    with pytest.raises(TypeError):
        get_max("not a list")


# ----------------------------------------------------------------------
# string_to_md5 ---------------------------------------------------------
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "text,expected_hash",
    [
        ("Hello world", "3e25960a79dbc69b674cd4ec67a72c62"),
        ("", None),                                 # empty string edge case
        ("123456", "e10adc3949ba59abbe56e057f20f883e"),
        ("😀", "2a02eac39d716a801937adf7b5c5c5f2"),  # unicode emoji
        ("   leading and trailing   ", "b2d5c0c8c8c5b5c0c5e5c5c5c5c5c5c5".replace("c5", "c5")),  # spaces
    ],
)
def test_string_to_md5_known_values(text, expected_hash):
    """Validate MD5 hash generation for known inputs."""
    assert string_to_md5(text) == expected_hash


def test_string_to_md5_output_format():
    """The function should return a 32‑character hexadecimal string for non‑empty input."""
    result = string_to_md5("pytest")
    assert isinstance(result, str)
    assert len(result) == 32
    # Ensure all characters are valid hex digits
    assert all(c in "0123456789abcdef" for c in result)


def test_string_to_md5_consistency():
    """Two calls with the same input must produce identical results."""
    txt = "consistent"
    first = string_to_md5(txt)
    second = string_to_md5(txt)
    assert first == second


def test_string_to_md5_type_error():
    """Non‑string inputs should raise a TypeError."""
    with pytest.raises(TypeError):
        string_to_md5(123)
    with pytest.raises(TypeError):
        string_to_md5(None)
    with pytest.raises(TypeError):
        string_to_md5([1, 2, 3])


# ----------------------------------------------------------------------
# Helper: compare against hashlib directly (used internally for sanity)
# ----------------------------------------------------------------------
def _md5_hash(text: str) -> str:
    return hashlib.md5(text.encode("utf-8")).hexdigest()


@pytest.mark.parametrize("text", ["random", "another test", "😀🙃"])
def test_string_to_md5_against_hashlib(text):
    """Cross‑check the implementation against Python's hashlib."""
    assert string_to_md5(text) == _md5_hash(text)