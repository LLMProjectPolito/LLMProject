
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
    spaces = 0
    for char in text:
        if char == ' ':
            spaces += 1
            if spaces > 2:
                result += '-'
            else:
                result += '_'
        else:
            result += char
            spaces = 0
    return result


### Tests (Pytest):
def test_fix_spaces_basic():
    assert fix_spaces("Example") == "Example"
    assert fix_spaces("Example 1") == "Example_1"
    assert fix_spaces(" Example 2") == "_Example_2"
    assert fix_spaces(" Example   3") == "_Example-3"

def test_fix_spaces_empty():
    assert fix_spaces("") == ""

def test_fix_spaces_trailing():
    assert fix_spaces("text   ") == "text-"

def test_fix_spaces_leading():
    assert fix_spaces("   text") == "-_text"

def test_fix_spaces_both_ends():
    assert fix_spaces("  text  ") == "_text-"

def test_fix_spaces_multiple_sequences():
    assert fix_spaces("text   text") == "text-text"

def test_fix_spaces_four_spaces():
    assert fix_spaces("text   text") == "text-text"

def test_fix_spaces_only_spaces():
    assert fix_spaces("   ") == "-"

def test_fix_spaces_mixed():
    assert fix_spaces("text _ text  text   text") == "text _ text-text-"