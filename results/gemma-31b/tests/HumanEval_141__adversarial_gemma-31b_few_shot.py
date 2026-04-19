
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

# The function to be tested
def file_name_check(file_name):
    """
    Implementation provided for context to ensure tests are meaningful.
    (The QA engineer tests against the requirements provided in the docstring).
    """
    # Condition 2: Exactly one dot
    if file_name.count('.') != 1:
        return 'No'
    
    prefix, extension = file_name.split('.')
    
    # Condition 3: Prefix not empty and starts with a latin letter
    if not prefix or not prefix[0].isalpha():
        return 'No'
    
    # Condition 1: Not more than three digits in the whole file name
    digit_count = sum(c.isdigit() for c in file_name)
    if digit_count > 3:
        return 'No'
    
    # Condition 4: Extension must be one of ['txt', 'exe', 'dll']
    if extension not in ['txt', 'exe', 'dll']:
        return 'No'
    
    return 'Yes'

# --- Pytest Suite ---

@pytest.mark.parametrize("valid_name", [
    "example.txt",          # Basic valid
    "MyFile.exe",           # Uppercase start
    "test123.dll",          # Exactly 3 digits
    "a.txt",                # Minimum valid prefix
    "document1.txt",        # Single digit
    "file.dll",             # No digits
    "VeryLongFileName12.exe" # Multiple digits (< 3)
])
def test_file_name_valid(valid_name):
    """Tests cases that should return 'Yes'."""
    assert file_name_check(valid_name) == 'Yes'

@pytest.mark.parametrize("invalid_prefix", [
    "1example.dll",         # Starts with digit
    "_file.txt",            # Starts with underscore
    ".txt",                 # Empty prefix
    " file.exe",            # Starts with space
    "!.dll",                # Starts with special char
])
def test_file_name_invalid_prefix(invalid_prefix):
    """Tests Condition 3: Prefix must start with a latin letter and not be empty."""
    assert file_name_check(invalid_prefix) == 'No'

@pytest.mark.parametrize("invalid_extension", [
    "file.pdf",             # Unsupported extension
    "file.txt1",            # Extension too long
    "file.t",               # Extension too short
    "file.TXT",             # Case sensitivity check (should be 'No' based on provided list)
    "file.",                # Empty extension
])
def test_file_name_invalid_extension(invalid_extension):
    """Tests Condition 4: Extension must be exactly 'txt', 'exe', or 'dll'."""
    assert file_name_check(invalid_extension) == 'No'

@pytest.mark.parametrize("invalid_dots", [
    "filename",             # No dot
    "file.name.txt",        # Two dots
    "file..txt",            # Double dot
    "...",                  # Multiple dots
])
def test_file_name_dot_count(invalid_dots):
    """Tests Condition 2: Must contain exactly one dot."""
    assert file_name_check(invalid_dots) == 'No'

@pytest.mark.parametrize("too_many_digits", [
    "file1234.txt",         # 4 digits in prefix
    "f1234.exe",            # 4 digits in prefix
    "f12.34txt",            # 4 digits total (though this would fail dot check too)
    "a1b2c3d4.dll",         # 4 digits scattered
])
def test_file_name_digit_limit(too_many_digits):
    """Tests Condition 1: No more than three digits allowed."""
    assert file_name_check(too_many_digits) == 'No'

def test_file_name_edge_cases():
    """Additional edge cases for robustness."""
    # Test with non-string input if the environment doesn't enforce types
    with pytest.raises(AttributeError):
        file_name_check(None)
    
    with pytest.raises(AttributeError):
        file_name_check(123)