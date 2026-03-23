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
    digit_count = sum(c.isdigit() for c in file_name)
    if digit_count > 3:
        return 'No'

    if file_name.count('.') != 1:
        return 'No'

    parts = file_name.split('.')
    if not parts[0]:
        return 'No'

    if not parts[0][0].isalpha():
        return 'No'

    extension = parts[1]
    if extension not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'


def test_valid_filename():
    assert file_name_check("example.txt") == 'Yes'

def test_invalid_digit_count():
    assert file_name_check("1234example.txt") == 'No'

def test_invalid_dot_count():
    assert file_name_check("exampletxt") == 'No'
    assert file_name_check("example.txt.") == 'No'
    assert file_name_check("example..txt") == 'No'

def test_invalid_start_character():
    assert file_name_check("1example.dll") == 'No'
    assert file_name_check("_example.txt") == 'No'

def test_invalid_extension():
    assert file_name_check("example.pdf") == 'No'
    assert file_name_check("example.jpg") == 'No'

def test_empty_before_dot():
    assert file_name_check(".txt") == 'No'

def test_empty_filename():
    assert file_name_check("") == 'No'

def test_valid_filename_uppercase():
    assert file_name_check("Example.txt") == 'Yes'

def test_valid_filename_mixedcase():
    assert file_name_check("ExAmPlE.txt") == 'Yes'

def test_digit_at_start():
    assert file_name_check("123a.txt") == 'No'

def test_multiple_dots():
    assert file_name_check("example.mid.txt") == 'No'

def test_extension_case_sensitive():
    assert file_name_check("example.TXT") == 'No'
    assert file_name_check("example.ExE") == 'No'