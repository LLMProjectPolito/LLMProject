
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
    if not isinstance(file_name, str):
        return "No"

    if len(file_name) > 3:
        return "No"

    if not file_name.startswith('.'):
        return "No"

    if not file_name.startswith('a' <= file_name[1:].lower() <= 'z'):
        return "No"

    if file_name.endswith('txt') or file_name.endswith('exe') or file_name.endswith('dll'):
        return "Yes"

    return "No"


def test_file_name_check_valid():
    assert file_name_check("example.txt") == "Yes"
    assert file_name_check("1example.dll") == "No"
    assert file_name_check("test.txt") == "Yes"
    assert file_name_check("test.txt.bak") == "No"
    assert file_name_check("test.txt.exe") == "Yes"
    assert file_name_check("test.txt.dll") == "Yes"
    assert file_name_check("test.txt.txt") == "Yes"
    assert file_name_check("test.txt.exe.txt") == "No"
    assert file_name_check("test.txt.dll.txt") == "No"
    assert file_name_check("test.txt.exe.dll") == "Yes"
    assert file_name_check("test.txt.txt.exe") == "No"
    assert file_name_check("test.txt.txt.dll.txt") == "No"
    assert file_name_check("test.txt.exe.txt.dll") == "No"
    assert file_name_check("test.txt.exe.dll.txt.exe") == "No"
    assert file_name_check("test.txt.exe.dll.txt.exe.txt") == "No"
    assert file_name_check("test.txt.exe.dll.txt.exe.dll") == "No"
    assert file_name_check("test.txt.exe.dll.txt.exe.dll.txt.exe") == "No"
    assert file_name_check("test.txt.exe.dll.txt.exe.dll.txt.exe.txt.exe") == "No"
    assert file_name_check("test.txt.exe.dll.txt.exe.dll.txt.exe.dll.txt.exe.txt.exe") == "No"

def test_file_name_check_invalid():
    assert file_name_check("example") == "No"
    assert file_name_check("123example.dll") == "No"
    assert file_name_check("test.txt") == "No"
    assert file_name_check("test.txt.exe") == "No"
    assert file_name_check("test.txt.dll") == "No"
    assert file_name_check("test.txt.txt.exe") == "No"
    assert file_name_check("test.txt.txt.dll.txt") == "No"
    assert file_name_check("test.txt.exe.txt") == "No"
    assert file_name_check("test.txt.dll.txt.exe") == "No"
    assert file_name_check("test.txt.exe.dll.txt.exe.txt") == "No"
    assert file_name_check("test.txt.exe.dll.txt.exe.dll.txt.exe") == "No"
    assert file_name_check("test.txt.exe.dll.txt.exe.dll.txt.exe.txt.exe") == "No"

def test_file_name_check_empty():
    assert file_name_check("") == "No"

def test_file_name_check_non_string():
    assert file_name_check(123) == "No"
    assert file_name_check(None) == "No"
    assert file_name_check(True) == "No"
    assert file_name_check("") == "No"