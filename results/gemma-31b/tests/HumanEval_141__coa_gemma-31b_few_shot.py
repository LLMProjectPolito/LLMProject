
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
def test_file_name_digit_boundaries():
    # Boundary: exactly 3 digits (valid) vs 4 digits (invalid)
    assert file_name_check("a123.txt") == 'Yes'
    assert file_name_check("a1234.txt") == 'No'

def test_file_name_prefix_boundaries():
    # Boundary: minimum length of prefix (1 letter) vs empty prefix
    assert file_name_check("a.txt") == 'Yes'
    assert file_name_check(".txt") == 'No'

def test_file_name_dot_boundaries():
    # Boundary: exactly one dot (valid) vs zero or two dots (invalid)
    assert file_name_check("a.txt") == 'Yes'
    assert file_name_check("atxt") == 'No'
    assert file_name_check("a.b.txt") == 'No'

# Focus: Logic Branches
import pytest

def test_file_name_check_valid_branches():
    # Valid cases covering different allowed extensions and digit counts (0-3)
    assert file_name_check("document.txt") == 'Yes'
    assert file_name_check("app123.exe") == 'Yes'
    assert file_name_check("Lib.dll") == 'Yes'

def test_file_name_check_invalid_digit_and_dot_branches():
    # Branch: More than three digits
    assert file_name_check("file1234.txt") == 'No'
    # Branch: Zero dots
    assert file_name_check("filenametxt") == 'No'
    # Branch: More than one dot
    assert file_name_check("file.name.txt") == 'No'

def test_file_name_check_invalid_prefix_and_extension_branches():
    # Branch: Starts with non-letter (digit)
    assert file_name_check("1file.txt") == 'No'
    # Branch: Empty substring before dot
    assert file_name_check(".txt") == 'No'
    # Branch: Extension not in ['txt', 'exe', 'dll']
    assert file_name_check("file.pdf") == 'No'
    assert file_name_check("file.png") == 'No'

# Focus: Type Scenarios
import pytest

def test_file_name_check_none():
    with pytest.raises((TypeError, AttributeError)):
        file_name_check(None)

def test_file_name_check_int():
    with pytest.raises((TypeError, AttributeError)):
        file_name_check(123)

def test_file_name_check_list():
    with pytest.raises((TypeError, AttributeError)):
        file_name_check(["example.txt"])