import pytest

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
    digits = 0
    dot_count = 0
    name, ext = file_name.split('.', 1) if '.' in file_name else (file_name, '')

    dot_count = file_name.count('.')
    if dot_count != 1:
        return 'No'

    if not name:
        return 'No'

    if not name[0].isalpha():
        return 'No'

    if not ext in ['txt', 'exe', 'dll']:
        return 'No'

    if sum(c.isdigit() for c in name) > 3:
        return 'No'

    return 'Yes'

def test_valid_file_name():
    assert file_name_check("example.txt") == 'Yes'
    assert file_name_check("my_file.dll") == 'Yes'
    assert file_name_check("another.exe") == 'Yes'
    assert file_name_check("valid123.txt") == 'Yes'
    assert file_name_check("a.txt") == 'Yes'

def test_invalid_file_name_too_many_digits():
    assert file_name_check("123example.txt") == 'No'
    assert file_name_check("1234example.txt") == 'No'
    assert file_name_check("12example.txt") == 'No'
    assert file_name_check("123.123") == 'No'

def test_invalid_file_name_no_dot():
    assert file_name_check("example") == 'No'
    assert file_name_check("1example") == 'No'

def test_invalid_file_name_multiple_dots():
    assert file_name_check("example.extra.txt") == 'No'
    assert file_name_check("example..txt") == 'No'

def test_invalid_file_name_empty_before_dot():
    assert file_name_check(".txt") == 'No'
    assert file_name_check("1.txt") == 'No'

def test_invalid_file_name_starts_with_digit():
    assert file_name_check("1example.txt") == 'No'
    assert file_name_check("12example.txt") == 'No'

def test_invalid_file_name_invalid_extension():
    assert file_name_check("example.pdf") == 'No'
    assert file_name_check("example.jpg") == 'No'
    assert file_name_check("example.123") == 'No'

def test_edge_case_empty_string():
    assert file_name_check("") == 'No'

def test_edge_case_dot_only():
    assert file_name_check(".") == 'No'

def test_edge_case_digit_dot_digit():
    assert file_name_check("1.2") == 'No'

def test_edge_case_long_name():
    assert file_name_check("averylongfilename.txt") == 'No'