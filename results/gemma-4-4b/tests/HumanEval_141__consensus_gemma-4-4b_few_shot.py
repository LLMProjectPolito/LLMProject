
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
        if '0' <= char <= '9':
            digit_count += 1

    if digit_count > 3:
        return "No"

    if len(parts) != 2:
      return "No"
    
    if dot_count != 1:
        return "No"

    if not name_before_dot:
        return "No"

    if not ('a' <= name_before_dot[0] <= 'z' or 'A' <= name_before_dot[0] <= 'Z'):
        return "No"

    if extension not in ['txt', 'exe', 'dll']:
        return "No"

    return "Yes"


@pytest.mark.parametrize(
    "file_name, expected",
    [
        ("example.txt", "Yes"),
        ("1example.dll", "No"),
        ("example.TXT", "Yes"),
        ("example.EXE", "Yes"),
        ("example.DLL", "Yes"),
        ("example.txt.bak", "No"),
        ("example", "No"),
        ("example.123", "No"),
        ("12345.txt", "No"),
        ("a.txt", "Yes"),
        ("A.exe", "Yes"),
        ("a.DLL", "Yes"),
        ("a.TXT", "Yes"),
        ("a.xyz", "No"),
        ("a.123", "No"),
        ("1.txt", "No"),
        ("abc.txt", "Yes"),
        ("abc1.txt", "No"),
        ("a.txt.bak", "No"),
        ("a.txt.exe", "No"),
        ("a.txt.", "No"),
        ("", "No"),
        (" .txt", "No"),
        ("a.txt ", "No"),
        ("a.txt. ", "No"),
        ("a.txt.exe", "No"),
        ("a.txt.DLL", "No"),
        ("a.txt.XEX", "No"),
        ("a.txt.dLL", "No"),
        ("a.txt.DLL.bak", "No"),
    ],
)
def test_file_name_check(file_name, expected):
    assert file_name_check(file_name) == expected