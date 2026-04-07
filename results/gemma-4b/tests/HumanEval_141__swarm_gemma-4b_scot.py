
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

### SCoT Steps:
### STEP 1: REASONING - The function checks for a specific file name format. An edge case is a file name with only digits and a dot, which should return 'No' because the initial part before the dot must start with a letter.
### STEP 2: PLAN - Test function name: test_edge_case. Scenario: A file name consisting only of digits and a dot.
### STEP 3: CODE - Write the high-quality pytest suite.
def test_edge_case():
    assert file_name_check("123.456") == 'No'

def test_valid_name():
    assert file_name_check("example.txt") == 'Yes'

def test_valid_name_2():
    assert file_name_check("another.exe") == 'Yes'

def test_valid_name_3():
    assert file_name_check("test.dll") == 'Yes'

def test_too_many_digits():
    assert file_name_check("1234.txt") == 'No'

def test_no_dot():
    assert file_name_check("exampletxt") == 'No'

def test_multiple_dots():
    assert file_name_check("example.txt.bak") == 'No'

def test_starts_with_digit():
    assert file_name_check("1example.txt") == 'No'

def test_invalid_extension():
    assert file_name_check("example.pdf") == 'No'