
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

    if sum(1 for c in file_name if c.isdigit()) > 3:
        return 'No'

    parts = file_name.split('.')
    prefix = parts[0]
    suffix = parts[1]

    if not prefix:
        return 'No'

    if not re.match(r'^[a-zA-Z]', prefix):
        return 'No'

    if not re.match(r'^[a-zA-Z]+$', suffix):
        return 'No'

    if suffix.lower() not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'

import pytest

def test_valid_file_name():
    assert file_name_check("example.txt") == "Yes"
    assert file_name_check("document.dll") == "Yes"
    assert file_name_check("program.exe") == "Yes"
    assert file_name_check("a.txt") == "Yes"
    assert file_name_check("A.TXT") == "Yes"
    assert file_name_check("long_file_name.exe") == "Yes"
    assert file_name_check("file123.txt") == "Yes"
    assert file_name_check("file1234.txt") == "No"

def test_invalid_file_name():
    assert file_name_check("1example.dll") == "No"
    assert file_name_check(".txt") == "No"
    assert file_name_check("example") == "No"
    assert file_name_check("example.com") == "No"
    assert file_name_check("example..txt") == "No"
    assert file_name_check("12345.txt") == "No"
    assert file_name_check("1234.txt") == "No"
    assert file_name_check("123.txt") == "No"
    assert file_name_check("12.txt") == "No"
    assert file_name_check("1.txt") == "No"
    assert file_name_check("example.tx") == "No"
    assert file_name_check("example.t") == "No"
    assert file_name_check("example.abc") == "No"
    assert file_name_check(123) == "No"
    assert file_name_check(None) == "No"
    assert file_name_check("") == "No"
    assert file_name_check("example.txt.dll") == "No"
    assert file_name_check("example..txt") == "No"
    assert file_name_check("1234567890.txt") == "No"
    assert file_name_check("a1234.txt") == "No"
    assert file_name_check("a12345.txt") == "No"
    assert file_name_check("a123456.txt") == "No"
    assert file_name_check("a1234567.txt") == "No"
    assert file_name_check("a12345678.txt") == "No"
    assert file_name_check("a123456789.txt") == "No"
    assert file_name_check("a1234567890.txt") == "No"
    assert file_name_check("example.txt-") == "No"
    assert file_name_check("example!.txt") == "No"
    assert file_name_check("1234.txtx") == "No"