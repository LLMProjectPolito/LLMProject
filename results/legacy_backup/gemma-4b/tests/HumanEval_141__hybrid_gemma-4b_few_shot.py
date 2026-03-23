import pytest

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    s = ''.join(filter(str.isalnum, s)).lower()
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
    parts = file_name.split('.')
    if len(parts) != 2:
        return 'No'

    before_dot = parts[0]
    after_dot = parts[1]

    digit_count = 0
    for char in before_dot:
        if char.isdigit():
            digit_count += 1

    if digit_count > 3:
        return 'No'

    if not before_dot:
        return 'No'

    if not 'a' <= before_dot[0] <= 'z' and not 'A' <= before_dot[0] <= 'Z':
        return 'No'

    if after_dot not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'


def test_is_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False
    assert is_palindrome('A man, a plan, a canal: Panama') == True
    assert is_palindrome('Race car') == True
    assert is_palindrome('Was it a car or a cat I saw?') == True
    assert is_palindrome('Madam, I\'m Adam') == True
    assert is_palindrome('No ' + 'lemon') == True

def test_is_palindrome_case_insensitive():
    assert is_palindrome('RaceCar') == True
    assert is_palindrome('RaCeCaR') == True

def test_is_palindrome_with_spaces():
    assert is_palindrome('A man, a plan, a canal: Panama') == True
    assert is_palindrome('Race car') == True

def test_is_palindrome_empty():
    assert is_palindrome('') == True

def test_is_palindrome_single_char():
    assert is_palindrome('a') == True

def test_is_palindrome_non_alphanumeric():
    assert is_palindrome('12321') == True
    assert is_palindrome('!@#$') == True
    assert is_palindrome('a!b@c') == False

def test_get_max_positive():
    assert get_max([1, 2, 3]) == 3
    assert get_max([3, 2, 1]) == 3
    assert get_max([1, 3, 2]) == 3

def test_get_max_negative():
    assert get_max([-1, -2, -3]) == -1

def test_get_max_mixed():
    assert get_max([-1, 2, -3, 4]) == 4

def test_get_max_empty():
    assert get_max([]) == None

def test_get_max_single_element():
    assert get_max([5]) == 5

def test_file_name_check_valid():
    assert file_name_check("example.txt") == 'Yes'
    assert file_name_check("document.dll") == 'Yes'
    assert file_name_check("my_file.exe") == 'Yes'
    assert file_name_check("test.txt") == 'Yes'
    assert file_name_check("a.txt") == 'Yes'
    assert file_name_check("A.TXT") == 'Yes'

def test_file_name_check_invalid_digits():
    assert file_name_check("1example.txt") == 'No'
    assert file_name_check("12example.txt") == 'No'
    assert file_name_check("123example.txt") == 'No'
    assert file_name_check("1234example.txt") == 'No'

def test_file_name_check_invalid_dot():
    assert file_name_check("example..txt") == 'No'
    assert file_name_check("example.txt.") == 'No'

def test_file_name_check_invalid_prefix():
    assert file_name_check("1example.txt") == 'No'
    assert file_name_check("1example.txt") == 'No'
    assert file_name_check("abc.txt") == 'No'

def test_file_name_check_invalid_suffix():
    assert file_name_check("example.pdf") == 'No'
    assert file_name_check("example.jpg") == 'No'
    assert file_name_check("example.doc") == 'No'

def test_file_name_check_empty_prefix():
    assert file_name_check(".txt") == 'No'
    assert file_name_check("") == 'No'

def test_file_name_check_multiple_dots():
    assert file_name_check("example..txt") == 'No'
    assert file_name_check("example.txt.txt") == 'No'

def test_file_name_check_no_dot():
    assert file_name_check("example") == 'No'