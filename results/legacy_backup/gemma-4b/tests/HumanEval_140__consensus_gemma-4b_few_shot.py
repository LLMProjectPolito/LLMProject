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
    result = ''
    i = 0
    while i < len(text):
        if text[i] == ' ':
            count = 0
            while i < len(text) and text[i] == ' ':
                count += 1
                i += 1
            if count > 2:
                result += '-'
            else:
                result += '_'
        else:
            result += text[i]
            i += 1
    return result

def test_is_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_is_palindrome_empty():
    assert is_palindrome('') == True

def test_is_palindrome_mixed_case():
    assert is_palindrome('Racecar') == True

def test_is_palindrome_with_punctuation():
    assert is_palindrome('A man, a plan, a canal: Panama') == True

def test_is_palindrome_with_spaces():
    assert is_palindrome('Was it a car or a cat I saw?') == True

def test_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_max_empty():
    assert get_max([]) == None

def test_max_negative():
    assert get_max([-1, -2, -3]) == -1

def test_max_mixed():
    assert get_max([-1, 2, -3, 4]) == 4

def test_fix_spaces_no_spaces():
    assert fix_spaces("Example") == "Example"

def test_fix_spaces_single_space():
    assert fix_spaces("Example 1") == "Example_1"

def test_fix_spaces_double_spaces():
    assert fix_spaces(" Example 2") == "_Example_2"

def test_fix_spaces_triple_spaces():
    assert fix_spaces(" Example   3") == "_Example-3"

def test_fix_spaces_multiple_triple_spaces():
    assert fix_spaces("  This   is   a   test  ") == "_This-is-a-test"

def test_fix_spaces_leading_and_trailing_spaces():
    assert fix_spaces("  Leading and trailing spaces  ") == "_Leading_and_trailing_spaces"

def test_fix_spaces_only_spaces():
    assert fix_spaces("   ") == "-"