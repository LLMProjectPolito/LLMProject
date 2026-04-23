
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
    parts = file_name.split('.')

    if len(parts) != 2:
        return "No"

    base_name = parts[0]
    extension = parts[1]

    for char in base_name:
        if char.isdigit():
            digit_count += 1

    if digit_count > 3:
        return "No"

    if dot_count != 1:
        return "No"

    if not base_name or not base_name[0].isalpha():
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
        ("example.123", "No"),
        ("1234.txt", "No"),
        ("a.txt", "Yes"),
        ("A.exe", "Yes"),
        ("a.DLL", "Yes"),
        ("a1.txt", "No"),
        ("1a.txt", "No"),
        ("a.123", "No"),
        ("1.a", "No"),
        ("", "No"),
        ("example", "No"),
        ("example.com", "No"),
        ("example..txt", "No"),
        ("example.txt.", "No"),
        ("example.tXt", "Yes"),
        ("example.tXT", "Yes"),
        ("example.tXt.txt", "No"),
        ("example.txt.txt", "No"),
        ("example.txt.exe", "No"),
    ],
)
def test_file_name_check(file_name, expected):
    assert file_name_check(file_name) == expected

@pytest.mark.parametrize(
    "file_name, expected",
    [
        ("file with spaces.txt", "Yes"),
        ("file with  spaces.txt", "Yes"),
        ("file with spaces.exe", "Yes"),
        ("file with spaces.dll", "Yes"),
    ],
)
def test_file_name_check_with_spaces(file_name, expected):
    assert file_name_check(file_name) == expected

@pytest.mark.parametrize(
    "file_name, expected",
    [
        ("file_name_with_underscores.txt", "Yes"),
        ("file_name_with_underscores.exe", "Yes"),
        ("file_name_with_underscores.dll", "Yes"),
    ],
)
def test_file_name_check_with_underscores(file_name, expected):
    assert file_name_check(file_name) == expected

@pytest.mark.parametrize(
    "file_name, expected",
    [
        ("file_name_with_hyphens.txt", "Yes"),
        ("file_name_with_hyphens.exe", "Yes"),
        ("file_name_with_hyphens.dll", "Yes"),
    ],
)
def test_file_name_check_with_hyphens(file_name, expected):
    assert file_name_check(file_name) == expected

@pytest.mark.parametrize(
    "file_name, expected",
    [
        ("file_name_with_numbers_and_underscores.txt", "Yes"),
        ("file_name_with_numbers_and_underscores.exe", "Yes"),
        ("file_name_with_numbers_and_underscores.dll", "Yes"),
    ],
)
def test_file_name_check_with_mixed_characters(file_name, expected):
    assert file_name_check(file_name) == expected