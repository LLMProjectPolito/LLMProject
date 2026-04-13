
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

@pytest.mark.parametrize("file_name, expected", [
    # Valid cases
    ("example.txt", "Yes"),
    ("a.exe", "Yes"),
    ("file123.dll", "Yes"),
    ("MyFile.txt", "Yes"),
    ("a1b2c3.exe", "Yes"),
    ("Test.dll", "Yes"),
    ("v1.0.txt", "No"), # This should be No because it has two dots
])
def test_file_name_check_valid(file_name, expected):
    assert file_name_check(file_name) == expected

@pytest.mark.parametrize("file_name", [
    "file1234.txt",    # 4 digits
    "1234.exe",        # 4 digits
    "a1b2c3d4.dll",    # 4 digits
    "12345.txt",       # 5 digits
])
def test_file_name_check_too_many_digits(file_name):
    assert file_name_check(file_name) == "No"

@pytest.mark.parametrize("file_name", [
    "exampletxt",      # No dot
    "example.txt.txt", # Two dots
    "example..txt",    # Two dots
    "...",            # Three dots
])
def test_file_name_check_dot_count(file_name):
    assert file_name_check(file_name) == "No"

@pytest.mark.parametrize("file_name", [
    ".txt",            # Empty before dot
    "1example.txt",    # Starts with digit
    "_example.txt",    # Starts with underscore
    " example.txt",    # Starts with space
    "!example.exe",    # Starts with special char
])
def test_file_name_check_invalid_prefix(file_name):
    assert file_name_check(file_name) == "No"

@pytest.mark.parametrize("file_name", [
    "example.pdf",     # Invalid extension
    "example.tx",      # Invalid extension (too short)
    "example.txt1",    # Invalid extension (too long/contains digit)
    "example.",        # Empty extension
    "example.exee",    # Invalid extension
    "example.dll ",    # Trailing space
])
def test_file_name_check_invalid_extension(file_name):
    assert file_name_check(file_name) == "No"

def test_file_name_check_empty_string():
    assert file_name_check("") == "No"