
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
    # Positive Cases
    ("example.txt", "Yes"),
    ("document1.exe", "Yes"),
    ("archive123.dll", "Yes"),
    ("A.txt", "Yes"),
    ("myFile1a2b3.exe", "Yes"),
    ("Test.dll", "Yes"),
    
    # Digit Constraint: More than 3 digits
    ("file1234.txt", "No"),
    ("1234.exe", "No"),
    ("a1b2c3d4.dll", "No"),
    
    # Dot Constraint: Exactly one dot
    ("exampletxt", "No"),        # No dot
    ("example.test.txt", "No"),  # Too many dots
    ("...", "No"),               # Too many dots
    
    # Prefix Constraint: Not empty and starts with Latin letter
    (".txt", "No"),              # Empty prefix
    ("1example.txt", "No"),      # Starts with digit
    ("_example.txt", "No"),      # Starts with special char
    (" example.txt", "No"),      # Starts with space
    
    # Suffix Constraint: Must be ['txt', 'exe', 'dll']
    ("example.pdf", "No"),       # Invalid extension
    ("example.png", "No"),       # Invalid extension
    ("example.", "No"),          # Empty extension
    ("example.txt1", "No"),      # Extension too long
    ("example.TXT", "No"),       # Case sensitivity check
    ("example.exe ", "No"),      # Trailing space
    
    # Edge Cases
    ("", "No"),                  # Empty string
    (".", "No"),                 # Only a dot
    ("a.txt ", "No"),            # Trailing space in extension
])
def test_file_name_check(file_name, expected):
    """
    Comprehensive test suite for file_name_check function.
    Tests digit limits, dot counts, prefix requirements, and allowed extensions.
    """
    assert file_name_check(file_name) == expected