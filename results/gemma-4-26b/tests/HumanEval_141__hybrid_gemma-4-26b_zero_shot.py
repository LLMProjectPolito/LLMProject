
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

def file_name_check(file_name):
    """Create a function which takes a string representing a file's name, and returns
    'Yes' if the the file's name is valid, and returns 'No' otherwise.
    """
    # Condition 2: Exactly one dot
    if file_name.count('.') != 1:
        return 'No'
    
    parts = file_name.split('.')
    before_dot = parts[0]
    after_dot = parts[1]
    
    # Condition 1: Not more than three digits
    digit_count = sum(c.isdigit() for c in file_name)
    if digit_count > 3:
        return 'No'
    
    # Condition 3: Substring before dot not empty and starts with a letter
    if not before_dot or not before_dot[0].isalpha():
        return 'No'
    
    # Condition 4: Substring after dot is one of ['txt', 'exe', 'dll']
    if after_dot not in ['txt', 'exe', 'dll']:
        return 'No'
    
    return 'Yes'

@pytest.mark.parametrize("file_name", [
    "example.txt",        # Standard valid
    "A.dll",              # Single letter prefix, uppercase
    "z.dll",              # Single letter prefix, lowercase
    "abc123.txt",         # Exactly three digits
    "a1b2c3.exe",         # Three digits scattered
    "ValidFile12.txt",    # Mixed alphanumeric
    "my_file.exe",        # Underscores allowed in prefix
    "File_Name.dll",      # Underscores allowed in prefix
    "a.txt",              # Minimal valid name
    "LongPrefixName.exe", # Long prefix
    "a1.txt",             # One digit
    "a12.dll",            # Two digits
    "a123.txt",           # Boundary: exactly 3 digits
    "a!@#123.txt",        # Non-latin chars allowed if start is letter
])
def test_valid_filenames(file_name):
    """Tests cases that should return 'Yes'."""
    assert file_name_check(file_name) == 'Yes'

@pytest.mark.parametrize("file_name", [
    "abc1234.txt",        # 4 digits
    "12345.exe",          # 5 digits
    "a1b2c3d4.dll",       # 4 digits scattered
    "a1234.txt",          # 4 digits in prefix
    "1234.exe",           # 4 digits (also fails prefix rule)
    "abc1234.dll",        # 4 digits in prefix
])
def test_invalid_digit_count(file_name):
    """Tests filenames with more than three digits."""
    assert file_name_check(file_name) == 'No'

@pytest.mark.parametrize("file_name", [
    "exampletxt",         # No dot
    "example.txt.dll",    # Two dots
    "file..txt",          # Two dots
    "a.b.txt",            # Multiple dots
    "abc..exe",           # Double dot
    "example.txt.bak",    # Multiple dots
])
def test_invalid_dot_count(file_name):
    """Tests filenames with incorrect number of dots."""
    assert file_name_check(file_name) == 'No'

@pytest.mark.parametrize("file_name", [
    "1example.txt",       # Starts with digit
    ".txt",               # Empty prefix (also fails dot logic if interpreted as start)
    "_example.dll",       # Starts with underscore
    " example.exe",       # Starts with space
    "!test.txt",          # Starts with special char
    "12.txt",             # Starts with digit
    "1a.txt",             # Starts with digit
    "_example.txt",       # Starts with underscore
    "!example.dll",       # Starts with special char
])
def test_invalid_prefix(file_name):
    """Tests filenames that don't start with a Latin letter or have empty prefix."""
    assert file_name_check(file_name) == 'No'

@pytest.mark.parametrize("file_name", [
    "example.pdf",        # Invalid extension
    "file.txt1",          # Invalid extension
    "test.EXE",           # Case sensitivity
    "data.zip",           # Invalid extension
    "file.",              # Empty extension
    "example.txt1",       # Extension contains extra chars
    "example.dll ",       # Trailing space
    "example.t",          # Incomplete extension
    "example.txt.exe",    # Extension looks like multiple dots
])
def test_invalid_extension(file_name):
    """Tests filenames with unsupported or malformed extensions."""
    assert file_name_check(file_name) == 'No'

@pytest.mark.parametrize("file_name", [
    "",                   # Empty string
    "123",                # Only digits, no dot
    "1234",               # Only digits, no dot, too many
])
def test_edge_cases(file_name):
    """Tests extreme boundary conditions."""
    assert file_name_check(file_name) == 'No'