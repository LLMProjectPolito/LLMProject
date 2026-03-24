
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

def test_valid_filename_basic():
    assert file_name_check("example.txt") == "Yes"
    assert file_name_check("document.dll") == "Yes"
    assert file_name_check("my_file.exe") == "Yes"

def test_valid_filename_edge_cases():
    assert file_name_check("a.txt") == "Yes"
    assert file_name_check("A.TXT") == "Yes"
    assert file_name_check("longname.txt") == "Yes"
    assert file_name_check("valid.exe") == "Yes"
    assert file_name_check("another.dll") == "Yes"

def test_invalid_filename_too_many_digits():
    assert file_name_check("1234567890example.txt") == "No"  # Clarify the limit

def test_invalid_filename_no_dot():
    assert file_name_check("example") == "No"
    assert file_name_check("exampletxt") == "No"

def test_invalid_filename_multiple_dots():
    assert file_name_check("example.txt.dll") == "No"
    assert file_name_check("example..txt") == "No"

def test_invalid_filename_empty_before_dot():
    assert file_name_check(".txt") == "No"
    assert file_name_check(".exe") == "No"
    assert file_name_check(".dll") == "No"

def test_invalid_filename_non_letter_before_dot():
    assert file_name_check("1.txt") == "No"
    assert file_name_check("_example.txt") == "No"
    assert file_name_check("!.txt") == "No"

def test_invalid_filename_invalid_extension():
    assert file_name_check("example.pdf") == "No"
    assert file_name_check("example.jpg") == "No"
    assert file_name_check("example.dat") == "No"
    assert file_name_check("example.") == "No"

def test_filename_with_digits_and_letters():
    assert file_name_check("ex1ample.txt") == "Yes"
    assert file_name_check("ex2ample.exe") == "Yes"
    assert file_name_check("ex3ample.dll") == "Yes"
    assert file_name_check("1ex2ample.txt") == "No"
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

def test_long_filename():
    long_filename = "a" * 200 + ".txt"
    assert file_name_check(long_filename) == "Yes"

def test_filename_with_path():
    assert file_name_check("/path/to/example.txt") == "No"
    assert file_name_check("C:\\path\\to\\example.txt") == "No"
    assert file_name_check("path/to/example.txt") == "No" # Relative path

def test_case_insensitive_extension():
    assert file_name_check("example.TXT") == "No"
    assert file_name_check("example.Exe") == "No"
    assert file_name_check("example.DLL") == "No"

def test_unicode_filename():
    assert file_name_check("你好.txt") == "No"
    assert file_name_check("example.你好") == "No"

def test_valid_extensions():
    assert file_name_check("example.txt") == "Yes"
    assert file_name_check("example.exe") == "Yes"
    assert file_name_check("example.dll") == "Yes"

def test_filename_with_leading_whitespace():
    assert file_name_check("  example.txt") == "No"

def test_filename_with_trailing_whitespace():
    assert file_name_check("example.txt  ") == "No"