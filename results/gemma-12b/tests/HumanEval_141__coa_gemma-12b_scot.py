
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


# Focus: Boundary Values
def test_boundary_valid_name_with_max_digits():
    assert file_name_check("a123.txt") == 'Yes'

def test_boundary_valid_name_no_digits():
    assert file_name_check("example.txt") == 'Yes'

def test_boundary_invalid_name_empty_before_dot():
    assert file_name_check(".txt") == 'No'

# Focus: Type Scenarios
def test_file_name_check_valid_scenario():
    assert file_name_check("example.txt") == 'Yes'

def test_file_name_check_invalid_digit_scenario():
    assert file_name_check("1234example.txt") == 'No'

def test_file_name_check_invalid_extension_scenario():
    assert file_name_check("example.pdf") == 'No'

# Focus: Logic Branches
def test_file_name_check_valid_name():
    assert file_name_check("example.txt") == 'Yes'

def test_file_name_check_invalid_digit_count():
    assert file_name_check("1234example.txt") == 'No'

def test_file_name_check_invalid_extension():
    assert file_name_check("example.pdf") == 'No'