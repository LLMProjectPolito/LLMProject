
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
                result += '-'
                count = 1
            else:
                result += '_'
        else:
            result += char
    return result

def test_fix_spaces_basic():
    assert fix_spaces("Example") == "Example"
    assert fix_spaces("Example 1") == "Example_1"
    assert fix_spaces(" Example 2") == "_Example_2"
    assert fix_spaces(" Example   3") == "_Example-3"

def test_fix_spaces_empty():
    assert fix_spaces("") == ""

def test_fix_spaces_multiple_spaces():
    assert fix_spaces("   ") == "---"

def test_fix_spaces_mixed():
    assert fix_spaces("a b c   d") == "a_b_c-d"

def test_fix_spaces_leading_trailing():
    assert fix_spaces("  a  ") == "_a_"

def test_fix_spaces_single_space():
    assert fix_spaces("a ") == "a_"