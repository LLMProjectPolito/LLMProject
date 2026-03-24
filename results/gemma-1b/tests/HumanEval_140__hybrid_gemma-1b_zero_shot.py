
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
        else:
            if count > 2:
                result += '-'
                count = 0
            else:
                result += char
    return result

def test_fix_spaces_basic():
    assert fix_spaces("Example") == "Example"
    assert fix_spaces("Example 1") == "Example_1"
    assert fix_spaces(" Example 2") == "_Example_2"
    assert fix_spaces(" Example   3") == "_Example-3"
    
def test_fix_spaces_with_multiple_spaces():
    assert fix_spaces("Example   ") == "_Example-3"
    
def test_fix_spaces_empty_string():
    assert fix_spaces("") == ""
    
def test_fix_spaces_single_space():
    assert fix_spaces(" ") == " "
    
def test_fix_spaces_with_leading_and_trailing_spaces():
    assert fix_spaces("  Example ") == "_Example_"
    
def test_fix_spaces_with_multiple_spaces_at_start():
    assert fix_spaces("  Example  ") == "_Example_"
    
def test_fix_spaces_with_multiple_spaces_at_end():
    assert fix_spaces("Example   ") == "_Example-"
    
def test_fix_spaces_with_mixed_spaces():
    assert fix_spaces("Example -1") == "_Example-"
    
def test_fix_spaces_with_numbers():
    assert fix_spaces("1 2 3") == "1_2_3"
    
def test_fix_spaces_with_special_characters():
    assert fix_spaces("!@#$%^") == "!@#$%^"