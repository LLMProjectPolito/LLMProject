
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

import re

def test_file_name_check_valid_name():
    assert file_name_check("example.txt") == "Yes"
    assert file_name_check("document.pdf") == "Yes"
    assert file_name_check("myFile.exe") == "Yes"
    assert file_name_check("a.txt") == "Yes"
    assert file_name_check("A.TXT") == "Yes"
    assert file_name_check("long_file_name.dll") == "Yes"

def test_file_name_check_invalid_name_too_many_digits():
    assert file_name_check("123example.txt") == "No"
    assert file_name_check("1234example.txt") == "No"

def test_file_name_check_invalid_name_no_dot():
    assert file_name_check("example") == "No"
    assert file_name_check("exampletxt") == "No"

def test_file_name_check_invalid_name_empty_before_dot():
    assert file_name_check(".txt") == "No"
    assert file_name_check(".exe") == "No"

def test_file_name_check_invalid_name_dot_before_letter():
    assert file_name_check(".txt") == "No"

def test_file_name_check_invalid_name_invalid_extension():
    assert file_name_check("example.pdf") == "No"
    assert file_name_check("example.jpg") == "No"
    assert file_name_check("example.abc") == "No"

def test_file_name_check_invalid_name_extension_case():
    assert file_name_check("example.TXT") == "No"
    assert file_name_check("example.EXE") == "No"
    assert file_name_check("example.DLL") == "No"

def test_file_name_check_invalid_name_starts_with_digit():
    assert file_name_check("1.txt") == "No"
    assert file_name_check("2.exe") == "No"
    assert file_name_check("3.dll") == "No"

def test_file_name_check_empty_string():
    assert file_name_check("") == "No"

def test_file_name_check_name_with_special_characters():
    assert file_name_check("example!.txt") == "No"
    assert file_name_check("example#.exe") == "No"
    assert file_name_check("example$.dll") == "No"