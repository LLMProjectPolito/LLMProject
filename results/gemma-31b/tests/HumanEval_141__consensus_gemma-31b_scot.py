
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
    ("example.exe", "Yes"),
    ("example.dll", "Yes"),
    ("a.txt", "Yes"),
    ("a.exe", "Yes"),
    ("File1.txt", "Yes"),
    ("File12.exe", "Yes"),
    ("File123.dll", "Yes"),
    ("MyFile123.exe", "Yes"),
    ("A1B2C3.dll", "Yes"),
    ("A1B2C3.txt", "Yes"),
    ("Document.txt", "Yes"),
    ("library.dll", "Yes"),
    ("Test12.dll", "Yes"),
    ("VeryLongFileNameWithDigits123.txt", "Yes"),
    ("LongFileNameWithNoDigits.exe", "Yes"),
    
    # Invalid: More than three digits
    ("file1234.txt", "No"),
    ("1234.exe", "No"),
    ("a1b2c3d4.dll", "No"),
    ("1234example.exe", "No"),
    ("12345.txt", "No"),
    ("f1i2l3e4.dll", "No"),
    ("1a2b3c4d.txt", "No"),
    
    # Invalid: Dot conditions (must be exactly one dot)
    ("filetxt", "No"),
    ("exampletxt", "No"),
    ("file.txt.txt", "No"),
    ("example.test.txt", "No"),
    ("my.file.txt", "No"),
    ("file..txt", "No"),
    ("example..txt", "No"),
    ("..txt", "No"),
    ("file.", "No"),
    ("example.", "No"),
    
    # Invalid: Prefix conditions (must start with letter, no empty prefix)
    (".txt", "No"),
    (".exe", "No"),
    ("1example.dll", "No"),
    ("1example.txt", "No"),
    ("_file.txt", "No"),
    ("_example.txt", "No"),
    ("!file.dll", "No"),
    ("!file.exe", "No"),
    (" 1file.exe", "No"),
    (" 1file.dll", "No"),
    (" example.exe", "No"),
    
    # Invalid: Extension conditions (must be txt, exe, or dll - case sensitive)
    ("file.pdf", "No"),
    ("example.jpg", "No"),
    ("example.py", "No"),
    ("file.tx", "No"),
    ("example.ex", "No"),
    ("file.txt1", "No"),
    ("file.exe1", "No"),
    ("example.txts", "No"),
    ("file.DLL", "No"),
    ("example.TXT", "No"),
    ("example.EXE", "No"),
    
    # Edge cases and Mixed failures
    ("", "No"),
    (" ", "No"),
    ("a.txt ", "No"),
    (" a.txt", "No"),
    ("1234.notext", "No"),
])
def test_file_name_check(file_name, expected):
    assert file_name_check(file_name) == expected

def test_additional_edge_cases():
    # Test very long valid filename
    assert file_name_check("A" * 100 + ".txt") == "Yes"
    # Test filename with exactly 3 digits scattered
    assert file_name_check("a1b2c3.exe") == "Yes"
    # Test filename with 4 digits scattered
    assert file_name_check("a1b2c3d4.exe") == "No"