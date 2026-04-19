
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
    ("test.exe", "Yes"),
    ("library.dll", "Yes"),
    ("A.txt", "Yes"),
    ("file1.txt", "Yes"),
    ("file12.exe", "Yes"),
    ("file123.dll", "Yes"),
    ("myFile1a2b3.txt", "Yes"),
    ("UpperStart.exe", "Yes"),
    
    # Invalid: Too many digits
    ("file1234.txt", "No"),
    ("f1i2l3e4.exe", "No"),
    ("1234.dll", "No"),
    
    # Invalid: Dot constraints
    ("exampletxt", "No"),          # No dot
    ("example.test.txt", "No"),    # More than one dot
    ("example.", "No"),            # Dot at end
    (".txt", "No"),                # Dot at start
    
    # Invalid: Substring before dot
    ("1example.dll", "No"),        # Starts with digit
    ("_example.txt", "No"),        # Starts with special char
    (" example.exe", "No"),        # Starts with space
    (".exe", "No"),                # Empty before dot
    
    # Invalid: Substring after dot
    ("example.jpg", "No"),         # Wrong extension
    ("example.pdf", "No"),         # Wrong extension
    ("example.txt1", "No"),        # Extension too long
    ("example.tx", "No"),          # Extension too short
    ("example.TXT", "No"),         # Case sensitivity check (assuming strict match)
    ("example.exe ", "No"),        # Trailing space in extension
])
def test_file_name_check(file_name, expected):
    assert file_name_check(file_name) == expected