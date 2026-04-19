
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
    ("MyFile_123.exe", "Yes"),
    ("A.dll", "Yes"),
    
    # Invalid: More than three digits
    ("file1234.txt", "No"),
    ("1234.exe", "No"),
    ("a1b2c3d4.dll", "No"),
    ("123456.txt", "No"),
    
    # Invalid: Dot conditions (exactly one dot)
    ("exampletxt", "No"),          # No dot
    ("example.test.txt", "No"),    # More than one dot
    ("example..txt", "No"),        # More than one dot
    ("example.", "No"),            # Dot at end, empty suffix
    (".txt", "No"),                # Dot at start, empty prefix
    
    # Invalid: Prefix conditions (not empty, starts with Latin letter)
    ("1example.txt", "No"),        # Starts with digit
    ("_example.txt", "No"),        # Starts with underscore
    (" example.txt", "No"),        # Starts with space
    (".txt", "No"),                # Empty prefix
    ("!file.exe", "No"),           # Starts with special char
    
    # Invalid: Suffix conditions (must be txt, exe, or dll)
    ("example.pdf", "No"),         # Wrong extension
    ("example.png", "No"),         # Wrong extension
    ("example.tx", "No"),          # Partial match
    ("example.txts", "No"),        # Partial match
    ("example.EXE", "No"),         # Case sensitivity check (usually extensions are case sensitive unless specified)
    ("example.dll1", "No"),        # Extra char in extension
    
    # Edge cases
    ("", "No"),                    # Empty string
    (" .txt", "No"),               # Prefix is space
    ("a.txt1", "No"),              # Suffix invalid
    ("a123.txt", "Yes"),           # Exactly 3 digits
    ("a1234.txt", "No"),           # 4 digits
])
def test_file_name_check(file_name, expected):
    assert file_name_check(file_name) == expected