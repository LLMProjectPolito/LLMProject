
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

# The function is assumed to be imported or defined in the environment.
# Since I am not allowed to redefine it, I will write the test suite 
# assuming 'file_name_check' is available in the namespace.

@pytest.mark.parametrize("valid_name", [
    "example.txt",
    "a.exe",
    "Z.dll",
    "file123.txt",      # Exactly 3 digits
    "abc.exe",          # 0 digits
    "A1b2C3.dll",       # 3 digits mixed with letters
    "LongFileName.txt", # No digits
])
def test_valid_filenames(valid_name):
    """Tests filenames that satisfy all criteria."""
    assert file_name_check(valid_name) == 'Yes'

@pytest.mark.parametrize("too_many_digits", [
    "a1234.txt",        # 4 digits
    "1234abc.exe",      # 4 digits at start
    "file1234.dll",     # 4 digits at end
    "a1b2c3d4.txt",     # 4 digits scattered
])
def test_invalid_digit_count(too_many_digits):
    """Tests that more than three digits returns 'No'."""
    assert file_name_check(too_many_digits) == 'No'

@pytest.mark.parametrize("dot_issue", [
    "filename",         # No dot
    "file.name.txt",    # Two dots
    "file..txt",        # Double dot
    "file.txt.exe",     # Multiple dots
])
def test_invalid_dot_usage(dot_issue):
    """Tests that anything other than exactly one dot returns 'No'."""
    assert file_name_check(dot_issue) == 'No'

@pytest.mark.parametrize("bad_prefix", [
    ".txt",             # Empty prefix
    "1abc.txt",         # Starts with digit
    "_abc.txt",         # Starts with underscore
    " abc.txt",         # Starts with space
    "!abc.txt",         # Starts with special char
    "a1234.txt",        # (Also tests digit rule)
])
def test_invalid_prefix(bad_prefix):
    """Tests that the prefix must be non-empty and start with a Latin letter."""
    assert file_name_check(bad_prefix) == 'No'

@pytest.mark.parametrize("bad_extension", [
    "file.pdf",         # Unsupported extension
    "file.txt1",        # Extension contains extra chars
    "file.TXT",         # Case sensitivity (requirement says 'txt', 'exe', 'dll')
    "file.exe ",        # Trailing space in extension
    "file.dll ",        # Trailing space in extension
    "file.",            # Empty extension
    "file.t",           # Incomplete extension
])
def test_invalid_extension(bad_extension):
    """Tests that the extension must be exactly 'txt', 'exe', or 'dll'."""
    assert file_name_check(bad_extension) == 'No'

def test_edge_case_empty_string():
    """Tests an entirely empty input."""
    assert file_name_check("") == 'No'

def test_edge_case_only_digits():
    """Tests a string that is only digits."""
    assert file_name_check("123") == 'No'