
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

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    processed_string = ''.join(filter(str.isalnum, s)).lower()
    return processed_string == processed_string[::-1]

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
    digit_count = sum(c.isdigit() for c in file_name)
    dot_count = file_name.count('.')

    if digit_count > 3 or dot_count != 1:
        return 'No'

    parts = file_name.split('.')
    if not parts[0]:
        return 'No'

    if not parts[0][0].isalpha():
        return 'No'

    extension = parts[1]
    if extension not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'



@pytest.mark.parametrize("input_string, expected", [
    ("radar", True),
    ("hello", False),
    ("", True),
    ("A man, a plan, a canal: Panama", True),
    ("Racecar", True),
    ("Was it a car or a cat I saw?", True),
    ("123", False),
    ("abc123xyz", False),
    ("abc.txt", "Yes"),
    ("1abc.txt", "No"),
    ("abc.123", "No"),
    ("abc.XYZ", "No"),
    ("abc.xyz", "Yes"),
    ("a.txt", "Yes"),
    ("A.txt", "Yes"),
    ("a.exe", "Yes"),
    ("A.dll", "Yes"),
    ("a.txt.bak", "No"),
    ("a..txt", "No"),
    ("..txt", "No"),
    ("txt", "Yes"),
    ("exe", "Yes"),
    ("dll", "Yes"),
    ("12345", "No"),
    ("abc.12345", "No"),
    ("abc.123.txt", "No"),
    ("abc.", "No"),
    (".", "No"),
    ("a.txt", "Yes"),
    ("A.txt", "Yes"),
    ("a.exe", "Yes"),
    ("A.dll", "Yes"),
    ("a.txt.bak", "No"),
    ("a..txt", "No"),
    ("..txt", "No"),
    ("txt", "Yes"),
    ("exe", "Yes"),
    ("dll", "Yes"),
    ("12345", "No"),
    ("abc.12345", "No"),
    ("abc.123.txt", "No"),
    ("abc.", "No"),
    (".", "No"),
])
def test_file_name_check(input_string, expected):
    assert file_name_check(input_string) == expected

@pytest.mark.parametrize("input_array, expected", [
    ([1, 2, 3], 3),
    ([], None),
    ([5, 2, 8, 1, 9], 9),
    ([-1, -5, -2], -1),
    ([0, 0, 0], 0),
])
def test_get_max(input_array, expected):
    assert get_max(input_array) == expected