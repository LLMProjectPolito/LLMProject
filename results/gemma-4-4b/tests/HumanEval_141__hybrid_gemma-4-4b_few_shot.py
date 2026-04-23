
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
    digit_count = 0
    dot_count = 0
    parts = file_name.split('.')

    if len(parts) != 2:
        return 'No'

    name_before_dot = parts[0]
    extension = parts[1]

    for char in name_before_dot:
        if '0' <= char <= '9':
            digit_count += 1

    if digit_count > 3:
        return 'No'

    if dot_count != 1:
        return 'No'

    if not name_before_dot:
        return 'No'
    
    if not ('a' <= name_before_dot[0] <= 'z' or 'A' <= name_before_dot[0] <= 'Z'):
        return 'No'

    if extension not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'

class TestFileNameCheck:

    def test_valid_file_name(self):
        assert file_name_check("example.txt") == "Yes"
        assert file_name_check("document.exe") == "Yes"
        assert file_name_check("program.dll") == "Yes"
        assert file_name_check("MyFile.TXT") == "Yes"
        assert file_name_check("a123.txt") == "Yes"

    def test_invalid_digit_count(self):
        assert file_name_check("1234.txt") == "No"
        assert file_name_check("abc1234.exe") == "No"
        assert file_name_check("12345.dll") == "No"

    def test_invalid_dot_count(self):
        assert file_name_check("example") == "No"
        assert file_name_check("example.txt.bak") == "No"

    def test_empty_name(self):
        assert file_name_check("") == "No"

    def test_empty_name_before_dot(self):
        assert file_name_check(".txt") == "No"
        assert file_name_check("..txt") == "No"

    def test_invalid_first_char(self):
        assert file_name_check("1example.txt") == "No"
        assert file_name_check("!example.dll") == "No"
        assert file_name_check("a123.exe") == "Yes"

    def test_invalid_extension(self):
        assert file_name_check("example.pdf") == "No"
        assert file_name_check("example.csv") == "No"
        assert file_name_check("example.jpg") == "No"

    def test_special_characters(self):
        assert file_name_check("example_file.txt") == "No"
        assert file_name_check("example-file.exe") == "No"

    def test_mixed_case(self):
        assert file_name_check("Example.TXT") == "Yes"
        assert file_name_check("eXample.DLL") == "Yes"

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    processed_string = ''.join(filter(str.isalnum, s)).lower()
    return processed_string == processed_string[::-1]

def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_palindrome_empty():
    assert is_palindrome('') == True
def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)

def test_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_max_empty():
    assert get_max([]) == None