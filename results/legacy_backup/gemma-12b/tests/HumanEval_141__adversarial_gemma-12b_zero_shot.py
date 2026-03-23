import pytest
import re

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

    parts = file_name.split('.')
    if len(parts[0]) == 0:
        return 'No'

    if not re.match(r'^[a-zA-Z]', parts[0]):
        return 'No'

    if parts[0].isdigit():
        return 'No'

    if len(re.findall(r'\d', file_name)) > 3:
        return 'No'

    if parts[1] not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'


class TestFileNameCheck:
    def test_valid_file_name(self):
        assert file_name_check("example.txt") == "Yes"
        assert file_name_check("document.dll") == "Yes"
        assert file_name_check("my_program.exe") == "Yes"
        assert file_name_check("a.txt") == "Yes"
        assert file_name_check("A.TXT") == "Yes"
        assert file_name_check("long_file_name.exe") == "Yes"
        assert file_name_check("file123.txt") == "Yes"
        assert file_name_check("file1234.txt") == "No"

    def test_invalid_file_name_no_dot(self):
        assert file_name_check("example") == "No"
        assert file_name_check("example.txt.pdf") == "No"

    def test_invalid_file_name_empty_before_dot(self):
        assert file_name_check(".txt") == "No"

    def test_invalid_file_name_not_letter_before_dot(self):
        assert file_name_check("1example.txt") == "No"
        assert file_name_check("!example.txt") == "No"
        assert file_name_check(" example.txt") == "No"

    def test_invalid_file_name_invalid_extension(self):
        assert file_name_check("example.pdf") == "No"
        assert file_name_check("example.jpg") == "No"
        assert file_name_check("example.") == "No"

    def test_invalid_file_name_too_many_digits(self):
        assert file_name_check("1234example.txt") == "No"
        assert file_name_check("11111.txt") == "No"

    def test_invalid_file_name_all_digits(self):
        assert file_name_check("123.txt") == "No"
        assert file_name_check("1234.txt") == "No"