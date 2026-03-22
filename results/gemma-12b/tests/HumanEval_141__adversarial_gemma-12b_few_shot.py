import re

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
    if not isinstance(file_name, str):
        return 'No'

    if file_name.count('.') != 1:
        return 'No'

    parts = file_name.split('.')
    if len(parts) != 2:
        return 'No'

    prefix = parts[0]
    suffix = parts[1]

    if not prefix:
        return 'No'

    if not re.match(r'^[a-zA-Z]', prefix):
        return 'No'

    if suffix not in ['txt', 'exe', 'dll']:
        return 'No'

    if sum(c.isdigit() for c in file_name) > 3:
        return 'No'

    return 'Yes'


import pytest

def test_valid_filename():
    assert file_name_check("example.txt") == "Yes"
    assert file_name_check("document.dll") == "Yes"
    assert file_name_check("my_program.exe") == "Yes"
    assert file_name_check("a.txt") == "Yes"
    assert file_name_check("A.TXT") == "Yes"
    assert file_name_check("long_file_name.exe") == "Yes"
    assert file_name_check("file123.txt") == "Yes"
    assert file_name_check("file1234.txt") == "No"


def test_invalid_filename_no_dot():
    assert file_name_check("example") == "No"
    assert file_name_check("exampletxt") == "No"

def test_invalid_filename_multiple_dots():
    assert file_name_check("example.txt.dll") == "No"
    assert file_name_check("example..txt") == "No"

def test_invalid_filename_empty_prefix():
    assert file_name_check(".txt") == "No"
    assert file_name_check(".exe") == "No"

def test_invalid_filename_prefix_not_letter():
    assert file_name_check("1example.txt") == "No"
    assert file_name_check("_example.txt") == "No"
    assert file_name_check(" example.txt") == "No"

def test_invalid_filename_invalid_suffix():
    assert file_name_check("example.pdf") == "No"
    assert file_name_check("example.jpg") == "No"
    assert file_name_check("example.something") == "No"

def test_invalid_filename_too_many_digits():
    assert file_name_check("1234example.txt") == "No"
    assert file_name_check("1111.txt") == "No"

def test_invalid_filename_type():
    assert file_name_check(123) == "No"
    assert file_name_check(None) == "No"