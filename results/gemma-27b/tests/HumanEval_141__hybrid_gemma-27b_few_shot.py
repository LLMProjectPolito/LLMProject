
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
    if file_name.count('.') != 1:
        return 'No'

    parts = file_name.split('.')
    if not parts[0]:
        return 'No'

    if not parts[0][0].isalpha():
        return 'No'

    digit_count = sum(c.isdigit() for c in file_name)
    if digit_count > 3:
        return 'No'

    extension = parts[1]
    if extension not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'

# Pytest Suite - Combined and Superior
def test_valid_filenames():
    assert file_name_check("example.txt") == 'Yes'
    assert file_name_check("MyFile.exe") == 'Yes'
    assert file_name_check("document1.dll") == 'Yes'
    assert file_name_check("A.txt") == 'Yes'
    assert file_name_check("file123.txt") == 'Yes'
    assert file_name_check("FILE1.exe") == 'Yes'
    assert file_name_check("FileWithNumbers12.exe") == 'Yes'
    assert file_name_check("file1.txt") == 'Yes'
    assert file_name_check("file12.exe") == 'Yes'
    assert file_name_check("file123.dll") == 'Yes'
    assert file_name_check("a.txt") == 'Yes'
    assert file_name_check("A.exe") == 'Yes'
    assert file_name_check("file.dll") == 'Yes'

def test_invalid_filenames_dot_count():
    assert file_name_check("exampletxt") == 'No'
    assert file_name_check("example.txt.txt") == 'No'
    assert file_name_check(".txt") == 'No'
    assert file_name_check("..txt") == 'No'
    assert file_name_check("example.") == 'No'

def test_invalid_filenames_starting_char():
    assert file_name_check("1example.txt") == 'No'
    assert file_name_check("2file.exe") == 'No'
    assert file_name_check("!file.dll") == 'No'
    assert file_name_check(" file.txt") == 'No'
    assert file_name_check("9document.dll") == 'No'

def test_invalid_filenames_digit_count():
    assert file_name_check("file1234.txt") == 'No'
    assert file_name_check("file12345.exe") == 'No'
    assert file_name_check("1234file.dll") == 'No'
    assert file_name_check("name12345.exe") == 'No'
    assert file_name_check("doc123456.dll") == 'No'

def test_invalid_filenames_extension():
    assert file_name_check("example.pdf") == 'No'
    assert file_name_check("myfile.jpg") == 'No'
    assert file_name_check("document.zip") == 'No'
    assert file_name_check("file.something") == 'No'

def test_empty_filename():
    assert file_name_check("") == 'No'

def test_filename_with_only_dot():
    assert file_name_check(".") == 'No'

def test_filename_with_space_before_dot():
    assert file_name_check(" file.txt") == 'No'

def test_filename_with_space_after_dot():
    assert file_name_check("file. txt") == 'No'

def test_filename_with_special_characters():
    assert file_name_check("file@.txt") == 'No'
    assert file_name_check("file#.exe") == 'No'
    assert file_name_check("file$.dll") == 'No'

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    return s == s[::-1]

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