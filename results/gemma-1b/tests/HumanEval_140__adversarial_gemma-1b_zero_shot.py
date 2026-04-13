
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

def test_fix_spaces_one_space_consecutive():
    assert fix_spaces("Example 1") == "Example_1"

def test_fix_spaces_two_spaces_consecutive():
    assert fix_spaces("Example 2") == "_Example_2"

def test_fix_spaces_three_spaces_consecutive():
    assert fix_spaces("Example 3") == "_Example-3"

def test_fix_spaces_multiple_spaces_consecutive():
    assert fix_spaces("Example 4") == "_Example-4"

def test_fix_spaces_empty_string():
    assert fix_spaces("") == ""

def test_fix_spaces_string_with_only_spaces():
    assert fix_spaces("   ") == ""

def test_fix_spaces_mixed_spaces_and_underscores():
    assert fix_spaces("Example with spaces") == "Example with spaces"

def test_fix_spaces_with_hyphens():
    assert fix_spaces("Example-1") == "Example-1"