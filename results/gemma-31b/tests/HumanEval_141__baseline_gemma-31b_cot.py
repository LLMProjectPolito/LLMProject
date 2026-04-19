
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
    ("a.txt", "Yes"),
    ("File1.txt", "Yes"),
    ("File12.txt", "Yes"),
    ("File123.txt", "Yes"),
    ("MyFile123.exe", "Yes"),
    ("A1B2C3.dll", "Yes"),
    ("LongFileNameWithNoDigits.txt", "Yes"),
    
    # Invalid: More than three digits
    ("file1234.txt", "No"),
    ("1234file.txt", "No"),
    ("f1i2l3e4.txt", "No"),
    ("a1b2c3d4.exe", "No"),
    
    # Invalid: Dot count
    ("exampletxt", "No"),          # No dot
    ("example.txt.txt", "No"),     # Two dots
    ("example..txt", "No"),        # Two dots
    ("example.t.xt", "No"),        # Two dots
    
    # Invalid: Substring before dot
    (".txt", "No"),                # Empty before dot
    ("1example.txt", "No"),        # Starts with digit
    ("2.exe", "No"),               # Starts with digit
    ("_example.dll", "No"),        # Starts with underscore
    (" example.txt", "No"),        # Starts with space
    ("!file.txt", "No"),           # Starts with special char
    
    # Invalid: Substring after dot
    ("example.pdf", "No"),         # Wrong extension
    ("example.png", "No"),         # Wrong extension
    ("example.txt1", "No"),        # Extension too long
    ("example.tx", "No"),          # Extension too short
    ("example.", "No"),            # Empty after dot
    ("example.TXT", "No"),         # Case sensitivity (assuming exact match)
    ("example.EXE", "No"),         # Case sensitivity
    ("example.DLL", "No"),         # Case sensitivity
    
    # Mixed edge cases
    ("a123.txt", "Yes"),            # Exactly 3 digits, starts with letter
    ("123a.txt", "No"),             # 3 digits, but starts with digit
    ("a1234.exe", "No"),            # 4 digits
    ("a.txt ", "No"),               # Trailing space in extension
    (" a.txt", "No"),               # Leading space before name
])
def test_file_name_check(file_name, expected):
    assert file_name_check(file_name) == expected