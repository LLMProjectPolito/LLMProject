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
    dot_count = file_name.count('.')
    if dot_count != 1:
        return 'No'

    parts = file_name.split('.')
    before_dot = parts[0]
    file_extension = parts[1]

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

    if file_extension.lower() not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'


def test_valid_filename():
    assert file_name_check("example.txt") == 'Yes'
    assert file_name_check("MyFile.exe") == 'Yes'
    assert file_name_check("another_file.dll") == 'Yes'
    assert file_name_check("a123.txt") == 'Yes'
    assert file_name_check("A123.exe") == 'Yes'
    assert file_name_check("example123.txt") == 'Yes' # Digits at the end

def test_invalid_filename_digit_start():
    assert file_name_check("1example.dll") == 'No'
    assert file_name_check("2file.txt") == 'No'

def test_invalid_filename_too_many_digits():
    assert file_name_check("example1234.txt") == 'No'
    assert file_name_check("a1234.exe") == 'No'

def test_invalid_filename_multiple_dots():
    assert file_name_check("example.file.txt") == 'No'
    assert file_name_check("file.name.dll") == 'No'

def test_invalid_filename_empty_before_dot():
    assert file_name_check(".txt") == 'No'
    assert file_name_check(".exe") == 'No'

def test_invalid_filename_empty_string():
    assert file_name_check("") == 'No'

def test_invalid_filename_invalid_extension():
    assert file_name_check("example.pdf") == 'No'
    assert file_name_check("file.jpg") == 'No'

def test_filename_only_digits():
    assert file_name_check("123.txt") == 'No'

def test_long_filename():
    long_string = "a" * 250 + ".txt"
    assert file_name_check(long_string) == 'Yes'