
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
    digit_count = 0
    dot_count = 0
    parts = file_name.split('.')

    if len(parts) != 2:
        return 'No'

    before_dot = parts[0]
    after_dot = parts[1]

    for char in before_dot:
        if char.isdigit():
            digit_count += 1

    if digit_count > 3:
        return 'No'

    if dot_count != 1:
        return 'No'

    if not before_dot:
        return 'No'

    if not before_dot[0].isalpha() and not before_dot[0].isspace():
        return 'No'

    if after_dot not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'


@pytest.mark.parametrize(
    "file_name, expected",
    [
        ("example.txt", "Yes"),
        ("1example.dll", "No"),
        ("a.txt", "Yes"),
        ("a.TXT", "Yes"),
        ("a.xyz", "No"),
        ("a.123", "No"),
        ("a.txt.bak", "No"),
        ("example", "No"),
        ("example.exe", "Yes"),
        ("example.DLL", "Yes"),
        (" .txt", "No"),
        ("a. ", "No"),
        ("0001.txt", "Yes"),
        ("a.123.txt", "No"),
        ("a.txt0", "Yes"),
        ("", "No"),
        ("a.txt ", "No"),
        ("a.txt.", "No"),
        ("a.tXt", "Yes"),
        ("a.  txt", "No"),
        ("a.txt ", "No"),
        ("a.txt.bak", "No"),
        ("a.txt.exe", "No"),
        ("a.txt.dll", "No"),
        ("a.txt.txt", "No"),
        ("a.txt.exe.bak", "No"),
        ("a.txt.exe.dll", "No"),
        ("a.txt.txt.bak", "No"),
        ("a.txt.txt.exe", "No"),
        ("a.txt.txt.dll", "No"),
        ("a.txt.txt.txt", "No"),
        ("a.txt.txt.exe", "No"),
        ("a.txt.txt.dll", "No"),
        ("a.txt.txt.txt.bak", "No"),
        ("a.txt.txt.txt.exe", "No"),
        ("a.txt.txt.txt.dll", "No"),
        ("a.txt.txt.txt.txt", "No"),
        ("a.txt.txt.txt.exe", "No"),
        ("a.txt.txt.txt.dll", "No"),
        ("a.txt.txt.txt.txt.bak", "No"),
        ("a.txt.txt.txt.txt.exe", "No"),
        ("a.txt.txt.txt.txt.dll", "No"),
        ("a.txt.txt.txt.txt.txt", "No"),
        ("a.txt.txt.txt.txt.exe", "No"),
        ("a.txt.txt.txt.txt.dll", "No"),
        ("a.txt.txt.txt.txt.txt.bak", "No"),
        ("a.txt.txt.txt.txt.txt.exe", "No"),
        ("a.txt.txt.txt.txt.txt.dll", "No"),
        ("a.txt.txt.txt.txt.txt.txt", "No"),
        ("a.txt.txt.txt.txt.txt.exe", "No"),
        ("a.txt.txt.txt.txt.txt.dll", "No"),
        ("a.txt.txt.txt.txt.txt.txt.bak", "No"),
        ("a.txt.txt.txt.txt.txt.txt.exe", "No"),
        ("a.txt.txt.txt.txt.txt.txt.dll", "No"),
        ("a.txt.txt.txt.txt.txt.txt.txt", "No"),
        ("a.txt.txt.txt.txt.txt.txt.exe", "No"),
        ("a.txt.txt.txt.txt.txt.txt.dll", "No"),
        ("a.txt.txt.txt.txt.txt.txt.txt.bak", "No"),
        ("a.txt.txt.txt.txt.txt.txt.txt.exe", "No"),
        ("a.txt.txt.txt.txt.txt.txt.txt.dll", "No"),
        ("a.txt.txt.txt.txt.txt.txt.txt.txt", "No"),
        ("a.txt.txt.txt.txt.txt.txt.txt.exe", "No"),
        ("a.txt.txt.txt.txt.txt.txt.txt.dll", "No"),
        ("a.txt.txt.txt.txt.txt.txt.txt.txt.bak", "No"),
        ("a.txt.txt.txt.txt.txt.txt.txt.txt.exe", "No"),
        ("a.txt.txt.txt.txt.txt.txt.txt.txt.dll", "No"),
    ],
)
def test_file_name_check(file_name, expected):
    assert file_name_check(file_name) == expected