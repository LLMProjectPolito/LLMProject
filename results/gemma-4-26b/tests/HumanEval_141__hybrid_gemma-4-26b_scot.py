
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

# The function file_name_check is assumed to be provided by the environment.

@pytest.mark.parametrize("valid_name", [
    "example.txt",                   # Standard valid
    "A.exe",                         # Single letter prefix, uppercase
    "abc123.dll",                    # Max allowed digits (3)
    "file12a.txt",                   # Digits mixed in prefix
    "Test_File.dll",                 # Underscores in prefix
    "a.txt",                         # Minimal valid
    "LongFileNameWithNumbers123.exe",# Long name with 3 digits
    "v1.txt",                        # Single digit
    "z.txt",                         # Single letter
    "abc12.dll",                     # 2 digits
])
def test_valid_filenames(valid_name):
    """Tests all scenarios that should return 'Yes'."""
    assert file_name_check(valid_name) == 'Yes'


@pytest.mark.parametrize("bad_prefix", [
    "1example.txt",          # Starts with digit
    "_example.txt",          # Starts with underscore
    " example.txt",          # Starts with space
    "!example.exe",          # Starts with special char
    ".txt",                  # Dot at start (empty prefix)
])
def test_invalid_prefix(bad_prefix):
    """Tests that the prefix must start with a Latin letter and not be empty."""
    assert file_name_check(bad_prefix) == 'No'


@pytest.mark.parametrize("too_many_digits", [
    "a1234.txt",             # 4 digits
    "1234abc.exe",           # 4 digits at start (also fails prefix rule)
    "a1b2c3d4.dll",          # Multiple digits totaling > 3
    "test1234.pdf",          # 4 digits and wrong extension
    "abc.txt1234",           # 4 digits in suffix
])
def test_invalid_digit_count(too_many_digits):
    """Tests that more than three digits returns 'No'."""
    assert file_name_check(too_many_digits) == 'No'


@pytest.mark.parametrize("dot_issues", [
    "exampletxt",            # Zero dots
    "example.txt.bak",       # Two dots
    "my.file.exe",           # Two dots
    "file..txt",             # Double dot
    "a.b.txt",               # Multiple dots
])
def test_invalid_dot_count(dot_issues):
    """Tests that anything other than exactly one dot returns 'No'."""
    assert file_name_check(dot_issues) == 'No'


@pytest.mark.parametrize("bad_extension", [
    "example.pdf",           # Not in allowed list
    "example.png",           # Not in allowed list
    "example.TXT",           # Case sensitivity check
    "example.EXE",           # Case sensitivity check
    "example.exe1",          # Partial match/Malformed
    "example.dll ",          # Trailing space in extension
    "example.",              # Empty extension
    "abc.dll.txt",           # Multiple dots (extension logic check)
])
def test_invalid_extensions(bad_extension):
    """Tests that the extension must be exactly 'txt', 'exe', or 'dll' (lowercase)."""
    assert file_name_check(bad_extension) == 'No'


def test_empty_string():
    """Tests the edge case of an empty input string."""
    assert file_name_check("") == 'No'


@pytest.mark.parametrize("non_string", [
    None,
    123,
    4.5,
    ["example.txt"],
])
def test_non_string_input(non_string):
    """
    Tests how the function handles non-string input. 
    Expected to raise TypeError.
    """
    with pytest.raises(TypeError):
        file_name_check(non_string)