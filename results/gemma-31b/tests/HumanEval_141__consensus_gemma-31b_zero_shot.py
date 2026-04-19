
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
    ("a.txt", "Yes"),
    ("MyFile.exe", "Yes"),
    ("test1.dll", "Yes"),
    ("file123.txt", "Yes"),
    ("A1B2C3.exe", "Yes"),
    ("ValidName.dll", "Yes"),
    ("test.exe", "Yes"),
    ("library.dll", "Yes"),
    ("File1.txt", "Yes"),
    ("File12.exe", "Yes"),
    ("File123.dll", "Yes"),
    ("MyFile_12.txt", "Yes"),
    ("UpperAndLower.exe", "Yes"),
    ("Example.exe", "Yes"),
    ("my_file123.dll", "Yes"),
    ("test1.txt", "Yes"),
    ("test12.txt", "Yes"),
    ("test123.txt", "Yes"),
    ("CaseSensitive.dll", "Yes"),
    ("ValidName_99.txt", "Yes"),
    ("a1b2c3.dll", "Yes"),
    
    # Condition 1: More than three digits
    ("file1234.txt", "No"),
    ("1234a.exe", "No"),
    ("a1b2c3d4.dll", "No"),
    ("123456.txt", "No"),
    ("1234file.txt", "No"),
    ("f1i2l3e4.txt", "No"),
    ("abc1234.exe", "No"),
    ("test1234.txt", "No"),
    ("t1e2s3t4.txt", "No"),
    ("1234test.txt", "No"),
    ("a1b2c3d4.exe", "No"),
    
    # Condition 2: Exactly one dot
    ("filetxt", "No"),
    ("file.txt.txt", "No"),
    ("file..txt", "No"),
    ("file.t.xt", "No"),
    ("exampletxt", "No"),
    ("example.txt.bak", "No"),
    ("...", "No"),
    
    # Condition 3: Before dot non-empty and starts with latin letter
    (".txt", "No"),
    ("1example.dll", "No"),
    ("_example.txt", "No"),
    (" example.exe", "No"),
    ("!file.txt", "No"),
    (".exe", "No"),
    ("1example.txt", "No"),
    ("!example.txt", "No"),
    ("πile.txt", "No"),
    
    # Condition 4: Extension must be ['txt', 'exe', 'dll']
    ("file.jpg", "No"),
    ("file.png", "No"),
    ("file.py", "No"),
    ("file.tx", "No"),
    ("file.text", "No"),
    ("file.EXE", "No"),
    ("file.DLL", "No"),
    ("file.TXT", "No"),
    ("file.pdf", "No"),
    ("file.txt1", "No"),
    ("file.txt ", "No"),
    ("file.exee", "No"),
    ("file.", "No"),
    ("example.pdf", "No"),
    ("example.jpg", "No"),
    ("example.tx", "No"),
    ("example.txts", "No"),
    ("example.TXT", "No"),
    ("example.EXE", "No"),
    ("example.DLL", "No"),
    
    # Mixed failure cases
    ("1234.pdf", "No"),
    ("..txt", "No"),
    ("123.exe.txt", "No"),
    ("123.txt", "No"),
])
def test_file_name_check(file_name, expected):
    assert file_name_check(file_name) == expected