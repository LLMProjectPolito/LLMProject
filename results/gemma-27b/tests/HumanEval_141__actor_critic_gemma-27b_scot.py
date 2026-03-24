
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
    >>> file_name_check("example.txt")
    'Yes'
    >>> file_name_check("1example.dll")
    'No'
    """
    if file_name.count('.') != 1:
        return 'No'

    parts = file_name.split('.')
    if not parts[0]:
        return 'No'

    if not parts[0][0].isalpha():
        return 'No'

    digit_count = sum(c.isdigit() for c in file_name)
    if digit_count > 3:
        return 'No'

    extension = parts[1]
    if extension not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'


def test_valid_filename():
    assert file_name_check("example.txt") == 'Yes'

def test_invalid_filename_no_dot():
    assert file_name_check("exampletxt") == 'No'

def test_invalid_filename_multiple_dots():
    assert file_name_check("example.txt.dll") == 'No'

def test_invalid_filename_starts_with_digit():
    assert file_name_check("1example.dll") == 'No'

def test_invalid_filename_too_many_digits():
    assert file_name_check("example1234.txt") == 'No'

def test_invalid_filename_empty_before_dot():
    assert file_name_check(".txt") == 'No'

def test_invalid_filename_invalid_extension():
    assert file_name_check("example.jpg") == 'No'

def test_valid_filename_mixedcase():
    assert file_name_check("ExAmPlE.txt") == 'Yes'

def test_valid_filename_three_digits():
    assert file_name_check("example123.txt") == 'Yes'

def test_filename_with_spaces():
    assert file_name_check("example file.txt") == 'No'

def test_filename_with_leading_whitespace():
    assert file_name_check("  example.txt") == 'No'

def test_filename_with_trailing_whitespace():
    assert file_name_check("example.txt  ") == 'No'

def test_filename_with_unicode_characters():
    assert file_name_check("пример.txt") == 'No'

def test_filename_digits_only_before_dot():
    assert file_name_check("123.txt") == 'Yes'

def test_invalid_filename_digits_after_dot():
    assert file_name_check("example.txt1") == 'No'

def test_invalid_filename_special_chars():
    assert file_name_check("example!.txt") == 'No'

def test_long_filename():
    long_name = "a" * 200 + ".txt"
    assert file_name_check(long_name) == 'Yes'