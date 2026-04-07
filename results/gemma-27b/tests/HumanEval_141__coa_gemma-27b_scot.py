
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
import pytest

def test_boundary_digit_count_max():
    assert file_name_check("abc123.txt") == "Yes"

def test_boundary_digit_count_over():
    assert file_name_check("abc1234.txt") == "No"

def test_boundary_dot_count_one():
    assert file_name_check("example.txt") == "Yes"

def test_boundary_dot_count_zero():
    assert file_name_check("exampletxt") == "No"

def test_boundary_dot_count_multiple():
    assert file_name_check("example.txt.txt") == "No"

def test_boundary_prefix_empty():
    assert file_name_check(".txt") == "No"

def test_boundary_prefix_letter():
    assert file_name_check("a.txt") == "Yes"

def test_boundary_prefix_digit():
    assert file_name_check("1.txt") == "No"

def test_boundary_suffix_valid():
    assert file_name_check("example.txt") == "Yes"

def test_boundary_suffix_invalid():
    assert file_name_check("example.doc") == "No"

# Focus: Logic Branches
import pytest

def test_file_name_check_valid():
    assert file_name_check("example.txt") == "Yes"
    assert file_name_check("AnotherExample.exe") == "Yes"
    assert file_name_check("file123.dll") == "Yes"
    assert file_name_check("A.txt") == "Yes"

def test_file_name_check_invalid_digit_count():
    assert file_name_check("1234example.txt") == "No"
    assert file_name_check("example1234.dll") == "No"
    assert file_name_check("123example123.exe") == "No"

def test_file_name_check_invalid_dot_count():
    assert file_name_check("example.txt.txt") == "No"
    assert file_name_check("exampletxt") == "No"
    assert file_name_check(".txt") == "No"

def test_file_name_check_invalid_extension():
    assert file_name_check("example.pdf") == "No"
    assert file_name_check("example.jpg") == "No"
    assert file_name_check("example.py") == "No"

def test_file_name_check_invalid_start_character():
    assert file_name_check("1example.txt") == "No"
    assert file_name_check("!example.exe") == "No"
    assert file_name_check("_example.dll") == "No"

# Focus: Invalid Input Handling
import pytest

def test_invalid_input_too_many_digits():
    assert file_name_check("1234example.txt") == "No"

def test_invalid_input_no_dot():
    assert file_name_check("exampletxt") == "No"

def test_invalid_input_empty_before_dot():
    assert file_name_check(".txt") == "No"

def test_invalid_input_invalid_extension():
    assert file_name_check("example.pdf") == "No"

def test_invalid_input_starts_with_digit():
    assert file_name_check("1example.txt") == "No"

def test_invalid_input_multiple_dots():
    assert file_name_check("example.txt.txt") == "No"