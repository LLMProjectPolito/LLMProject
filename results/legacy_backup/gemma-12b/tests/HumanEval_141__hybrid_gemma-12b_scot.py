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
    if not isinstance(file_name, str):
        return 'No'

    if file_name.count('.') != 1:
        return 'No'

    parts = file_name.split('.')
    if len(parts[0]) == 0:
        return 'No'

    if not parts[0][0].isalpha():
        return 'No'

    if len(parts[0]) > 0 and sum(c.isdigit() for c in parts[0]) > 3:
        return 'No'

    if parts[1] not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'


def test_valid_file_name():
    assert file_name_check("example.txt") == 'Yes'

def test_invalid_too_many_digits():
    assert file_name_check("1234example.txt") == 'No'

def test_invalid_no_dot():
    assert file_name_check("exampletxt") == 'No'

def test_invalid_multiple_dots():
    assert file_name_check("example.sub.txt") == 'No'

def test_invalid_extension():
    assert file_name_check("example.pdf") == 'No'

def test_invalid_empty_before_dot():
    assert file_name_check(".txt") == 'No'

def test_invalid_non_letter_start():
    assert file_name_check("1example.txt") == 'No'

def test_valid_file_name_exe():
    assert file_name_check("example.exe") == 'Yes'

def test_valid_file_name_dll():
    assert file_name_check("example.dll") == 'Yes'

def test_empty_string():
    assert file_name_check("") == 'No'

def test_digits_only():
    assert file_name_check("12345") == 'No'

def test_dot_only():
    assert file_name_check(".") == 'No'

def test_valid_file_name_with_digits():
    assert file_name_check("ex123ample.txt") == 'Yes'

def test_valid_file_name_with_digits_exe():
    assert file_name_check("ex123ample.exe") == 'Yes'

def test_valid_file_name_with_digits_dll():
    assert file_name_check("ex123ample.dll") == 'Yes'