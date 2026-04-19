
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
def test_file_name_check_digit_boundary():
    assert file_name_check("abc123.txt") == 'Yes'
    assert file_name_check("abc1234.txt") == 'No'

def test_file_name_check_prefix_boundary():
    assert file_name_check("a.txt") == 'Yes'
    assert file_name_check(".txt") == 'No'

def test_file_name_check_dot_boundary():
    assert file_name_check("a.txt") == 'Yes'
    assert file_name_check("a..txt") == 'No'

# Focus: Logic Branches
import pytest

def test_file_name_check_valid_branches():
    assert file_name_check("example.txt") == 'Yes'
    assert file_name_check("Document123.exe") == 'Yes'
    assert file_name_check("A.dll") == 'Yes'

def test_file_name_check_structural_branches():
    # More than three digits
    assert file_name_check("file1234.txt") == 'No'
    # Zero dots
    assert file_name_check("filenametxt") == 'No'
    # More than one dot
    assert file_name_check("file.name.txt") == 'No'

def test_file_name_check_content_branches():
    # Empty substring before dot
    assert file_name_check(".txt") == 'No'
    # Substring before dot starts with non-letter
    assert file_name_check("1file.txt") == 'No'
    # Invalid extension
    assert file_name_check("file.jpg") == 'No'
    assert file_name_check("file.py") == 'No'

# Focus: Type Scenarios
import pytest

def test_file_name_check_none():
    """Test the function with None as input to check for type handling."""
    assert file_name_check(None) == 'No'

def test_file_name_check_int():
    """Test the function with an integer as input to check for type handling."""
    assert file_name_check(123) == 'No'

def test_file_name_check_list():
    """Test the function with a list as input to check for type handling."""
    assert file_name_check(['example.txt']) == 'No'