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

    if not prefix or not prefix[0].isalpha():
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
# Edge cases include empty strings, names with more than three digits, multiple dots,
# prefixes that are empty or don't start with a letter, and suffixes that are not allowed.

# STEP 2: PLAN
# Test functions:
# - test_valid_name: Tests a valid file name.
# - test_too_many_digits: Tests a file name with more than three digits.
# - test_multiple_dots: Tests a file name with more than one dot.
# - test_empty_prefix: Tests a file name with an empty prefix.
# - test_non_letter_prefix: Tests a file name with a prefix that doesn't start with a letter.
# - test_invalid_suffix: Tests a file name with an invalid suffix.
# - test_empty_string: Tests an empty string.
# - test_dot_at_start: Tests a file name with a dot at the beginning.
# - test_dot_at_end: Tests a file name with a dot at the end.
# - test_complex_name: Tests a complex file name with multiple digits and a valid suffix.

# STEP 3: CODE
# pytest suite
###
def test_valid_name():
    assert file_name_check("example.txt") == 'Yes'

def test_too_many_digits():
    assert file_name_check("1example.txt") == 'No'
    assert file_name_check("12example.txt") == 'No'
    assert file_name_check("123example.txt") == 'No'
    assert file_name_check("1234example.txt") == 'No'

def test_multiple_dots():
    assert file_name_check("example..txt") == 'No'
    assert file_name_check("example.txt.txt") == 'No'

def test_empty_prefix():
    assert file_name_check(".txt") == 'No'
    assert file_name_check("1.txt") == 'No'

def test_non_letter_prefix():
    assert file_name_check("1example.txt") == 'No'
    assert file_name_check("1example.dll") == 'No'

def test_invalid_suffix():
    assert file_name_check("example.doc") == 'No'
    assert file_name_check("example.pdf") == 'No'

def test_empty_string():
    assert file_name_check("") == 'No'

def test_dot_at_start():
    assert file_name_check(".txt") == 'No'

def test_dot_at_end():
    assert file_name_check("example.") == 'No'

def test_complex_name():
    assert file_name_check("abc123def.txt") == 'Yes'
    assert file_name_check("abc123def.exe") == 'Yes'
    assert file_name_check("abc123def.dll") == 'Yes'