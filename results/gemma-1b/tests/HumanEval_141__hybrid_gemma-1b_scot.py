
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

def validate_file_name(file_name):
    """
    Validates a file name according to the rules in Suite 1.

    Args:
        file_name: The file name to validate (string).

    Returns:
        'Yes' if the file name is valid, 'No' otherwise.
    """
    if not isinstance(file_name, str):
        return "No"

    if len(file_name) > 3:
        return "No"

    if not file_name.startswith('.'):
        return "No"

    if not file_name.startswith('a' <= file_name[1:].lower() <= 'z'):
        return "No"

    allowed_substrings = ['txt', 'exe', 'dll']
    if not file_name[1:].startswith(allowed_substrings):
        return "No"

    return "Yes"


def test_validate_file_name_valid():
    assert validate_file_name("example.txt") == "Yes"
    assert validate_file_name("1example.dll") == "No"
    assert validate_file_name("test.txt") == "Yes"
    assert validate_file_name("test.txt.txt") == "Yes"
    assert validate_file_name("test.txt.exe") == "Yes"
    assert validate_file_name("test.txt.dll") == "Yes"
    assert validate_file_name("test.txt.txt.txt") == "Yes"
    assert validate_file_name("test.txt.exe.dll") == "Yes"
    assert validate_file_name("test.txt.txt.exe") == "Yes"
    assert validate_file_name("test.txt.txt.exe.dll") == "Yes"
    assert validate_file_name("test.txt.exe.dll.txt") == "Yes"
    assert validate_file_name("test.txt.exe.dll.txt.txt") == "Yes"
    assert validate_file_name("test.txt.exe.dll.txt.exe") == "Yes"
    assert validate_file_name("test.txt.exe.dll.txt.exe.dll") == "Yes"
    assert validate_file_name("test.txt.exe.dll.txt.exe.dll.txt.txt") == "Yes"
    assert validate_file_name("test.txt.exe.dll.txt.exe.dll.txt.exe.dll") == "Yes"
    assert validate_file_name("test.txt.exe.dll.txt.exe.dll.txt.exe.dll.txt.exe.dll") == "Yes"


def test_validate_file_name_invalid():
    assert validate_file_name("123.txt") == "No"
    assert validate_file_name("abc.txt") == "No"
    assert validate_file_name("123.txt.txt") == "No"
    assert validate_file_name("123.txt.txt.txt") == "No"
    assert validate_file_name("123.txt.txt.exe") == "No"
    assert validate_file_name("123.txt.txt.exe.dll") == "No"
    assert validate_file_name("123.txt.txt.exe.dll.txt") == "No"
    assert validate_file_name("123.txt.txt.exe.dll.txt.txt.txt") == "No"
    assert validate_file_name("123.txt.txt.exe.dll.txt.exe") == "No"
    assert validate_file_name("123.txt.txt.exe.dll.txt.exe.dll") == "No"
    assert validate_file_name("123.txt.txt.exe.dll.txt.exe.dll.txt.exe.dll") == "No"
    assert validate_file_name("123.txt.txt.exe.dll.txt.exe.dll.txt.exe.dll.txt.exe.dll") == "No"
    print("All tests passed.")