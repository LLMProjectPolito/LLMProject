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

# STEP 1: REASONING - Analyze functional goals and constraints.
# The function `file_name_check` validates a file name based on several criteria:
# 1. Maximum three digits.
# 2. Exactly one dot.
# 3. Prefix (before the dot) starts with a letter.
# 4. Suffix (after the dot) is one of 'txt', 'exe', or 'dll'.
# Edge cases include empty strings, strings with multiple dots, strings starting with digits,
# and suffixes that are not in the allowed list.

# STEP 2: PLAN - List test functions names and scenarios.
# Test cases:
# 1. Valid file name: "example.txt"
# 2. File name with more than three digits: "123example.txt"
# 3. File name with multiple dots: "example..txt"
# 4. File name starting with a digit: "1example.txt"
# 5. File name with invalid suffix: "example.pdf"
# 6. Empty string: ""
# 7. File name with only one character: "a."
# 8. File name with a number before the dot: "1.txt"
# 9. File name with a number after the dot: "example.1"
# 10. File name with special characters: "example.!"
# 11. Valid file name with digits: "abc123def.txt"
# 12. Valid file name with uppercase: "Abc123Def.TXT"
# 13. File name with only one letter: "a.txt"
# 14. File name with one digit: "a1.txt"
# 15. File name with two digits: "a23.txt"
# 16. File name with three digits: "a456.txt"
# 17. Non-string input: 123
# 18. Invalid prefix: "1example.txt"
# 19. Invalid suffix: "example.pdf"
# 20. Mixed case prefix and suffix: "Abc123Def.TXT"

# STEP 3: CODE - Write the high-quality pytest suite.
###
import pytest

def test_valid_file_name():
    assert file_name_check("example.txt") == 'Yes'

def test_more_than_three_digits():
    assert file_name_check("123example.txt") == 'No'

def test_multiple_dots():
    assert file_name_check("example..txt") == 'No'

def test_starts_with_digit():
    assert file_name_check("1example.txt") == 'No'

def test_invalid_suffix():
    assert file_name_check("example.pdf") == 'No'

def test_empty_string():
    assert file_name_check("") == 'No'

def test_single_character_file():
    assert file_name_check("a.") == 'No'

def test_number_before_dot():
    assert file_name_check("1.txt") == 'No'

def test_number_after_dot():
    assert file_name_check("example.1") == 'No'

def test_special_characters():
    assert file_name_check("example.!") == 'No'

def test_valid_file_name_with_digits():
    assert file_name_check("abc123def.txt") == 'Yes'

def test_valid_file_name_with_uppercase():
    assert file_name_check("Abc123Def.TXT") == 'Yes'

def test_file_name_with_only_one_letter():
    assert file_name_check("a.txt") == 'Yes'

def test_file_name_with_one_digit():
    assert file_name_check("a1.txt") == 'Yes'

def test_file_name_with_two_digits():
    assert file_name_check("a23.txt") == 'Yes'

def test_file_name_with_three_digits():
    assert file_name_check("a456.txt") == 'No'

def test_non_string_input():
    assert file_name_check(123) == 'No'

def test_invalid_prefix():
    assert file_name_check("1example.txt") == 'No'

def test_invalid_suffix():
    assert file_name_check("example.pdf") == 'No'

def test_mixed_case_prefix_and_suffix():
    assert file_name_check("Abc123Def.TXT") == 'Yes'

def test_valid_three_digit_suffix():
    assert file_name_check("abc3def.txt") == 'Yes'