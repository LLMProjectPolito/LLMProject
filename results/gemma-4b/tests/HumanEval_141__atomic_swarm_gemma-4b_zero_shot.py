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
    dot_count = 0
    parts = file_name.split('.')
    if len(parts) != 2:
        return 'No'
    
    before_dot = parts[0]
    after_dot = parts[1]
    
    for char in before_dot:
        if char.isdigit():
            digits += 1
    
    dot_count = before_dot.count('.')
    
    if digits > 3 or dot_count != 1:
        return 'No'
    
    if not before_dot or not before_dot[0].isalpha():
        return 'No'
    
    if after_dot not in ['txt', 'exe', 'dll']:
        return 'No'
    
    return 'Yes'

def test_edge_empty_string():
    assert file_name_check("") == 'No'

def test_edge_only_digits():
    assert file_name_check("1234") == 'No'

def test_edge_multiple_dots():
    assert file_name_check("file..txt") == 'No'

def test_edge_no_dot():
    assert file_name_check("file") == 'No'

def test_edge_dot_at_start():
    assert file_name_check(".txt") == 'No'

def test_edge_dot_at_end():
    assert file_name_check("file.") == 'No'

def test_edge_invalid_extension():
    assert file_name_check("file.pdf") == 'No'

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

    parts = file_name.split('.')
    if not parts[0] or not parts[0][0].isalpha():
        return 'No'

    if parts[1] not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'

def test_invalid_type():
    assert file_name_check(123) == 'No'

def test_too_many_digits():
    assert file_name_check("123example.txt") == 'No'

def test_no_dot():
    assert file_name_check("exampletxt") == 'No'

def test_empty_before_dot():
    assert file_name_check(" .txt") == 'No'

def test_invalid_extension():
    assert file_name_check("example.pdf") == 'No'