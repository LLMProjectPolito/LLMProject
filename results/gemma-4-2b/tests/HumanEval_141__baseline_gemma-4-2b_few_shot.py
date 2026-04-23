
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

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    return s == s[::-1]

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)

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
        return "No"

    if file_name.count('.') != 1:
        return "No"

    parts = file_name.split('.')
    if not parts[0]:
        return "No"

    first_part = parts[0]
    if not first_part[0].isalpha():
        return "No"

    second_part = parts[1]
    if second_part not in ['txt', 'exe', 'dll']:
        return "No"

    if file_name.count('0') + file_name.count('1') + file_name.count('2') + file_name.count('3') + file_name.count('4') + file_name.count('5') + file_name.count('6') + file_name.count('7') + file_name.count('8') + file_name.count('9') > 3:
        return "No"

    return "Yes"

import pytest

def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_file_name_check_valid():
    assert file_name_check("example.txt") == "Yes"
    assert file_name_check("file.exe") == "Yes"
    assert file_name_check("document.dll") == "Yes"

def test_file_name_check_invalid_digits():
    assert file_name_check("123example.txt") == "No"
    assert file_name_check("12345.txt") == "No"

def test_file_name_check_no_dot():
    assert file_name_check("example") == "No"

def test_file_name_check_no_dot_multiple():
    assert file_name_check("example.") == "No"
    assert file_name_check("example..txt") == "No"

def test_file_name_check_empty_first_part():
    assert file_name_check(".txt") == "No"
    assert file_name_check("   .txt") == "No"

def test_file_name_check_invalid_first_char():
    assert file_name_check("1example.txt") == "No"
    assert file_name_check("example1.txt") == "No"

def test_file_name_check_invalid_second_part():
    assert file_name_check("example.java") == "No"
    assert file_name_check("example.pdf") == "No"

def test_file_name_check_invalid_length_digits():
    assert file_name_check("1234567890.txt") == "No"
    assert file_name_check("123.txt") == "No"

def test_file_name_check_not_string():
    assert file_name_check(123) == "No"
    assert file_name_check(None) == "No"