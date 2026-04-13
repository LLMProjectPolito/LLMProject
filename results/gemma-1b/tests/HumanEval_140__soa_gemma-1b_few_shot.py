
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
            else:
                result += char
            count = 0
    return result

def test_fix_spaces_empty():
    assert fix_spaces("") == ""

def test_fix_spaces_single_space():
    assert fix_spaces("Example") == "Example"

def test_fix_spaces_multiple_spaces():
    assert fix_spaces("Example 1") == "Example_1"

def test_fix_spaces_consecutive_spaces():
    assert fix_spaces("Example 2") == "_Example_2"

def test_fix_spaces_multiple_consecutive_spaces():
    assert fix_spaces("Example   3") == "_Example-3"

def test_fix_spaces_mixed_spaces():
    assert fix_spaces("Example 1 2") == "Example_1_2"

def test_fix_spaces_leading_and_trailing_spaces():
    assert fix_spaces("Example ") == "Example"

def test_fix_spaces_with_numbers():
    assert fix_spaces("Example 123") == "Example_123"