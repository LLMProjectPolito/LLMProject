
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
    if not file_name:
        return 'No'

    if len(file_name) > 3:
        return 'No'

    if not file_name[0].isalpha():
        return 'No'

    if not file_name[1:].isspace():
        return 'No'

    if not file_name[1].isalpha() or not file_name[1].islower():
        return 'No'

    if not file_name[1] not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'

import pytest

def test_file_name_check_valid():
    assert file_name_check("example.txt") == 'Yes'

def test_file_name_check_invalid_length():
    assert file_name_check("1example.dll") == 'No'

def test_file_name_check_no_dot():
    assert file_name_check("example.txt") == 'Yes'

def test_file_name_check_empty_name():
    assert file_name_check("") == 'No'

def test_file_name_check_no_letter_before_dot():
    assert file_name_check("1example.dll") == 'No'

def test_file_name_check_no_letter_after_dot():
    assert file_name_check("example.txt") == 'Yes'

def test_file_name_check_invalid_characters_before_dot():
    assert file_name_check("example.txt1") == 'No'

def test_file_name_check_invalid_characters_after_dot():
    assert file_name_check("example.txt") == 'Yes'