
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

# Configuration for allowed extensions
ALLOWED_EXTENSIONS = ['txt', 'exe', 'dll']

def test_valid_filename():
    assert file_name_check("example.txt") == "Yes"
    assert file_name_check("document.dll") == "Yes"
    assert file_name_check("my_file.exe") == "Yes"
    assert file_name_check("a.txt") == "Yes"
    assert file_name_check("longname.txt") == "Yes"

def test_invalid_filename_too_many_leading_digits():
    assert file_name_check("123example.txt") == "No"
    assert file_name_check("1234example.txt") == "No"

def test_invalid_filename_no_dot():
    assert file_name_check("example") == "No"
    assert file_name_check("exampletxt") == "No"

def test_invalid_filename_multiple_dots():
    assert file_name_check("example.txt.dll") == "No"
    assert file_name_check("example..txt") == "No"

def test_invalid_filename_empty_before_dot():
    assert file_name_check(".txt") == "No"

def test_invalid_filename_non_letter_before_dot():
    assert file_name_check("1.txt") == "No"
    assert file_name_check("_.txt") == "No"
    assert file_name_check("!.txt") == "No"

def test_invalid_filename_invalid_extension():
    for ext in ALLOWED_EXTENSIONS:
        assert file_name_check(f"example.{ext}") == "Yes"
    assert file_name_check("example.pdf") == "No"
    assert file_name_check("example.jpg") == "No"
    assert file_name_check("example.xyz") == "No"

def test_invalid_filename_empty_extension():
    assert file_name_check("example.") == "No"

def test_filename_with_digits_and_letters():
    assert file_name_check("ex1ample.txt") == "Yes"
    assert file_name_check("ex2ample.exe") == "Yes"
    assert file_name_check("ex3ample.dll") == "Yes"
    assert file_name_check("a123example.txt") == "Yes"

def test_filename_with_special_characters():
    assert file_name_check("example!.txt") == "No"
    assert file_name_check("example#.txt") == "No"
    assert file_name_check("example$.txt") == "No"
    assert file_name_check("example with spaces.txt") == "No"
    assert file_name_check("example(parentheses).txt") == "No"
    assert file_name_check("example[brackets].txt") == "No"

def test_empty_filename():
    assert file_name_check("") == "No"

def test_filename_only_dot():
    assert file_name_check(".") == "No"

def test_long_filename():
    long_filename = "a" * 100 + ".txt"
    assert file_name_check(long_filename) == "Yes"

def test_digit_limit_boundary():
    assert file_name_check("0.txt") == "Yes"
    assert file_name_check("1.txt") == "Yes"
    assert file_name_check("2.txt") == "Yes"
    assert file_name_check("3.txt") == "Yes"
    assert file_name_check("4.txt") == "No"
    assert file_name_check("123.txt") == "Yes"
    assert file_name_check("1234.txt") == "No"

def test_unicode_filename():
    assert file_name_check("你好.txt") == "No"

def test_long_path_filename():
    long_path = "/very/long/path/to/a/very/long/filename.txt"
    assert file_name_check(long_path) == "Yes"

def test_control_character_filename():
    assert file_name_check("example\n.txt") == "No"