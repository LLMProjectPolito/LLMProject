
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
    ("Example.exe", "Yes"),
    ("test.dll", "Yes"),
    ("file1.txt", "Yes"),
    ("file12.exe", "Yes"),
    ("file123.dll", "Yes"),
    ("a1b2c3.txt", "Yes"),
    ("MyFile_12.txt", "Yes"),
    
    # Invalid: More than three digits
    ("file1234.txt", "No"),
    ("f1i2l3e4.exe", "No"),
    ("1234.dll", "No"),
    
    # Invalid: Dot count
    ("exampletxt", "No"),          # No dot
    ("example.test.txt", "No"),    # More than one dot
    ("example..txt", "No"),        # More than one dot
    
    # Invalid: Prefix conditions
    (".txt", "No"),                # Empty prefix
    ("1example.txt", "No"),        # Starts with digit
    ("_example.txt", "No"),        # Starts with non-latin character
    ("!example.exe", "No"),        # Starts with non-latin character
    
    # Invalid: Extension conditions
    ("example.pdf", "No"),         # Wrong extension
    ("example.txt1", "No"),        # Extension contains digits
    ("example.TXT", "No"),         # Case sensitivity check
    ("example.exe ", "No"),        # Trailing space
    ("example.", "No"),            # Empty extension
    
    # Edge cases
    ("", "No"),                    # Empty string
    ("a.txt", "Yes"),              # Minimum valid prefix
    ("a123.txt", "Yes"),           # Max digits, min prefix
    ("a1234.txt", "No"),           # Max digits exceeded, min prefix
])
def test_file_name_check(file_name, expected):
    assert file_name_check(file_name) == expected