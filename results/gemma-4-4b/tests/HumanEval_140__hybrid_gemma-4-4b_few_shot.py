
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
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    result = ""
    space_count = 0
    for char in text:
        if char == ' ':
            space_count += 1
            if space_count > 2:
                result += "-" * space_count
                space_count = 0
            else:
                result += "_"
        else:
            result += char
    
    if space_count > 0:
        result += "_" * space_count
    
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


def test_fix_spaces_empty():
    assert fix_spaces("") == ""

def test_fix_spaces_no_spaces():
    assert fix_spaces("Example") == "Example"

def test_fix_spaces_single_space():
    assert fix_spaces("Example ") == "Example_"

def test_fix_spaces_multiple_spaces():
    assert fix_spaces("Example 1") == "Example_1"

def test_fix_spaces_many_spaces():
    assert fix_spaces(" Example 2") == "_Example_2"

def test_fix_spaces_three_spaces():
    assert fix_spaces(" Example   3") == "_Example-3"

def test_fix_spaces_leading_and_trailing_spaces():
    assert fix_spaces("  Example   ") == "__Example--"

def test_fix_spaces_mixed_spaces_and_other_chars():
    assert fix_spaces("a b   c  d") == "a_b--c_d"

def test_fix_spaces_only_spaces():
    assert fix_spaces("   ") == "--"

def test_fix_spaces_complex_case():
    assert fix_spaces("This   is a   test  string.") == "This___is-a___test--string."

def test_is_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_is_palindrome_empty():
    assert is_palindrome('') == True

def test_is_palindrome_case_insensitive():
    assert is_palindrome('Racecar') == True

def test_is_palindrome_with_spaces():
    assert is_palindrome('A man, a plan, a canal: Panama') == True

def test_is_palindrome_with_punctuation():
    assert is_palindrome('Madam, I\'m Adam') == True

def test_is_palindrome_non_alphanumeric():
    assert is_palindrome('12321') == True

def test_is_palindrome_mixed():
    assert is_palindrome('Was it a car or a cat I saw?') == True

def test_get_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_get_max_empty():
    assert get_max([]) == None

def test_get_max_negative():
    assert get_max([-1, -2, -3]) == -1

def test_get_max_mixed():
    assert get_max([-1, 2, -3, 4]) == 4

def test_get_max_single_element():
    assert get_max([5]) == 5