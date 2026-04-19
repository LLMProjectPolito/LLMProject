
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
    ("A.txt", "Yes"),
    ("MyFile_123.txt", "Yes"),
    ("MixedCase.EXE", "No"), # Extension must be exactly 'exe'
    
    # Invalid: Too many digits
    ("file1234.txt", "No"),
    ("1234file.exe", "No"),
    ("12.345.dll", "No"), # Also fails dot check, but primarily digits
    
    # Invalid: Dot conditions
    ("exampletxt", "No"),       # No dot
    ("example.txt.txt", "No"),  # More than one dot
    (".txt", "No"),             # Empty before dot
    ("example.", "No"),         # Empty after dot
    
    # Invalid: Start character
    ("1example.txt", "No"),     # Starts with digit
    ("_example.txt", "No"),     # Starts with underscore
    (" example.txt", "No"),     # Starts with space
    ("!example.exe", "No"),     # Starts with special char
    
    # Invalid: Extension
    ("example.pdf", "No"),
    ("example.jpg", "No"),
    ("example.py", "No"),
    ("example.txt1", "No"),
    ("example.ex", "No"),
    
    # Edge cases
    ("", "No"),                 # Empty string
    ("a.txt", "Yes"),           # Minimum valid length
    ("a123.txt", "Yes"),        # Max digits, valid start
    ("1a23.txt", "No"),         # Max digits, invalid start
])
def test_file_name_check(file_name, expected):
    assert file_name_check(file_name) == expected