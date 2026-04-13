
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

def test_valid_file_name():
    assert file_name_check("example.txt") == "Yes"
    assert file_name_check("MyFile.exe") == "Yes"
    assert file_name_check("AnotherFile.dll") == "Yes"
    assert file_name_check("a.txt") == "Yes"
    assert file_name_check("A.exe") == "Yes"
    assert file_name_check("file1.txt") == "Yes"
    assert file_name_check("file123.dll") == "Yes"
    assert file_name_check("fileABC.exe") == "Yes"

def test_invalid_file_name_too_many_digits():
    assert file_name_check("1234example.txt") == "No"
    assert file_name_check("example1234.dll") == "No"
    assert file_name_check("1234.exe") == "No"

def test_invalid_file_name_no_dot():
    assert file_name_check("exampletxt") == "No"
    assert file_name_check("MyFileexe") == "No"
    assert file_name_check("AnotherFiledll") == "No"

def test_invalid_file_name_multiple_dots():
    assert file_name_check("example.txt.txt") == "No"
    assert file_name_check("My.File.exe") == "No"
    assert file_name_check("Another.File.dll") == "No"

def test_invalid_file_name_empty_before_dot():
    assert file_name_check(".txt") == "No"
    assert file_name_check(".exe") == "No"
    assert file_name_check(".dll") == "No"

def test_invalid_file_name_starts_with_digit():
    assert file_name_check("1example.txt") == "No"
    assert file_name_check("2MyFile.exe") == "No"
    assert file_name_check("3AnotherFile.dll") == "No"

def test_invalid_file_name_invalid_extension():
    assert file_name_check("example.pdf") == "No"
    assert file_name_check("MyFile.jpg") == "No"
    assert file_name_check("AnotherFile.png") == "No"

def test_invalid_file_name_starts_with_special_character():
    assert file_name_check("!example.txt") == "No"
    assert file_name_check("@MyFile.exe") == "No"
    assert file_name_check("#AnotherFile.dll") == "No"

def test_invalid_file_name_empty_string():
    assert file_name_check("") == "No"

def test_valid_file_name_with_uppercase():
    assert file_name_check("EXAMPLE.txt") == "Yes"
    assert file_name_check("MyFILE.exe") == "Yes"
    assert file_name_check("AnotherFILE.dll") == "Yes"