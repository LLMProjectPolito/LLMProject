
def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    """

import pytest

def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    """
    result = ""
    count = 0
    for char in text:
        if char == ' ':
            count += 1
            if count > 2:
                result += "-"
                count = 1
            else:
                result += "_"
        else:
            result += char
            count = 0
    return result


def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    processed_string = ''.join(filter(str.isalnum, s)).lower()
    return processed_string == processed_string[::-1]


def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)


def test_fix_spaces_all():
    assert fix_spaces("   ") == "---"
    assert fix_spaces("Example   with   many   spaces") == "_Example-with-many-spaces"
    assert fix_spaces("   Example   ") == "_Example"
    assert fix_spaces("Example") == "Example"
    assert fix_spaces("Example   ") == "_Example-"
    assert fix_spaces("  Example  ") == "_Example_"
    assert fix_spaces("") == ""
    assert fix_spaces("   ") == "---"
    assert fix_spaces("Example!  123") == "Example!_123"


def test_is_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False
    assert is_palindrome('') == True
    assert is_palindrome('A man, a plan, a canal: Panama') == True
    assert is_palindrome('Racecar') == True
    assert is_palindrome('Was it a car or a cat I saw?') == True

def test_is_palindrome_empty():
    assert is_palindrome('') == True

def test_is_palindrome_single_char():
    assert is_palindrome('a') == True
    assert is_palindrome('A') == True

def test_is_palindrome_mixed_case():
    assert is_palindrome('Racecar') == True
    assert is_palindrome('Madam') == True

def test_is_palindrome_with_spaces():
    assert is_palindrome('A man, a plan, a canal: Panama') == True

def test_is_palindrome_with_punctuation():
    assert is_palindrome('Was it a car or a cat I saw?') == True

def test_is_palindrome_with_numbers():
    assert is_palindrome('121') == True
    assert is_palindrome('12321') == True

def test_is_palindrome_with_mixed_characters():
    assert is_palindrome('A1b2c3ba') == True

def test_is_palindrome_with_special_characters():
    assert is_palindrome('!@#$%^&*()') == False
    assert is_palindrome('1234567890') == True

def test_is_palindrome_with_non_alphanumeric():
    assert is_palindrome(".,?!") == False



def test_get_max_positive():
    assert get_max([1, 2, 3]) == 3
    assert get_max([5, 1, 9, 2]) == 9
    assert get_max([10, 2, 5, 1]) == 10

def test_get_max_empty():
    assert get_max([]) == None
    assert get_max([1]) == 1

def test_get_max_negative():
    assert get_max([-1, -2, -3]) == -1
    assert get_max([-5, 1, -9, 2]) == 2

def test_get_max_mixed():
    assert get_max([-1, 2, -3, 4]) == 4
    assert get_max([1, -2, 3, -4]) == 3

def test_get_max_single_element():
    assert get_max([5]) == 5
    assert get_max([-5]) == -5