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
    digits = 0
    for char in file_name:
        if char.isdigit():
            digits += 1
    if digits > 3:
        return 'No'

    if file_name.count('.') != 1:
        return 'No'

    dot_index = file_name.find('.')
    prefix = file_name[:dot_index]
    suffix = file_name[dot_index + 1:]

    if not prefix or not 'a' <= prefix[0] <= 'z' or not 'A' <= prefix[0] <= 'Z':
        return 'No'

    if suffix not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'

def test_valid_file_name():
    assert file_name_check("example.txt") == 'Yes'

def test_valid_file_name_with_digits():
    assert file_name_check("example123.txt") == 'No'

def test_no_dot():
    assert file_name_check("example") == 'No'

def test_multiple_dots():
    assert file_name_check("example.txt.txt") == 'No'

def test_empty_prefix():
    assert file_name_check(".txt") == 'No'

def test_invalid_prefix():
    assert file_name_check("1example.txt") == 'No'

def test_invalid_suffix():
    assert file_name_check("example.pdf") == 'No'

def test_prefix_with_digits():
    assert file_name_check("1example.txt") == 'No'

def test_prefix_with_special_characters():
    assert file_name_check("!example.txt") == 'No'

def test_long_prefix():
    assert file_name_check("abcdefg.txt") == 'No'

def test_long_prefix_with_digits():
    assert file_name_check("abcdefg123.txt") == 'No'

def test_empty_suffix():
    assert file_name_check("example.") == 'No'

def test_file_name_with_only_digits():
    assert file_name_check("12345.txt") == 'No'

def test_file_name_with_leading_and_trailing_spaces():
    assert file_name_check("  example.txt  ") == 'Yes'

def test_file_name_with_spaces_before_dot():
    assert file_name_check(" example.txt ") == 'No'

def test_file_name_with_spaces_after_dot():
    assert file_name_check("example. txt") == 'No'

def test_file_name_with_spaces_around_dot():
    assert file_name_check("example.  txt") == 'No'