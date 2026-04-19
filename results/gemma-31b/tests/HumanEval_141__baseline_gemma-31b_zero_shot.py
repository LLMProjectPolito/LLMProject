
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
    ("example.exe", "Yes"),
    ("example.dll", "Yes"),
    ("a.txt", "Yes"),
    ("A.dll", "Yes"),
    ("file1.txt", "Yes"),
    ("file12.exe", "Yes"),
    ("file123.dll", "Yes"),
    ("f1i2l3.txt", "Yes"),
    ("MyFile_12.txt", "Yes"),
    
    # Invalid: Too many digits (> 3)
    ("file1234.txt", "No"),
    ("f1i2l3u4.exe", "No"),
    ("1234.dll", "No"),
    
    # Invalid: Dot conditions (exactly one dot)
    ("filename", "No"),            # No dot
    ("file.name.txt", "No"),       # More than one dot
    ("file..txt", "No"),           # More than one dot
    
    # Invalid: Prefix conditions
    (".txt", "No"),                # Empty prefix
    ("1example.dll", "No"),        # Starts with digit
    ("_example.txt", "No"),        # Starts with special character
    (" example.exe", "No"),        # Starts with space
    
    # Invalid: Extension conditions
    ("file.pdf", "No"),            # Not in ['txt', 'exe', 'dll']
    ("file.png", "No"),            # Not in ['txt', 'exe', 'dll']
    ("file.", "No"),               # Empty extension
    ("file.txt1", "No"),           # Extension contains digit/wrong string
    ("file.TXT", "No"),            # Case sensitivity check (assuming strict match)
    ("file.Exe", "No"),            # Case sensitivity check
])
def test_file_name_check(file_name, expected):
    assert file_name_check(file_name) == expected