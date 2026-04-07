
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
    if "   " in text:
        return text.replace("   ", "-").replace(" ", "_")
    else:
        return text.replace(" ", "_")

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    return s == s[::-1]

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)


def test_fix_spaces_no_spaces():
    assert fix_spaces("Example") == "Example"

def test_fix_spaces_single_space():
    assert fix_spaces("Example 1") == "Example_1"

def test_fix_spaces_leading_space():
    assert fix_spaces(" Example 2") == "_Example_2"

def test_fix_spaces_multiple_spaces():
    assert fix_spaces("Example   3") == "_Example-3"

def test_fix_spaces_trailing_space():
    assert fix_spaces("Example 4 ") == "Example_4_"

def test_fix_spaces_leading_and_trailing_spaces():
    assert fix_spaces(" Example 5 ") == "_Example_5_"

def test_fix_spaces_multiple_space_sequences():
    assert fix_spaces("Example  1   2") == "Example_1-2"
    assert fix_spaces("Example   6  7") == "_Example-6_7"

def test_fix_spaces_only_spaces():
    assert fix_spaces("   ") == "-"

def test_fix_spaces_mixed_spaces():
    assert fix_spaces("  Example   7  ") == "-Example-7_"
    assert fix_spaces("  Example    7  ") == "-Example-7_"

def test_fix_spaces_long_string_with_multiple_space_groups():
    long_string = "This is a long string with   multiple   space   groups."
    expected_string = "This_is_a_long_string_with-multiple-space-groups."
    assert fix_spaces(long_string) == expected_string

def test_fix_spaces_long_string_with_multiple_space_patterns():
    long_string = "This is a long string with   multiple   spaces and some  single spaces."
    expected_string = "This_is_a_long_string_with-multiple-spaces_and_some_single_spaces."
    assert fix_spaces(long_string) == expected_string

def test_fix_spaces_string_with_tabs():
    assert fix_spaces("Example\t1") == "Example_1" # Tabs are treated as single spaces

def test_fix_spaces_string_with_newlines():
    assert fix_spaces("Example\n1") == "Example_1" # Newlines are treated as single spaces

def test_fix_spaces_string_with_carriage_returns():
    assert fix_spaces("Example\r1") == "Example_1" # Carriage returns are treated as single spaces

def test_fix_spaces_consecutive_spaces_at_start():
    assert fix_spaces("   Hello") == "-Hello"

def test_fix_spaces_consecutive_spaces_at_end():
    assert fix_spaces("Hello   ") == "Hello-"

def test_fix_spaces_empty_string():
    assert fix_spaces("") == ""

# Palindrome tests
def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_palindrome_single_char():
    assert is_palindrome('a') == True

def test_palindrome_mixed_case():
    assert is_palindrome('Racecar') == False

# Max tests
def test_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_max_empty():
    assert get_max([]) == None

def test_max_negative():
    assert get_max([-1, -2, -3]) == -1

def test_max_mixed():
    assert get_max([-1, 2, -3, 4]) == 4