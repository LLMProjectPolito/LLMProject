
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
    ("file1.dll", "Yes"),
    ("file12.txt", "Yes"),
    ("file123.exe", "Yes"),
    ("a1b2c3.dll", "Yes"),
    ("MyFile_123.txt", "Yes"),
    ("A.exe", "Yes"),
    
    # Invalid: More than three digits
    ("file1234.txt", "No"),
    ("1234.exe", "No"),
    ("a1b2c3d4.dll", "No"),
    ("123456.txt", "No"),
    
    # Invalid: Dot conditions (exactly one dot)
    ("exampletxt", "No"),
    ("example.txt.bak", "No"),
    ("example..txt", "No"),
    ("...", "No"),
    
    # Invalid: Substring before dot (empty or doesn't start with letter)
    (".txt", "No"),
    ("1example.txt", "No"),
    ("_example.exe", "No"),
    (" example.dll", "No"),
    ("!file.txt", "No"),
    
    # Invalid: Substring after dot (not in ['txt', 'exe', 'dll'])
    ("example.pdf", "No"),
    ("example.png", "No"),
    ("example.txt1", "No"),
    ("example.", "No"),
    ("example.TXT", "No"), # Case sensitivity check
    ("example.ex", "No"),
    ("example.dl", "No"),
])
def test_file_name_check(file_name, expected):
    assert file_name_check(file_name) == expected