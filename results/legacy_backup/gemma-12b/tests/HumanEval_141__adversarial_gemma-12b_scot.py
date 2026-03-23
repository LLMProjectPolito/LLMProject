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

    if file_name.count('.') != 1:
        return 'No'

    parts = file_name.split('.')
    if len(parts[0]) == 0:
        return 'No'

    if not parts[0][0].isalpha():
        return 'No'

    if len(parts) != 2:
        return 'No'

    if parts[1] not in ['txt', 'exe', 'dll']:
        return 'No'

    if sum(c.isdigit() for c in file_name) > 3:
        return 'No'

    return 'Yes'


class TestFileNameCheck:
    def test_valid_file_name(self):
        assert file_name_check("example.txt") == 'Yes'

    def test_valid_file_name_exe(self):
        assert file_name_check("myprogram.exe") == 'Yes'

    def test_valid_file_name_dll(self):
        assert file_name_check("library.dll") == 'Yes'

    def test_too_many_digits(self):
        assert file_name_check("1234example.txt") == 'No'

    def test_no_dot(self):
        assert file_name_check("example") == 'No'

    def test_multiple_dots(self):
        assert file_name_check("example.part1.txt") == 'No'

    def test_empty_before_dot(self):
        assert file_name_check(".txt") == 'No'

    def test_non_letter_start(self):
        assert file_name_check("1example.txt") == 'No'

    def test_invalid_extension(self):
        assert file_name_check("example.pdf") == 'No'

    def test_empty_file_name(self):
        assert file_name_check("") == 'No'

    def test_digit_start(self):
        assert file_name_check("123.txt") == 'No'

    def test_exactly_three_digits(self):
        assert file_name_check("123abc.txt") == 'Yes'

    def test_special_characters(self):
        assert file_name_check("example!.txt") == 'No'