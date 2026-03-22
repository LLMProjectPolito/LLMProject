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
    if file_name.count('.') != 1:
        return 'No'

    prefix, suffix = file_name.split('.')

    if not prefix:
        return 'No'

    if not prefix[0].isalpha():
        return 'No'

    if suffix not in ['txt', 'exe', 'dll']:
        return 'No'

    digit_count = sum(c.isdigit() for c in file_name)
    if digit_count > 3:
        return 'No'

    return 'Yes'


class TestFileNameCheck:
    def test_valid_file_name(self):
        assert file_name_check("example.txt") == 'Yes'

    def test_invalid_digit_count(self):
        assert file_name_check("1234example.txt") == 'No'

    def test_no_dot(self):
        assert file_name_check("example") == 'No'

    def test_multiple_dots(self):
        assert file_name_check("example.sub.txt") == 'No'

    def test_empty_prefix(self):
        assert file_name_check(".txt") == 'No'

    def test_prefix_not_letter(self):
        assert file_name_check("1example.txt") == 'No'

    def test_invalid_suffix(self):
        assert file_name_check("example.pdf") == 'No'

    def test_empty_string(self):
        assert file_name_check("") == 'No'

    def test_suffix_case_sensitive(self):
        assert file_name_check("example.TXT") == 'No'

    def test_digit_prefix(self):
        assert file_name_check("12345.txt") == 'No'

    def test_digit_prefix_valid_suffix(self):
        assert file_name_check("123.txt") == 'Yes'

    def test_valid_file_name_all_digits(self):
        assert file_name_check("123.txt") == 'Yes'