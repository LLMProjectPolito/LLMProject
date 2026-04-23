
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
from your_module import file_name_check  # Replace your_module

def test_valid_file_name():
    assert file_name_check("example.txt") == "Yes"
    assert file_name_check("my_file.exe") == "Yes"
    assert file_name_check("data.dll") == "Yes"
    assert file_name_check("report.pdf") == "No" #Add PDF as a test case

def test_invalid_too_many_digits():
    assert file_name_check("123example.txt") == "No"
    assert file_name_check("12345example.txt") == "No"
    assert file_name_check("123.txt") == "No"

def test_invalid_no_dot():
    assert file_name_check("example") == "No"
    assert file_name_check("example.") == "No"

def test_invalid_multiple_dots():
    assert file_name_check("example..txt") == "No"
    assert file_name_check("example.txt.exe") == "No"

def test_invalid_empty_prefix():
    assert file_name_check(".txt") == "No"
    assert file_name_check("txt") == "No"

def test_invalid_suffix():
    assert file_name_check("example.xyz") == "No"
    assert file_name_check("example.data") == "No"
    assert file_name_check("example.abc") == "No"

def test_invalid_prefix_start_with_digit():
    assert file_name_check("1example.txt") == "No"
    assert file_name_check("1.txt") == "No"
    assert file_name_check("a1example.txt") == "No" #Added a case to make sure it doesn't work if it starts with a number

def test_empty_string():
    assert file_name_check("") == "No"

def test_special_characters():
    assert file_name_check("example!@#txt") == "No"
    assert file_name_check("example$%\^&\*txt") == "No"

def test_mixed_case_prefix():
    assert file_name_check("aExample.txt") == "Yes"
    assert file_name_check("AExample.txt") == "Yes"

def test_numbers_in_prefix():
    assert file_name_check("123a.txt") == "No"

def test_dot_at_start():
    assert file_name_check(".txt") == "No"

def test_dot_at_end():
    assert file_name_check("txt.") == "No"

# Suite 2 Tests
import pytest

def file_name_check(file_name):
    """Create a function which takes a string representing a file's name, and returns
    'Yes' if the the file's name is valid, and returns 'No' otherwise.
    A file's name is considered to be valid if and only if all the following conditions 
    are met:
    - There should not be more than three digits ('0'-'9) in the file's name.
    - The file's name contains exactly one dot '.'
    - The substring before the dot should not be empty, and it starts with a letter from 
    the latin alphapet ('a'-'z' and 'A'-'Z').
    - The substring after the dot should be one of these: ['txt', 'exe', 'dll']
    Examples:
    file_name_check("example.txt") # => 'Yes'
    file_name_check("1example.dll") # => 'No' (the name should start with a latin alphapet letter)
    """
    digit_count = 0
    dot_index = -1
    suffix = ""

    for i, char in enumerate(file_name):
        if char.isdigit():
            digit_count += 1
        if char == '.':
            if dot_index != -1:
                return 'No'
            dot_index = i
    
    if digit_count > 3:
        return 'No'
    
    if dot_index == -1:
        return 'No'

    prefix = file_name[:dot_index]
    suffix = file_name[dot_index + 1:]
    
    if not prefix:
        return 'No'

    if not (prefix[0].isalpha() and len(prefix) > 0):
        return 'No'

    if suffix not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'



@pytest.mark.parametrize(
    "file_name, expected",
    [
        ("example.txt", "Yes"),
        ("1example.dll", "No"),
        ("a.txt", "Yes"),
        ("A.exe", "Yes"),
        ("a1.txt", "No"),
        ("example1.txt", "No"),
        ("example.exe", "Yes"),
        ("example.DLL", "Yes"),
        ("example.dLL", "No"),
        ("example.123", "No"),
        ("example..txt", "No"),
        ("example.txt.", "No"),
        ("", "No"),
        ("123.txt", "No"),
        ("a.txt", "Yes"),
        ("A.exe", "Yes"),
        ("a.123", "No"),
        ("a1.txt", "No"),
        ("example.xyz", "No"),
        ("example.XYZ", "No"),
        ("example.a", "No"),
        ("example.A", "No"),
        ("example.1", "No"),
        ("example. ", "No"),
        ("a. ", "No"),
        ("a.1", "No"),
        ("1a.txt", "No"),
        ("1.txt", "No"),
    ],
)
def test_file_name_check(file_name, expected):
    assert file_name_check(file_name) == expected

@pytest.mark.parametrize(
    "file_name, expected",
    [
        ("abc.txt", "Yes"),
        ("a1b.txt", "No"),
        ("a.txt", "Yes"),
        ("A.exe", "Yes"),
        ("1.txt", "No"),
        ("a.1txt", "No"),
        ("a1.txt", "No"),
    ],
)
def test_prefix_validity(file_name, expected):
    assert file_name_check(file_name) == expected

@pytest.mark.parametrize(
    "file_name, expected",
    [
        ("example.xyz", "No"),
        ("example.ABC", "No"),
        ("example.123", "No"),
        ("example.a", "No"),
        ("example.A", "No"),
        ("example.1", "No"),
    ],
)
def test_suffix_validity(file_name, expected):
    assert file_name_check(file_name) == expected

@pytest.mark.parametrize(
    "file_name, expected",
    [
        ("a.txt", "Yes"),
        ("A.exe", "Yes"),
        ("a.txt", "Yes"),
        ("a1.txt", "No"),
    ],
)
def test_digit_count(file_name, expected):
    assert file_name_check(file_name) == expected

@pytest.mark.parametrize(
    "file_name, expected",
    [
        ("a.txt", "Yes"),
        ("A.exe", "Yes"),
        ("a.txt.", "No"),
        ("a.txt.", "No"),
    ],
)
def test_dot_count(file_name, expected):
    assert file_name_check(file_name) == expected