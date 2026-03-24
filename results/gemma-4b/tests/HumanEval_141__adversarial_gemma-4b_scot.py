
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

### SCoT Steps:

# STEP 1: REASONING
# The function `file_name_check` validates a file name based on several criteria:
# 1. Maximum three digits.
# 2. Exactly one dot.
# 3. Prefix (before the dot) starts with a letter.
# 4. Suffix (after the dot) is one of 'txt', 'exe', or 'dll'.
# We need to test all combinations of these conditions to ensure the function behaves correctly.
# Edge cases include empty strings, names with more than three digits, multiple dots, invalid prefixes, and invalid suffixes.

# STEP 2: PLAN
# Test Cases:
# 1. Valid file name: "example.txt"
# 2. Valid file name: "test.exe"
# 3. Invalid file name (more than three digits): "123example.txt"
# 4. Invalid file name (multiple dots): "example..txt"
# 5. Invalid file name (prefix not starting with a letter): "1example.txt"
# 6. Invalid file name (suffix not in the allowed list): "example.pdf"
# 7. Empty string: ""
# 8. File name with only digits: "12345.txt"
# 9. File name with a dot at the beginning: ".txt"
# 10. File name with a dot at the end: "example.txt."

# Test Functions:
# test_valid_names()
# test_invalid_names()
# test_edge_cases()

# STEP 3: CODE
###
def test_valid_names():
    assert file_name_check("example.txt") == 'Yes'
    assert file_name_check("test.exe") == 'Yes'
    assert file_name_check("data.dll") == 'Yes'
    assert file_name_check("a.txt") == 'Yes'
    assert file_name_check("A.dll") == 'Yes'

def test_invalid_names():
    assert file_name_check("123example.txt") == 'No'
    assert file_name_check("example..txt") == 'No'
    assert file_name_check("1example.txt") == 'No'
    assert file_name_check("example.pdf") == 'No'
    assert file_name_check("12345.txt") == 'No'
    assert file_name_check(".txt") == 'No'
    assert file_name_check("example.txt.") == 'No'

def test_edge_cases():
    assert file_name_check("") == 'No'
    assert file_name_check("123") == 'No'
    assert file_name_check("a123.txt") == 'No'
    assert file_name_check("a.b.c") == 'No'
    assert file_name_check("a.txt.b") == 'No'