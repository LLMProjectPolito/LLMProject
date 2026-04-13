
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
import math

import pytest

def test_basic():
    assert file_name_check("example.txt") == 'Yes'

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
    for char in file_name:
        if char.isdigit():
            digits += 1
    if digits > 3:
        return 'No'

    if file_name.count('.') != 1:
        return 'No'

    parts = file_name.split('.')
    if not parts[0] or not parts[0][0].isalpha():
        return 'No'

    if parts[1] not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'

def test_edge_empty():
    assert file_name_check("") == 'No'

def test_edge_too_many_digits():
    assert file_name_check("1234.txt") == 'No'

def test_edge_no_dot():
    assert file_name_check("exampletxt") == 'No'

def test_edge_dot_before_letter():
    assert file_name_check(".example.txt") == 'No'

def test_edge_dot_after_letter():
    assert file_name_check("example.txt.") == 'No'

def test_edge_invalid_extension():
    assert file_name_check("example.pdf") == 'No'

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

    digit_count = 0
    for char in file_name:
        if char.isdigit():
            digit_count += 1

    if digit_count > 3:
        return 'No'

    if file_name.count('.') != 1:
        return 'No'

    dot_index = file_name.find('.')
    prefix = file_name[:dot_index]
    suffix = file_name[dot_index + 1:]

    if not prefix or not 'a' <= prefix[0] <= 'z' or not 'A' <= prefix[0] <= 'Z':
        return 'No'

    if suffix not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'

def test_invalid_type():
    assert file_name_check(123) == 'No'

def test_too_many_digits():
    assert file_name_check("123example.txt") == 'No'

def test_no_dot():
    assert file_name_check("exampletxt") == 'No'

def test_empty_prefix():
    assert file_name_check(" .example.txt") == 'No'

def test_prefix_not_letter():
    assert file_name_check("1example.txt") == 'No'

def test_invalid_suffix():
    assert file_name_check("example.pdf") == 'No'