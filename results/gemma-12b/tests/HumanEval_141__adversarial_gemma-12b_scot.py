
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
    if file_name is None or not isinstance(file_name, str):
        return 'No'

    if file_name.count('.') != 1:
        return 'No'

    parts = file_name.split('.')
    if len(parts[0]) == 0:
        return 'No'

    if not parts[0][0].isalpha():
        return 'No'

    if len(parts[0]) > 3 and any(char.isdigit() for char in parts[0]):
        return 'No'

    if len(parts[0]) > 3:
        digit_count = sum(1 for char in parts[0] if char.isdigit())
        if digit_count > 3:
            return 'No'

    if parts[1] not in ['txt', 'exe', 'dll']:
        return 'No'

    digit_count = sum(1 for char in file_name if char.isdigit())
    if digit_count > 3:
        return 'No'

    return 'Yes'


class TestFileNameCheck:
    def test_valid_file_name(self):
        assert file_name_check("example.txt") == 'Yes'

    def test_invalid_too_many_digits(self):
        assert file_name_check("1234example.txt") == 'No'

    def test_invalid_no_dot(self):
        assert file_name_check("exampletxt") == 'No'

    def test_invalid_multiple_dots(self):
        assert file_name_check("example.txt.dll") == 'No'

    def test_invalid_empty_before_dot(self):
        assert file_name_check(".txt") == 'No'

    def test_invalid_non_letter_start(self):
        assert file_name_check("1example.txt") == 'No'

    def test_invalid_wrong_extension(self):
        assert file_name_check("example.pdf") == 'No'

    def test_valid_file_name_uppercase(self):
        assert file_name_check("example.EXE") == 'No'

    def test_valid_file_name_mixed_case(self):
        assert file_name_check("ExAmPlE.txt") == 'Yes'

    def test_empty_file_name(self):
        assert file_name_check("") == 'No'

    def test_file_name_with_special_characters(self):
        assert file_name_check("example!.txt") == 'No'

    def test_file_name_with_leading_and_trailing_spaces(self):
        assert file_name_check(" example.txt ") == 'No'

    def test_valid_file_name_with_digits(self):
        assert file_name_check("ex123ample.txt") == 'Yes'

    def test_invalid_file_name_with_four_digits(self):
        assert file_name_check("ex1234ample.txt") == 'No'