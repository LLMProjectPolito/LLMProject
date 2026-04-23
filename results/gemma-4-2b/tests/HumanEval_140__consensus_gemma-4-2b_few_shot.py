
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
                count = 0
            else:
                result += "_"
        else:
            result += char
    return result

def test_empty_string():
    assert fix_spaces("") == ""

def test_no_spaces():
    assert fix_spaces("Example") == "Example"

def test_single_space():
    assert fix_spaces("Example ") == "_Example"

def test_multiple_spaces():
    assert fix_spaces(" Example   3") == "_Example-3"

def test_consecutive_spaces():
    assert fix_spaces(" Example 2") == "_Example_2"

def test_mixed_spaces_and_other_chars():
    assert fix_spaces("Example 123") == "Example_123"

def test_leading_and_trailing_spaces():
    assert fix_spaces(" Example 1") == "_Example_1"

def test_complex_string():
    assert fix_spaces("  This is a test  ") == "_This_is_a_test_"

def test_string_with_numbers():
    assert fix_spaces("Example 123") == "Example_123"

def test_string_with_special_characters():
    assert fix_spaces("Example! 123") == "Example!_123"

def test_string_with_tabs():
    assert fix_spaces("Example\t123") == "Example_123"