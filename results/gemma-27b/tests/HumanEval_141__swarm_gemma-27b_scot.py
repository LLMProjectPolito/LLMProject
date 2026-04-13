
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
    digit_count = 0
    for char in file_name:
        if char.isdigit():
            digit_count += 1

    if digit_count > 3:
        return 'No'

    if file_name.count('.') != 1:
        return 'No'

    parts = file_name.split('.')
    if not parts[0]:
        return 'No'

    if not parts[0][0].isalpha():
        return 'No'

    if parts[1] not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'

def test_edge_case_many_digits_before_dot():
    assert file_name_check("1234example.txt") == "No"

def test_valid_file_name():
    assert file_name_check("example.txt") == "Yes"

def test_invalid_file_name_starts_with_digit():
    assert file_name_check("1example.dll") == "No"

def test_invalid_file_name_no_dot():
    assert file_name_check("exampletxt") == "No"

def test_invalid_file_name_multiple_dots():
    assert file_name_check("example.txt.txt") == "No"

def test_invalid_file_name_empty_before_dot():
    assert file_name_check(".txt") == "No"

def test_invalid_file_name_invalid_extension():
    assert file_name_check("example.pdf") == "No"

def test_valid_file_name_with_digits():
    assert file_name_check("example12.txt") == "Yes"

def test_valid_file_name_with_uppercase():
    assert file_name_check("Example.txt") == "Yes"

def test_invalid_file_name_more_than_three_digits():
    assert file_name_check("example1234.txt") == "No"