
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
# 3. The part before the dot starts with a letter.
# 4. The part after the dot is one of the allowed extensions.
# We need to test all combinations of these conditions to ensure the function behaves correctly.
# Edge cases include empty strings, strings with multiple dots, strings starting with digits,
# and invalid extensions.

# STEP 2: PLAN
# Test functions:
# - test_valid_name: Tests a valid file name.
# - test_too_many_digits: Tests a file name with more than three digits.
# - test_no_dot: Tests a file name without a dot.
# - test_multiple_dots: Tests a file name with multiple dots.
# - test_invalid_prefix: Tests a file name with an invalid prefix (not starting with a letter).
# - test_invalid_suffix: Tests a file name with an invalid suffix.
# - test_empty_prefix: Tests a file name with an empty prefix.
# - test_empty_suffix: Tests a file name with an empty suffix.
# - test_invalid_input: Tests with invalid input type (non-string).

# STEP 3: CODE
# pytest suite
###
def test_valid_name():
    assert file_name_check("example.txt") == 'Yes'
    assert file_name_check("my_file.dll") == 'Yes'
    assert file_name_check("A1b2c.exe") == 'Yes'

def test_too_many_digits():
    assert file_name_check("123example.txt") == 'No'
    assert file_name_check("1234example.txt") == 'No'

def test_no_dot():
    assert file_name_check("examplefile") == 'No'

def test_multiple_dots():
    assert file_name_check("example..txt") == 'No'

def test_invalid_prefix():
    assert file_name_check("1example.txt") == 'No'
    assert file_name_check("example.1txt") == 'No'
    assert file_name_check("example. 1txt") == 'No'

def test_invalid_suffix():
    assert file_name_check("example.pdf") == 'No'
    assert file_name_check("example.jpg") == 'No'

def test_empty_prefix():
    assert file_name_check(".txt") == 'No'

def test_empty_suffix():
    assert file_name_check("example.") == 'No'

def test_invalid_input():
    assert file_name_check(123) == 'No'
    assert file_name_check(None) == 'No'
    assert file_name_check(1.23) == 'No'