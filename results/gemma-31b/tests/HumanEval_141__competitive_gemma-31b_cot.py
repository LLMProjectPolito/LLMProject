
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
    ("file1.exe", "Yes"),
    ("file12.dll", "Yes"),
    ("file123.txt", "Yes"),
    ("a1b2c3.exe", "Yes"),
    ("MyFile.dll", "Yes"),
    
    # Invalid: More than three digits
    ("file1234.txt", "No"),
    ("1234.exe", "No"),
    ("a1b2c3d4.dll", "No"),
    
    # Invalid: Dot count
    ("exampletxt", "No"),        # Zero dots
    ("example.txt.txt", "No"),   # Two dots
    ("example..txt", "No"),      # Two dots
    ("...", "No"),               # Three dots
    
    # Invalid: Substring before dot (empty or doesn't start with letter)
    (".txt", "No"),              # Empty before dot
    ("1example.txt", "No"),      # Starts with digit
    ("_example.exe", "No"),      # Starts with underscore
    (" example.dll", "No"),      # Starts with space
    ("!file.txt", "No"),         # Starts with special char
    
    # Invalid: Substring after dot (wrong extension)
    ("example.pdf", "No"),       # Not in allowed list
    ("example.py", "No"),        # Not in allowed list
    ("example.tx", "No"),        # Partial match
    ("example.txt1", "No"),      # Extra char in extension
    ("example.", "No"),          # Empty after dot
    ("example.EXE", "No"),       # Case sensitivity check (usually extensions are case sensitive unless specified)
])
def test_file_name_check(file_name, expected):
    assert file_name_check(file_name) == expected