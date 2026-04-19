
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

# Assuming the function file_name_check is imported from the source module
# from your_module import file_name_check

@pytest.mark.parametrize("filename", [
    "example.txt",              # Standard valid
    "document.exe",             # Standard valid
    "library.dll",              # Standard valid
    "MyFile.txt",               # Mixed case prefix
    "A.exe",                    # Minimum valid prefix length
    "file1.txt",                # 1 digit
    "file12.txt",               # 2 digits
    "file123.txt",              # 3 digits
    "a1b2c3.dll",               # 3 digits scattered, starts with letter
    "LongNameWithNoDigits.dll", # No digits (<= 3)
])
def test_file_name_valid_cases(filename):
    """Tests various filenames that satisfy all criteria."""
    assert file_name_check(filename) == 'Yes'

@pytest.mark.parametrize("filename", [
    "file1234.txt",             # 4 digits
    "12345.exe",                # 5 digits
    "a1b2c3d4.dll",             # 4 digits mixed
])
def test_file_name_digit_constraints(filename):
    """Tests the rule: no more than three digits allowed in the entire string."""
    assert file_name_check(filename) == 'No'

@pytest.mark.parametrize("filename", [
    "filename",                 # No dot
    "file.name.txt",            # Two dots
    "file..txt",                # Two dots (adjacent)
    "...",                      # Multiple dots
])
def test_file_name_dot_constraints(filename):
    """Tests the rule: exactly one dot must be present."""
    assert file_name_check(filename) == 'No'

@pytest.mark.parametrize("filename", [
    ".txt",                     # Empty prefix
    "1example.dll",             # Starts with digit
    "_example.txt",             # Starts with underscore
    " example.exe",             # Starts with space
    "!example.exe",             # Starts with special character
])
def test_file_name_prefix_constraints(filename):
    """Tests rules for the substring before the dot: not empty and must start with a letter."""
    assert file_name_check(filename) == 'No'

@pytest.mark.parametrize("filename", [
    "file.pdf",                 # Unsupported extension
    "file.jpeg",                # Unsupported extension
    "file.txt1",                # Extension too long
    "file.tx",                  # Extension too short
    "file.",                    # Empty extension
    "file.TXT",                 # Case sensitivity (must be lowercase)
    "file.dll ",                # Trailing space in extension
])
def test_file_name_extension_constraints(filename):
    """Tests the rule: extension must be exactly 'txt', 'exe', or 'dll'."""
    assert file_name_check(filename) == 'No'

def test_file_name_extreme_edge_cases():
    """Tests boundary inputs like empty strings."""
    assert file_name_check("") == 'No'