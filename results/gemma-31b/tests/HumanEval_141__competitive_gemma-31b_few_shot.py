
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
    ("f1i2l3e.txt", "Yes"),
    ("a.exe", "Yes"),
    ("myFile123.dll", "Yes"),
    ("Test_File.txt", "Yes"),
    
    # Invalid: More than three digits
    ("file1234.txt", "No"),
    ("1234.exe", "No"),
    ("a1b2c3d4.dll", "No"),
    
    # Invalid: Dot count
    ("exampletxt", "No"),
    ("example.txt.bak", "No"),
    ("my.file.txt", "No"),
    ("...", "No"),
    
    # Invalid: Substring before dot
    (".txt", "No"),
    ("1example.dll", "No"),
    ("2.exe", "No"),
    ("_example.txt", "No"),
    (" example.txt", "No"),
    ("!file.exe", "No"),
    
    # Invalid: Substring after dot
    ("example.jpg", "No"),
    ("example.pdf", "No"),
    ("example.txt1", "No"),
    ("example.", "No"),
    ("example.TXT", "No"), # Case sensitivity check based on provided list
    ("example.ex", "No"),
    ("example.dlls", "No"),
])
def test_file_name_check(file_name, expected):
    assert file_name_check(file_name) == expected