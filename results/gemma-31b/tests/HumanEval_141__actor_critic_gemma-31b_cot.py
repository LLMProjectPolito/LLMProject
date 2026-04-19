
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
    ("A.exe", "Yes"),
    ("file123.dll", "Yes"),
    ("MyFile.txt", "Yes"),
    ("a1b2c3.exe", "Yes"),
    ("file_1.txt", "Yes"),    # Special character after first letter
    ("file-1.txt", "Yes"),    # Special character after first letter
    ("a123.dll", "Yes"),      # Starts with letter, exactly 3 digits
    
    # Invalid: Too many digits (> 3)
    ("file1234.txt", "No"),
    ("1234file.txt", "No"),
    ("f1i2l3e4.txt", "No"),
    ("12345.exe", "No"),
    
    # Invalid: Dot count (not exactly one)
    ("exampletxt", "No"),        # 0 dots
    ("example.txt.txt", "No"),   # 2 dots
    ("...", "No"),               # 3 dots
    
    # Invalid: Substring before dot (empty or doesn't start with letter)
    ("", "No"),                  # Empty string
    (".txt", "No"),              # Empty before dot
    ("1example.txt", "No"),      # Starts with digit
    ("_example.txt", "No"),      # Starts with special char
    (" example.txt", "No"),      # Starts with space
    ("!file.exe", "No"),         # Starts with special char
    ("éxample.txt", "No"),       # Non-ASCII/Unicode start
    
    # Invalid: Substring after dot (not in ['txt', 'exe', 'dll'])
    ("example.pdf", "No"),       # Wrong extension
    ("example.TXT", "No"),       # Case sensitivity check
    ("example.exe1", "No"),      # Extension contains digit
    ("example.", "No"),          # Empty extension
    ("example.tx", "No"),        # Partial match
    ("example.txt ", "No"),      # Trailing whitespace
    
    # Edge cases: Mixed constraints
    ("123.txt", "No"),           # Starts with digit
    ("a1234.txt", "No"),         # Starts with letter, but 4 digits
    ("a.txt.exe", "No"),         # Starts with letter, valid extensions, but 2 dots
])
def test_file_name_check(file_name, expected):
    assert file_name_check(file_name) == expected