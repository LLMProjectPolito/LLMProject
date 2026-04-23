
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

def test_valid_filenames():
    """Tests filenames that meet all criteria."""
    assert file_name_check("example.txt") == 'Yes'
    assert file_name_check("A1b2.exe") == 'Yes'
    assert file_name_check("z999.dll") == 'Yes'
    assert file_name_check("abc.txt") == 'Yes'
    assert file_name_check("Test.exe") == 'Yes'

def test_invalid_digit_count():
    """Tests filenames with more than three digits."""
    assert file_name_check("a1234.txt") == 'No'
    assert file_name_check("1234abc.exe") == 'No'
    assert file_name_check("abc1234.dll") == 'No'

def test_invalid_dot_count():
    """Tests filenames with zero or multiple dots."""
    assert file_name_check("filename") == 'No'
    assert file_name_check("my.file.txt") == 'No'
    assert file_name_check("file.name.exe") == 'No'
    assert file_name_check("file..txt") == 'No'

def test_invalid_prefix():
    """Tests filenames where the prefix is empty or does not start with a letter."""
    assert file_name_check(".txt") == 'No'  # Empty prefix
    assert file_name_check("1abc.txt") == 'No'  # Starts with digit
    assert file_name_check("_abc.txt") == 'No'  # Starts with underscore
    assert file_name_check(" abc.txt") == 'No'  # Starts with space
    assert file_name_check("!abc.txt") == 'No'  # Starts with special char

def test_invalid_extension():
    """Tests filenames with unsupported extensions."""
    assert file_name_check("file.png") == 'No'
    assert file_name_check("file.pdf") == 'No'
    assert file_name_check("file.txt1") == 'No'
    assert file_name_check("file.exe ") == 'No'  # Trailing space in extension
    assert file_name_check("file.TXT") == 'No'  # Assuming case sensitivity based on list

def test_edge_cases():
    """Tests various edge cases combining multiple rules."""
    # More than 3 digits AND invalid extension
    assert file_name_check("a1234.png") == 'No'
    # Starts with digit AND more than 3 digits
    assert file_name_check("12345.txt") == 'No'
    # Exactly 3 digits but invalid start
    assert file_name_check("1ab2c3.txt") == 'No'
    # Valid prefix and extension but multiple dots
    assert file_name_check("a.txt.exe") == 'No'