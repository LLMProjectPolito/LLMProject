
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
    parts = file_name.split('.')
    if len(parts) != 2:
        return 'No'
    
    prefix = parts[0]
    suffix = parts[1]
    
    for char in prefix:
        if char.isdigit():
            digits += 1
    
    dot_count = file_name.count('.')
    
    if digits > 3 or dot_count != 1:
        return 'No'
    
    if not prefix or not 'a' <= prefix[0] <= 'z' or not 'A' <= prefix[0] <= 'Z':
        return 'No'
    
    if suffix not in ['txt', 'exe', 'dll']:
        return 'No'
    
    return 'Yes'

def test_valid_file_name():
    assert file_name_check("example.txt") == 'Yes'

def test_valid_file_name_with_digits():
    assert file_name_check("example123.txt") == 'No'

def test_valid_file_name_with_multiple_dots():
    assert file_name_check("example..txt") == 'No'

def test_invalid_prefix_not_letter():
    assert file_name_check("1example.txt") == 'No'

def test_invalid_suffix():
    assert file_name_check("example.pdf") == 'No'

def test_empty_prefix():
    assert file_name_check(".txt") == 'No'

def test_file_name_with_only_digits():
    assert file_name_check("123.txt") == 'No'

def test_file_name_with_more_than_three_digits():
    assert file_name_check("1234.txt") == 'No'

def test_file_name_with_leading_and_trailing_spaces():
    assert file_name_check("  example.txt  ") == 'Yes'

def test_file_name_with_special_characters():
    assert file_name_check("example!@#.txt") == 'No'

def test_file_name_with_unicode_characters():
    assert file_name_check("éxample.txt") == 'No'