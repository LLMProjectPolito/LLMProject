
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

import re

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

    if file_name.count('.') != 1:
        return 'No'

    parts = file_name.split('.')
    if len(parts) != 2:
        return 'No'

    prefix = parts[0]
    suffix = parts[1]

    if not prefix:
        return 'No'

    if not re.match(r'^[a-zA-Z]', prefix):
        return 'No'

    if suffix not in ['txt', 'exe', 'dll']:
        return 'No'

    if sum(c.isdigit() for c in file_name) > 3:
        return 'No'

    return 'Yes'

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    s = s.lower()
    return s == s[::-1]

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)

import pytest

def test_valid_file_names():
    assert file_name_check("example.txt") == "Yes"
    assert file_name_check("document.dll") == "Yes"
    assert file_name_check("program.exe") == "Yes"
    assert file_name_check("a.txt") == "Yes"
    assert file_name_check("A.TXT") == "Yes"
    assert file_name_check("long_file_name.exe") == "Yes"
    assert file_name_check("file123.txt") == "Yes"
    assert file_name_check("file1234.txt") == "No"  # More than 3 digits
    assert file_name_check("file123a.txt") == "Yes" # Added test case

def test_invalid_file_names():
    assert file_name_check("1example.dll") == "No"  # Starts with digit
    assert file_name_check("example") == "No"  # No dot
    assert file_name_check("example..txt") == "No"  # Multiple dots
    assert file_name_check(".txt") == "No"  # Empty before dot
    assert file_name_check("example.") == "No"  # Empty after dot
    assert file_name_check("example.jpg") == "No"  # Invalid extension
    assert file_name_check("12345.txt") == "No" # Too many digits
    assert file_name_check("example_with_space.txt") == "Yes" # Spaces are allowed
    assert file_name_check("example-dash.txt") == "Yes" # Dashes are allowed
    assert file_name_check("example.tx") == "No"
    assert file_name_check("example.tXt") == "No"
    assert file_name_check(123) == "No"
    assert file_name_check(None) == "No"
    assert file_name_check("") == "No"
    assert file_name_check("example.txt.") == "No"
    assert file_name_check("example.txt ") == "No"
    assert file_name_check("example.txt_") == "No"

def test_edge_cases():
    assert file_name_check("a.txt") == "Yes"
    assert file_name_check("A.TXT") == "Yes"
    assert file_name_check("000.txt") == "Yes"
    assert file_name_check("001.txt") == "Yes"
    assert file_name_check("1234567890.txt") == "No"
    assert file_name_check("a123.txt") == "Yes"
    assert file_name_check("a1234.txt") == "No"
    assert file_name_check("a12.txt") == "Yes"
    assert file_name_check("a.123") == "No"
    assert file_name_check("a.txt.txt") == "No"

def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_max_empty():
    assert get_max([]) == None