
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
def test_digit_boundary():
    # Boundary: Exactly 3 digits (Valid) vs 4 digits (Invalid)
    assert file_name_check("abc123.txt") == 'Yes'
    assert file_name_check("abc1234.txt") == 'No'

def test_dot_boundary():
    # Boundary: Exactly 1 dot (Valid) vs 0 dots (Invalid) vs 2 dots (Invalid)
    assert file_name_check("abc.txt") == 'Yes'
    assert file_name_check("abctxt") == 'No'
    assert file_name_check("abc.txt.txt") == 'No'

def test_prefix_boundary():
    # Boundary: Minimum length of prefix (1 char - Valid) vs empty prefix (Invalid)
    assert file_name_check("a.txt") == 'Yes'
    assert file_name_check(".txt") == 'No'

# Focus: Logic Branches
import pytest

def test_file_name_check_digit_and_dot_branches():
    # Valid: exactly 3 digits, exactly one dot
    assert file_name_check("file123.txt") == 'Yes'
    # Invalid: more than 3 digits
    assert file_name_check("file1234.txt") == 'No'
    # Invalid: no dot
    assert file_name_check("filenametxt") == 'No'
    # Invalid: more than one dot
    assert file_name_check("file.name.txt") == 'No'

def test_file_name_check_prefix_branches():
    # Invalid: starts with a digit
    assert file_name_check("1file.txt") == 'No'
    # Invalid: starts with a special character
    assert file_name_check("_file.txt") == 'No'
    # Invalid: empty substring before dot
    assert file_name_check(".txt") == 'No'
    # Valid: starts with letter
    assert file_name_check("A1.exe") == 'Yes'

def test_file_name_check_extension_branches():
    # Valid extensions
    assert file_name_check("test.txt") == 'Yes'
    assert file_name_check("test.exe") == 'Yes'
    assert file_name_check("test.dll") == 'Yes'
    # Invalid extensions
    assert file_name_check("test.pdf") == 'No'
    assert file_name_check("test.py") == 'No'
    assert file_name_check("test.txt1") == 'No'

# Focus: Equivalence Partitioning
import pytest

def test_file_name_check_valid_partitions():
    # Valid: 0-3 digits, 1 dot, starts with letter, valid extension
    assert file_name_check("document123.txt") == 'Yes'
    assert file_name_check("App.exe") == 'Yes'
    assert file_name_check("system.dll") == 'Yes'

def test_file_name_check_invalid_digit_partition():
    # Invalid: More than three digits
    assert file_name_check("file1234.txt") == 'No'
    assert file_name_check("data12345.exe") == 'No'

def test_file_name_check_invalid_extension_partition():
    # Invalid: Extension not in ['txt', 'exe', 'dll']
    assert file_name_check("image.jpg") == 'No'
    assert file_name_check("script.py") == 'No'
    assert file_name_check("archive.zip") == 'No'