
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
    name_parts = file_name.split('.')
    if len(name_parts) != 2:
        return 'No'
    
    prefix = name_parts[0]
    suffix = name_parts[1]

    for char in prefix:
        if char.isdigit():
            digits += 1
    
    dot_count = prefix.count('.')
    if dot_count != 1:
        return 'No'
    
    if not prefix[0].isalpha():
        return 'No'
    
    if suffix not in ['txt', 'exe', 'dll']:
        return 'No'
    
    if digits > 3:
        return 'No'
    
    return 'Yes'

def test_file_name_check_valid():
    assert file_name_check("example.txt") == 'Yes'

def test_file_name_check_invalid_digits():
    assert file_name_check("123example.txt") == 'No'

def test_file_name_check_invalid_dot():
    assert file_name_check("example.exe") == 'No'

def test_file_name_check_invalid_prefix():
    assert file_name_check("1example.txt") == 'No'

def test_file_name_check_invalid_suffix():
    assert file_name_check("example.pdf") == 'No'

def test_file_name_check_empty_prefix():
    assert file_name_check(".txt") == 'No'

def test_file_name_check_multiple_dots():
    assert file_name_check("example..txt") == 'No'