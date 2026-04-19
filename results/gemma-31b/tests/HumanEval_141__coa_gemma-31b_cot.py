
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
def test_file_name_check_digit_boundaries():
    # Boundary: exactly 3 digits (valid) vs 4 digits (invalid)
    assert file_name_check("a123.txt") == 'Yes'
    assert file_name_check("a1234.txt") == 'No'

def test_file_name_check_dot_boundaries():
    # Boundary: 0 dots (invalid), 1 dot (valid), 2 dots (invalid)
    assert file_name_check("exampletxt") == 'No'
    assert file_name_check("example.txt") == 'Yes'
    assert file_name_check("example.txt.txt") == 'No'

def test_file_name_check_prefix_boundaries():
    # Boundary: minimum valid prefix length (1 letter) vs empty prefix
    assert file_name_check("a.txt") == 'Yes'
    assert file_name_check(".txt") == 'No'

# Focus: Logic Branches
def test_file_name_check_valid_branches():
    assert file_name_check("example.txt") == 'Yes'
    assert file_name_check("MyFile123.exe") == 'Yes'
    assert file_name_check("a.dll") == 'Yes'

def test_file_name_check_invalid_structure_branches():
    assert file_name_check("file1234.txt") == 'No'  # More than 3 digits
    assert file_name_check("file.txt.txt") == 'No'  # More than one dot
    assert file_name_check("filename") == 'No'      # No dot

def test_file_name_check_invalid_content_branches():
    assert file_name_check("1file.txt") == 'No'     # Starts with digit
    assert file_name_check(".txt") == 'No'          # Empty prefix
    assert file_name_check("file.pdf") == 'No'      # Invalid extension

# Focus: Equivalence Partitioning
import pytest

def test_file_name_check_valid_partitions():
    # Valid: starts with letter, <= 3 digits, 1 dot, valid extension
    assert file_name_check("myFile123.txt") == 'Yes'
    assert file_name_check("A.exe") == 'Yes'
    assert file_name_check("test.dll") == 'Yes'

def test_file_name_check_invalid_prefix_and_dots():
    # Invalid: starts with digit, empty prefix, or incorrect dot count
    assert file_name_check("1file.txt") == 'No'
    assert file_name_check(".txt") == 'No'
    assert file_name_check("file.name.txt") == 'No'
    assert file_name_check("filenametxt") == 'No'

def test_file_name_check_invalid_extension_and_digits():
    # Invalid: extension not in list or > 3 digits
    assert file_name_check("file.pdf") == 'No'
    assert file_name_check("file.txt1") == 'No'
    assert file_name_check("file1234.exe") == 'No'