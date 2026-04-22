
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

# The function is assumed to be imported from the source module
# from solution import file_name_check

@pytest.mark.parametrize("valid_name", [
    "example.txt",          # Standard valid
    "a.exe",                # Minimum length prefix
    "File123.dll",          # Exactly 3 digits (boundary)
    "MyFile.txt",           # Mixed case prefix
    "A1.exe",               # Single letter, single digit
    "test.dll",             # Standard valid
])
def test_file_name_check_valid(valid_name):
    """Tests filenames that meet all criteria."""
    assert file_name_check(valid_name) == 'Yes'


@pytest.mark.parametrize("invalid_digits", [
    "a1234.txt",            # 4 digits (boundary + 1)
    "1234abc.exe",          # 4 digits at start
    "abc1234.dll",          # 4 digits at end
    "a1b2c3d4.txt",         # Scattered digits exceeding 3
])
def test_file_name_check_too_many_digits(invalid_digits):
    """Tests the rule: 'There should not be more than three digits'."""
    assert file_name_check(invalid_digits) == 'No'


@pytest.mark.parametrize("invalid_dots", [
    "filename",             # No dot
    "file.name.txt",        # Two dots
    "file.txt.exe",         # Multiple dots
    "file..txt",            # Double dot
    ".txt",                 # Dot at start (empty prefix)
    "file.",                # Dot at end (empty extension)
])
def test_file_name_check_dot_count(invalid_dots):
    """Tests the rule: 'The file's name contains exactly one dot'."""
    assert file_name_check(invalid_dots) == 'No'


@pytest.mark.parametrize("invalid_prefix", [
    "1example.txt",         # Starts with a digit
    "_example.txt",         # Starts with special character
    " example.txt",         # Starts with a space
    ".txt",                 # Empty prefix (already covered by dot test, but good for safety)
    "a1234.txt",            # (Already covered by digit test, but tests prefix logic)
])
def test_file_name_check_prefix_rules(invalid_prefix):
    """Tests the rule: 'Substring before dot not empty and starts with a latin letter'."""
    assert file_name_check(invalid_prefix) == 'No'


@pytest.mark.parametrize("invalid_extension", [
    "file.jpg",             # Not in allowed list
    "file.png",             # Not in allowed list
    "file.TXT",             # Case sensitivity check (prompt specifies 'txt')
    "file.exe1",            # Partial match
    "file.txt ",            # Trailing space
    "file.ex",              # Too short
    "file.dll.txt",         # Multiple dots (already covered, but tests extension logic)
])
def test_file_name_check_extension_rules(invalid_extension):
    """Tests the rule: 'Substring after the dot should be one of ['txt', 'exe', 'dll']'."""
    assert file_name_check(invalid_extension) == 'No'


def test_file_name_check_extreme_cases():
    """Tests extreme/unusual string inputs."""
    # Very long string with valid structure
    long_name = "a" * 100 + ".txt"
    assert file_name_check(long_name) == 'Yes'
    
    # String with only digits and a dot
    assert file_name_check("123.txt") == 'No' # Starts with digit
    
    # String with special characters but valid extension
    assert file_name_check("a!@#.txt") == 'Yes' # Rule only specifies start char and digit count