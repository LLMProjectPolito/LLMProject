
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
    dot_count = 0
    parts = file_name.split(".")

    if len(parts) != 2:
        return "No"

    name_before_dot = parts[0]
    extension = parts[1]

    for char in name_before_dot:
        if char.isdigit():
            digit_count += 1

    if digit_count > 3:
        return "No"

    if dot_count != 1:
        return "No"

    if not name_before_dot:
        return "No"

    if not 'a' <= name_before_dot[0] <= 'z' and not 'A' <= name_before_dot[0] <= 'Z':
        return "No"

    if extension not in ["txt", "exe", "dll"]:
        return "No"

    return "Yes"


@pytest.mark.parametrize(
    "file_name, expected",
    [
        ("example.txt", "Yes"),
        ("1example.dll", "No"),
        ("example.TXT", "Yes"),
        ("example.exe", "Yes"),
        ("example.DLL", "Yes"),
        ("example.txt.bak", "No"),
        ("example", "No"),
        ("example.123.txt", "No"),
        ("12345.txt", "No"),
        ("a.txt", "Yes"),
        ("A.exe", "Yes"),
        ("a_file.txt", "No"),
        ("file.", "No"),
        ("file..txt", "No"),
        ("file.txt.", "No"),
        ("file.xyz", "No"),
        ("file.txt!", "No"),
        ("file.txt ", "No"),
        ("file.txt\n", "No"),
        ("file.txt\t", "No"),
        ("file.tXt", "Yes"),
        ("file.txt.txt", "No"),
        ("file.txt1", "No"),
        ("a.txt1", "No"),
        ("a.txt.exe", "No"),
        ("a.txt.dll", "No"),
        ("a.txt.txt", "No"),
        ("a.txt.123", "No"),
        ("a.txt.", "No"),
        ("a..txt", "No"),
        ("", "No"),
        ("txt", "No"),
        ("a", "No"),
        ("a.txt", "Yes"),
        ("a.txt.exe", "No"),
        ("a.txt.dll", "No"),
        ("a.txt.txt", "No"),
        ("a.txt1", "No"),
    ],
)
def test_file_name_check(file_name, expected):
    assert file_name_check(file_name) == expected