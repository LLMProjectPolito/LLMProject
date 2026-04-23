
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
    digits = 0
    dot_count = 0
    for char in file_name:
        if char.isdigit():
            digits += 1
        if char == '.':
            dot_count += 1

    if digits > 3 or dot_count != 1:
        return 'No'

    parts = file_name.split('.')
    if len(parts) != 2:
        return 'No'

    prefix = parts[0]
    suffix = parts[1]

    if not prefix or not prefix[0].isalpha():
        return 'No'

    if suffix not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'

class TestFileNameCheck:

    def test_valid_file_name_1(self):
        assert file_name_check("example.txt") == "Yes"

    def test_valid_file_name_2(self):
        assert file_name_check("my_file.exe") == "Yes"

    def test_valid_file_name_3(self):
        assert file_name_check("data.dll") == "Yes"

    def test_invalid_file_name_1(self):
        assert file_name_check("1example.dll") == "No"

    def test_invalid_file_name_2(self):
        assert file_name_check("example123.txt") == "No"

    def test_invalid_file_name_3(self):
        assert file_name_check("example.xyz") == "No"

    def test_invalid_file_name_4(self):
        assert file_name_check("example..txt") == "No"

    def test_invalid_file_name_5(self):
        assert file_name_check("example.txt.") == "No"

    def test_invalid_file_name_6(self):
        assert file_name_check("example.txt1") == "No"

    def test_empty_string(self):
        assert file_name_check("") == "No"

    def test_only_dot(self):
        assert file_name_check(".") == "No"

    def test_no_dot(self):
        assert file_name_check("example") == "No"

    def test_multiple_dots(self):
        assert file_name_check("example..txt") == "No"

    def test_leading_digit(self):
        assert file_name_check("123example.txt") == "No"

    def test_trailing_digit(self):
        assert file_name_check("example.123") == "No"

    def test_special_characters(self):
        assert file_name_check("example!@#txt") == "No"

    def test_mixed_case_prefix(self):
        assert file_name_check("ExAmple.txt") == "No"

    def test_prefix_with_spaces(self):
        assert file_name_check(" example.txt") == "No"

    def test_suffix_not_in_allowed_list(self):
        assert file_name_check("example.log") == "No"