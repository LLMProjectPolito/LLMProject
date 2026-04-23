
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

```python
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
    
    digits = 0
    for char in file_name:
        if '0' <= char <= '9':
            digits += 1
    
    if digits > 3:
        return 'No'

    if '.' not in file_name:
        return 'No'

    parts = file_name.split('.')
    if len(parts) != 2:
        return 'No'

    name_before_dot = parts[0]
    extension = parts[1]

    if not name_before_dot:
        return 'No'
    
    first_char = name_before_dot[0]
    if not ('a' <= first_char <= 'z' or 'A' <= first_char <= 'Z'):
        return 'No'

    if extension not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'


def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    processed_string = ''.join(filter(str.isalnum, s)).lower()
    return processed_string == processed_string[::-1]


def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)


# Pytest Suite 1
class TestFileNaming:
    def test_file_name_check_valid():
        assert file_name_check("example.txt") == "Yes"
        assert file_name_check("my_file.exe") == "Yes"
        assert file_name_check("data.dll") == "Yes"
        assert file_name_check("report.docx") == "Yes"
        assert file_name_check("config.ini") == "Yes"
        assert file_name_check("a.txt") == "Yes"
        assert file_name_check("A.exe") == "Yes"
        assert file_name_check("example123.txt") == "No"
        assert file_name_check("example.123") == "No"
        assert file_name_check("1example.txt") == "No"
        assert file_name_check("example.123.txt") == "No"
        assert file_name_check(".txt") == "No"
        assert file_name_check("txt.") == "No"
        assert file_name_check("example..txt") == "No"
        assert file_name_check("example.XXX") == "No"
        assert file_name_check("example.txt.") == "No"
        assert file_name_check("example.1234.txt") == "No"
        assert file_name_check("example.123.dll") == "No"
        assert file_name_check("example.123.exe") == "No"
        assert file_name_check("example.123.txt") == "No"
        assert file_name_check("example.txt.") == "No"
        assert file_name_check("example.txt") == "Yes"
        assert file_name_check("example.txt.") == "No"
        assert file_name_check("example.txt") == "Yes"


    def test_file_name_check_invalid_digits():
        assert file_name_check("1234example.txt") == "No"
        assert file_name_check("123.txt") == "No"
        assert file_name_check("123.exe") == "No"
        assert file_name_check("12345.txt") == "No"

    def test_file_name_check_no_dot():
        assert file_name_check("example") == "No"
        assert file_name_check("example.xyz") == "No"

    def test_file_name_check_no_dot_and_empty_name():
        assert file_name_check("") == "No"
        assert file_name_check("  ") == "No"
        assert file_name_check(" .txt") == "No"

    def test_file_name_check_invalid_start_char():
        assert file_name_check("1example.txt") == "No"
        assert file_name_check("Example.txt") == "No"
        assert file_name_check("Example1.txt") == "No"
        assert file_name_check("1Example.txt") == "No"

    def test_file_name_check_invalid_extension():
        assert file_name_check("example.java") == "No"
        assert file_name_check("example.py") == "No"
        assert file_name_check("example.csv") == "No"
        assert file_name_check("example.log") == "No"
        assert file_name_check("example.pdf") == "No"

    def test_file_name_check_empty_string():
        assert file_name_check("") == "No"

    def test_file_name_check_non_string_input():
        assert file_name_check(123) == "No"
        assert file_name_check(None) == "No"
        assert file_name_check(True) == "No"


# Pytest Suite 2
class TestPalindrome:
    def test_palindrome_basic():
        assert is_palindrome('radar') == True
        assert is_palindrome('hello') == False

    def test_palindrome_empty():
        assert is_palindrome('') == True

    def test_palindrome_single_char():
        assert is_palindrome('a') == True

    def test_palindrome_with_spaces():
        assert is_palindrome('race car') == True

    def test_palindrome_with_punctuation():
        assert is_palindrome('A man, a plan, a canal: Panama') == True

    def test_palindrome_mixed_case():
        assert is_palindrome('Racecar') == True

    def test_palindrome_with_numbers():
        assert is_palindrome('121') == True

    def test_palindrome_not_a_palindrome():
        assert is_palindrome('level') == True
        assert is_palindrome('rotor') == True
        assert is_palindrome('madam') == True
        assert is_palindrome('refer') == True
        assert is_palindrome('deified') == True
        assert is_palindrome('detartrated') == True
        assert is_palindrome('stats') == True
        assert is_palindrome('noon') == True
        assert is_palindrome('kayak') == True
        assert is_palindrome('civic') == True
        assert is_palindrome('redder') == True
        assert is_palindrome('reviver') == True
        assert is_palindrome('wow') == True
        assert is_palindrome('a') == True
        assert is_palindrome('ab') == False
        assert is_palindrome('abc') == False
        assert is_palindrome('aba') == True
        assert is_palindrome('aa') == True
        assert is_palindrome('a.b') == False
        assert is_palindrome('a.b.c') == False
        assert is_palindrome('a.b.c.d') == False


class TestGetMax:
    def test_get_max_positive():
        assert get_max([1, 2, 3]) == 3

    def test_get_max_empty():
        assert get_max([]) == None

    def test_get_max_single_element():
        assert get_max([5]) == 5

    def test_get_