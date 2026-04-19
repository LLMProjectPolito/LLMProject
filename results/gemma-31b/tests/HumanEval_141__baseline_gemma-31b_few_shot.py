
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
    ("document.exe", "Yes"),
    ("library.dll", "Yes"),
    ("a.txt", "Yes"),
    ("File123.txt", "Yes"),
    ("MyFile1.exe", "Yes"),
    ("test22.dll", "Yes"),
    ("A1B2C3.txt", "Yes"),
    ("MixedCaseName.exe", "Yes"),
])
def test_file_name_check_valid(file_name, expected):
    assert file_name_check(file_name) == expected

@pytest.mark.parametrize("file_name", [
    # Too many digits (> 3)
    ("file1234.txt"),
    ("1234example.exe"),
    ("a1b2c3d4.dll"),
    ("1a2b3c4.txt"),
])
def test_file_name_check_too_many_digits(file_name):
    assert file_name_check(file_name) == "No"

@pytest.mark.parametrize("file_name", [
    # Dot constraints (exactly one dot)
    ("exampletxt"),          # No dot
    ("example.txt.bak"),     # Multiple dots
    ("example..txt"),        # Multiple dots
    ("example."),            # Dot at end
    (".txt"),                # Dot at start
])
def test_file_name_check_dot_constraints(file_name):
    assert file_name_check(file_name) == "No"

@pytest.mark.parametrize("file_name", [
    # Prefix constraints (starts with letter, not empty)
    ("1example.txt"),        # Starts with digit
    ("_example.exe"),        # Starts with special char
    (".txt"),                # Empty prefix
    (" example.dll"),        # Starts with space
])
def test_file_name_check_prefix_constraints(file_name):
    assert file_name_check(file_name) == "No"

@pytest.mark.parametrize("file_name", [
    # Suffix constraints (must be txt, exe, or dll)
    ("example.jpg"),         # Invalid extension
    ("example.pdf"),         # Invalid extension
    ("example.txt1"),        # Extension contains digit
    ("example.TXT"),         # Case sensitivity check
    ("example.exe "),        # Trailing space
    ("example.dlls"),        # Extra character
])
def test_file_name_check_suffix_constraints(file_name):
    assert file_name_check(file_name) == "No"