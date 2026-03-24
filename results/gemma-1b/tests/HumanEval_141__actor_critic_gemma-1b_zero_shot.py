
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
        return 'No'

    if len(file_name) > 3:
        return 'No'

    if not file_name.startswith('.'):
        return 'No'

    parts = file_name.split('.')
    if len(parts) != 2:
        return 'No'

    if not parts[0][0].isalpha():
        return 'No'

    if parts[1] not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'


def test_file_name_check_valid():
    assert file_name_check("example.txt") == "Yes"
    assert file_name_check("1example.dll") == "No"
    assert file_name_check("example.txt.bak") == "No"
    assert file_name_check("example.txt.txt") == "Yes"
    assert file_name_check("example.txt.exe") == "Yes"
    assert file_name_check("example.txt.dll") == "Yes"
    assert file_name_check("example.txt.txt.exe") == "No"
    assert file_name_check("example.txt.txt.dll.exe") == "No"
    assert file_name_check("example.txt.txt.exe.dll") == "No"
    assert file_name_check("example.txt.txt.exe.dll.exe") == "No"
    assert file_name_check("example.txt.txt.exe.dll.dll") == "No"
    assert file_name_check("example.txt.txt.exe.dll.exe.dll") == "No"
    assert file_name_check("example.txt.txt.exe.dll.dll.exe.dll") == "No"
    assert file_name_check("example.txt.txt.exe.dll.dll.exe.dll.exe") == "No"
    assert file_name_check("example.txt.txt.exe.dll.dll.exe.dll.exe.dll") == "No"

def test_file_name_check_invalid():
    assert file_name_check(123) == "No"
    assert file_name_check("123.txt") == "No"
    assert file_name_check("123.txt.txt") == "No"
    assert file_name_check("123.txt.txt.txt") == "No"
    assert file_name_check("123.txt.txt.txt.txt") == "No"
    assert file_name_check("123.txt.txt.txt.txt.txt") == "No"
    assert file_name_check("") == "No"
    assert file_name_check(" ") == "No"
    assert file_name_check("a.txt") == "No"
    assert file_name_check("a.txt.txt") == "No"
    assert file_name_check("a.txt.txt.txt.txt") == "No"
    assert file_name_check("a.txt.txt.txt.txt.txt.txt") == "No"
    assert file_name_check("a.txt.txt.txt.txt.txt.txt.txt.txt") == "No"
    assert file_name_check("a.txt.txt.txt.txt.txt.txt.txt.txt.txt.txt") == "No"
    assert file_name_check("a.txt.txt.txt.txt.txt.txt.txt.txt.txt.txt.txt.txt") == "No"
    print("All tests passed")