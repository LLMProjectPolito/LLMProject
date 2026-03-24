
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
    if not file_name:
        return 'No'

    dot_count = file_name.count('.')
    if dot_count != 1:
        return 'No'

    parts = file_name.split('.')
    before_dot = parts[0]
    after_dot = parts[1]

    if not before_dot:
        return 'No'

    if not before_dot[0].isalpha():
        return 'No'

    digit_count = 0
    for char in before_dot:
        if char.isdigit():
            digit_count += 1

    if digit_count > 3:
        return 'No'

    if after_dot.lower() not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'

### Tests (Pytest):
import pytest

def test_valid_filename():
    assert file_name_check("example.txt") == 'Yes'
    assert file_name_check("MyFile.exe") == 'Yes'
    assert file_name_check("another_file.dll") == 'Yes'
    assert file_name_check("example1.txt") == 'Yes'
    assert file_name_check("examp12le.dll") == 'Yes'
    assert file_name_check("examp123le.exe") == 'Yes'

def test_filename_must_start_with_letter():
    assert file_name_check("1example.dll") == 'No'

def test_invalid_filename_too_many_digits():
    assert file_name_check("ex1234mple.txt") == 'No'

def test_invalid_filename_multiple_dots():
    assert file_name_check("example.file.txt") == 'No'

def test_invalid_filename_no_dot():
    assert file_name_check("exampletxt") == 'No'

def test_invalid_filename_empty_string():
    assert file_name_check("") == 'No'

def test_invalid_filename_space_before_dot():
    assert file_name_check("example file.txt") == 'No'

def test_invalid_filename_whitespace():
    assert file_name_check(" example.txt ") == 'No'
    assert file_name_check("example.txt ") == 'No'

def test_invalid_filename_long_filename():
    long_filename = "a" * 200 + ".txt"
    assert file_name_check(long_filename) == 'Yes'

def test_valid_filename_uppercase_extension():
    assert file_name_check("example.TXT") == 'Yes'
    assert file_name_check("example.EXE") == 'Yes'
    assert file_name_check("example.DLL") == 'Yes'