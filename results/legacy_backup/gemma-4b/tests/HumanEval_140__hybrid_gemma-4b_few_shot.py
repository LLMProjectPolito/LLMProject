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
    result = ""
    space_count = 0
    for char in text:
        if char == ' ':
            space_count += 1
            if space_count > 2:
                result += "-"
            else:
                result += "_"
        else:
            result += char
            space_count = 0
    return result

def test_is_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False
    assert is_palindrome('A man, a plan, a canal: Panama') == True
    assert is_palindrome('Race car') == True
    assert is_palindrome('Was it a car or a cat I saw?') == True
    assert is_palindrome('Madam') == True
    assert is_palindrome('level') == True
    assert is_palindrome('rotor') == True
    assert is_palindrome('stats') == True
    assert is_palindrome('deified') == True

def test_is_palindrome_empty():
    assert is_palindrome('') == True
    assert is_palindrome(' ') == True
    assert is_palindrome('a') == True

def test_is_palindrome_mixed_case():
    assert is_palindrome('Racecar') == True
    assert is_palindrome('RaCeCaR') == True

def test_is_palindrome_with_punctuation():
    assert is_palindrome('A man, a plan, a canal: Panama') == True
    assert is_palindrome('Race car') == True

def test_get_max_positive():
    assert get_max([1, 2, 3]) == 3
    assert get_max([3, 2, 1]) == 3
    assert get_max([1, 3, 2]) == 3
    assert get_max([1, 1, 1]) == 1

def test_get_max_negative():
    assert get_max([-1, -2, -3]) == -1
    assert get_max([-3, -2, -1]) == -1
    assert get_max([-1, -1, -1]) == -1

def test_get_max_mixed():
    assert get_max([-1, 2, -3]) == 2
    assert get_max([1, -2, 3]) == 3

def test_get_max_empty():
    assert get_max([]) == None

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

def test_fix_spaces_mixed_spaces():
    assert fix_spaces("Hello   World") == "Hello__World"

def test_fix_spaces_all_spaces():
    assert fix_spaces("   ") == "---"

def test_fix_spaces_empty_string():
    assert fix_spaces("") == ""