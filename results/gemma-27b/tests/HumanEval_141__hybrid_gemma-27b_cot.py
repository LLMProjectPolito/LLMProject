
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

def test_valid_file_names():
    assert file_name_check("example.txt") == "Yes"
    assert file_name_check("MyFile.exe") == "Yes"
    assert file_name_check("document1.dll") == "Yes"
    assert file_name_check("A.txt") == "Yes"
    assert file_name_check("file123.txt") == "Yes"
    assert file_name_check("fileABC.exe") == "Yes"

def test_invalid_file_names_digit_count():
    assert file_name_check("1234example.txt") == "No"
    assert file_name_check("example1234.dll") == "No"
    assert file_name_check("123example1.exe") == "No"

def test_invalid_file_names_dot_count():
    assert file_name_check("example.txt.txt") == "No"
    assert file_name_check("example..txt") == "No"
    assert file_name_check("exampletxt") == "No"

def test_invalid_file_names_empty_prefix():
    assert file_name_check(".txt") == "No"
    assert file_name_check(".exe") == "No"
    assert file_name_check(".dll") == "No"

def test_invalid_file_names_invalid_prefix():
    assert file_name_check("1example.txt") == "No"
    assert file_name_check("2file.exe") == "No"
    assert file_name_check("9document.dll") == "No"
    assert file_name_check("_file.txt") == "No"
    assert file_name_check("!file.dll") == "No"
    assert file_name_check(" file.txt") == "No"

def test_invalid_file_names_invalid_extension():
    assert file_name_check("example.jpg") == "No"
    assert file_name_check("file.pdf") == "No"
    assert file_name_check("document.zip") == "No"

def test_edge_cases():
    assert file_name_check("a.txt") == "Yes"
    assert file_name_check("A.exe") == "Yes"
    assert file_name_check("file.dll") == "Yes"
    assert file_name_check("file1.txt") == "Yes"
    assert file_name_check("file12.exe") == "Yes"
    assert file_name_check("file123.dll") == "Yes"

def test_empty_string():
    assert file_name_check("") == "No"

def test_file_name_with_spaces():
    assert file_name_check("example file.txt") == "No"
    assert file_name_check("file name.exe") == "No"
    assert file_name_check("example.txt ") == "No"

def test_file_name_with_special_characters():
    assert file_name_check("example!.txt") == "No"
    assert file_name_check("file@.exe") == "No"
    assert file_name_check("document#.dll") == "No"