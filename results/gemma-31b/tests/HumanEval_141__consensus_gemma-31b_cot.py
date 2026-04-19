
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
    ("A.txt", "Yes"),
    ("File1.txt", "Yes"),
    ("File12.exe", "Yes"),
    ("File123.dll", "Yes"),
    ("My_File_01.dll", "Yes"),
    ("my_file_123.txt", "Yes"),
    ("Document.txt", "Yes"),
    ("MixedCaseName.exe", "Yes"),
    ("A1B2C3.dll", "Yes"),
    ("A1B2C3.exe", "Yes"),
    ("A123.exe", "Yes"),
    ("a" * 100 + ".txt", "Yes"),
    
    # Invalid: More than three digits
    ("file1234.txt", "No"),
    ("1234.exe", "No"),
    ("a1b2c3d4.dll", "No"),
    ("12345.txt", "No"),
    ("A1234.exe", "No"),
    ("1234file.exe", "No"),
    
    # Invalid: Dot count/position
    ("filename", "No"),
    ("exampletxt", "No"),
    ("file.txt.txt", "No"),
    ("example.test.txt", "No"),
    ("file..txt", "No"),
    ("example..txt", "No"),
    ("file.", "No"),
    ("example.", "No"),
    ("file.txt.", "No"),
    
    # Invalid: Prefix conditions (Empty or doesn't start with letter)
    (".txt", "No"),
    ("1example.dll", "No"),
    ("1file.txt", "No"),
    ("2example.dll", "No"),
    ("_file.txt", "No"),
    ("_example.txt", "No"),
    ("_file.exe", "No"),
    (" file.exe", "No"),
    (" example.exe", "No"),
    (" file.txt", "No"),
    ("!test.dll", "No"),
    ("!file.txt", "No"),
    ("!file.dll", "No"),
    
    # Invalid: Suffix conditions
    ("example.pdf", "No"),
    ("example.png", "No"),
    ("example.txt1", "No"),
    ("example.ex", "No"),
    ("example.exe_old", "No"),
    ("file.dlls", "No"),
    ("example.TXT", "No"),
    ("example.EXE", "No"),
    ("example.DLL", "No"),
    
    # Edge cases and mixed failures
    ("", "No"),
    ("..txt", "No"),
    ("1.1.txt", "No"),
    ("1234.pdf", "No"),
])
def test_file_name_check(file_name, expected):
    assert file_name_check(file_name) == expected