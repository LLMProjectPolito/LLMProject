import pytest

# Adjust the import path according to where the functions are defined.
# If the functions live in a file called `solution.py` in the same directory,
# the following import works.  Change `solution` to the appropriate module name
# if needed.
from solution import is_palindrome, get_max, file_name_check


# ----------------------------------------------------------------------
# Tests for `is_palindrome`
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("radar", True),                     # classic palindrome
        ("hello", False),                    # simple non‑palindrome
        ("", True),                          # empty string (trivially palindrome)
        ("a", True),                         # single character
        ("Able was I ere I saw ElbA", False),# case‑sensitive check
        ("Aba", False),                      # case‑sensitive check
        ("12321", True),                     # numeric palindrome
        ("123321", True),                    # even‑length numeric palindrome
        ("12345", False),                    # numeric non‑palindrome
        ("😀🙃😀", True),                     # Unicode characters palindrome
        ("😀🙃😎", False),                    # Unicode non‑palindrome
        ("  ", True),                        # spaces only (two spaces)
        (" a ", True),                       # spaces around a single letter
        ("ab ba", False),                    # internal space makes it non‑palindrome
    ],
)
def test_is_palindrome_various(input_str, expected):
    """Parametrized test covering typical, edge‑case and Unicode inputs."""
    assert is_palindrome(input_str) is expected


# ----------------------------------------------------------------------
# Tests for `get_max`
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "arr, expected",
    [
        ([1, 2, 3], 3),                      # simple positive numbers
        ([-1, -5, -2], -1),                  # all negative numbers
        ([0], 0),                            # single element list
        ([5, 5, 5], 5),                      # all equal elements
        ([-10, 0, 10], 10),                  # mix of negative, zero, positive
        (list(range(1000)), 999),            # large list
        ([-100, -50, -1, -99], -1),          # max is the least negative
        ([2**31 - 1, -2**31], 2**31 - 1),    # extreme 32‑bit ints
    ],
)
def test_get_max_normal_cases(arr, expected):
    """Check that `get_max` returns the correct maximum for typical lists."""
    assert get_max(arr) == expected


def test_get_max_empty():
    """Empty list should return ``None``."""
    assert get_max([]) is None


def test_get_max_mutable_input_not_modified():
    """The function must not mutate the original list."""
    original = [3, 1, 4, 1, 5]
    copy = original.copy()
    _ = get_max(original)
    assert original == copy, "Original list was altered by get_max"


# ----------------------------------------------------------------------
# Tests for `file_name_check`
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "file_name, expected",
    [
        ("example.txt", "Yes"),               # basic valid case
        ("myProgram.exe", "Yes"),             # another valid extension
        ("lib.dll", "Yes"),                   # third valid extension
        ("a.txt", "Yes"),                     # minimal valid name (1 letter)
        ("Abc123.txt", "Yes"),                # exactly three digits allowed
        ("Abc12.txt", "Yes"),                 # fewer than three digits
        ("Abc.txt", "Yes"),                   # no digits
        ("Abc1234.txt", "No"),                # four digits – too many
        ("Abc1.2.txt", "No"),                 # dot inside the name part
        ("Abc..txt", "No"),                   # more than one dot
        (".txt", "No"),                       # empty name before dot
        ("1example.dll", "No"),               # starts with a digit
        ("_example.dll", "No"),               # starts with non‑letter symbol
        ("example", "No"),                    # missing dot/extension
        ("example.", "No"),                   # empty extension
        ("example.pdf", "No"),                # unsupported extension
        ("example.TXT", "No"),                # case‑sensitive extension (only lower‑case allowed)
        ("example .txt", "No"),               # space before dot (invalid name part)
        ("example .txt", "No"),               # space after name part
        ("example .txt", "No"),               # repeated to emphasize whitespace handling
        ("ex ample.txt", "Yes"),              # spaces inside name part are allowed (not prohibited)
        ("ex-ample.txt", "Yes"),              # hyphen inside name part is allowed
        ("ex_ample.txt", "Yes"),              # underscore inside name part is allowed
    ],
)
def test_file_name_check_various(file_name, expected):
    """Comprehensive parametrized test for the file name validation rules."""
    assert file_name_check(file_name) == expected


def test_file_name_check_digit_boundary():
    """Explicitly test the three‑digit boundary."""
    # Exactly three digits – should be accepted
    assert file_name_check("Abc123.txt") == "Yes"
    # Four digits – should be rejected
    assert file_name_check("Abc1234.txt") == "No"


def test_file_name_check_multiple_dots():
    """Only a single dot separating name and extension is allowed."""
    assert file_name_check("my.file.txt") == "No"
    assert file_name_check("myfile..txt") == "No"


def test_file_name_check_non_string_input():
    """If a non‑string is passed, the function should raise a TypeError (defensive)."""
    with pytest.raises(TypeError):
        file_name_check(123)          # integer
    with pytest.raises(TypeError):
        file_name_check(None)         # NoneType
    with pytest.raises(TypeError):
        file_name_check(["a.txt"])    # list


# ----------------------------------------------------------------------
# End of test suite
# ----------------------------------------------------------------------