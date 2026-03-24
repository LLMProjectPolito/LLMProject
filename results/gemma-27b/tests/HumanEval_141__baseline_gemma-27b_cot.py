
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
    if len(parts) != 2:
        return 'No'

    before_dot = parts[0]
    after_dot = parts[1]

    if not before_dot:
        return 'No'

    if not before_dot[0].isalpha():
        return 'No'

    if after_dot not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'

def test_valid_file_names():
    assert file_name_check("example.txt") == 'Yes'
    assert file_name_check("MyFile.exe") == 'Yes'
    assert file_name_check("document1.dll") == 'Yes'
    assert file_name_check("a123.txt") == 'Yes'
    assert file_name_check("A123.exe") == 'Yes'

def test_invalid_file_names_digit_count():
    assert file_name_check("1234example.txt") == 'No'
    assert file_name_check("example1234.dll") == 'No'
    assert file_name_check("1234.exe") == 'No'

def test_invalid_file_names_dot_count():
    assert file_name_check("example.txt.txt") == 'No'
    assert file_name_check("exampletxt") == 'No'
    assert file_name_check(".txt") == 'No'

def test_invalid_file_names_starts_with_digit():
    assert file_name_check("1example.dll") == 'No'
    assert file_name_check("2MyFile.exe") == 'No'

def test_invalid_file_names_empty_before_dot():
    assert file_name_check(".txt") == 'No'

def test_invalid_file_names_invalid_extension():
    assert file_name_check("example.pdf") == 'No'
    assert file_name_check("document.jpg") == 'No'

def test_edge_cases():
    assert file_name_check("a.txt") == 'Yes'
    assert file_name_check("A.exe") == 'Yes'
    assert file_name_check("abc.dll") == 'Yes'
    assert file_name_check("a1.txt") == 'Yes'
    assert file_name_check("a12.exe") == 'Yes'
    assert file_name_check("a123.dll") == 'Yes'
    assert file_name_check("a1234.txt") == 'No'
    assert file_name_check("1a.txt") == 'No'
    assert file_name_check("example..txt") == 'No'
    assert file_name_check("example.txt.") == 'No'