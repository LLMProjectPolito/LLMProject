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
    digit_count = 0
    for char in file_name:
        if char.isdigit():
            digit_count += 1

    if digit_count > 3:
        return 'No'

    if file_name.count('.') != 1:
        return 'No'

    parts = file_name.split('.')
    if len(parts) != 2:
        return 'No'

    before_dot = parts[0]
    after_dot = parts[1]

    if not before_dot:
        return 'No'

    if not before_dot[0].isalpha():
        return 'No'

    if after_dot not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'

# STEP 2: PLAN - List test functions names and scenarios.
# Test functions:
# - test_valid_file_name: Tests valid file names.
# - test_invalid_digit_count: Tests file names with more than three digits.
# - test_invalid_dot_count: Tests file names with incorrect number of dots.
# - test_invalid_before_dot_empty: Tests file names where the part before the dot is empty.
# - test_invalid_before_dot_not_alpha: Tests file names where the part before the dot does not start with a letter.
# - test_invalid_after_dot: Tests file names where the part after the dot is not in the allowed list.
# - test_edge_cases: Tests edge cases like empty string, only dot, etc.

# STEP 3: CODE - Write the high-quality pytest suite.
class TestFileNameCheck:
    def test_valid_file_name(self):
        assert file_name_check("example.txt") == 'Yes'
        assert file_name_check("MyFile.exe") == 'Yes'
        assert file_name_check("document1.dll") == 'Yes'
        assert file_name_check("A.txt") == 'Yes'
        assert file_name_check("file123.txt") == 'Yes'

    def test_invalid_digit_count(self):
        assert file_name_check("1234example.txt") == 'No'
        assert file_name_check("example1234.txt") == 'No'
        assert file_name_check("1234.exe") == 'No'

    def test_invalid_dot_count(self):
        assert file_name_check("example.txt.txt") == 'No'
        assert file_name_check("example") == 'No'
        assert file_name_check(".txt") == 'No'

    def test_invalid_before_dot_empty(self):
        assert file_name_check(".txt") == 'No'

    def test_invalid_before_dot_not_alpha(self):
        assert file_name_check("1example.dll") == 'No'
        assert file_name_check("!example.txt") == 'No'

    def test_invalid_after_dot(self):
        assert file_name_check("example.pdf") == 'No'
        assert file_name_check("example.jpg") == 'No'
        assert file_name_check("example.something") == 'No'

    def test_edge_cases(self):
        assert file_name_check("") == 'No'
        assert file_name_check("abc.123") == 'No'
        assert file_name_check("a.txt1") == 'No'
        assert file_name_check("a1.txt") == 'Yes'
        assert file_name_check("a123.txt") == 'Yes'