
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
    assert file_name_check("document.dll") == "Yes"
    assert file_name_check("image.exe") == "Yes"
    assert file_name_check("a.txt") == "Yes"
    assert file_name_check("A.TXT") == "Yes"
    assert file_name_check("long_file_name.txt") == "Yes"
    assert file_name_check("valid12.txt") == "Yes"

def test_invalid_file_name_too_many_digits():
    assert file_name_check("1234example.txt") == "No"
    assert file_name_check("1234.txt") == "No"

def test_invalid_file_name_no_dot():
    assert file_name_check("example") == "No"
    assert file_name_check("exampletxt") == "No"

def test_invalid_file_name_multiple_dots():
    assert file_name_check("example.txt.dll") == "No"
    assert file_name_check(".txt") == "No"

def test_invalid_file_name_empty_before_dot():
    assert file_name_check(".txt") == "No"

def test_invalid_file_name_non_letter_start():
    assert file_name_check("1example.txt") == "No"
    assert file_name_check("_example.txt") == "No"
    assert file_name_check(" example.txt") == "No"

def test_invalid_file_name_invalid_extension():
    assert file_name_check("example.pdf") == "No"
    assert file_name_check("example.jpg") == "No"
    assert file_name_check("example.") == "No"
    assert file_name_check("example.txt1") == "No"

def test_invalid_file_name_empty_extension():
    assert file_name_check("example.") == "No"

def test_file_name_with_digits_and_letters():
    assert file_name_check("12abc.txt") == "Yes"
    assert file_name_check("abc12.txt") == "Yes"
    assert file_name_check("1a.txt") == "Yes"
    assert file_name_check("a1.txt") == "Yes"
    assert file_name_check("123abc.txt") == "Yes"
    assert file_name_check("abc123.txt") == "Yes"
    assert file_name_check("1234abc.txt") == "No"
    assert file_name_check("abc1234.txt") == "No"