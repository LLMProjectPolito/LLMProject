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


# Fix Spaces Tests
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

def test_fix_spaces_only_spaces():
    assert fix_spaces("   ") == "-"

def test_fix_spaces_mixed_spaces():
    assert fix_spaces("  Example   Test  ") == "_Example-Test_"

def test_fix_spaces_long_string_with_multiple_space_groups():
    long_string = "This is a long string with   multiple   space   groups."
    expected_string = "This_is_a_long_string_with-multiple-space-groups."
    assert fix_spaces(long_string) == expected_string

def test_fix_spaces_string_with_tabs():
    assert fix_spaces("Example\t1") == "Example_1" # Tabs are treated as single spaces

def test_fix_spaces_string_with_newlines():
    assert fix_spaces("Example\n1") == "Example_1" # Newlines are treated as single spaces

def test_fix_spaces_trailing_space_suite2():
    assert fix_spaces("Example 1 ") == "Example_1_"

def test_fix_spaces_leading_and_trailing_spaces_suite2():
    assert fix_spaces(" Example 1 ") == "_Example_1_"

def test_fix_spaces_mixed_spaces_suite2():
    assert fix_spaces("  Example   1  ") == "_Example-1_"

def test_fix_spaces_long_string_with_multiple_space_patterns():
    long_string = "This is a long string with   multiple   spaces and  some single ones."
    expected_string = "This_is_a_long_string_with-multiple-spaces_and_some_single_ones."
    assert fix_spaces(long_string) == expected_string

def test_fix_spaces_empty_string():
    assert fix_spaces("") == ""

def test_fix_spaces_three_spaces():
    assert fix_spaces("abc   def") == "abc-def"

def test_fix_spaces_four_spaces():
    assert fix_spaces("abc    def") == "abc-def"

# Palindrome Tests
def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_palindrome_empty():
    assert is_palindrome('') == True

# Get Max Tests
def test_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_max_empty():
    assert get_max([]) == None