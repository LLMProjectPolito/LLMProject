
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
from your_module import file_name_check  # Replace your_module

def test_valid_file_name():
    assert file_name_check("example.txt") == "Yes"
    assert file_name_check("document.dll") == "Yes"
    assert file_name_check("my_program.exe") == "Yes"
    assert file_name_check("a.txt") == "Yes"
    assert file_name_check("A.TXT") == "Yes"
    assert file_name_check("long_file_name.txt") == "Yes"
    assert file_name_check("file12.txt") == "Yes"
    assert file_name_check("file1.txt") == "Yes"
    assert file_name_check("file0.txt") == "Yes"

def test_invalid_file_name_no_dot():
    assert file_name_check("example") == "No"
    assert file_name_check("exampletxt") == "No"
    assert file_name_check("example.txt.extra") == "No"

def test_invalid_file_name_too_many_digits():
    assert file_name_check("1234example.txt") == "No"
    assert file_name_check("1234.txt") == "No"
    assert file_name_check("12345.txt") == "No"

def test_invalid_file_name_wrong_extension():
    assert file_name_check("example.pdf") == "No"
    assert file_name_check("example.jpg") == "No"
    assert file_name_check("example.dat") == "No"

def test_invalid_file_name_empty_prefix():
    assert file_name_check(".txt") == "No"
    assert file_name_check(".exe") == "No"
    assert file_name_check(".dll") == "No"

def test_invalid_file_name_prefix_not_letter():
    assert file_name_check("1example.txt") == "No"
    assert file_name_check("_example.txt") == "No"
    assert file_name_name("!example.txt") == "No"
    assert file_name_check(" example.txt") == "No"

def test_invalid_file_name_extension_case():
    assert file_name_check("example.tXt") == "No"
    assert file_name_check("example.ExE") == "No"
    assert file_name_check("example.DlL") == "No"

def test_empty_file_name():
    assert file_name_check("") == "No"

def test_file_name_with_spaces():
    assert file_name_check("example .txt") == "No"
    assert file_name_check("example. txt") == "No"
    assert file_name_check(" example.txt") == "No"

def test_file_name_with_special_characters():
    assert file_name_check("example!.txt") == "No"
    assert file_name_check("example#.txt") == "No"
    assert file_name_check("example$.txt") == "No"