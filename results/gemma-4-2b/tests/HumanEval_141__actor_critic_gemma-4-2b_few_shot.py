
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
    digits = 0
    dot_count = 0
    for char in file_name:
        if char.isdigit():
            digits += 1
        if char == '.':
            dot_count += 1

    if digits > 3 or dot_count != 1:
        return 'No'

    parts = file_name.split('.')
    if not parts[0]:
        return 'No'

    first_part = parts[0]
    if not first_part[0].isalpha():
        return 'No'

    second_part = parts[1]
    if second_part not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'

def test_file_name_check_valid():
    assert file_name_check("example.txt") == "Yes"
    assert file_name_check("my_file.exe") == "Yes"
    assert file_name_check("another.dll") == "Yes"
    assert file_name_check("a.txt") == "Yes"
    assert file_name_check("A.exe") == "Yes"
    assert file_name_check("test.DLL") == "Yes"
    assert file_name_check("test.txt") == "Yes"
    assert file_name_check("test.exe") == "Yes"

def test_file_name_check_invalid_digits():
    assert file_name_check("123example.txt") == "No"
    assert file_name_check("12345example.txt") == "No"

def test_file_name_check_invalid_dot_count():
    assert file_name_check("example") == "No"
    assert file_name_check("example..txt") == "No"

def test_file_name_check_empty_first_part():
    assert file_name_check(".txt") == "No"

def test_file_name_check_invalid_first_char():
    assert file_name_check("1example.txt") == "No"
    assert file_name_check("123example.txt") == "No"

def test_file_name_check_invalid_second_part():
    assert file_name_check("example.java") == "No"
    assert file_name_check("example.py") == "No"

def test_file_name_check_edge_case_empty_string():
    assert file_name_check("") == "No"

def test_file_name_check_edge_case_only_dot():
    assert file_name_check(".").isalpha() == "No"

def test_file_name_check_edge_case_dot_at_start():
    assert file_name_check(".txt") == "No"

def test_file_name_check_special_characters():
    assert file_name_check("example!txt") == "No"

def test_file_name_check_numbers_only():
    assert file_name_check("12345.txt") == "No"

def test_file_name_check_leading_trailing_dot():
    assert file_name_check("example..txt") == "No"

def test_file_name_check_multiple_dots():
    assert file_name_check("example.a.txt") == "No"

def test_file_name_check_special_characters_before_dot():
    assert file_name_check("example!txt") == "No"

def test_file_name_check_special_characters_after_dot():
    assert file_name_check("example.!") == "No"

def test_file_name_check_invalid_extension():
    assert file_name_check("example.java") == "No"

def test_file_name_check_extension_number():
    assert file_name_check("example.123") == "No"

def test_file_name_check_extension_special_char():
    assert file_name_check("example.!txt") == "No"

def test_file_name_check_extension_special_char_num():
    assert file_name_check("example.1!txt") == "No"

def test_file_name_check_extension_special_char_letter():
    assert file_name_check("example.a!txt") == "No"