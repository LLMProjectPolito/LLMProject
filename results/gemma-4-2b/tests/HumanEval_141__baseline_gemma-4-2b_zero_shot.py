
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
    digits = 0
    dot_count = 0
    for char in file_name:
        if char.isdigit():
            digits += 1
        if char == '.':
            dot_count += 1

    if digits > 3 or dot_count != 1:
        return 'No'

    parts = file_name.split('.')
    if not parts[0]:
        return 'No'

    first_char = parts[0][0]
    if not 'a' <= first_char <= 'z' or not 'A' <= first_char <= 'Z':
        return 'No'

    if parts[1] not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'

def test_valid_file_name():
    assert file_name_check("example.txt") == 'Yes'
    assert file_name_check("my_file.exe") == 'Yes'
    assert file_name_check("another.dll") == 'Yes'
    assert file_name_check("a.txt") == 'Yes'
    assert file_name_check("A.exe") == 'Yes'
    assert file_name_check("a1.txt") == 'Yes'
    assert file_name_check("a.dll") == 'Yes'
    assert file_name_check("a.exe") == 'Yes'

def test_invalid_file_name_too_many_digits():
    assert file_name_check("1234example.txt") == 'No'
    assert file_name_check("123.txt") == 'No'
    assert file_name_check("123.exe") == 'No'

def test_invalid_file_name_no_dot():
    assert file_name_check("example") == 'No'
    assert file_name_check("example.") == 'No'

def test_invalid_file_name_no_dot_and_too_few_digits():
    assert file_name_check("example") == 'No'
    assert file_name_check("a.txt") == 'No'

def test_invalid_file_name_empty_prefix():
    assert file_name_check(".txt") == 'No'
    assert file_name_check("..txt") == 'No'

def test_invalid_file_name_invalid_extension():
    assert file_name_check("example.java") == 'No'
    assert file_name_check("example.py") == 'No'
    assert file_name_check("example.csv") == 'No'

def test_invalid_file_name_invalid_first_char():
    assert file_name_check("1example.txt") == 'No'
    assert file_name_check("example1.txt") == 'No'
    assert file_name_check("example.txt1") == 'No'