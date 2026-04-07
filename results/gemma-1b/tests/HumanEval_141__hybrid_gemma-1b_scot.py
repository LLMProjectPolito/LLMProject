
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
from typing import List

def file_name_check(file_name: str) -> str:
    """
    Check if a file name is valid according to the specified rules.

    Args:
        file_name: The file name to check.

    Returns:
        'Yes' if the file name is valid, 'No' otherwise.
    """
    parts = file_name.split(".")
    if len(parts) > 3:
        return "No"
    if len(parts) == 1:
        if not parts[0]:
            return "No"
        if not parts[0][0].isalpha():
            return "No"
    if len(parts) == 2:
        if not parts[1]:
            return "No"
        if not parts[1][0].isalpha():
            return "No"
    if len(parts) == 3:
        if not parts[0].isalnum():
            return "No"
        if not parts[2].isalnum():
            return "No"
    return "Yes"


def test_file_name_check_valid():
    assert file_name_check("example.txt") == "Yes"

def test_file_name_check_invalid_too_many_digits():
    assert file_name_check("1example.dll") == "No"

def test_file_name_check_invalid_dot_only():
    assert file_name_check("example.txt.") == "No"

def test_file_name_check_invalid_name_length():
    assert file_name_check("example.txt.") == "No"

def test_file_name_check_invalid_name_letters():
    assert file_name_check("example.txt") == "No"

def test_file_name_check_invalid_name_letters_and_dot():
    assert file_name_check("example.txt.") == "No"

def test_file_name_check_invalid_name_letters_and_dot_and_alphanumeric():
    assert file_name_check("example.txt.") == "No"

def test_file_name_check_invalid_name_alphanumeric_and_dot():
    assert file_name_check("example.txt.") == "No"

def test_file_name_check_invalid_name_alphanumeric_and_dot_and_letter():
    assert file_name_check("example.txt.") == "No"

def test_file_name_check_invalid_name_alphanumeric_and_dot_and_letter_and_number():
    assert file_name_check("example.txt.") == "No"

def test_file_name_check_invalid_name_alphanumeric_and_letter_and_number():
    assert file_name_check("example.txt.") == "No"

def test_file_name_check_invalid_name_alphanumeric_and_letter_and_number_and_dot():
    assert file_name_check("example.txt.") == "No"

def test_file_name_check_invalid_name_alphanumeric_and_letter_and_number_and_dot_and_letter():
    assert file_name_check("example.txt.") == "No"

def test_file_name_check_invalid_name_alphanumeric_and_letter_and_number_and_dot_and_letter():
    assert file_name_check("example.txt.") == "No"

def test_file_name_check_invalid_name_alphanumeric_and_letter_and_number_and_dot_and_letter_and_letter():
    assert file_name_check("example.txt.") == "No"