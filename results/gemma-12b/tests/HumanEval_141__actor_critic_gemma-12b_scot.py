
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

    if not 'a' <= parts[0][0] <= 'z' and not 'A' <= parts[0][0] <= 'Z':
        return 'No'

    digit_count = sum(c.isdigit() for c in file_name)
    if digit_count > 3:
        return 'No'

    extension = parts[1].strip()  # Remove potential whitespace
    if extension not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'


def test_valid_file_name():
    assert file_name_check("example.txt") == 'Yes'

def test_valid_file_name_exe():
    assert file_name_check("example.exe") == 'Yes'

def test_valid_file_name_dll():
    assert file_name_check("example.dll") == 'Yes'

def test_too_many_digits():
    assert file_name_check("1234example.txt") == 'No'

def test_no_dot():
    assert file_name_check("example") == 'No'

def test_multiple_dots():
    assert file_name_check("example.txt.pdf") == 'No'

def test_empty_before_dot():
    assert file_name_check(".txt") == 'No'

def test_non_letter_start():
    assert file_name_check("1example.txt") == 'No'

def test_invalid_extension():
    assert file_name_check("example.pdf") == 'No'

def test_empty_string():
    assert file_name_check("") == 'No'

def test_digit_only():
    assert file_name_check("123.txt") == 'No'

def test_dot_only():
    assert file_name_check(".") == 'No'

def test_extension_with_numbers():
    assert file_name_check("example.txt1") == 'No'

def test_extension_with_special_characters():
    assert file_name_check("example.txt!") == 'No'

def test_three_digits():
    assert file_name_check("123example.txt") == 'Yes'

def test_uppercase_start():
    assert file_name_check("Example.txt") == 'Yes'

def test_numbers_at_beginning():
    assert file_name_check("12a.txt") == 'Yes'

def test_multiple_chars_before_dot():
    assert file_name_check("abc12example.txt") == 'No'

def test_mixed_case():
    assert file_name_check("ExAmPlE.txt") == 'Yes'

def test_special_chars():
    assert file_name_check("example!.txt") == 'No'

def test_spaces_in_filename():
    assert file_name_check("example .txt") == 'No'

def test_extension_with_spaces():
    assert file_name_check("example. txt") == 'No'

def test_non_string_input():
    assert file_name_check(123) == 'No'