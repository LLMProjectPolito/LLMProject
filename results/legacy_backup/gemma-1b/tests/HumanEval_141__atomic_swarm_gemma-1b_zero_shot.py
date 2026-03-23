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
    if not isinstance(file_name, str):
        return 'No'

    if len(file_name) <= 3:
        return 'No'

    if not file_name.startswith('.'):
        return 'No'

    if not file_name.endswith('txt') and not file_name.endswith('exe') and not file_name.endswith('dll'):
        return 'No'

    return 'Yes'

def test_file_name_check():
    assert file_name_check("example.txt") == 'Yes'
    assert file_name_check("1example.dll") == 'No'
    assert file_name_check("a.txt") == 'No'
    assert file_name_check("1a.txt") == 'No'
    assert file_name_check("1a.txt.txt") == 'No'
    assert file_name_check("1a.txt.txt.txt") == 'No'
    assert file_name_check("1a.txt.txt.txt.txt") == 'No'
    assert file_name_check("") == 'No'
    assert file_name_check("1") == 'No'
    assert file_name_check("a.txt") == 'No'
    assert file_name_check("A.txt") == 'No'

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
    parts = file_name.split(".")
    if len(parts) > 3:
        return 'No'
    if len(parts) == 1:
        return 'No'
    if not parts[0]:
        return 'No'
    if not parts[1][0].isalpha():
        return 'No'
    if parts[1][-1] not in ['txt', 'exe', 'dll']:
        return 'No'
    return 'Yes'