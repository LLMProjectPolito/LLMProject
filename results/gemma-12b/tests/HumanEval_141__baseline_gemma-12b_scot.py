
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
    digit_count = sum(c.isdigit() for c in file_name)
    if digit_count > 3:
        return 'No'

    if file_name.count('.') != 1:
        return 'No'

    parts = file_name.split('.')
    if len(parts[0]) == 0:
        return 'No'

    if not parts[0][0].isalpha():
        return 'No'

    if parts[1] not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'

class TestFileNameCheck:

    def test_valid_file_name(self):
        assert file_name_check("example.txt") == "Yes"
        assert file_name_check("document.dll") == "Yes"
        assert file_name_check("program.exe") == "Yes"
        assert file_name_check("a.txt") == "Yes"
        assert file_name_check("A.TXT") == "Yes"
        assert file_name_check("long_file_name.exe") == "Yes"

    def test_invalid_too_many_digits(self):
        assert file_name_check("1234example.txt") == "No"
        assert file_name_check("12345.txt") == "No"

    def test_invalid_no_dot(self):
        assert file_name_check("example") == "No"
        assert file_name_check("exampletxt") == "No"

    def test_invalid_multiple_dots(self):
        assert file_name_check("example.txt.dll") == "No"
        assert file_name_check("example..txt") == "No"

    def test_invalid_empty_before_dot(self):
        assert file_name_check(".txt") == "No"
        assert file_name_check(".exe") == "No"
        assert file_name_check(".dll") == "No"

    def test_invalid_not_letter_before_dot(self):
        assert file_name_check("1example.txt") == "No"
        assert file_name_check("_example.txt") == "No"
        assert file_name_check(" example.txt") == "No"

    def test_invalid_extension(self):
        assert file_name_check("example.pdf") == "No"
        assert file_name_check("example.jpg") == "No"
        assert file_name_check("example.xyz") == "No"

    def test_edge_cases(self):
        assert file_name_check("000.txt") == "Yes"
        assert file_name_check("a000.txt") == "No"
        assert file_name_check("a123.txt") == "No"
        assert file_name_check("a.TXT") == "Yes"