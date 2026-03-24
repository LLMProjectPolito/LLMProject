
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
import math

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
            if space_count <= 2:
                result += "_"
            else:
                result += "-"
        else:
            result += char
            space_count = 0
    return result

def test_fix_spaces_empty():
    assert fix_spaces("") == ""

def test_fix_spaces_no_spaces():
    assert fix_spaces("Example") == "Example"

def test_fix_spaces_single_space():
    assert fix_spaces("Example 1") == "Example_1"

def test_fix_spaces_leading_spaces():
    assert fix_spaces(" Example 1") == "_Example_1"

def test_fix_spaces_trailing_spaces():
    assert fix_spaces("Example 1 ") == "Example_1_"

def test_fix_spaces_multiple_consecutive_spaces():
    assert fix_spaces("  hello   world  ") == "_hello---world-"

def test_fix_spaces_multiple_consecutive_spaces_2():
    assert fix_spaces("   this   is   a   test  ") == "_this---is---a---test_"