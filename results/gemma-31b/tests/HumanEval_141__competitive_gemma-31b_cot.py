
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
    ("my_file1.dll", "Yes"),
    ("test123.txt", "Yes"),
    ("a.exe", "Yes"),
    ("file.dll", "Yes"),
    ("valid-name_12.txt", "Yes"),
    
    # Invalid: More than three digits
    ("file1234.txt", "No"),
    ("1234.exe", "No"),
    ("a1b2c3d4.dll", "No"),
    
    # Invalid: Dot count
    ("exampletxt", "No"),          # No dot
    ("example.txt.bak", "No"),     # Too many dots
    ("example..txt", "No"),        # Too many dots
    
    # Invalid: Substring before dot
    (".txt", "No"),                # Empty before dot
    ("1example.dll", "No"),        # Starts with digit
    ("_example.txt", "No"),        # Starts with special char
    ("!file.exe", "No"),           # Starts with special char
    
    # Invalid: Substring after dot
    ("example.pdf", "No"),         # Wrong extension
    ("example.png", "No"),         # Wrong extension
    ("example.", "No"),            # Empty extension
    ("example.txt1", "No"),        # Extension contains digit
    ("example.TXT", "No"),         # Case sensitivity check (prompt specifies lowercase list)
    ("example.ex", "No"),          # Partial match
    
    # Edge cases
    ("", "No"),                    # Empty string
    (" .txt", "No"),               # Starts with space
    ("a123.txt", "Yes"),           # Exactly 3 digits, starts with letter
    ("a1234.txt", "No"),           # 4 digits, starts with letter
])
def test_file_name_check(file_name, expected):
    assert file_name_check(file_name) == expected