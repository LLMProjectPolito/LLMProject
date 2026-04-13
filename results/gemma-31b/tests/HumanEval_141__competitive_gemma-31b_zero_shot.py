
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
    ("File1.txt", "Yes"),
    ("File12.exe", "Yes"),
    ("File123.dll", "Yes"),
    ("a1b2c3.txt", "Yes"),
    ("A.exe", "Yes"),
    ("MyFile_123.dll", "Yes"),
    
    # Invalid: Too many digits
    ("file1234.txt", "No"),
    ("f1i2l3e4.exe", "No"),
    ("1234.dll", "No"),
    
    # Invalid: Dot conditions
    ("exampletxt", "No"),        # No dot
    ("example.txt.txt", "No"),   # More than one dot
    ("example..txt", "No"),      # More than one dot
    
    # Invalid: Before the dot
    (".txt", "No"),              # Empty before dot
    ("1example.txt", "No"),      # Starts with digit
    ("_example.exe", "No"),      # Starts with non-latin letter
    (" example.dll", "No"),      # Starts with space
    
    # Invalid: After the dot (Extensions)
    ("example.pdf", "No"),       # Wrong extension
    ("example.png", "No"),       # Wrong extension
    ("example.", "No"),          # Empty extension
    ("example.txt1", "No"),      # Extension contains digit
    ("example.TXT", "No"),       # Case sensitivity check (assuming strict match)
    ("example.ex", "No"),        # Partial match
])
def test_file_name_check(file_name, expected):
    assert file_name_check(file_name) == expected