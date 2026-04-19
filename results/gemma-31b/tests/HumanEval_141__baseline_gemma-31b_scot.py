
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
    ("file1.txt", "Yes"),
    ("file12.exe", "Yes"),
    ("file123.dll", "Yes"),
    ("MyFile_12.txt", "Yes"),
    ("A.txt", "Yes"),
    ("LongFileNameWithNoDigits.exe", "Yes"),
    
    # Digit constraint: More than 3 digits
    ("file1234.txt", "No"),
    ("1234.exe", "No"),
    ("a1b2c3d4.dll", "No"),
    
    # Dot constraint: Not exactly one dot
    ("exampletxt", "No"),        # Zero dots
    ("example.test.txt", "No"),  # Two dots
    ("example..txt", "No"),      # Two dots
    
    # Prefix constraints: Empty or doesn't start with letter
    (".txt", "No"),              # Empty prefix
    ("1example.dll", "No"),      # Starts with digit
    ("_example.txt", "No"),      # Starts with underscore
    (".exe", "No"),              # Empty prefix
    ("!file.txt", "No"),         # Starts with symbol
    
    # Suffix constraints: Invalid extensions
    ("example.pdf", "No"),       # Not in allowed list
    ("example.png", "No"),       # Not in allowed list
    ("example.", "No"),          # Empty suffix
    ("example.txt1", "No"),      # Suffix contains digit
    ("example.TXT", "No"),       # Case sensitivity check (assuming strict match)
    ("example.ex", "No"),        # Partial match
])
def test_file_name_check(file_name, expected):
    """
    Tests the file_name_check function against various valid and invalid 
    filename scenarios based on the provided business rules.
    """
    assert file_name_check(file_name) == expected

def test_empty_string():
    """Test behavior with an empty string input."""
    assert file_name_check("") == "No"

def test_whitespace_handling():
    """Test filenames containing whitespace."""
    # Prefix starts with space (not a letter)
    assert file_name_check(" file.txt") == "No"
    # Prefix contains space but starts with letter (valid if digits <= 3 and dot is 1)
    assert file_name_check("my file.txt") == "Yes"