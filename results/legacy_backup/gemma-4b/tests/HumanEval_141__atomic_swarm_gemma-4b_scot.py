import pytest
import math

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
    if not file_name:
        return 'No'

    digit_count = 0
    for char in file_name:
        if char.isdigit():
            digit_count += 1

    if digit_count > 3:
        return 'No'

    if file_name.count('.') != 1:
        return 'No'

    dot_index = file_name.find('.')
    prefix = file_name[:dot_index]
    suffix = file_name[dot_index + 1:]

    if not prefix or not 'a' <= prefix[0] <= 'z' or not 'A' <= prefix[0] <= 'Z':
        return 'No'

    if suffix not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'

def test_basic():
    assert file_name_check("example.txt") == 'Yes'

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
    if not file_name:
        return 'No'

    digit_count = 0
    for char in file_name:
        if char.isdigit():
            digit_count += 1

    if digit_count > 3:
        return 'No'

    if file_name.count('.') != 1:
        return 'No'

    parts = file_name.split('.')
    if not parts[0] or not parts[0][0].isalpha():
        return 'No'

    if parts[1] not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'

### SCoT Steps:
### STEP 1: REASONING - Analyze functional goals and constraints.
### The function `file_name_check` needs to be tested with various edge cases to ensure it correctly validates file names according to the specified rules.
### Specifically, we need to test cases with invalid digits, multiple dots, invalid prefixes, and invalid suffixes.
### STEP 2: PLAN - List test functions names and scenarios.
### test_empty_file_name
### test_too_many_digits
### test_multiple_dots
### test_invalid_prefix
### test_invalid_suffix
### STEP 3: CODE - Write the high-quality pytest suite.
###

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

    digit_count = 0
    for char in file_name:
        if char.isdigit():
            digit_count += 1

    if digit_count > 3:
        return 'No'

    if file_name.count('.') != 1:
        return 'No'

    dot_index = file_name.find('.')
    prefix = file_name[:dot_index]
    suffix = file_name[dot_index + 1:]

    if not prefix or not 'a' <= prefix[0] <= 'z' or not 'A' <= prefix[0] <= 'Z':
        return 'No'

    if suffix not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'

### SCoT Steps:
# STEP 1: REASONING - The function needs to be tested for invalid input types, invalid characters in the filename, and incorrect number of digits.
# STEP 2: PLAN - Test cases: 1) Invalid input type (int). 2) Filename with more than three digits. 3) Filename with more than one dot. 4) Filename with an invalid prefix. 5) Filename with an invalid suffix.
# STEP 3: CODE -
###
@pytest.mark.parametrize(
    "file_name, expected",
    [
        (123, 'No'),
        ("example.txt.txt", 'No'),
        ("1example.dll", 'No'),
        ("example.pdf", 'No'),
        ("example..txt", 'No'),
        ("example.exe", 'No'),
        ("Example.TXT", 'Yes'),
        ("a.txt", 'Yes'),
        ("1a.txt", 'No'),
        ("a1.txt", 'No'),
        ("a12.txt", 'No'),
    ],
)
def test_file_name_check(file_name, expected):
    assert file_name_check(file_name) == expected