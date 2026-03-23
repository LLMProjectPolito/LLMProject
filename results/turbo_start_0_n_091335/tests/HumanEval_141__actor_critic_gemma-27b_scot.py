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
    if file_name.count('.') != 1:
        return 'No'

    parts = file_name.split('.')
    if not parts[0] or not parts[0][0].isalpha():
        return 'No'

    digit_count = sum(c.isdigit() for c in file_name)
    if digit_count > 3:
        return 'No'

    extension = parts[1].lower()
    if extension not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'

def test_valid_filename():
    assert file_name_check("example.txt") == 'Yes'

def test_invalid_filename_no_dot():
    assert file_name_check("exampletxt") == 'No'

def test_invalid_filename_multiple_dots():
    assert file_name_check("example.txt.dll") == 'No'

def test_filename_must_start_with_letter():
    assert file_name_check("1example.dll") == 'No'

def test_invalid_filename_too_many_digits():
    assert file_name_check("example1234.txt") == 'No'

def test_invalid_filename_empty_before_dot():
    assert file_name_check(".txt") == 'No'

def test_invalid_filename_invalid_extension():
    assert file_name_check("example.jpg") == 'No'

def test_valid_filename_uppercase():
    assert file_name_check("Example.txt") == 'Yes'

def test_valid_filename_mixedcase():
    assert file_name_check("ExAmPlE.txt") == 'Yes'

def test_valid_filename_three_digits():
    assert file_name_check("example123.txt") == 'Yes'

def test_empty_filename():
    assert file_name_check("") == 'No'

def test_filename_only_dot():
    assert file_name_check(".") == 'No'

def test_filename_with_spaces():
    assert file_name_check("example file.txt") == 'No'

def test_filename_starts_with_digits():
    assert file_name_check("1234example.txt") == 'No'

def test_filename_with_digits_after_extension():
    assert file_name_check("example.txt1") == 'No'