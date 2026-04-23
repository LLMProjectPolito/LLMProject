
def file_name_check(file_name):
    """Create a function which takes a string representing a file's name, and returns
    'Yes' if the the file's name is valid, and returns 'No' otherwise.
    A file's name is considered to be valid if and only if all the following conditions 
    are met:
    - There should not be more than three digits ('0'-'9') in the file's name.
    - The file's name contains exactly one dot '.'
    - The substring before the dot should not be empty, and it starts with a letter from 
    the latin alphapet ('a'-'z' and 'A'-'Z').
    - The substring after the dot should be one of these: ['txt', 'exe', 'dll']
    Examples:
    file_name_check("example.txt") # => 'Yes'
    file_name_check("1example.dll") # => 'No' (the name should start with a latin alphapet letter)
    """

import pytest

@pytest.mark.parametrize("file_name", [
    "example.txt",          # Standard valid
    "A.exe",                # Single letter prefix, uppercase
    "abc.dll",              # Standard valid
    "a123.txt",             # Exactly 3 digits (boundary)
    "z.txt",                # Minimal valid prefix
    "LongNameWith123.exe",  # Mixed alphanumeric
])
def test_valid_filenames(file_name):
    """Tests filenames that meet all criteria."""
    assert file_name_check(file_name) == 'Yes'


@pytest.mark.parametrize("file_name", [
    "a1234.txt",            # 4 digits (consecutive)
    "abc1234.dll",          # 4 digits (consecutive)
    "a1b2c3d4.txt",         # 4 digits (total, non-consecutive)
    "a123456789.txt",       # Many digits
])
def test_invalid_digit_count(file_name):
    """Tests filenames that exceed the maximum of three digits total."""
    assert file_name_check(file_name) == 'No'


@pytest.mark.parametrize("file_name", [
    "exampletxt",           # Zero dots
    "a.b.txt",              # Two dots
    "file..txt",            # Double dot
    "..",                   # Two dots (edge case)
])
def test_invalid_dot_count(file_name):
    """Tests filenames that do not have exactly one dot."""
    assert file_name_check(file_name) == 'No'


@pytest.mark.parametrize("file_name", [
    "1example.txt",         # Starts with digit
    ".txt",                 # Empty prefix
    ".",                    # Single dot (empty prefix)
    "_example.txt",         # Starts with special character
    "éxample.txt",          # Non-ASCII character
    " example.txt",         # Starts with space
    "abc def.txt",          # Whitespace in middle
])
def test_invalid_prefix(file_name):
    """Tests filenames where the prefix is invalid (empty, wrong start, or invalid middle chars)."""
    assert file_name_check(file_name) == 'No'


@pytest.mark.parametrize("file_name", [
    "example.jpg",          # Unsupported extension
    "example.TXT",          # Case sensitivity
    "a.tx",                 # Partial extension
    "a.",                   # Empty extension
])
def test_invalid_extension(file_name):
    """Tests filenames with extensions not in ['txt', 'exe', 'dll']."""
    assert file_name_check(file_name) == 'No'


@pytest.mark.parametrize("file_name", [
    "",                     # Empty input
])
def test_empty_input(file_name):
    """Tests handling of empty string input."""
    assert file_name_check(file_name) == 'No'


def test_complex_failure_cases():
    """Tests cases that fail multiple conditions simultaneously."""
    # Fails digit count AND prefix AND extension
    assert file_name_check("12345.png") == 'No'
    # Fails dot count AND extension
    assert file_name_check("abc_txt") == 'No'
    # Fails prefix AND dot count
    assert file_name_check("1.2.txt") == 'No'